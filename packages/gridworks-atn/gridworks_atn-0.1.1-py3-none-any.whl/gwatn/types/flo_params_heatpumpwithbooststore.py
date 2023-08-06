"""Type flo.params.heatpumpwithbooststore, version 000"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

import gridworks.property_format as property_format
from fastapi_utils.enums import StrEnum
from gridworks.errors import SchemaError
from gridworks.message import as_enum
from gridworks.property_format import predicate_validator
from pydantic import BaseModel
from pydantic import validator

from gwatn.enums import DistributionTariff
from gwatn.enums import EmitterPumpFeedbackModel as PumpModel
from gwatn.enums import EnergySupplyType
from gwatn.enums import MixingValveFeedbackModel as MixingValveModel
from gwatn.enums import RecognizedCurrencyUnit
from gwatn.enums import RecognizedTemperatureUnit


class DistributionTariff000SchemaEnum:
    enum_name: str = "distribution.tariff.000"
    symbols: List[str] = [
        "00000000",
        "2127aba6",
        "ea5c675a",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class DistributionTariff000(StrEnum):
    Unknown = auto()
    VersantStorageHeatTariff = auto()
    VersantATariff = auto()

    @classmethod
    def default(cls) -> "DistributionTariff000":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class DistributionTariffMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> DistributionTariff:
        if not DistributionTariff000SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to DistributionTariff000 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, DistributionTariff, DistributionTariff.default())

    @classmethod
    def local_to_type(cls, distribution_tariff: DistributionTariff) -> str:
        if not isinstance(distribution_tariff, DistributionTariff):
            raise SchemaError(
                f"{distribution_tariff} must be of type {DistributionTariff}"
            )
        versioned_enum = as_enum(
            distribution_tariff, DistributionTariff000, DistributionTariff000.default()
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, DistributionTariff000] = {
        "00000000": DistributionTariff000.Unknown,
        "2127aba6": DistributionTariff000.VersantStorageHeatTariff,
        "ea5c675a": DistributionTariff000.VersantATariff,
    }

    versioned_enum_to_type_dict: Dict[DistributionTariff000, str] = {
        DistributionTariff000.Unknown: "00000000",
        DistributionTariff000.VersantStorageHeatTariff: "2127aba6",
        DistributionTariff000.VersantATariff: "ea5c675a",
    }


class EmitterPumpFeedbackModel000SchemaEnum:
    enum_name: str = "emitter.pump.feedback.model.000"
    symbols: List[str] = [
        "00000000",
        "f6bde4fa",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class EmitterPumpFeedbackModel000(StrEnum):
    ConstantDeltaT = auto()
    ConstantGpm = auto()

    @classmethod
    def default(cls) -> "EmitterPumpFeedbackModel000":
        return cls.ConstantDeltaT

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class EmitterPumpFeedbackModelMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> PumpModel:
        if not EmitterPumpFeedbackModel000SchemaEnum.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to EmitterPumpFeedbackModel000 symbols"
            )
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, PumpModel, PumpModel.default())

    @classmethod
    def local_to_type(cls, emitter_pump_feedback_model: PumpModel) -> str:
        if not isinstance(emitter_pump_feedback_model, PumpModel):
            raise SchemaError(
                f"{emitter_pump_feedback_model} must be of type {PumpModel}"
            )
        versioned_enum = as_enum(
            emitter_pump_feedback_model,
            EmitterPumpFeedbackModel000,
            EmitterPumpFeedbackModel000.default(),
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, EmitterPumpFeedbackModel000] = {
        "00000000": EmitterPumpFeedbackModel000.ConstantDeltaT,
        "f6bde4fa": EmitterPumpFeedbackModel000.ConstantGpm,
    }

    versioned_enum_to_type_dict: Dict[EmitterPumpFeedbackModel000, str] = {
        EmitterPumpFeedbackModel000.ConstantDeltaT: "00000000",
        EmitterPumpFeedbackModel000.ConstantGpm: "f6bde4fa",
    }


class RecognizedCurrencyUnit000SchemaEnum:
    enum_name: str = "recognized.currency.unit.000"
    symbols: List[str] = [
        "00000000",
        "e57c5143",
        "f7b38fc5",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class RecognizedCurrencyUnit000(StrEnum):
    UNKNOWN = auto()
    USD = auto()
    GBP = auto()

    @classmethod
    def default(cls) -> "RecognizedCurrencyUnit000":
        return cls.UNKNOWN

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class RecognizedCurrencyUnitMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> RecognizedCurrencyUnit:
        if not RecognizedCurrencyUnit000SchemaEnum.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to RecognizedCurrencyUnit000 symbols"
            )
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(
            versioned_enum, RecognizedCurrencyUnit, RecognizedCurrencyUnit.default()
        )

    @classmethod
    def local_to_type(cls, recognized_currency_unit: RecognizedCurrencyUnit) -> str:
        if not isinstance(recognized_currency_unit, RecognizedCurrencyUnit):
            raise SchemaError(
                f"{recognized_currency_unit} must be of type {RecognizedCurrencyUnit}"
            )
        versioned_enum = as_enum(
            recognized_currency_unit,
            RecognizedCurrencyUnit000,
            RecognizedCurrencyUnit000.default(),
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, RecognizedCurrencyUnit000] = {
        "00000000": RecognizedCurrencyUnit000.UNKNOWN,
        "e57c5143": RecognizedCurrencyUnit000.USD,
        "f7b38fc5": RecognizedCurrencyUnit000.GBP,
    }

    versioned_enum_to_type_dict: Dict[RecognizedCurrencyUnit000, str] = {
        RecognizedCurrencyUnit000.UNKNOWN: "00000000",
        RecognizedCurrencyUnit000.USD: "e57c5143",
        RecognizedCurrencyUnit000.GBP: "f7b38fc5",
    }


class RecognizedTemperatureUnit000SchemaEnum:
    enum_name: str = "recognized.temperature.unit.000"
    symbols: List[str] = [
        "00000000",
        "6f16ee63",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class RecognizedTemperatureUnit000(StrEnum):
    C = auto()
    F = auto()

    @classmethod
    def default(cls) -> "RecognizedTemperatureUnit000":
        return cls.C

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class RecognizedTemperatureUnitMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> RecognizedTemperatureUnit:
        if not RecognizedTemperatureUnit000SchemaEnum.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to RecognizedTemperatureUnit000 symbols"
            )
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(
            versioned_enum,
            RecognizedTemperatureUnit,
            RecognizedTemperatureUnit.default(),
        )

    @classmethod
    def local_to_type(
        cls, recognized_temperature_unit: RecognizedTemperatureUnit
    ) -> str:
        if not isinstance(recognized_temperature_unit, RecognizedTemperatureUnit):
            raise SchemaError(
                f"{recognized_temperature_unit} must be of type {RecognizedTemperatureUnit}"
            )
        versioned_enum = as_enum(
            recognized_temperature_unit,
            RecognizedTemperatureUnit000,
            RecognizedTemperatureUnit000.default(),
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, RecognizedTemperatureUnit000] = {
        "00000000": RecognizedTemperatureUnit000.C,
        "6f16ee63": RecognizedTemperatureUnit000.F,
    }

    versioned_enum_to_type_dict: Dict[RecognizedTemperatureUnit000, str] = {
        RecognizedTemperatureUnit000.C: "00000000",
        RecognizedTemperatureUnit000.F: "6f16ee63",
    }


class MixingValveFeedbackModel000SchemaEnum:
    enum_name: str = "mixing.valve.feedback.model.000"
    symbols: List[str] = [
        "00000000",
        "0397c1df",
        "6a668ab8",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class MixingValveFeedbackModel000(StrEnum):
    ConstantSwt = auto()
    NaiveVariableSwt = auto()
    CautiousVariableSwt = auto()

    @classmethod
    def default(cls) -> "MixingValveFeedbackModel000":
        return cls.ConstantSwt

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class MixingValveFeedbackModelMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> MixingValveModel:
        if not MixingValveFeedbackModel000SchemaEnum.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to MixingValveFeedbackModel000 symbols"
            )
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, MixingValveModel, MixingValveModel.default())

    @classmethod
    def local_to_type(cls, mixing_valve_feedback_model: MixingValveModel) -> str:
        if not isinstance(mixing_valve_feedback_model, MixingValveModel):
            raise SchemaError(
                f"{mixing_valve_feedback_model} must be of type {MixingValveModel}"
            )
        versioned_enum = as_enum(
            mixing_valve_feedback_model,
            MixingValveFeedbackModel000,
            MixingValveFeedbackModel000.default(),
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, MixingValveFeedbackModel000] = {
        "00000000": MixingValveFeedbackModel000.ConstantSwt,
        "0397c1df": MixingValveFeedbackModel000.NaiveVariableSwt,
        "6a668ab8": MixingValveFeedbackModel000.CautiousVariableSwt,
    }

    versioned_enum_to_type_dict: Dict[MixingValveFeedbackModel000, str] = {
        MixingValveFeedbackModel000.ConstantSwt: "00000000",
        MixingValveFeedbackModel000.NaiveVariableSwt: "0397c1df",
        MixingValveFeedbackModel000.CautiousVariableSwt: "6a668ab8",
    }


class EnergySupplyType000SchemaEnum:
    enum_name: str = "energy.supply.type.000"
    symbols: List[str] = [
        "00000000",
        "cb18f937",
        "e9dc99a6",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class EnergySupplyType000(StrEnum):
    Unknown = auto()
    StandardOffer = auto()
    RealtimeLocalLmp = auto()

    @classmethod
    def default(cls) -> "EnergySupplyType000":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class EnergySupplyTypeMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> EnergySupplyType:
        if not EnergySupplyType000SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to EnergySupplyType000 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, EnergySupplyType, EnergySupplyType.default())

    @classmethod
    def local_to_type(cls, energy_supply_type: EnergySupplyType) -> str:
        if not isinstance(energy_supply_type, EnergySupplyType):
            raise SchemaError(
                f"{energy_supply_type} must be of type {EnergySupplyType}"
            )
        versioned_enum = as_enum(
            energy_supply_type, EnergySupplyType000, EnergySupplyType000.default()
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, EnergySupplyType000] = {
        "00000000": EnergySupplyType000.Unknown,
        "cb18f937": EnergySupplyType000.StandardOffer,
        "e9dc99a6": EnergySupplyType000.RealtimeLocalLmp,
    }

    versioned_enum_to_type_dict: Dict[EnergySupplyType000, str] = {
        EnergySupplyType000.Unknown: "00000000",
        EnergySupplyType000.StandardOffer: "cb18f937",
        EnergySupplyType000.RealtimeLocalLmp: "e9dc99a6",
    }


class FloParamsHeatpumpwithbooststore(BaseModel):
    StoreSizeGallons: int = 240  #
    MaxStoreTempF: int = 190  #
    StoreMaxPowerKw: float = 9  #
    RatedHeatpumpElectricityKw: float = 5.5  #
    MaxHeatpumpSourceWaterTempF: int = 135  #
    SystemMaxHeatOutputSwtF: int = 160  #
    SystemMaxHeatOutputDeltaTempF: int = 20  #
    SystemMaxHeatOutputGpm: float = 6  #
    EmitterMaxSafeSwtF: int = 170  #
    CirculatorPumpMaxGpm: float = 10  #
    HeatpumpTariff: DistributionTariff = DistributionTariff.VersantStorageHeatTariff  #
    HeatpumpEnergySupplyType: EnergySupplyType = EnergySupplyType.RealtimeLocalLmp  #
    BoostTariff: DistributionTariff = DistributionTariff.VersantStorageHeatTariff  #
    BoostEnergySupplyType: EnergySupplyType = EnergySupplyType.RealtimeLocalLmp  #
    StandardOfferPriceDollarsPerMwh: int = 110  #
    DistributionTariffDollarsPerMwh: int = 113  #
    AmbientTempStoreF: int = 65  #
    StorePassiveLossRatio: float = 0.001  #
    RoomTempF: int = 70  #
    AmbientPowerInKw: float = 1.25  #
    ZeroPotentialEnergyWaterTempF: int = 100  #
    EmitterPumpFeedbackModel: PumpModel = PumpModel.ConstantDeltaT  #
    MixingValveFeedbackModel: MixingValveModel = MixingValveModel.NaiveVariableSwt  #
    CautiousMixingValveTempDeltaF: int = 5  #
    Cop1TempF: int = -20  #
    Cop4TempF: int = 70  #
    CurrencyUnit: RecognizedCurrencyUnit = RecognizedCurrencyUnit.USD  #
    TempUnit: RecognizedTemperatureUnit = RecognizedTemperatureUnit.F  #
    TimezoneString: str = "US/Eastern"  #
    HomeCity: str = "MILLINOCKET_ME"  #
    StorageSteps: int = 100  #
    HouseWorstCaseTempF: int = -7  #
    SystemMaxHeatOutputKwAvg: float = 11.68  #
    K: float = -1.1  #
    IsRegulating: bool = False  #
    SliceDurationMinutes: List[int] = [60]  #
    PowerRequiredByHouseFromSystemAvgKwList: List[float] = [3.42]  #
    OutsideTempF: List[float] = [-5.1]  #
    RealtimeElectricityPrice: List[float] = [10.35]  #
    DistributionPrice: List[float] = [40.0]  #
    RegulationPrice: List[float] = [25.3]  #
    RtElecPriceUid: str  #
    WeatherUid: str  #
    DistPriceUid: Optional[str] = None
    RegPriceUid: Optional[str] = None
    StartYearUtc: int = 2020  #
    StartMonthUtc: int = 1  #
    StartDayUtc: int = 1  #
    StartHourUtc: int = 1  #
    StartMinuteUtc: int = 0  #
    StartingStoreIdx: int = 50  #
    TypeName: Literal[
        "flo.params.heatpumpwithbooststore"
    ] = "flo.params.heatpumpwithbooststore"
    Version: str = "000"

    @validator("HeatpumpTariff")
    def _validator_heatpump_tariff(cls, v: DistributionTariff) -> DistributionTariff:
        return as_enum(v, DistributionTariff, DistributionTariff.Unknown)

    @validator("HeatpumpEnergySupplyType")
    def _validator_heatpump_energy_supply_type(
        cls, v: EnergySupplyType
    ) -> EnergySupplyType:
        return as_enum(v, EnergySupplyType, EnergySupplyType.Unknown)

    @validator("BoostTariff")
    def _validator_boost_tariff(cls, v: DistributionTariff) -> DistributionTariff:
        return as_enum(v, DistributionTariff, DistributionTariff.Unknown)

    @validator("BoostEnergySupplyType")
    def _validator_boost_energy_supply_type(
        cls, v: EnergySupplyType
    ) -> EnergySupplyType:
        return as_enum(v, EnergySupplyType, EnergySupplyType.Unknown)

    @validator("EmitterPumpFeedbackModel")
    def _validator_emitter_pump_feedback_model(
        cls, v: EmitterPumpFeedbackModel
    ) -> EmitterPumpFeedbackModel:
        return as_enum(v, PumpModel, PumpModel.ConstantDeltaT)

    @validator("MixingValveFeedbackModel")
    def _validator_mixing_valve_feedback_model(
        cls, v: MixingValveFeedbackModel
    ) -> MixingValveFeedbackModel:
        return as_enum(v, MixingValveModel, MixingValveModel.ConstantSwt)

    @validator("CurrencyUnit")
    def _validator_currency_unit(
        cls, v: RecognizedCurrencyUnit
    ) -> RecognizedCurrencyUnit:
        return as_enum(v, RecognizedCurrencyUnit, RecognizedCurrencyUnit.UNKNOWN)

    @validator("TempUnit")
    def _validator_temp_unit(
        cls, v: RecognizedTemperatureUnit
    ) -> RecognizedTemperatureUnit:
        return as_enum(v, RecognizedTemperatureUnit, RecognizedTemperatureUnit.C)

    _validator_rt_elec_price_uid = predicate_validator(
        "RtElecPriceUid", property_format.is_uuid_canonical_textual
    )

    _validator_weather_uid = predicate_validator(
        "WeatherUid", property_format.is_uuid_canonical_textual
    )

    @validator("DistPriceUid")
    def _validator_dist_price_uid(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        if not property_format.is_uuid_canonical_textual(v):
            raise ValueError(f"DistPriceUid {v} must have UuidCanonicalTextual")
        return v

    @validator("RegPriceUid")
    def _validator_reg_price_uid(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        if not property_format.is_uuid_canonical_textual(v):
            raise ValueError(f"RegPriceUid {v} must have UuidCanonicalTextual")
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["HeatpumpTariff"]
        HeatpumpTariff = as_enum(
            self.HeatpumpTariff, DistributionTariff, DistributionTariff.default()
        )
        d["HeatpumpTariffGtEnumSymbol"] = DistributionTariffMap.local_to_type(
            HeatpumpTariff
        )
        del d["HeatpumpEnergySupplyType"]
        HeatpumpEnergySupplyType = as_enum(
            self.HeatpumpEnergySupplyType, EnergySupplyType, EnergySupplyType.default()
        )
        d["HeatpumpEnergySupplyTypeGtEnumSymbol"] = EnergySupplyTypeMap.local_to_type(
            HeatpumpEnergySupplyType
        )
        del d["BoostTariff"]
        BoostTariff = as_enum(
            self.BoostTariff, DistributionTariff, DistributionTariff.default()
        )
        d["BoostTariffGtEnumSymbol"] = DistributionTariffMap.local_to_type(BoostTariff)
        del d["BoostEnergySupplyType"]
        BoostEnergySupplyType = as_enum(
            self.BoostEnergySupplyType, EnergySupplyType, EnergySupplyType.default()
        )
        d["BoostEnergySupplyTypeGtEnumSymbol"] = EnergySupplyTypeMap.local_to_type(
            BoostEnergySupplyType
        )
        del d["EmitterPumpFeedbackModel"]
        EmitterPumpFeedbackModel = as_enum(
            self.EmitterPumpFeedbackModel,
            PumpModel,
            PumpModel.default(),
        )
        d[
            "EmitterPumpFeedbackModelGtEnumSymbol"
        ] = EmitterPumpFeedbackModelMap.local_to_type(EmitterPumpFeedbackModel)
        del d["MixingValveFeedbackModel"]
        MixingValveFeedbackModel = as_enum(
            self.MixingValveFeedbackModel,
            MixingValveModel,
            MixingValveModel.default(),
        )
        d[
            "MixingValveFeedbackModelGtEnumSymbol"
        ] = MixingValveFeedbackModelMap.local_to_type(MixingValveFeedbackModel)
        del d["CurrencyUnit"]
        CurrencyUnit = as_enum(
            self.CurrencyUnit, RecognizedCurrencyUnit, RecognizedCurrencyUnit.default()
        )
        d["CurrencyUnitGtEnumSymbol"] = RecognizedCurrencyUnitMap.local_to_type(
            CurrencyUnit
        )
        del d["TempUnit"]
        TempUnit = as_enum(
            self.TempUnit,
            RecognizedTemperatureUnit,
            RecognizedTemperatureUnit.default(),
        )
        d["TempUnitGtEnumSymbol"] = RecognizedTemperatureUnitMap.local_to_type(TempUnit)
        if d["DistPriceUid"] is None:
            del d["DistPriceUid"]
        if d["RegPriceUid"] is None:
            del d["RegPriceUid"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class FloParamsHeatpumpwithbooststore_Maker:
    type_name = "flo.params.heatpumpwithbooststore"
    version = "000"

    def __init__(
        self,
        store_size_gallons: int,
        max_store_temp_f: int,
        store_max_power_kw: float,
        rated_heatpump_electricity_kw: float,
        max_heatpump_source_water_temp_f: int,
        system_max_heat_output_swt_f: int,
        system_max_heat_output_delta_temp_f: int,
        system_max_heat_output_gpm: float,
        emitter_max_safe_swt_f: int,
        circulator_pump_max_gpm: float,
        heatpump_tariff: DistributionTariff,
        heatpump_energy_supply_type: EnergySupplyType,
        boost_tariff: DistributionTariff,
        boost_energy_supply_type: EnergySupplyType,
        standard_offer_price_dollars_per_mwh: int,
        distribution_tariff_dollars_per_mwh: int,
        ambient_temp_store_f: int,
        store_passive_loss_ratio: float,
        room_temp_f: int,
        ambient_power_in_kw: float,
        zero_potential_energy_water_temp_f: int,
        emitter_pump_feedback_model: PumpModel,
        mixing_valve_feedback_model: MixingValveModel,
        cautious_mixing_valve_temp_delta_f: int,
        cop1_temp_f: int,
        cop4_temp_f: int,
        currency_unit: RecognizedCurrencyUnit,
        temp_unit: RecognizedTemperatureUnit,
        timezone_string: str,
        home_city: str,
        storage_steps: int,
        house_worst_case_temp_f: int,
        system_max_heat_output_kw_avg: float,
        k: float,
        is_regulating: bool,
        slice_duration_minutes: List[int],
        power_required_by_house_from_system_avg_kw_list: List[float],
        outside_temp_f: List[float],
        realtime_electricity_price: List[float],
        distribution_price: List[float],
        regulation_price: List[float],
        rt_elec_price_uid: str,
        weather_uid: str,
        dist_price_uid: Optional[str],
        reg_price_uid: Optional[str],
        start_year_utc: int,
        start_month_utc: int,
        start_day_utc: int,
        start_hour_utc: int,
        start_minute_utc: int,
        starting_store_idx: int,
    ):
        self.tuple = FloParamsHeatpumpwithbooststore(
            StoreSizeGallons=store_size_gallons,
            MaxStoreTempF=max_store_temp_f,
            StoreMaxPowerKw=store_max_power_kw,
            RatedHeatpumpElectricityKw=rated_heatpump_electricity_kw,
            MaxHeatpumpSourceWaterTempF=max_heatpump_source_water_temp_f,
            SystemMaxHeatOutputSwtF=system_max_heat_output_swt_f,
            SystemMaxHeatOutputDeltaTempF=system_max_heat_output_delta_temp_f,
            SystemMaxHeatOutputGpm=system_max_heat_output_gpm,
            EmitterMaxSafeSwtF=emitter_max_safe_swt_f,
            CirculatorPumpMaxGpm=circulator_pump_max_gpm,
            HeatpumpTariff=heatpump_tariff,
            HeatpumpEnergySupplyType=heatpump_energy_supply_type,
            BoostTariff=boost_tariff,
            BoostEnergySupplyType=boost_energy_supply_type,
            StandardOfferPriceDollarsPerMwh=standard_offer_price_dollars_per_mwh,
            DistributionTariffDollarsPerMwh=distribution_tariff_dollars_per_mwh,
            AmbientTempStoreF=ambient_temp_store_f,
            StorePassiveLossRatio=store_passive_loss_ratio,
            RoomTempF=room_temp_f,
            AmbientPowerInKw=ambient_power_in_kw,
            ZeroPotentialEnergyWaterTempF=zero_potential_energy_water_temp_f,
            EmitterPumpFeedbackModel=emitter_pump_feedback_model,
            MixingValveFeedbackModel=mixing_valve_feedback_model,
            CautiousMixingValveTempDeltaF=cautious_mixing_valve_temp_delta_f,
            Cop1TempF=cop1_temp_f,
            Cop4TempF=cop4_temp_f,
            CurrencyUnit=currency_unit,
            TempUnit=temp_unit,
            TimezoneString=timezone_string,
            HomeCity=home_city,
            StorageSteps=storage_steps,
            HouseWorstCaseTempF=house_worst_case_temp_f,
            SystemMaxHeatOutputKwAvg=system_max_heat_output_kw_avg,
            K=k,
            IsRegulating=is_regulating,
            SliceDurationMinutes=slice_duration_minutes,
            PowerRequiredByHouseFromSystemAvgKwList=power_required_by_house_from_system_avg_kw_list,
            OutsideTempF=outside_temp_f,
            RealtimeElectricityPrice=realtime_electricity_price,
            DistributionPrice=distribution_price,
            RegulationPrice=regulation_price,
            RtElecPriceUid=rt_elec_price_uid,
            WeatherUid=weather_uid,
            DistPriceUid=dist_price_uid,
            RegPriceUid=reg_price_uid,
            StartYearUtc=start_year_utc,
            StartMonthUtc=start_month_utc,
            StartDayUtc=start_day_utc,
            StartHourUtc=start_hour_utc,
            StartMinuteUtc=start_minute_utc,
            StartingStoreIdx=starting_store_idx,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: FloParamsHeatpumpwithbooststore) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> FloParamsHeatpumpwithbooststore:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> FloParamsHeatpumpwithbooststore:
        d2 = dict(d)
        if "StoreSizeGallons" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StoreSizeGallons")
        if "MaxStoreTempF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MaxStoreTempF")
        if "StoreMaxPowerKw" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StoreMaxPowerKw")
        if "RatedHeatpumpElectricityKw" not in d2.keys():
            raise SchemaError(f"dict {d2} missing RatedHeatpumpElectricityKw")
        if "MaxHeatpumpSourceWaterTempF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MaxHeatpumpSourceWaterTempF")
        if "SystemMaxHeatOutputSwtF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SystemMaxHeatOutputSwtF")
        if "SystemMaxHeatOutputDeltaTempF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SystemMaxHeatOutputDeltaTempF")
        if "SystemMaxHeatOutputGpm" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SystemMaxHeatOutputGpm")
        if "EmitterMaxSafeSwtF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing EmitterMaxSafeSwtF")
        if "CirculatorPumpMaxGpm" not in d2.keys():
            raise SchemaError(f"dict {d2} missing CirculatorPumpMaxGpm")
        if "HeatpumpTariffGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HeatpumpTariffGtEnumSymbol")
        if d2["HeatpumpTariffGtEnumSymbol"] in DistributionTariff000SchemaEnum.symbols:
            d2["HeatpumpTariff"] = DistributionTariffMap.type_to_local(
                d2["HeatpumpTariffGtEnumSymbol"]
            )
        else:
            d2["HeatpumpTariff"] = DistributionTariff.default()
        if "HeatpumpEnergySupplyTypeGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HeatpumpEnergySupplyTypeGtEnumSymbol")
        if (
            d2["HeatpumpEnergySupplyTypeGtEnumSymbol"]
            in EnergySupplyType000SchemaEnum.symbols
        ):
            d2["HeatpumpEnergySupplyType"] = EnergySupplyTypeMap.type_to_local(
                d2["HeatpumpEnergySupplyTypeGtEnumSymbol"]
            )
        else:
            d2["HeatpumpEnergySupplyType"] = EnergySupplyType.default()
        if "BoostTariffGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing BoostTariffGtEnumSymbol")
        if d2["BoostTariffGtEnumSymbol"] in DistributionTariff000SchemaEnum.symbols:
            d2["BoostTariff"] = DistributionTariffMap.type_to_local(
                d2["BoostTariffGtEnumSymbol"]
            )
        else:
            d2["BoostTariff"] = DistributionTariff.default()
        if "BoostEnergySupplyTypeGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing BoostEnergySupplyTypeGtEnumSymbol")
        if (
            d2["BoostEnergySupplyTypeGtEnumSymbol"]
            in EnergySupplyType000SchemaEnum.symbols
        ):
            d2["BoostEnergySupplyType"] = EnergySupplyTypeMap.type_to_local(
                d2["BoostEnergySupplyTypeGtEnumSymbol"]
            )
        else:
            d2["BoostEnergySupplyType"] = EnergySupplyType.default()
        if "StandardOfferPriceDollarsPerMwh" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StandardOfferPriceDollarsPerMwh")
        if "DistributionTariffDollarsPerMwh" not in d2.keys():
            raise SchemaError(f"dict {d2} missing DistributionTariffDollarsPerMwh")
        if "AmbientTempStoreF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing AmbientTempStoreF")
        if "StorePassiveLossRatio" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StorePassiveLossRatio")
        if "RoomTempF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing RoomTempF")
        if "AmbientPowerInKw" not in d2.keys():
            raise SchemaError(f"dict {d2} missing AmbientPowerInKw")
        if "ZeroPotentialEnergyWaterTempF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ZeroPotentialEnergyWaterTempF")
        if "EmitterPumpFeedbackModelGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing EmitterPumpFeedbackModelGtEnumSymbol")
        if (
            d2["EmitterPumpFeedbackModelGtEnumSymbol"]
            in EmitterPumpFeedbackModel000SchemaEnum.symbols
        ):
            d2["EmitterPumpFeedbackModel"] = EmitterPumpFeedbackModelMap.type_to_local(
                d2["EmitterPumpFeedbackModelGtEnumSymbol"]
            )
        else:
            d2["EmitterPumpFeedbackModel"] = PumpModel.default()
        if "MixingValveFeedbackModelGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MixingValveFeedbackModelGtEnumSymbol")
        if (
            d2["MixingValveFeedbackModelGtEnumSymbol"]
            in MixingValveFeedbackModel000SchemaEnum.symbols
        ):
            d2["MixingValveFeedbackModel"] = MixingValveFeedbackModelMap.type_to_local(
                d2["MixingValveFeedbackModelGtEnumSymbol"]
            )
        else:
            d2["MixingValveFeedbackModel"] = MixingValveModel.default()
        if "CautiousMixingValveTempDeltaF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing CautiousMixingValveTempDeltaF")
        if "Cop1TempF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing Cop1TempF")
        if "Cop4TempF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing Cop4TempF")
        if "CurrencyUnitGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing CurrencyUnitGtEnumSymbol")
        if (
            d2["CurrencyUnitGtEnumSymbol"]
            in RecognizedCurrencyUnit000SchemaEnum.symbols
        ):
            d2["CurrencyUnit"] = RecognizedCurrencyUnitMap.type_to_local(
                d2["CurrencyUnitGtEnumSymbol"]
            )
        else:
            d2["CurrencyUnit"] = RecognizedCurrencyUnit.default()
        if "TempUnitGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TempUnitGtEnumSymbol")
        if d2["TempUnitGtEnumSymbol"] in RecognizedTemperatureUnit000SchemaEnum.symbols:
            d2["TempUnit"] = RecognizedTemperatureUnitMap.type_to_local(
                d2["TempUnitGtEnumSymbol"]
            )
        else:
            d2["TempUnit"] = RecognizedTemperatureUnit.default()
        if "TimezoneString" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TimezoneString")
        if "HomeCity" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HomeCity")
        if "StorageSteps" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StorageSteps")
        if "HouseWorstCaseTempF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HouseWorstCaseTempF")
        if "SystemMaxHeatOutputKwAvg" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SystemMaxHeatOutputKwAvg")
        if "K" not in d2.keys():
            raise SchemaError(f"dict {d2} missing K")
        if "IsRegulating" not in d2.keys():
            raise SchemaError(f"dict {d2} missing IsRegulating")
        if "SliceDurationMinutes" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SliceDurationMinutes")
        if "PowerRequiredByHouseFromSystemAvgKwList" not in d2.keys():
            raise SchemaError(
                f"dict {d2} missing PowerRequiredByHouseFromSystemAvgKwList"
            )
        if "OutsideTempF" not in d2.keys():
            raise SchemaError(f"dict {d2} missing OutsideTempF")
        if "RealtimeElectricityPrice" not in d2.keys():
            raise SchemaError(f"dict {d2} missing RealtimeElectricityPrice")
        if "DistributionPrice" not in d2.keys():
            raise SchemaError(f"dict {d2} missing DistributionPrice")
        if "RegulationPrice" not in d2.keys():
            raise SchemaError(f"dict {d2} missing RegulationPrice")
        if "RtElecPriceUid" not in d2.keys():
            raise SchemaError(f"dict {d2} missing RtElecPriceUid")
        if "WeatherUid" not in d2.keys():
            raise SchemaError(f"dict {d2} missing WeatherUid")
        if "DistPriceUid" not in d2.keys():
            d2["DistPriceUid"] = None
        if "RegPriceUid" not in d2.keys():
            d2["RegPriceUid"] = None
        if "StartYearUtc" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StartYearUtc")
        if "StartMonthUtc" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StartMonthUtc")
        if "StartDayUtc" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StartDayUtc")
        if "StartHourUtc" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StartHourUtc")
        if "StartMinuteUtc" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StartMinuteUtc")
        if "StartingStoreIdx" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StartingStoreIdx")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return FloParamsHeatpumpwithbooststore(
            StoreSizeGallons=d2["StoreSizeGallons"],
            MaxStoreTempF=d2["MaxStoreTempF"],
            StoreMaxPowerKw=d2["StoreMaxPowerKw"],
            RatedHeatpumpElectricityKw=d2["RatedHeatpumpElectricityKw"],
            MaxHeatpumpSourceWaterTempF=d2["MaxHeatpumpSourceWaterTempF"],
            SystemMaxHeatOutputSwtF=d2["SystemMaxHeatOutputSwtF"],
            SystemMaxHeatOutputDeltaTempF=d2["SystemMaxHeatOutputDeltaTempF"],
            SystemMaxHeatOutputGpm=d2["SystemMaxHeatOutputGpm"],
            EmitterMaxSafeSwtF=d2["EmitterMaxSafeSwtF"],
            CirculatorPumpMaxGpm=d2["CirculatorPumpMaxGpm"],
            HeatpumpTariff=d2["HeatpumpTariff"],
            HeatpumpEnergySupplyType=d2["HeatpumpEnergySupplyType"],
            BoostTariff=d2["BoostTariff"],
            BoostEnergySupplyType=d2["BoostEnergySupplyType"],
            StandardOfferPriceDollarsPerMwh=d2["StandardOfferPriceDollarsPerMwh"],
            DistributionTariffDollarsPerMwh=d2["DistributionTariffDollarsPerMwh"],
            AmbientTempStoreF=d2["AmbientTempStoreF"],
            StorePassiveLossRatio=d2["StorePassiveLossRatio"],
            RoomTempF=d2["RoomTempF"],
            AmbientPowerInKw=d2["AmbientPowerInKw"],
            ZeroPotentialEnergyWaterTempF=d2["ZeroPotentialEnergyWaterTempF"],
            EmitterPumpFeedbackModel=d2["EmitterPumpFeedbackModel"],
            MixingValveFeedbackModel=d2["MixingValveFeedbackModel"],
            CautiousMixingValveTempDeltaF=d2["CautiousMixingValveTempDeltaF"],
            Cop1TempF=d2["Cop1TempF"],
            Cop4TempF=d2["Cop4TempF"],
            CurrencyUnit=d2["CurrencyUnit"],
            TempUnit=d2["TempUnit"],
            TimezoneString=d2["TimezoneString"],
            HomeCity=d2["HomeCity"],
            StorageSteps=d2["StorageSteps"],
            HouseWorstCaseTempF=d2["HouseWorstCaseTempF"],
            SystemMaxHeatOutputKwAvg=d2["SystemMaxHeatOutputKwAvg"],
            K=d2["K"],
            IsRegulating=d2["IsRegulating"],
            SliceDurationMinutes=d2["SliceDurationMinutes"],
            PowerRequiredByHouseFromSystemAvgKwList=d2[
                "PowerRequiredByHouseFromSystemAvgKwList"
            ],
            OutsideTempF=d2["OutsideTempF"],
            RealtimeElectricityPrice=d2["RealtimeElectricityPrice"],
            DistributionPrice=d2["DistributionPrice"],
            RegulationPrice=d2["RegulationPrice"],
            RtElecPriceUid=d2["RtElecPriceUid"],
            WeatherUid=d2["WeatherUid"],
            DistPriceUid=d2["DistPriceUid"],
            RegPriceUid=d2["RegPriceUid"],
            StartYearUtc=d2["StartYearUtc"],
            StartMonthUtc=d2["StartMonthUtc"],
            StartDayUtc=d2["StartDayUtc"],
            StartHourUtc=d2["StartHourUtc"],
            StartMinuteUtc=d2["StartMinuteUtc"],
            StartingStoreIdx=d2["StartingStoreIdx"],
            TypeName=d2["TypeName"],
            Version="000",
        )
