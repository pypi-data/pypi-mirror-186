import csv
import random
import time
import uuid
from typing import Dict
from typing import List

import dotenv
import gridworks.utils as utils
import pendulum
from gridworks.utils import RestfulResponse

import gwmm.config as config
from gwmm.data_classes.market_type import Rt60Gate30B
from gwmm.enums import MarketPriceUnit
from gwmm.enums import UniverseType
from gwmm.types import AcceptedBid
from gwmm.types import AcceptedBid_Maker
from gwmm.types import AtnBid
from gwmm.types import MarketMakerInfo_Maker
from gwmm.types import MarketPrice
from gwmm.types import MarketSlot
from gwmm.types import MarketTypeGt
from gwmm.types import MarketTypeGt_Maker
from gwmm.types.price_quantity_unitless import PriceQuantityUnitless


class MarketMakerApi:
    def __init__(
        self,
        settings: config.MarketMakerSettings = config.MarketMakerSettings(
            _env_file=dotenv.find_dotenv()
        ),
    ):
        self.settings = settings

        self.alias = settings.g_node_alias
        self.universe_type = UniverseType(self.settings.universe_type_value)
        self.mm_type: MarketTypeGt = MarketTypeGt_Maker.dc_to_tuple(Rt60Gate30B)
        self.market_types: List[MarketTypeGt] = [self.mm_type]
        # sample_market = self.market_types[0]
        # sample_market_name = f"{sample_market.Name}.{self.alias}"
        # sample_market_slot_name = f"{sample_market_name}.1577836800"
        sample_market_name = "rt60gate30b.d1.isone.ver.keene"
        sample_market_slot_name = "rt60gate30b.d1.isone.ver.keene.1577836800"
        self.info = MarketMakerInfo_Maker(
            g_node_alias=self.alias,
            market_type_list=self.market_types,
            sample_market_name=sample_market_name,
            sample_market_slot_name=sample_market_slot_name,
        ).tuple

    def check_market_creds(self, payload: AtnBid) -> RestfulResponse:
        """
        payload.MarketFeeTxId needs to be a transaction id for a payment
        from the bidder's Algo address to the MarketMaker. Linking the bidder's
        GNodeInstance to the bidder's Algo address can be checked with a call
        to the World registry.

        The Market fee has to be sufficient (comparable to gas).

        The transaction has to have happened within a reasonable time (last hour).

        The bidder's Algo address must own a single TaTradingRights, and that
        must be the current TaTradingRights for the corresponding TerminalAsset.

        Most of this will be tucked into axioms checked by Bid_Maker, which
        will run for the bid generator as well and hopefully catch a lot of
        the mistakes before the bid is submitted.

        Args:
            payload (Bid): _description_

        Returns:
            RestfulResponse: HttpStatusCode 200 if everything checks out,
            otherwise 422 with Note explaining why.
        """
        txn = payload.SignedMarketFeeTxn
        return RestfulResponse(Note="Has TaTradingRights; paid market fee")

    def atn_bid(self, payload: AtnBid, ts_ns: int) -> RestfulResponse:
        ts = ts_ns * 10**-9
        rr = self.check_market_creds(payload)
        if rr.HttpStatusCode > 200:
            return rr
        msn = payload.MarketSlotName
        slot: MarketSlot = utils.market_slot_from_name(msn)

        if slot.Type not in self.market_types:
            return RestfulResponse(
                Note=f"MarketType {slot.Type} not served by {self.alias}!",
                HttpStatusCode=422,
            )
        if slot.MarketMakerAlias != self.alias:
            return RestfulResponse(
                Note=f"{payload.MarketSlotName} not run by {self.alias}!",
                HttpStatusCode=422,
            )
        gate_closing = slot.StartUnixS - slot.Type.GateClosingSeconds
        ts_str = pendulum.from_timestamp(ts).to_iso8601_string()
        gc_str = pendulum.from_timestamp(gate_closing).to_iso8601_string()
        if gate_closing < ts:
            note = (
                f"Missed gate closing: Received time {ts_str}, Gate closing {gc_str}"
                "Contract not accepted"
            )
            return RestfulResponse(
                Note=note,
                HttpStatusCode=422,
            )

        # this should be sharpened by checking that there are no MarketMakers
        # between the two - but that requires some GNodeTree mechanics in the MarketMaker
        if not payload.BidderAlias.startswith(self.alias):
            return RestfulResponse(
                Note=f"MarketMaker {self.alias} not an ancestor of {payload.BidderAlias}!"
            )
        # Move the following into AtnBid_Maker axioms:
        if payload.PriceUnit != slot.Type.PriceUnit:
            return RestfulResponse(
                Note=f"PriceUnit {payload.PriceUnit} must match market type "
                f"{slot.Type.Name} price_unit {slot.Type.PriceUnit}",
                HttpStatusCode=422,
            )
        if payload.QuantityUnit != slot.Type.QuantityUnit:
            return RestfulResponse(
                Note=f"QuantityUnit {payload.QuantityUnit} must match market type "
                f"{slot.Type.Name} quantity_unit {slot.Type.QuantityUnit}",
                HttpStatusCode=422,
            )
        bid_list = payload.BidList
        if payload.InjectionIsPositive:
            demand_bid_list: List[PriceQuantityUnitless] = []
            for gen_pq in payload.BidList:
                demand_pq = PriceQuantityUnitless(
                    PriceTimes1000=gen_pq.PriceTimes1000,
                    QuantityTimes1000=-gen_pq.QuantityTimes1000,
                )
                demand_bid_list.append(demand_pq)
            bid_list = demand_bid_list
        accepted_bid = AcceptedBid(
            MarketSlotName=payload.MarketSlotName,
            BidderAlias=payload.BidderAlias,
            BidList=bid_list,
            ReceivedTimeUnixNs=ts_ns,
        )
        # TODO: put slot books in database and/or redis
        # self.slot_books[slot.Type.Name][slot.StartUnixS].Bids.append(rb)
        ts_str = pendulum.from_timestamp(ts).to_iso8601_string()
        gc_str = pendulum.from_timestamp(gate_closing).to_iso8601_string()

        return RestfulResponse(
            Note=f"Contract live. Received time {ts_str}, Gate closing {gc_str}",
            PayloadTypeName="accepted.bid",
            PayloadAsDict=accepted_bid.dict(),
        )

    def time(self):
        # TODO: find time from in-memory redis
        hack_first_time = pendulum.datetime(year=2020, month=1, day=1, hour=5)
        return hack_first_time.int_timestamp
