import logging
import subprocess

import gridworks.algo_utils as algo_utils
import gridworks.dev_utils.algo_setup as algo_setup
import gridworks.errors as errors
import requests
from algosdk import encoding
from algosdk.future import transaction
from algosdk.v2client.algod import AlgodClient
from gridworks.algo_utils import BasicAccount
from gridworks.algo_utils import MultisigAccount
from gridworks.utils import RestfulResponse

import gwatn.config as config

# Schemata sent by homeowner
from gwatn.types import InitialTadeedAlgoOptin_Maker
from gwatn.types import SlaEnter_Maker
from gwatn.types import TerminalassetCertifyHack_Maker


LOGGER = logging.getLogger(__name__)


class DevTaOwner:
    def __init__(
        self,
        settings: config.TaOwnerSettings,
    ):
        LOGGER.info(f"Initializing TaOwner for {settings.initial_ta_alias}")

        self.settings = settings
        self.client: AlgodClient = AlgodClient(
            settings.algo_api_secrets.algod_token.get_secret_value(),
            settings.public.algod_address,
        )
        self.acct: BasicAccount = BasicAccount(
            private_key=self.settings.sk.get_secret_value()
        )
        self.seed_fund_own_account()
        self.validator_multi = MultisigAccount(
            version=1,
            threshold=2,
            addresses=[
                self.settings.public.gnf_admin_addr,
                self.settings.validator_addr,
            ],
        )
        if self.settings.initial_ta_alias == "d1.isone.ver.keene.holly.ta":
            ta_daemon_sk = config.TaDaemonSettings().sk.get_secret_value()
            self.ta_daemon_acct = BasicAccount(ta_daemon_sk)
        else:
            self.ta_daemon_acct: BasicAccount = BasicAccount()
            self.settings.ta_daemon_addr = self.ta_daemon_acct.addr

        self.ta_daemon_api_root = (
            f"{self.settings.ta_daemon_api_fqdn}:{self.settings.ta_daemon_api_port}"
        )
        LOGGER.info(f"ta_owner_addr = {self.acct.addr}")
        LOGGER.info(f"ta_daemon_addr = {self.ta_daemon_acct.addr}")

    def start(self):
        LOGGER.info(
            f"Starting {self.short_alias}-daemon on port {self.settings.ta_daemon_api_port}"
        )
        self.pr: subprocess.Popen = self.start_ta_daemon()

    def stop(self):
        # self.pr.terminate()
        cmd = f"docker stop {self.short_alias}-daemon"
        subprocess.run(cmd.split())
        cmd = f"docker rm {self.short_alias}-daemon"
        subprocess.run(cmd.split())

    def start_ta_daemon(self) -> subprocess.Popen:
        LOGGER.info("Starting TaDaemon")
        port = self.settings.ta_daemon_api_port
        cmd = f"docker run  -e TAD_SK={self.ta_daemon_acct.sk} -e TAD_TA_OWNER_ADDR={self.acct.addr} -p {port}:8000 --name {self.short_alias}-daemon jessmillar/python-ta-daemon:chaos__2e38992__20221231"
        pr = subprocess.Popen(
            cmd.split(),
        )

        daemon_api_root = (
            f"{self.settings.ta_daemon_api_fqdn}:{self.settings.ta_daemon_api_port}"
        )
        api_endpoint = f"{daemon_api_root}/"
        daemon_up: bool = False
        while not daemon_up:
            try:
                daemon_up = True
                requests.get(url=api_endpoint)
            except:
                daemon_up = False
        return pr

    def __repr__(self) -> str:
        return self.short_alias

    ##########################
    # Messages Sent
    ##########################

    def enter_sla(self) -> RestfulResponse:
        ta_alias = self.settings.initial_ta_alias
        payload = SlaEnter_Maker(terminal_asset_alias=ta_alias).tuple
        api_endpoint = f"{self.ta_daemon_api_root}/sla-enter/"
        r = requests.post(url=api_endpoint, json=payload.as_dict())
        if r.status_code > 200:
            if r.status_code == 422:
                note = f"Error entering SLA: " + r.json()["detail"]
            else:
                note = r.reason
            rr = RestfulResponse(Note=note, HttpStatusCode=422)
            return rr
        return RestfulResponse(**r.json())

    def request_ta_certification(self) -> RestfulResponse:
        ta_alias = self.settings.initial_ta_alias
        payload = TerminalassetCertifyHack_Maker(
            terminal_asset_alias=ta_alias,
            ta_daemon_api_fqdn=self.settings.ta_daemon_api_fqdn,
            ta_daemon_api_port=self.settings.ta_daemon_api_port,
            ta_daemon_addr=self.settings.ta_daemon_addr,
        ).tuple

        LOGGER.info(f"Requesting certification for {ta_alias}")
        api_endpoint = (
            f"{self.settings.ta_validator_api_root}/terminalasset-certification/"
        )
        try:
            r = requests.post(url=api_endpoint, json=payload.as_dict())
        except:
            return RestfulResponse(
                Note=f"Validator address {api_endpoint} does not exist!",
                HttpStatusCode=422,
            )
        if r.status_code > 200:
            if r.status_code == 422:
                note = (
                    f"Error posting terminalasset-certification to validator: "
                    + r.json()["detail"]
                )
            else:
                note = r.reason
            rr = RestfulResponse(Note=note, HttpStatusCode=422)
            return rr
        rr1 = RestfulResponse(**r.json())
        rr2 = self.post_initial_tadeed_algo_optin()
        if rr2.HttpStatusCode > 200:
            return rr2
        return rr1

    def post_initial_tadeed_algo_optin(self) -> RestfulResponse:
        """
         - Sends 50 algos to TaDaemon acct
         - Sends InitialTadeedAlgoOptin to TaDaemon, with signed
         funding txn for proof of identity.

        Returns:
            RestfulResponse
        """
        LOGGER.info("Funding TaDaemon")
        required_algos = config.Public().ta_deed_consideration_algos
        txn = transaction.PaymentTxn(
            sender=self.acct.addr,
            receiver=self.settings.ta_daemon_addr,
            amt=required_algos * 10**6,
            sp=self.client.suggested_params(),
        )
        signed_txn = txn.sign(self.acct.sk)
        try:
            self.client.send_transaction(signed_txn)
        except Exception as e:
            note = f"Algorand Failure sending transaction: {e}"
            raise errors.AlgoError(note)
        algo_utils.wait_for_transaction(self.client, signed_txn.get_txid())
        payload = InitialTadeedAlgoOptin_Maker(
            terminal_asset_alias=self.settings.initial_ta_alias,
            ta_owner_addr=self.acct.addr,
            validator_addr=self.settings.ta_validator_addr,
            signed_initial_daemon_funding_txn=encoding.msgpack_encode(signed_txn),
        ).tuple
        api_endpoint = f"{self.ta_daemon_api_root}/initial-tadeed-algo-optin/"
        r = requests.post(url=api_endpoint, json=payload.as_dict())
        if r.status_code > 200:
            if r.status_code == 422:
                note = "Issue with InitialTadeedAlgoOptin" + r.json()["detail"]
            else:
                note = r.reason
            rr = RestfulResponse(Note=note, HttpStatusCode=422)
            return rr
        return RestfulResponse(**r.json())

    ##########################
    # dev methods
    ########################
    def seed_fund_own_account(self):
        algos = self.settings.public.ta_deed_consideration_algos + 1
        if algo_utils.algos(self.acct.addr) < algos:
            algo_setup.dev_fund_account(
                settings=self.settings,
                to_addr=self.acct.addr,
                amt_in_micros=10**6 * algos,
            )
        LOGGER.info(
            f"HollyHomeowner acct {self.acct.addr_short_hand} balance: ~{algo_utils.algos(self.acct.addr)} Algos"
        )

    @property
    def short_alias(self) -> str:
        alias = self.settings.initial_ta_alias
        words = alias.split(".")
        return ".".join(words[-2:-1])
