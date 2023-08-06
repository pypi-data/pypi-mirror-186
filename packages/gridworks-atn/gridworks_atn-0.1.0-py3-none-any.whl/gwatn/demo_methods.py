import json
import logging
from typing import List

import gridworks.api_utils as api_utils
from gridworks.algo_utils import BasicAccount
from gridworks.utils import RestfulResponse
from pydantic import SecretStr
from rich.pretty import pprint

import gwatn.config as config
from gwatn.dev_utils import DevDiscoverer
from gwatn.dev_utils import DevTaOwner
from gwatn.dev_utils import DevValidator
from gwatn.types import BaseGNodeGt_Maker
from gwatn.types import TadeedSpecsHack_Maker


logging.basicConfig(level="INFO")
LOGGER = logging.getLogger(__name__)


def certify_molly_metermaid() -> RestfulResponse:
    molly = DevValidator(config.ValidatorSettings())
    cert_idx = api_utils.get_validator_cert_idx(validator_addr=molly.acct.addr)
    if cert_idx is not None:
        raise Exception(
            f"There is already a Validator Certificate for Molly! Please ./sandbox reset and start the demo over."
        )
    return molly.post_tavalidatorcert_algo_create()


def create_ta_owner(plant: str) -> DevTaOwner:
    file = f"input_data/eventstore/d1.isone.ver.keene.{plant}.ta-tadeed.specs.hack.json"
    with open(file) as f:
        payload = TadeedSpecsHack_Maker.dict_to_tuple(json.load(f))

    settings = config.TaOwnerSettings()
    ta_owner_acct = BasicAccount()
    settings.sk = SecretStr(ta_owner_acct.sk)
    settings.initial_ta_alias = payload.TerminalAssetAlias
    settings.ta_daemon_api_port = payload.DaemonPort
    ta_owner = DevTaOwner(settings)
    return ta_owner


def create_ta_owners(plants: List[str]) -> List[DevTaOwner]:
    owners: List[DevTaOwner] = []
    for plant in plants:
        owners.append(create_ta_owner(plant))
    return owners


def start_ta_owners(ta_owners: List[DevTaOwner]) -> RestfulResponse:
    started_ta_owners: List[DevTaOwner] = []
    for owner in ta_owners:
        try:
            owner.start()
        except:
            for owner in started_ta_owners:
                owner.stop()
            return RestfulResponse(
                Note=f"Error starting {owner.settings.initial_ta_alias} owner.",
                HttpStatusCode=422,
            )
        started_ta_owners.append(owner)
    return RestfulResponse(Note="Successfully started all TaOwners and TaDaemons")


def create_terminal_asset(ta_owner: DevTaOwner) -> RestfulResponse:
    molly = DevValidator(config.ValidatorSettings())
    rr = ta_owner.request_ta_certification()
    if rr.HttpStatusCode > 200:
        note = (
            f"Stopping demo due to errors in requesting ta certification for "
            f"{ta_owner.settings.initial_ta_alias}" + rr.Note
        )
        return RestfulResponse(Note=note, HttpStatusCode=422)
    pprint(rr)
    terminal_asset = BaseGNodeGt_Maker.dict_to_tuple(rr.PayloadAsDict)
    ta_deed_idx = terminal_asset.OwnershipDeedNftId
    LOGGER.info(f"Made TaDeed {ta_deed_idx} for {terminal_asset.Alias}")

    rr = molly.certify_terminal_asset(
        ta_deed_idx=ta_deed_idx,
        ta_daemon_addr=ta_owner.ta_daemon_acct.addr,
        ta_owner_addr=ta_owner.acct.addr,
        micro_lat=ta_owner.settings.micro_lat,
        micro_lon=ta_owner.settings.micro_lon,
    )

    if rr.HttpStatusCode > 200:
        note = (
            "Stopping demo due to errors certifying terminal asset for "
            f"{ta_owner.settings.initial_ta_alias}" + rr.Note
        )
        return RestfulResponse(Note=note, HttpStatusCode=422)
    pprint(rr)
    return rr


def create_terminal_assets(ta_owners: List[DevTaOwner]) -> RestfulResponse:
    for ta_owner in ta_owners:
        if not isinstance(ta_owner, DevTaOwner):
            return RestfulResponse(
                Note=f"{ta_owner} is not a DevTaOwner!", HttpStatusCode=422
            )
    for ta_owner in ta_owners:
        rr = create_terminal_asset(ta_owner)
        if rr.HttpStatusCode > 200:
            for ta_owner in ta_owners:
                ta_owner.stop()
            return rr
    return RestfulResponse(Note="Success with create_terminal_assets")


