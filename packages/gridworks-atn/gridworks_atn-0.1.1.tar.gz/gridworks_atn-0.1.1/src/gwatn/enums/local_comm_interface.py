from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class LocalCommInterface(StrEnum):
    """
    Categorization of in-house comm mechanisms for SCADA

    Choices and descriptions:

      * Analog_4_20_mA:
      * RS232:
      * I2C:
      * Wifi:
      * SimRabbit:
      * Unknown:
      * Ethernet:
      * OneWire:
      * RS485:
    """

    ANALOG_4_20_MA = auto()
    RS232 = auto()
    I2C = auto()
    WIFI = auto()
    SIMRABBIT = auto()
    UNKNOWN = auto()
    ETHERNET = auto()
    ONEWIRE = auto()
    RS485 = auto()

    @classmethod
    def default(cls) -> "LocalCommInterface":
        """
        Returns default value UNKNOWN
        """
        return cls.UNKNOWN

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
