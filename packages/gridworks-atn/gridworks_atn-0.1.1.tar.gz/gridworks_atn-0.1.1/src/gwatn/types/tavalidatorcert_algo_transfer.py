"""Type tavalidatorcert.algo.transfer, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

import gridworks.algo_utils as algo_utils
import gridworks.api_utils as api_utils
import gridworks.gw_config as config
from algosdk import encoding
from algosdk.future import transaction
from algosdk.v2client.algod import AlgodClient
from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator


def check_is_algo_address_string_format(v: str) -> None:
    """
    AlgoAddressStringFormat format: The public key of a private/public Ed25519
    key pair, transformed into an  Algorand address, by adding a 4-byte checksum
    to the end of the public key and then encoding in base32.

    Raises:
        ValueError: if not AlgoAddressStringFormat format
    """
    import algosdk

    at = algosdk.abi.AddressType()
    try:
        result = at.decode(at.encode(v))
    except Exception as e:
        raise ValueError(f"Not AlgoAddressStringFormat: {e}")


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


class TavalidatorcertAlgoTransfer(BaseModel):
    """Used for Step 2 of TaValidator certification.

    Meant to be sent from a pending TaValidator  to the GNodeFactory (Gnf), so the
    Gnf will transfer its ValidatorCert to the pending TaValidator's Algorand address.
    [More info](https://gridworks.readthedocs.io/en/latest/ta-validator.html).
    """

    ValidatorAddr: str = Field(
        title="The address of the pending TaValidator",
    )
    HalfSignedCertTransferMtx: str = Field(
        title="Algo multi-transaction for certificate transfer, with 1 of 2 signatures",
    )
    TypeName: Literal["tavalidatorcert.algo.transfer"] = "tavalidatorcert.algo.transfer"
    Version: str = "000"

    @validator("ValidatorAddr")
    def check_validator_addr(cls, v: str) -> str:
        """
        Axiom 4: TaValidator has sufficient Algos.
        ValidatorAddr must have enough Algos to meet the GNodeFactory criterion.
        """
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"ValidatorAddr failed AlgoAddressStringFormat format validation: {e}"
            )

        if algo_utils.algos(v) < config.Public().ta_validator_funding_threshold_algos:
            raise ValueError(
                f"ValidatorAddr insufficiently funded with {algo_utils.algos(v)} algos. "
                f" Needs {config.Public().ta_validator_funding_threshold_algos} algos. "
            )

        return v

    @validator("HalfSignedCertTransferMtx")
    def _check_half_signed_cert_transfer_mtx(cls, v: str) -> str:
        try:
            check_is_algo_msg_pack_encoded(v)
        except ValueError as e:
            raise ValueError(
                f"HalfSignedCertTransferMtx failed AlgoMsgPackEncoded format validation: {e}"
            )
        return v

    @root_validator(pre=True)
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: Is correct Multisig.
        Decoded HalfSignedCertTransferMtx must have type MultisigTransaction from the
        2-sig MultiAccount  [GnfAdminAddr, ValidatorAddr], signed by the ValidatorAddr.
        [More info](https://gridworks.readthedocs.io/en/latest/g-node-factory.html#gnfadminaddr)
        """
        mtx = encoding.future_msgpack_decode(v.get("HalfSignedCertTransferMtx", None))
        ValidatorAddr = v.get("ValidatorAddr")
        gnf_admin_addr = config.Public().gnf_admin_addr
        multi = algo_utils.MultisigAccount(
            version=1,
            threshold=2,
            addresses=[gnf_admin_addr, ValidatorAddr],
        )

        if not isinstance(mtx, transaction.MultisigTransaction):
            raise ValueError(
                "Axiom 1: Decoded HalfSignedCertTransferMtx must have type MultisigTransaction,"
                f" got {type(mtx)}."
            )

        if not multi.addr == mtx.multisig.address():
            raise ValueError(
                "Axiom 1: Decoded HalfSignedCertTransferMtx must come from the 2-sig MultiAccount ,"
                f" [GnfAdminAddr, ValidatorAddr], got {type(mtx)}."
            )
        if mtx.multisig.subsigs[1].signature is None:
            raise ValueError(
                "Axiom 1: Decoded HalfSignedCertTransferMtx missing TaValidator signature.}"
            )
        return v

    @root_validator
    def check_axiom_2(cls, v: dict) -> dict:
        """
        Axiom 2: Transfers correct certificate.
         - The transaction must be the transfer of an Algorand Standard Asset
         - The sender must be the 2-sig Multi [GnfAdminAddr, TaValidatorAddr], which also created and owns the ASA
         - It must be getting sent to the ValidatorAddr
         -The ASA must have:
           - Total = 1
           - UnitName=VLDITR
           - GnfAdminAddr as manage
           - AssetName not blank.
        - The transfer amount must be 1
        [More info](https://gridworks.readthedocs.io/en/latest/ta-validator.html#tavalidator-certificate)

        Axiom 3: TaValidator has opted in.
        ValidatorAddr must be opted into the transferring ASA.
        """
        mtx = encoding.future_msgpack_decode(v.get("HalfSignedCertTransferMtx", None))
        txn = mtx.transaction
        gnf_admin_addr = config.Public().gnf_admin_addr
        ValidatorAddr = v.get("ValidatorAddr")
        multi = algo_utils.MultisigAccount(
            version=1,
            threshold=2,
            addresses=[gnf_admin_addr, ValidatorAddr],
        )

        if not isinstance(txn, transaction.AssetTransferTxn):
            raise ValueError(
                "Axiom 2: The transaction must have type AssetTransferTxn"
                f" got {type(txn)}."
            )
        if not txn.sender == multi.addr:
            raise ValueError(
                "Axiom 2: The transfer must be sending from the 2-sig Multi [GNfAdminAddr, TaValidatorAddr]"
            )

        settings = config.VanillaSettings()
        client: AlgodClient = AlgodClient(
            settings.algo_api_secrets.algod_token.get_secret_value(),
            settings.public.algod_address,
        )
        multi_balances = algo_utils.get_balances(client, multi.addr)
        if not txn.index in multi_balances.keys():
            raise ValueError(
                "Axiom 2: The 2-sig Multi [GnfAdminAddr, TaValidatorAddr] must have created and own the ASA"
            )
        if multi_balances[txn.index] != 1:
            raise ValueError(
                "Axiom 2: The ASA creator must be the 2-sig Multi [GnfAdminAddr, TaValidatorAddr]"
            )
        if not txn.receiver == ValidatorAddr:
            raise ValueError("Axiom 2: The ASA receiver must be the TaValiadatorAddr")
        if not txn.amount == 1:
            raise ValueError(f"Axiom 2: The amount sent must be 1, not {txn.amount}")
        asa_params = client.asset_info(txn.index)["params"]
        if asa_params["total"] != 1:
            raise ValueError(
                f"Axiom 2: The ASA Total must be 1, not {asa_params['total']}"
            )
        if asa_params["decimals"] != 0:
            raise ValueError(
                f"Axiom 2: The ASA Decimals must be 0, not {asa_params['decimals']}"
            )
        if asa_params["manager"] != gnf_admin_addr:
            raise ValueError(
                f"Axiom 2: The ASA manager must be GnfAdminAddr, not {asa_params['manager']}"
            )
        if asa_params["unit-name"] != "VLDTR":
            raise ValueError(
                f"Axiom 2: The ASA UnitName must be 'VLDTR, not {asa_params['unit-name']}"
            )
        if asa_params["name"] is None:
            raise ValueError(f"Axiom 2: The ASA AssetName cannot be None")
        if asa_params["name"] == "":
            raise ValueError(f"Axiom 2: The ASA AssetName cannot be blank")

        # Axiom 3 check
        validator_balances = algo_utils.get_balances(client, ValidatorAddr)
        if txn.index not in validator_balances.keys():
            raise ValueError(
                f"Axiom 3: ValidatorAddr must be opted into the transferring ASA."
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class TavalidatorcertAlgoTransfer_Maker:
    type_name = "tavalidatorcert.algo.transfer"
    version = "000"

    def __init__(self, validator_addr: str, half_signed_cert_transfer_mtx: str):
        self.tuple = TavalidatorcertAlgoTransfer(
            ValidatorAddr=validator_addr,
            HalfSignedCertTransferMtx=half_signed_cert_transfer_mtx,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: TavalidatorcertAlgoTransfer) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> TavalidatorcertAlgoTransfer:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> TavalidatorcertAlgoTransfer:
        d2 = dict(d)
        if "ValidatorAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValidatorAddr")
        if "HalfSignedCertTransferMtx" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HalfSignedCertTransferMtx")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return TavalidatorcertAlgoTransfer(
            ValidatorAddr=d2["ValidatorAddr"],
            HalfSignedCertTransferMtx=d2["HalfSignedCertTransferMtx"],
            TypeName=d2["TypeName"],
            Version="000",
        )