def enter_slas(ta_owners: List[DevTaOwner]) -> RestfulResponse:
    for ta_owner in ta_owners:
        if not isinstance(ta_owner, DevTaOwner):
            return RestfulResponse(
                Note=f"{ta_owner} is not a DevTaOwner!", HttpStatusCode=422
            )
    for ta_owner in ta_owners:
        rr = ta_owner.enter_sla()
        if rr.HttpStatusCode > 200:
            for ta_owner in ta_owners:
                ta_owner.stop()
            return rr
    return RestfulResponse(Note="Success with entering ServiceLevelAgreements")


def create_new_ctn():
    ada = DevDiscoverer(settings=config.DiscovererSettings())
    rr = ada.post_discoverycert_algo_create()
    LOGGER.info("Ada received response to discoverycert algo")


demo_plant_names: List[str] = [
    "holly",
    "juniper",
    "violet",
    "lettuce",
    "mushroom",
    "nettle",
    "orange",
    "pine",
    "quinoi",
    "rose",
    "leek",
    "umbrella",
    "kale",
    "wasabi",
    "yarrow",
    "zinnia",
    "apple",
    "beet",
    "acacia",
    "buxus",
    "calathea",
    "chestnut",
    "columnea",
    "cuphea",
    "dracaena",
    "eucharis",
    "gardenia",
    "hedera",
    "ixora",
    "lemon",
    "mansoa",
    "murraya",
    "pepper",
    "pilea",
    "redwood",
    "stapelia",
    "acca",
    "begonia",
    "callisia",
    "citronella",
    "cordyline",
    "cyanotis",
    "drosera",
    "euphorbia",
    "gasteria",
    "orchid",
    "jacobinia",
    "lepanthes",
    "maple",
    "myrtle",
    "pandanus",
    "punica",
    "rhapis",
    "strelitzia",
    "acorus",
    "billbergia",
    "campanula",
    "cleyera",
    "corokia",
    "cycas",
    "duchesnea",
    "exacum",
    "gloriosa",
    "hibiscus",
    "jasmine",
    "lilium",
    "maranta",
    "neoregelia",
    "passiflora",
    "pineapple",
    "rhoeo",
    "thistle",
    "aechmea",
    "biophytum",
    "capsicum",
    "clivia",
    "costus",
    "cyclamen",
    "carrot",
    "fatshedera",
    "gongora",
    "hoffmannia",
    "jatropha",
    "redbud",
    "maxillaria",
    "nepenthes",
    "celery",
    "pisonia",
    "rivina",
    "thunia",
    "aeonium",
    "birch",
    "caryota",
    "coccoloba",
    "cottonwood",
    "cyperus",
    "elm",
    "fatsia",
    "guzmania",
    "howea",
    "kalanchoe",
    "lily",
    "medinilla",
    "nerine",
    "pellionia",
    "pleione",
    "rochea",
    "tolmiea",
    "agapetes",
    "blechnum",
    "cattleya",
    "coconut",
    "cotyledon",
    "datura",
    "encyclia",
    "ficus",
    "gynura",
    "hoya",
    "kohleria",
    "liriope",
    "miltonia",
    "nertera",
    "pentas",
    "plumbago",
    "ruellia",
    "tomato",
    "agave",
    "bouvardia",
    "ceropegia",
    "coffea",
    "crassula",
    "dionaea",
    "epidendrum",
    "fir",
    "haemaria",
    "hydrangea",
    "laelia",
    "livistona",
    "mimosa",
    "oak",
    "peperomia",
    "polyscias",
    "saffron",
    "radish",
    "aloe",
    "brunfelsia",
    "chenolle",
    "coleus",
    "crinum",
    "dipladenia",
    "episcia",
    "fittonia",
    "haworth",
    "impatiens",
    "lantana",
    "macodes",
    "molineria",
    "oleander",
    "petunia",
    "primrose",
    "sanchezia",
    "willow",
    "beech",
    "cactus",
    "cherimoya",
    "colmanara",
    "crossandra",
    "dischidia",
    "erica",
    "fuchsia",
    "haworthia",
    "iresine",
    "laurus",
    "mallow",
    "monstera",
    "oncidium",
    "phoenix",
    "primula",
    "spruce",
    "camellia",
]
