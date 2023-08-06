from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ActorClass(StrEnum):
    """
    Determines code running Spaceheat Node supervised by SCADA

    Choices and descriptions:

      * NoActor:
      * PrimaryScada:
      * PrimaryMeter:
      * BooleanActuator:
      * SimpleSensor:
      * HomeAlone:
      * Atn:
      * MultipurposeSensor:
      * Thermostat:
    """

    NoActor = auto()
    PrimaryScada = auto()
    PrimaryMeter = auto()
    BooleanActuator = auto()
    SimpleSensor = auto()
    HomeAlone = auto()
    Atn = auto()
    MultipurposeSensor = auto()
    Thermostat = auto()

    @classmethod
    def default(cls) -> "ActorClass":
        """
        Returns default value NoActor
        """
        return cls.NoActor

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
