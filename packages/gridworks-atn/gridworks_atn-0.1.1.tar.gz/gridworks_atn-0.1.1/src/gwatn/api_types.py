""" List of all the types used"""
from typing import Dict
from typing import List
from typing import no_type_check

from gwatn.types import AcceptedBid_Maker
from gwatn.types import AtnParamsHeatpumpwithbooststore_Maker
from gwatn.types import AtnParamsReportHeatpumpwithbooststore_Maker
from gwatn.types import BaseGNodeGt_Maker
from gwatn.types import DiscoverycertAlgoCreate_Maker
from gwatn.types import DispatchContractConfirmed_Maker
from gwatn.types import FloParamsHeatpumpwithbooststore_Maker
from gwatn.types import GNodeGt_Maker
from gwatn.types import GNodeInstanceGt_Maker
from gwatn.types import GtDispatchBoolean_Maker
from gwatn.types import GwCertId_Maker
from gwatn.types import HeartbeatA_Maker
from gwatn.types import HeartbeatAlgoAudit_Maker
from gwatn.types import HeartbeatB_Maker
from gwatn.types import InitialTadeedAlgoCreate_Maker
from gwatn.types import InitialTadeedAlgoOptin_Maker
from gwatn.types import InitialTadeedAlgoTransfer_Maker
from gwatn.types import JoinDispatchContract_Maker
from gwatn.types import LatestPrice_Maker
from gwatn.types import MarketSlot_Maker
from gwatn.types import MarketTypeGt_Maker
from gwatn.types import NewTadeedAlgoOptin_Maker
from gwatn.types import NewTadeedSend_Maker
from gwatn.types import OldTadeedAlgoReturn_Maker
from gwatn.types import PriceQuantity_Maker
from gwatn.types import PriceQuantityUnitless_Maker
from gwatn.types import Ready_Maker
from gwatn.types import SimScadaDriverReport_Maker
from gwatn.types import SimTimestep_Maker
from gwatn.types import SlaEnter_Maker
from gwatn.types import SnapshotHeatpumpwithbooststore_Maker
from gwatn.types import SuperStarter_Maker
from gwatn.types import SupervisorContainerGt_Maker
from gwatn.types import TadeedSpecsHack_Maker
from gwatn.types import TavalidatorcertAlgoCreate_Maker
from gwatn.types import TavalidatorcertAlgoTransfer_Maker
from gwatn.types import TerminalassetCertifyHack_Maker


TypeMakerByName: Dict[str, HeartbeatA_Maker] = {}


@no_type_check
def type_makers() -> List[HeartbeatA_Maker]:
    return [
        AcceptedBid_Maker,
        AtnParamsHeatpumpwithbooststore_Maker,
        AtnParamsReportHeatpumpwithbooststore_Maker,
        BaseGNodeGt_Maker,
        DiscoverycertAlgoCreate_Maker,
        DispatchContractConfirmed_Maker,
        FloParamsHeatpumpwithbooststore_Maker,
        GNodeGt_Maker,
        GNodeInstanceGt_Maker,
        GtDispatchBoolean_Maker,
        GwCertId_Maker,
        HeartbeatA_Maker,
        HeartbeatAlgoAudit_Maker,
        HeartbeatB_Maker,
        InitialTadeedAlgoCreate_Maker,
        InitialTadeedAlgoOptin_Maker,
        InitialTadeedAlgoTransfer_Maker,
        JoinDispatchContract_Maker,
        LatestPrice_Maker,
        MarketSlot_Maker,
        MarketTypeGt_Maker,
        NewTadeedAlgoOptin_Maker,
        NewTadeedSend_Maker,
        OldTadeedAlgoReturn_Maker,
        PriceQuantity_Maker,
        PriceQuantityUnitless_Maker,
        Ready_Maker,
        SimScadaDriverReport_Maker,
        SimTimestep_Maker,
        SlaEnter_Maker,
        SnapshotHeatpumpwithbooststore_Maker,
        SuperStarter_Maker,
        SupervisorContainerGt_Maker,
        TadeedSpecsHack_Maker,
        TavalidatorcertAlgoCreate_Maker,
        TavalidatorcertAlgoTransfer_Maker,
        TerminalassetCertifyHack_Maker,
    ]


