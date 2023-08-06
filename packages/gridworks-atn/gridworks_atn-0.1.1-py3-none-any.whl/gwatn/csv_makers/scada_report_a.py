import json
from typing import List
from typing import Optional

import boto3
import pendulum
from gwproto.messages import GtDispatchBoolean
from gwproto.messages import GtDispatchBoolean_Maker
from gwproto.messages import GtShStatus
from gwproto.messages import GtShStatus_Maker
from gwproto.messages import GtTelemetry
from gwproto.messages import GtTelemetry_Maker
from gwproto.messages import SnapshotSpaceheat
from gwproto.messages import SnapshotSpaceheat_Maker
from pydantic import BaseModel

from gwatn.api_types_hack import HackTypeMakerByName


OUT_STUB = "output_data/scada_report_a"


class FileNameMeta(BaseModel):
    FromGNodeAlias: str
    PayloadTypeName: str
    UnixTimeMs: int
    FileName: str
    TypeName: str = "file.name.meta.000"


class StatusOutputRow(BaseModel):
    TimeUnixMs: int
    IntTimeUnixS: int
    Milliseconds: int
    TimeUtc: str
    Value: Optional[int]
    TelemetryName: Optional[str]
    AboutShNode: str
    FromShNode: Optional[str]
    DispatchCmd: Optional[int]
    TypeName: str = "ui.status.output.row.000"


class SnapshotWithSendTime(BaseModel):
    SendTimeUnixMs: int
    Snapshot: SnapshotSpaceheat
    TypeName: str = "wrapped.snapshot.spaceheat.000"


