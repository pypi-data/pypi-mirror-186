"""Type heartbeat.algo.audit, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwatn.types.heartbeat_b import HeartbeatB
from gwatn.types.heartbeat_b import HeartbeatB_Maker


def check_is_left_right_dot(v: str) -> None:
    """
    LeftRightDot format: Lowercase alphanumeric words separated by periods,
    most significant word (on the left) starting with an alphabet character.

    Raises:
        ValueError: if not LeftRightDot format
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate {v} into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(f"Most significant word of {v} must start with alphabet char.")
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of {v} split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of {v} must be lowercase.")


def check_is_algo_msg_pack_encoded(v: str) -> None:
    """
    AlgoMSgPackEncoded format: the format of an  transaction sent to
    the Algorand blockchain.

    Raises:
        ValueError: if not AlgoMSgPackEncoded  format
    """
    import algosdk

    try:
        algosdk.encoding.future_msgpack_decode(v)
    except Exception as e:
        raise ValueError(f"Not AlgoMsgPackEncoded format: {e}")


class HeartbeatAlgoAudit(BaseModel):
    """.

    Algo payload with report of last HeartbeatB sent to partner via Rabbit, to be sent to
    DispatchContract on Algo blockchain
    """

    SignedProof: str = Field(
        title="Tiny signed payment to DispatchContract to prove identity",
    )
    Heartbeat: HeartbeatB = Field(
        title="Heartbeat sender last sent to its partner",
    )
    TypeName: Literal["heartbeat.algo.audit"] = "heartbeat.algo.audit"
    Version: str = "000"

    @validator("SignedProof")
    def _check_signed_proof(cls, v: str) -> str:
        try:
            check_is_algo_msg_pack_encoded(v)
        except ValueError as e:
            raise ValueError(
                f"SignedProof failed AlgoMsgPackEncoded format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        d["Heartbeat"] = self.Heartbeat.as_dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class HeartbeatAlgoAudit_Maker:
    type_name = "heartbeat.algo.audit"
    version = "000"

    def __init__(self, signed_proof: str, heartbeat: HeartbeatB):
        self.tuple = HeartbeatAlgoAudit(
            SignedProof=signed_proof,
            Heartbeat=heartbeat,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: HeartbeatAlgoAudit) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> HeartbeatAlgoAudit:
        """
        Given a serialized JSON type object, returns the Python class object
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> HeartbeatAlgoAudit:
        d2 = dict(d)
        if "SignedProof" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SignedProof")
        if "Heartbeat" not in d2.keys():
            raise SchemaError(f"dict {d2} missing Heartbeat")
        if not isinstance(d2["Heartbeat"], dict):
            raise SchemaError(f"d['Heartbeat'] {d2['Heartbeat']} must be a HeartbeatB!")
        heartbeat = HeartbeatB_Maker.dict_to_tuple(d2["Heartbeat"])
        d2["Heartbeat"] = heartbeat
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return HeartbeatAlgoAudit(
            SignedProof=d2["SignedProof"],
            Heartbeat=d2["Heartbeat"],
            TypeName=d2["TypeName"],
            Version="000",
        )
