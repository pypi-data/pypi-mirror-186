from gwproto.messages import GtDispatchBoolean_Maker
from gwproto.messages import GtShStatus_Maker
from gwproto.messages import GtTelemetry_Maker
from gwproto.messages import SnapshotSpaceheat_Maker

from gwatn.api_types import TypeMakerByName


HackTypeMakerByName = dict(TypeMakerByName)

HackTypeMakerByName[GtDispatchBoolean_Maker.type_alias] = GtDispatchBoolean_Maker
HackTypeMakerByName[GtShStatus_Maker.type_alias] = GtShStatus_Maker
HackTypeMakerByName[SnapshotSpaceheat_Maker.type_alias] = SnapshotSpaceheat_Maker
HackTypeMakerByName[GtTelemetry_Maker.type_alias] = GtTelemetry_Maker
