"""MarketMaker"""

import csv
import logging
import math
import random
import time
import uuid
from typing import Dict
from typing import List

import dotenv
import gridworks.algo_utils as algo_utils
import gridworks.utils as utils
import pendulum
import requests
from gridworks.algo_utils import BasicAccount
from gridworks.utils import RestfulResponse

import gwmm.config as config
from gwmm.data_classes.market_type import Rt60Gate30B
from gwmm.enums import GNodeRole
from gwmm.enums import MarketPriceUnit
from gwmm.enums import MarketTypeName
from gwmm.enums import MessageCategory
from gwmm.enums import UniverseType
from gwmm.market_maker_base import MarketMakerBase
from gwmm.types import AtnBid
from gwmm.types import LatestPrice_Maker
from gwmm.types import MarketBook
from gwmm.types import MarketMakerInfo_Maker
from gwmm.types import MarketPrice
from gwmm.types import MarketSlot
from gwmm.types import MarketSlot_Maker
from gwmm.types import MarketTypeGt
from gwmm.types import MarketTypeGt_Maker
from gwmm.types import Ready_Maker
from gwmm.types import SimTimestep
from gwmm.types.price_quantity_unitless import PriceQuantityUnitless


LOG_FORMAT = (
    "%(levelname) -10s %(sasctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)


class MarketMaker(MarketMakerBase):
    def __init__(
        self,
        settings: config.MarketMakerSettings = config.MarketMakerSettings(
            _env_file=dotenv.find_dotenv()
        ),
    ):
        super().__init__(settings=settings)
        self.universe_type = UniverseType(self.settings.universe_type_value)
        self.acct: BasicAccount = BasicAccount(self.settings.sk.get_secret_value())
        # self.check_funding()
        self.mm_type: MarketTypeGt = MarketTypeGt_Maker.dc_to_tuple(Rt60Gate30B)
        self.market_types: List[MarketTypeGt] = [self.mm_type]

        self.market_type_names: List[MarketTypeName] = list(
            map(lambda x: x.Name, self.market_types)
        )

        self.slot_books: Dict[MarketTypeName, Dict[int, MarketBook]] = {
            self.mm_type.Name: {}
        }

        self.clearing_price: Dict[MarketTypeName, Dict[int, MarketPrice]] = {
            self.mm_type.Name: {}
        }

        self.hack_clearing_price: Dict[int, MarketPrice] = {}
        self.initialize_hack_clearing_price()
        LOGGER.info("MarketMaker initialized")

    def check_funding(self):
        if algo_utils.algos(self.acct.addr) < 0.5:
            raise Exception(f"MarketMaker must be funded!")

    def initialize_hack_clearing_price(self) -> Dict[int, MarketPrice]:
        file = "input_data/dev_prices.csv"
        from typing import List

        rows: List[str] = []
        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
        start_row = 14
        init_t = int(self.settings.initial_time_unix_s)
        start = (init_t - (init_t % 3600)) + 3600
        for ts_idx in range(8760):
            time = start + ts_idx * 3600
            price = float(rows[start_row + ts_idx][0])
            self.hack_clearing_price[time] = MarketPrice(
                ValueTimes1000=int(1000 * price),
                Unit=MarketPriceUnit.USDPerMWh,
            )

    def ready(self) -> None:
        payload = Ready_Maker(
            from_g_node_alias=self.alias,
            from_g_node_instance_id=self.g_node_instance_id,
            time_unix_s=int(self.time()),
        ).tuple
        self.send_message(
            payload=payload,
            to_role=GNodeRole.TimeCoordinator,
            to_g_node_alias=self.settings.my_time_coordinator_alias,
        )

    def new_timestep(self, payload: SimTimestep) -> None:
        if self._time in self.slot_books[self.mm_type.Name].keys():
            # get book from redis or other db
            pass
            # book: MarketBook = self.slot_books[self.mm_type.Name][self.time_s]
            # try:
            #     self.clear_market(book)
            # except Exception as e:
            #     LOGGER.warning(f"failure with mm.clear_market(book): {e}")
            # LOGGER.info("Broadcasting Market Book")
            # self.send_message(
            #     payload=book,
            #     message_category=MessageCategory.RabbitJsonBroadcast,
            #     radio_channel=self.mm_type.Name,
            # )
        try:
            self.broadcast_latest_prices()
        except Exception as e:
            LOGGER.warning(
                f"Failure: mm.broadcast_latest_prices() in new_timestep: {e}"
            )
        # try:
        #     self.update_slot_books()
        # except Exception as e:
        #     LOGGER.warning("Failure: mm.update_slot_books(): {e}")
        self.ready()

    def repeated_timestep(self, payload: SimTimestep) -> None:
        LOGGER.info("Received timestep again")
        try:
            self.broadcast_latest_prices()
            self.ready()
        except Exception as e:
            LOGGER.warning(
                f"Failure: mm.broadcast_latest_prices() in repeated_timestep: {e}"
            )

    def broadcast_latest_prices(self) -> None:
        market_type = self.market_types[0]
        start = self.time() - (self.time() % 3600)
        slot = MarketSlot(
            Type=market_type, MarketMakerAlias=self.alias, StartUnixS=start
        )
        try:
            mp = self.hack_clearing_price[int(self.time())]
        except:
            LOGGER.warning(f"Missing price for {self.time_str()}. NOT SENDING A PRICE")
            return
        payload = LatestPrice_Maker(
            from_g_node_alias=self.alias,
            from_g_node_instance_id=self.settings.g_node_instance_id,
            price_times1000=mp.ValueTimes1000,
            price_unit=slot.Type.PriceUnit,
            market_slot_name=utils.name_from_market_slot(slot),
            message_id=str(uuid.uuid4()),
            irl_time_utc=pendulum.from_timestamp(time.time()).to_iso8601_string(),
        ).tuple
        LOGGER.info(
            f"[{self.time_str()}: {self.short_alias}] Broadcasting price: "
            f"${round(mp.ValueTimes1000 / 1000, 3)}/MWh"
            # f" {mp.Unit.value}"
        )
        self.send_message(
            payload=payload,
            message_category=MessageCategory.RabbitJsonBroadcast,
            radio_channel=market_type.Name.value,
        )

    def real_broadcast_latest_prices(self) -> None:
        for market_type in self.market_types:
            starts: List[int] = list(self.slot_books[market_type.Name].keys())
            if len(starts) > 0:
                t = self._time
                latest_market_start = max(list(filter(lambda x: x <= t, starts)))
                slot = MarketSlot(
                    Type=market_type,
                    MarketMakerAlias=self.alias,
                    StartUnixS=latest_market_start,
                )
                slot_name = utils.name_from_market_slot(slot)

                try:
                    this_market_cp_dict: Dict[int, MarketPrice] = self.clearing_price[
                        market_type.Name
                    ]
                except:
                    raise Exception(
                        f"Expected to have clearing prices for {market_type.Name}!"
                    )
                try:
                    latest_market_price = this_market_cp_dict[slot.StartUnixS]
                except:
                    raise Exception(
                        f"Expected to have clearing prices for {slot_name}!"
                    )

                if slot.Type.PriceUnit != latest_market_price.Unit:
                    raise Exception(
                        f"Got slot.Type.PriceUnit {slot.Type.PriceUnit} "
                        f" and latest_market_price.Unit {latest_market_price.Unit}!"
                    )

                payload = LatestPrice_Maker(
                    from_g_node_alias=self.alias,
                    from_g_node_instance_id=self.settings.g_node_instance_id,
                    price_times1000=latest_market_price.ValueTimes1000,
                    price_unit=slot.Type.PriceUnit,
                    market_slot_name=slot_name,
                    message_id=str(uuid.uuid4()),
                    irl_time_utc=pendulum.from_timestamp(
                        time.time()
                    ).to_iso8601_string(),
                ).tuple
                LOGGER.info(
                    "Broadcasting price: "
                    f"{round(latest_market_price.ValueTimes1000 / 1000, 3)}"
                    f" {latest_market_price.Unit.value}"
                )
                self.send_message(
                    payload=payload,
                    message_category=MessageCategory.RabbitJsonBroadcast,
                    radio_channel=market_type.Name,
                )

    ###################
    # Managing books
    ###################

    def dev_solve_for_clearing_price(self, book: MarketBook) -> MarketPrice:
        return self.hack_clearing_price[book.Slot.StartUnixS]

    def solve_for_clearing_price(self, book: MarketBook) -> MarketPrice:
        if self.universe_type == UniverseType.Dev:
            return self.dev_solve_for_clearing_price(book)
        else:
            raise NotImplementedError

    def create_market_contracts(self, book: MarketBook, clearing_price: MarketPrice):
        pass

    def clear_market(self, book: MarketBook):
        price = self.solve_for_clearing_price(book)
        self.create_market_contracts(book, price)
        self.clearing_price[book.Slot.Type.Name][book.Slot.StartUnixS] = price

    def update_slot_books(self):
        for market_type in self.market_types:
            t = self._time
            gc_delta = market_type.GateClosingMinutes * 60
            market_delta = market_type.DurationMinutes * 60
            latest = math.floor(t / market_delta)
            next_to_open = math.ceil((t + gc_delta) / market_delta)
            for i in range(latest, next_to_open + 1):
                slot_start = i * market_delta
                slot = MarketSlot(
                    Type=market_type,
                    MarketMakerAlias=self.alias,
                    StartUnixS=slot_start,
                )
                if slot_start not in self.slot_books[market_type.Name].keys():
                    new_book = MarketBook(
                        Slot=slot,
                        Bids=[],
                    )
                    self.slot_books[market_type.Name][slot_start] = new_book

    ###################
    # helpers
    ###################

    def latest_market_slot_name(self, market_type: MarketTypeGt) -> str:
        return f"{market_type.Name}.{self.alias}.{self.latest_slot_start(market_type)}"

    def latest_slot_start(self, market_type: MarketTypeGt) -> int:
        t = self._time
        market_delta = market_type.DurationMinutes * 60
        return math.floor(t / market_delta) * market_delta

    def last_slot_start(self, market_type: MarketTypeGt) -> int:
        if int(self._time) == self.latest_slot_start(market_type):
            return self.latest_slot_start(market_type) - self.market_slot_duration_s(
                market_type
            )
        else:
            return self.latest_slot_start(market_type)

    def next_slot_start(self, market_type: MarketTypeGt) -> int:
        return self.last_slot_start(market_type) + self.market_slot_duration_s(
            market_type
        )

    def market_slot_duration_s(self, market_type: MarketTypeGt) -> int:
        return market_type.DurationMinutes * 60

    @property
    def short_alias(self) -> str:
        return self.alias.split(".")[-1]
