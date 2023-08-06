""" List of all the types used"""
from typing import Dict
from typing import List
from typing import no_type_check

from gwmm.types import AcceptedBid_Maker
from gwmm.types import AtnBid_Maker
from gwmm.types import GNodeGt_Maker
from gwmm.types import HeartbeatA_Maker
from gwmm.types import LatestPrice_Maker
from gwmm.types import MarketBook_Maker
from gwmm.types import MarketMakerInfo_Maker
from gwmm.types import MarketPrice_Maker
from gwmm.types import MarketSlot_Maker
from gwmm.types import MarketTypeGt_Maker
from gwmm.types import PriceQuantity_Maker
from gwmm.types import PriceQuantityUnitless_Maker
from gwmm.types import Ready_Maker
from gwmm.types import SimTimestep_Maker


TypeMakerByName: Dict[str, HeartbeatA_Maker] = {}


@no_type_check
def type_makers() -> List[HeartbeatA_Maker]:
    return [
        AcceptedBid_Maker,
        AtnBid_Maker,
        GNodeGt_Maker,
        HeartbeatA_Maker,
        LatestPrice_Maker,
        MarketBook_Maker,
        MarketMakerInfo_Maker,
        MarketPrice_Maker,
        MarketSlot_Maker,
        MarketTypeGt_Maker,
        PriceQuantity_Maker,
        PriceQuantityUnitless_Maker,
        Ready_Maker,
        SimTimestep_Maker,
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
        "atn.bid": "001",
        "g.node.gt": "002",
        "heartbeat.a": "100",
        "latest.price": "000",
        "market.book": "000",
        "market.maker.info": "000",
        "market.price": "000",
        "market.slot": "000",
        "market.type.gt": "000",
        "price.quantity": "000",
        "price.quantity.unitless": "000",
        "ready": "001",
        "sim.timestep": "000",
    }

    return v


def status_by_versioned_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are versioned TypeNames, values are type status
    """

    v: Dict[str, str] = {
        "accepted.bid.000": "Pending",
        "atn.bid.001": "Pending",
        "g.node.gt.002": "Pending",
        "heartbeat.a.100": "Pending",
        "latest.price.000": "Pending",
        "market.book.000": "Pending",
        "market.maker.info.000": "Pending",
        "market.price.000": "Pending",
        "market.slot.000": "Pending",
        "market.type.gt.000": "Pending",
        "price.quantity.000": "Pending",
        "price.quantity.unitless.000": "Pending",
        "ready.001": "Pending",
        "sim.timestep.000": "Pending",
    }

    return v
