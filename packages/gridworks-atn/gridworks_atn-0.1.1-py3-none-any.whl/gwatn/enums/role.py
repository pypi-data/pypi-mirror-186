from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class Role(StrEnum):
    """
    Determines the functional role of a SpaceHeat node supervised by a SCADA

    Choices and descriptions:

      * PrimaryScada:
      * HomeAlone:
      * PrimaryMeter:
      * BoostElement:
      * BooleanActuator:
      * Atn:
      * TankWaterTempSensor:
      * PipeTempSensor:
      * RoomTempSensor:
      * OutdoorTempSensor:
      * Heatpump:
      * MultipurposeSensor:
      * CurrentTransformer:
      * RadiatorFan:
      * PipeFlowMeter:
      * BaseboardRadiator:
      * CirculatorPump:
      * DedicatedThermalStore:
      * HeatedSpace:
      * HydronicPipe:
      * Outdoors:
    """

    PrimaryScada = auto()
    HomeAlone = auto()
    Heatpump = auto()
    MultipurposeSensor = auto()
    CurrentTransformer = auto()
    RadiatorFan = auto()
    PipeFlowMeter = auto()
    BaseboardRadiator = auto()
    CirculatorPump = auto()
    DedicatedThermalStore = auto()
    HeatedSpace = auto()
    HydronicPipe = auto()
    PrimaryMeter = auto()
    Outdoors = auto()
    BoostElement = auto()
    BooleanActuator = auto()
    Atn = auto()
    TankWaterTempSensor = auto()
    PipeTempSensor = auto()
    RoomTempSensor = auto()
    OutdoorTempSensor = auto()

    @classmethod
    def default(cls) -> "Role":
        """
        Returns default value HeatedSpace
        """
        return cls.HeatedSpace

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