for maker in type_makers():
    TypeMakerByName[maker.type_name] = maker


def version_by_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are TypeNames, values are versions
    """

    v: Dict[str, str] = {
        "accepted.bid": "000",
        "atn.params.heatpumpwithbooststore": "000",
        "atn.params.report.heatpumpwithbooststore": "000",
        "base.g.node.gt": "002",
        "discoverycert.algo.create": "000",
        "dispatch.contract.confirmed": "000",
        "flo.params.heatpumpwithbooststore": "000",
        "g.node.gt": "002",
        "g.node.instance.gt": "000",
        "gt.dispatch.boolean": "110",
        "gw.cert.id": "000",
        "heartbeat.a": "100",
        "heartbeat.algo.audit": "000",
        "heartbeat.b": "000",
        "initial.tadeed.algo.create": "000",
        "initial.tadeed.algo.optin": "002",
        "initial.tadeed.algo.transfer": "000",
        "join.dispatch.contract": "000",
        "latest.price": "000",
        "market.slot": "000",
        "market.type.gt": "000",
        "new.tadeed.algo.optin": "000",
        "new.tadeed.send": "000",
        "old.tadeed.algo.return": "000",
        "price.quantity": "000",
        "price.quantity.unitless": "000",
        "ready": "001",
        "sim.scada.driver.report": "000",
        "sim.timestep": "000",
        "sla.enter": "000",
        "snapshot.heatpumpwithbooststore": "000",
        "super.starter": "000",
        "supervisor.container.gt": "000",
        "tadeed.specs.hack": "000",
        "tavalidatorcert.algo.create": "000",
        "tavalidatorcert.algo.transfer": "000",
        "terminalasset.certify.hack": "000",
    }

    return v


def status_by_versioned_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are versioned TypeNames, values are type status
    """

    v: Dict[str, str] = {
        "accepted.bid.000": "Pending",
        "atn.params.heatpumpwithbooststore.000": "Active",
        "atn.params.report.heatpumpwithbooststore.000": "Pending",
        "base.g.node.gt.002": "Pending",
        "discoverycert.algo.create.000": "Pending",
        "dispatch.contract.confirmed.000": "Pending",
        "flo.params.heatpumpwithbooststore.000": "Active",
        "g.node.gt.002": "Pending",
        "g.node.instance.gt.000": "Pending",
        "gt.dispatch.boolean.110": "Pending",
        "gw.cert.id.000": "Active",
        "heartbeat.a.100": "Pending",
        "heartbeat.algo.audit.000": "Pending",
        "heartbeat.b.000": "Pending",
        "initial.tadeed.algo.create.000": "Active",
        "initial.tadeed.algo.optin.002": "Active",
        "initial.tadeed.algo.transfer.000": "Active",
        "join.dispatch.contract.000": "Active",
        "latest.price.000": "Pending",
        "market.slot.000": "Pending",
        "market.type.gt.000": "Pending",
        "new.tadeed.algo.optin.000": "Active",
        "new.tadeed.send.000": "Active",
        "old.tadeed.algo.return.000": "Active",
        "price.quantity.000": "Pending",
        "price.quantity.unitless.000": "Pending",
        "ready.001": "Pending",
        "sim.scada.driver.report.000": "Pending",
        "sim.timestep.000": "Pending",
        "sla.enter.000": "Pending",
        "snapshot.heatpumpwithbooststore.000": "Pending",
        "super.starter.000": "Pending",
        "supervisor.container.gt.000": "Pending",
        "tadeed.specs.hack.000": "Pending",
        "tavalidatorcert.algo.create.000": "Active",
        "tavalidatorcert.algo.transfer.000": "Active",
        "terminalasset.certify.hack.000": "Pending",
    }

    return v
