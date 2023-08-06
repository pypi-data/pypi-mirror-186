from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MakeModel(StrEnum):
    """
    Determines Make/Model of device associated to a Spaceheat Node supervised by SCADA

    Choices and descriptions:

      * Freedom__Relay:
      * OmegaEzo__Ftb800Flo:
      * UnknownMake__UnknownModel:
      * GridWorks__SimBool30AmpRelay:
      * Gridworks__SimPm1:
      * GridWorks__WaterTempHighPrecision:
      * NCD__PR8-14-SPST:
      * Adafruit__642:
      * SchneiderElectric__Iem3455:
      * OpenEnergy__EmonPi:
      * Egauge__3010:
      * Rheem__XE50T10H45U0:
      * Magnelab__SCT-0300-050:
      * YMDC__SCT013-100:
      * G1__NCD_ADS1115__TEWA_NTC_10K_A: 4.6 kOhm 5% accuracy voltage divider resistor, NCD ADS1115 i2c 16 bit resolution chip, Tewa TT0P-10KC3-T105 -1500 pipe measurement NTC 10K thermistor.
      * G1__NCD_ADS1115__AMPH_NTC_10K_A: 4.6 kOhm 5% accuracy voltage divider resistor, NCD ADS1115 i2c 16 bit resolution chip, Amphenol MA100GG103BN thermistor
    """

    FREEDOM__RELAY = auto()
    OMEGAEZO__FTB800FLO = auto()
    UNKNOWNMAKE__UNKNOWNMODEL = auto()
    GRIDWORKS__SIMBOOL30AMPRELAY = auto()
    MAGNELAB__SCT0300050 = auto()
    YMDC__SCT013100 = auto()
    G1__NCD_ADS1115__TEWA_NTC_10K_A = auto()
    G1__NCD_ADS1115__AMPH_NTC_10K_A = auto()
    GRIDWORKS__SIMPM1 = auto()
    GRIDWORKS__WATERTEMPHIGHPRECISION = auto()
    NCD__PR814SPST = auto()
    ADAFRUIT__642 = auto()
    SCHNEIDERELECTRIC__IEM3455 = auto()
    OPENENERGY__EMONPI = auto()
    EGAUGE__3010 = auto()
    RHEEM__XE50T10H45U0 = auto()

    @classmethod
    def default(cls) -> "MakeModel":
        """
        Returns default value UNKNOWNMAKE__UNKNOWNMODEL
        """
        return cls.UNKNOWNMAKE__UNKNOWNMODEL

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
