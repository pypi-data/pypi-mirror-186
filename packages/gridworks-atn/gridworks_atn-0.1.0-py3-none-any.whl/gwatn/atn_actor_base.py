""" AtnActorBase """
import functools
import logging
import random
import time
from abc import abstractmethod
from typing import no_type_check

import pendulum
from algosdk.v2client.algod import AlgodClient
from gridworks.algo_utils import BasicAccount
from gridworks.message import as_enum

from gwatn.config import AtnSettings
from gwatn.enums import GNodeRole
from gwatn.enums import MessageCategorySymbol
from gwatn.enums import UniverseType
from gwatn.two_channel_actor_base import TwoChannelActorBase
from gwatn.types import DispatchContractConfirmed_Maker
from gwatn.types import HeartbeatA
from gwatn.types import HeartbeatA_Maker
from gwatn.types import HeartbeatB
from gwatn.types import HeartbeatB_Maker
from gwatn.types import JoinDispatchContract
from gwatn.types import JoinDispatchContract_Maker
from gwatn.types import LatestPrice
from gwatn.types import LatestPrice_Maker
from gwatn.types import SimTimestep
from gwatn.types import SimTimestep_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(sasctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)


class AtnActorBase(TwoChannelActorBase):
    def __init__(self, settings: AtnSettings):
        super().__init__(settings=settings)
        self.settings: AtnSettings = settings
        self.acct: BasicAccount = BasicAccount(settings.sk.get_secret_value())
        self.client: AlgodClient = AlgodClient(
            settings.algo_api_secrets.algod_token.get_secret_value(),
            settings.public.algod_address,
        )
        self.universe_type = as_enum(
            self.settings.universe_type_value, UniverseType, UniverseType.default()
        )
        self._time: float = self.get_initial_time_s()

    def local_rabbit_startup(self) -> None:
        rjb = MessageCategorySymbol.rjb.value
        tc_alias_lrh = self.settings.time_coordinator_alias.replace(".", "-")
        binding = f"{rjb}.{tc_alias_lrh}.timecoordinator.sim-timestep"

        cb = functools.partial(self.on_timecoordinator_bindok, binding=binding)
        self._consume_channel.queue_bind(
            self.queue_name, "timecoordinatormic_tx", routing_key=binding, callback=cb
        )
        LOGGER.info(
            f"Queue {self.queue_name} bound to timecoordinatormic_tx with {binding} "
        )
        self.strategy_rabbit_startup()

    def strategy_rabbit_startup(self) -> None:
        pass

    @no_type_check
    def on_timecoordinator_bindok(self, _unused_frame, binding) -> None:
        LOGGER.info(f"Queue {self.queue_name} bound with {binding}")

    def time(self) -> float:
        if self.universe_type == UniverseType.Dev:
            return self._time
        else:
            return time.time()

    def get_initial_time_s(self) -> float:
        if self.universe_type == UniverseType.Dev:
            return self.settings.initial_time_unix_s
        else:
            return time.time()

    def prepare_for_death(self) -> None:
        self.actor_main_stopped = True

    ########################
    ## Receives
    ########################

    def route_message(
        self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA
    ) -> None:
        if payload.TypeName == HeartbeatA_Maker.type_name:
            if from_role != GNodeRole.Supervisor:
                LOGGER.info(
                    f"Ignoring HeartbeatA from GNode with role {from_role}; expects Supervisor"
                )
            try:
                self.heartbeat_from_super(from_alias, payload)
            except:
                LOGGER.exception("Error in heartbeat_received")
        elif payload.TypeName == HeartbeatB_Maker.type_name:
            if from_role != GNodeRole.SCADA:
                LOGGER.info(
                    f"Ignoring HeartbeatB from GNode with role {from_role}; expects SCADA"
                )
            try:
                self.heartbeat_from_partner(payload)
            except:
                LOGGER.exception("Error in heartbeat_from_partner")
        elif payload.TypeName == JoinDispatchContract_Maker.type_name:
            if from_role != GNodeRole.SCADA:
                LOGGER.info(
                    f"Ignoring HeartbeatB from GNode with role {from_role}; expects SCADA"
                )
            try:
                self.join_dispatch_contract_from_scada(payload)
            except:
                LOGGER.exception("join_dispatch_contract_from_scada")
        elif payload.TypeName == LatestPrice_Maker.type_name:
            if from_role == GNodeRole.MarketMaker:
                try:
                    self.latest_price_from_market_maker(payload)
                except:
                    LOGGER.exception("Error in latest_price_from_market_maker")
        elif payload.TypeName == SimTimestep_Maker.type_name:
            try:
                self.timestep_from_timecoordinator(payload)
            except:
                LOGGER.exception("Error in timestep_from_timecoordinator")

    def heartbeat_from_super(self, from_alias: str, ping: HeartbeatA) -> None:
        pong = HeartbeatA_Maker(
            my_hex=str(random.choice("0123456789abcdef")), your_last_hex=ping.MyHex
        ).tuple

        self.send_message(
            payload=pong,
            to_role=GNodeRole.Supervisor,
            to_g_node_alias=self.settings.my_super_alias,
        )

        LOGGER.debug(
            f"[{self.alias}] Sent HB: SuHex {pong.YourLastHex}, AtnHex {pong.MyHex}"
        )

    def heartbeat_from_partner(self, ping: HeartbeatB) -> None:
        """
        This is the Atn's half of the DispatchContract Heartbeat pattern.
        It:
          - Checks that it has opted into a DispatchContract
          - Checks the FromGNodeAlias and FromGNodeInstanceId to validate partner
          - Updates the last hex received (for use at the top of the next minute) along w time received
        [more info](https://gridworks.readthedocs.io/en/latest/dispatch-contract.html)

        Args:
            payload (HeartbeatB): The latest heartbeat received from its
            SCADA partner

        """
        ...

    @abstractmethod
    def join_dispatch_contract_from_scada(self, payload: JoinDispatchContract) -> None:
        raise NotImplementedError

    @abstractmethod
    def latest_price_from_market_maker(self, payload: LatestPrice) -> None:
        raise NotImplementedError

    def timestep_from_timecoordinator(self, payload: SimTimestep):
        if self._time == 0:
            self._time = payload.TimeUnixS
            self.new_timestep(payload)
            LOGGER.info(f"TIME STARTED: {self.time_str()}")
        elif self._time < payload.TimeUnixS:
            self._time = payload.TimeUnixS
            self.new_timestep(payload)
            LOGGER.debug(f"Time is now {self.time_str()}")
        elif self._time == payload.TimeUnixS:
            self.repeat_timestep(payload)

    @abstractmethod
    def new_timestep(self, payload: SimTimestep) -> None:
        # LOGGER.info("New timestep in atn_actor_base")
        raise NotImplementedError

    @abstractmethod
    def repeat_timestep(self, payload: SimTimestep) -> None:
        # LOGGER.info("Timestep received again in atn_actor_base")
        raise NotImplementedError

    def time_str(self) -> str:
        return pendulum.from_timestamp(self.time()).strftime("%m/%d/%Y, %H:%M")