class ScadaReportA_Maker:
    ATN_ALIAS_LIST = ["hw1.isone.ct.newhaven.orange1"]

    def __init__(self, out_stub=OUT_STUB):
        self.s3 = boto3.client("s3")
        self.aws_bucket_name = "gwdev"
        self.world_instance_name = "hw1__1"
        self.out_stub = f"{out_stub}"
        self.output_type_name = "atn.ui.000"
        self.processed_file_name_meta_list = List[FileNameMeta]
        self.new_file_name_meta_list = List[FileNameMeta]
        self.latest_status_list: List[GtShStatus] = []
        self.latest_snapshot_list: List[SnapshotSpaceheat] = []
        self.latest_dispatch_list: List[GtDispatchBoolean] = []

        self.status_rows_to_write: List[StatusOutputRow] = []
        print(f"Initialized {self.__class__}")

    def on_gw_message(self, from_g_node_alias: str, payload):
        if from_g_node_alias not in self.ATN_ALIAS_LIST:
            print(f"Does not record {from_g_node_alias}.")
        else:
            if isinstance(payload, GtShStatus):
                self.latest_status_list.append(payload)

    def get_atn_alias_from_alias(self, alias: str):
        x = alias.split(".")
        if x[-1] == "scada":
            return ".".join(x[:-2])
        else:
            return alias

    def get_status_rows_from_telemetry(
        self, from_sh_node_alias: str, payload: GtTelemetry
    ) -> List[StatusOutputRow]:
        time_unix_ms = payload.ScadaReadTimeUnixMs
        time_utc = pendulum.from_timestamp(time_unix_ms / 1000)
        row = StatusOutputRow(
            TimeUnixMs=time_unix_ms,
            IntTimeUnixS=int(time_unix_ms / 1000),
            Milliseconds=int(time_unix_ms) % 1000,
            TimeUtc=time_utc.strftime("%Y-%m-%d %H:%M:%S"),
            Value=payload.Value,
            TelemetryName=payload.Name.value,
            AboutShNode=from_sh_node_alias,
            FromShNode=from_sh_node_alias,
        )
        return [row]

    def get_status_rows_from_dispatch(
        self, payload: GtDispatchBoolean
    ) -> List[StatusOutputRow]:
        rows = []
        time_unix_ms = payload.SendTimeUnixMs
        time_utc = pendulum.from_timestamp(time_unix_ms / 1000)
        row = StatusOutputRow(
            TimeUnixMs=time_unix_ms,
            IntTimeUnixS=int(time_unix_ms / 1000),
            Milliseconds=int(time_unix_ms) % 1000,
            TimeUtc=time_utc.strftime("%Y-%m-%d %H:%M:%S"),
            AboutShNode=payload.AboutNodeAlias,
            FromShNode=payload.FromGNodeAlias,
            DispatchCmd=payload.RelayState,
        )
        rows.append(row)
        return rows

    def get_status_rows_from_snapshot(
        self, payload: SnapshotWithSendTime
    ) -> List[StatusOutputRow]:
        rows = []
        from_g_node_alias = payload.Snapshot.FromGNodeAlias
        snapshot = payload.Snapshot.Snapshot
        time_unix_ms = payload.SendTimeUnixMs
        time_utc = pendulum.from_timestamp(time_unix_ms / 1000)
        for i in range(len(snapshot.ValueList)):
            row = StatusOutputRow(
                TimeUnixMs=time_unix_ms,
                IntTimeUnixS=int(time_unix_ms / 1000),
                Milliseconds=int(time_unix_ms) % 1000,
                TimeUtc=time_utc.strftime("%Y-%m-%d %H:%M:%S"),
                Value=snapshot.ValueList[i],
                TelemetryName=snapshot.TelemetryNameList[i].value,
                AboutShNode=snapshot.AboutNodeAliasList[i],
                FromShNode=from_g_node_alias,
            )
            rows.append(row)
        return rows

    def get_status_rows_from_status(self, payload: GtShStatus) -> List[StatusOutputRow]:
        rows: List[StatusOutputRow] = []
        for single in payload.SimpleTelemetryList:
            for i in range(len(single.ValueList)):
                time_unix_ms = single.ReadTimeUnixMsList[i]
                time_utc = pendulum.from_timestamp(time_unix_ms / 1000)
                row = StatusOutputRow(
                    TimeUnixMs=time_unix_ms,
                    IntTimeUnixS=int(time_unix_ms / 1000),
                    Milliseconds=int(time_unix_ms) % 1000,
                    TimeUtc=time_utc.strftime("%Y-%m-%d %H:%M:%S"),
                    Value=single.ValueList[i],
                    TelemetryName=single.TelemetryName.value,
                    AboutShNode=single.ShNodeAlias,
                    FromShNode=single.ShNodeAlias,
                )
                rows.append(row)

        for cmd in payload.BooleanactuatorCmdList:
            about_node_alias = cmd.ShNodeAlias
            for i in range(len(cmd.RelayStateCommandList)):
                time_unix_ms = cmd.CommandTimeUnixMsList[i]
                time_utc = pendulum.from_timestamp(time_unix_ms / 1000)
                row = StatusOutputRow(
                    TimeUnixMs=time_unix_ms,
                    IntTimeUnixS=int(time_unix_ms / 1000),
                    Milliseconds=int(time_unix_ms) % 1000,
                    TimeUtc=time_utc.strftime("%Y-%m-%d %H:%M:%S"),
                    AboutShNode=about_node_alias,
                    DispatchCmd=cmd.RelayStateCommandList[i],
                )
                rows.append(row)

        for multi in payload.MultipurposeTelemetryList:
            for i in range(len(multi.ValueList)):
                time_unix_ms = multi.ReadTimeUnixMsList[i]
                time_utc = pendulum.from_timestamp(time_unix_ms / 1000)
                row = StatusOutputRow(
                    TimeUnixMs=time_unix_ms,
                    IntTimeUnixS=int(time_unix_ms / 1000),
                    Milliseconds=int(time_unix_ms) % 1000,
                    TimeUtc=time_utc.strftime("%Y-%m-%d %H:%M:%S"),
                    Value=multi.ValueList[i],
                    TelemetryName=multi.TelemetryName.value,
                    AboutShNode=multi.AboutNodeAlias,
                    FromShNode=multi.SensorNodeAlias,
                )
                rows.append(row)
        return rows

    def get_payload_from_s3(self, file_name_meta: FileNameMeta) -> GtShStatus:
        s3_object = self.s3.get_object(
            Bucket=self.aws_bucket_name, Key=file_name_meta.FileName
        )
        gw_type = s3_object["Body"].read()
        try:
            payload_as_dict = json.loads(gw_type)["Payload"]
        except:
            payload_as_dict = json.loads(gw_type)
        maker = HackTypeMakerByName[file_name_meta.PayloadTypeName]
        payload = maker.dict_to_tuple(payload_as_dict)
        if maker.type_alias == SnapshotSpaceheat_Maker.type_alias:
            payload = SnapshotWithSendTime(
                SendTimeUnixMs=file_name_meta.UnixTimeMs, Snapshot=payload
            )
        return payload

    def has_this_days_folder(self, time_s: int) -> bool:
        d = pendulum.from_timestamp(time_s)
        this_days_folder_name = d.strftime("%Y%m%d")
        prefix = f"{self.world_instance_name}/eventstore/{this_days_folder_name}"

        r = self.s3.list_objects_v2(Bucket=self.aws_bucket_name, Prefix=prefix)
        if "Contents" in r.keys():
            return True
        return False

    def get_date_folder_list(
        self, start_time_unix_ms: int, duration_hrs: int
    ) -> List[str]:
        start_s = start_time_unix_ms / 1000
        folder_list: List[str] = []
        found_latest_earlier: bool = False
        i = 0
        while (not found_latest_earlier) and i < 5:
            t = start_s - 3600 * 24 * (i + 1)
            if self.has_this_days_folder(t):
                folder_list.append(pendulum.from_timestamp(t).strftime("%Y%m%d"))
                found_latest_earlier = True
            i += 1

        if self.has_this_days_folder(start_s):
            folder_list.append(pendulum.from_timestamp(start_s).strftime("%Y%m%d"))

        add_hrs = 0
        while add_hrs < duration_hrs:
            add_hrs += 24
            add_hrs = min(add_hrs, duration_hrs)
            t = start_s + add_hrs * 3600
            if self.has_this_days_folder(t):
                folder_list.append(pendulum.from_timestamp(t).strftime("%Y%m%d"))

        return list(set(folder_list))

    def get_file_name_meta_list(
        self,
        start_time_unix_ms: int,
        end_time_unix_ms: int,
        date_folder_list: List[str],
        g_node_alias_list: List[str],
        type_name_list: List[str] = list(HackTypeMakerByName.keys()),
    ):
        fn_list: List[FileNameMeta] = []
        for date_folder in date_folder_list:
            prefix = f"{self.world_instance_name}/eventstore/{date_folder}/"
            paginator = self.s3.get_paginator("list_objects_v2")
            pages = paginator.paginate(Bucket=self.aws_bucket_name, Prefix=prefix)
            file_name_list = []
            for page in pages:
                for obj in page["Contents"]:
                    file_name_list.append(obj["Key"])

            for file_name in file_name_list:
                try:
                    from_g_node_alias = file_name.split("/")[-1].split("-")[0]
                    payload_type_name = file_name.split("/")[-1].split("-")[1]
                    payload_unix_time_ms = int(file_name.split("/")[-1].split("-")[2])
                except:
                    raise Exception(f"Failed file name parsing with {file_name}")

                if (
                    from_g_node_alias in g_node_alias_list
                    and payload_type_name in type_name_list
                    and payload_unix_time_ms > start_time_unix_ms - 300_000
                    and payload_unix_time_ms < end_time_unix_ms
                ):
                    fn_list.append(
                        FileNameMeta(
                            FromGNodeAlias=from_g_node_alias,
                            PayloadTypeName=payload_type_name,
                            UnixTimeMs=payload_unix_time_ms,
                            FileName=file_name,
                        )
                    )

        return fn_list

    def get_csv_rows(
        self, start_time_unix_ms: int, duration_hrs: int, atn_alias: str
    ) -> List[StatusOutputRow]:
        g_node_alias_list = [atn_alias, atn_alias + ".ta.scada"]
        hack_list = [
            "a.garage.temp1",
            "a.tank.out.temp1",
            "a.tank.in.temp1",
            "a.tank.temp0",
        ]
        g_node_alias_list += hack_list
        start_time_utc = pendulum.from_timestamp(start_time_unix_ms / 1000)
        end_time_utc = start_time_utc + pendulum.duration(hours=duration_hrs)
        end_time_unix_ms = end_time_utc.int_timestamp * 1000
        date_folder_list = self.get_date_folder_list(start_time_unix_ms, duration_hrs)
        fn_list = self.get_file_name_meta_list(
            start_time_unix_ms=start_time_unix_ms,
            end_time_unix_ms=end_time_unix_ms,
            date_folder_list=date_folder_list,
            g_node_alias_list=g_node_alias_list,
        )

        rows: List[StatusOutputRow] = []
        for i in range(len(fn_list)):
            fn = fn_list[i]
            if fn.PayloadTypeName == GtDispatchBoolean_Maker.type_alias:
                payload = self.get_payload_from_s3(fn)
                rows += self.get_status_rows_from_dispatch(payload)
            elif fn.PayloadTypeName == GtShStatus_Maker.type_alias:
                payload = self.get_payload_from_s3(fn)
                rows += self.get_status_rows_from_status(payload)
            elif fn.PayloadTypeName == SnapshotSpaceheat_Maker.type_alias:
                payload = self.get_payload_from_s3(fn)
                rows += self.get_status_rows_from_snapshot(payload)
            elif fn.PayloadTypeName == GtTelemetry_Maker.type_alias:
                payload = self.get_payload_from_s3(fn)
                rows += self.get_status_rows_from_telemetry(
                    from_sh_node_alias=fn.FromGNodeAlias,
                    payload=payload,
                )

        rows = sorted(rows, key=lambda x: x.TimeUnixMs)
        return rows

    def make_csv(
        self,
        start_s,
        duration_hrs: int = 48,
        atn_alias: str = "hw1.isone.ct.newhaven.orange1",
    ):
        s = start_s - (start_s % 3600)
        start_time_utc = pendulum.from_timestamp(s)
        print(f"starting at {start_time_utc.strftime('%Y-%m-%d %H:%M')}")
        start_time_unix_ms = s * 1000

        rows = self.get_csv_rows(
            start_time_unix_ms=start_time_unix_ms,
            duration_hrs=duration_hrs,
            atn_alias=atn_alias,
        )
        lines = [
            "TimeUtc, TimeUnixS, Ms, Value, TelemetryName, AboutShNode, FromShNode, DispatchCmd\n"
        ]
        for row in rows:
            line = f"{row.TimeUtc}, {row.IntTimeUnixS}, {row.Milliseconds}"
            if row.Value is None:
                line += ", "
            else:
                line += f",{row.Value}"
            if row.TelemetryName is None:
                line += ", "
            else:
                line += f", {row.TelemetryName}"
            line += f", {row.AboutShNode}"
            if row.FromShNode is None:
                line += ", "
            else:
                line += f", {row.FromShNode}"
            if row.DispatchCmd is None:
                line += ", \n"
            else:
                line += f", {row.DispatchCmd} \n"
            lines.append(line)

        atn_end = atn_alias.split(".")[-1]
        file_name = f"{self.out_stub}/{atn_end}-{start_time_utc.strftime('%Y%m%d-%H%M')}-{duration_hrs}-{atn_alias}.csv"
        print(f"Writing {file_name}")
        with open(file_name, "w") as outfile:
            outfile.writelines(lines)
