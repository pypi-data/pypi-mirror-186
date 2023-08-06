from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class TelemetryName(StrEnum):
    """
    Specifies the name of sensed data reported by SCADA

    Choices and descriptions:

      * Unknown:
      * PowerW:
      * RelayState:
      * WaterTempCTimes1000:
      * WaterTempFTimes1000:
      * WaterFlowGpmTimes100:
      * CurrentRmsMicroAmps:
      * GallonsPerMinuteTimes10:
      * CurrentRmsMilliAmps:
      * VoltageRmsMilliVolts:
      * PhaseAngleDegreesTimes10:
      * WattHours:
    """

    Unknown = auto()
    PowerW = auto()
    PhaseAngleDegreesTimes10 = auto()
    WattHours = auto()
    RelayState = auto()
    WaterTempCTimes1000 = auto()
    WaterTempFTimes1000 = auto()
    WaterFlowGpmTimes100 = auto()
    CurrentRmsMicroAmps = auto()
    GallonsPerMinuteTimes10 = auto()
    CurrentRmsMilliAmps = auto()
    VoltageRmsMilliVolts = auto()

    @classmethod
    def default(cls) -> "TelemetryName":
        """
        Returns default value Unknown
        """
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
