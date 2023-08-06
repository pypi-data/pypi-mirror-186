"""Type dispatch.contract.confirmed, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwatn.types.atn_params_heatpumpwithbooststore import (
    AtnParamsHeatpumpwithbooststore,
)
from gwatn.types.atn_params_heatpumpwithbooststore import (
    AtnParamsHeatpumpwithbooststore_Maker,
)


def check_is_uuid_canonical_textual(v: str) -> None:
    """
    UuidCanonicalTextual format:  A string of hex words separated by hyphens
    of length 8-4-4-4-12.

    Raises:
        ValueError: if not UuidCanonicalTextual format
    """
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}")
    if len(x) != 5:
        raise ValueError(f"{v} split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            raise ValueError(f"Words of {v} are not all hex")
    if len(x[0]) != 8:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[1]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[2]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[3]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[4]) != 12:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")


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


class DispatchContractConfirmed(BaseModel):
    """Message sent from AtomicTNode back to SCADA via Rabbit .

    Paired with join.dispatch.contract. Sent from AtomicTNode back to SCADA
    once the AtomicTNode has successfully finished bootstrapping the Dispatch
    Contract and opted in. Once it has done this, the Dispatch Contract is ready
     to collect audit information about heartbeats, dispatch, energy and power.

    https://gridworks.readthedocs.io/en/latest/dispatch-contract.html
    """

    FromGNodeAlias: str = Field(
        title="FromGNodeAlias",
    )
    FromGNodeInstanceId: str = Field(
        title="FromGNodeInstanceId",
    )
    SignedProof: str = Field(
        title="SignedProof",
    )
    AtnParams: AtnParamsHeatpumpwithbooststore = Field(
        title="AtnParams",
    )
    TypeName: Literal["dispatch.contract.confirmed"] = "dispatch.contract.confirmed"
    Version: str = "000"

    @validator("FromGNodeAlias")
    def _check_from_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("FromGNodeInstanceId")
    def _check_from_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

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
        d["AtnParams"] = self.AtnParams.as_dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class DispatchContractConfirmed_Maker:
    type_name = "dispatch.contract.confirmed"
    version = "000"

    def __init__(
        self,
        from_g_node_alias: str,
        from_g_node_instance_id: str,
        signed_proof: str,
        atn_params: AtnParamsHeatpumpwithbooststore,
    ):
        self.tuple = DispatchContractConfirmed(
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            SignedProof=signed_proof,
            AtnParams=atn_params,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: DispatchContractConfirmed) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> DispatchContractConfirmed:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> DispatchContractConfirmed:
        d2 = dict(d)
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeAlias")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeInstanceId")
        if "SignedProof" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SignedProof")
        if "AtnParams" not in d2.keys():
            raise SchemaError(f"dict {d2} missing AtnParams")
        if not isinstance(d2["AtnParams"], dict):
            raise SchemaError(
                f"d['AtnParams'] {d2['AtnParams']} must be a AtnParamsHeatpumpwithbooststore!"
            )
        atn_params = AtnParamsHeatpumpwithbooststore_Maker.dict_to_tuple(
            d2["AtnParams"]
        )
        d2["AtnParams"] = atn_params
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return DispatchContractConfirmed(
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeInstanceId=d2["FromGNodeInstanceId"],
            SignedProof=d2["SignedProof"],
            AtnParams=d2["AtnParams"],
            TypeName=d2["TypeName"],
            Version="000",
        )
