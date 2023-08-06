""" MarketMakerBase """
import functools
import logging
import time
import traceback
from abc import abstractmethod
from datetime import datetime
from typing import Optional
from typing import no_type_check

import pendulum
import requests
from gridworks.actor_base import ActorBase
from gridworks.utils import RestfulResponse

from gwmm.config import MarketMakerSettings
from gwmm.enums import GNodeRole
from gwmm.enums import MessageCategorySymbol
from gwmm.enums import UniverseType
from gwmm.types import HeartbeatA
from gwmm.types import HeartbeatA_Maker
from gwmm.types import LatestPrice_Maker
from gwmm.types import SimTimestep
from gwmm.types import SimTimestep_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(sasctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)


class MarketMakerBase(ActorBase):
    def __init__(self, settings: MarketMakerSettings):
        super().__init__(settings=settings)
        self.settings: Settings = settings
        self.initialize_time()

    def initialize_time(self):
        self._time: float = self.settings.initial_time_unix_s
        ts = SimTimestep_Maker(
            from_g_node_alias=self.alias,
            from_g_node_instance_id="00000000-0000-0000-0000-000000000000",
            time_unix_s=int(self._time),
            timestep_created_ms=int(time.time() * 1000),
            message_id="00000000-0000-0000-0000-000000000000",
        ).tuple
        api_endpoint = f"{self.settings.mm_api_root}/sim-timestep/"
        r = requests.post(url=api_endpoint, json=ts.as_dict())
        if r.status_code > 200:
            raise Exception("Failed to initialize time with RestAPI. Check uvicorn?")

    def local_rabbit_startup(self):
        rjb = MessageCategorySymbol.rjb.value
        tc_alias_lrh = self.settings.my_time_coordinator_alias.replace(".", "-")
        binding = f"{rjb}.{tc_alias_lrh}.timecoordinator.sim-timestep"

        cb = functools.partial(self.on_timecoordinator_bindok, binding=binding)
        self._consume_channel.queue_bind(
            self.queue_name, "timecoordinatormic_tx", routing_key=binding, callback=cb
        )

    @no_type_check
    def on_timecoordinator_bindok(self, _unused_frame, binding) -> None:
        LOGGER.info(f"Queue {self.queue_name} bound with {binding}")

    def prepare_for_death(self) -> None:
        self.actor_main_stopped = True

    ########################
    ## Receives
    ########################

    def route_message(
        self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA
    ) -> None:
        if payload.TypeName == SimTimestep_Maker.type_name:
            try:
                self.timestep_from_timecoordinator(payload)
            except:
                LOGGER.warning("Error in timestep_from_timecoordinator")
                LOGGER.warning(traceback.format_exc(True))

    def timestep_from_timecoordinator(self, payload: SimTimestep):
        if self._time < payload.TimeUnixS:
            api_endpoint = f"{self.settings.mm_api_root}/sim-timestep/"
            r = requests.post(url=api_endpoint, json=payload.as_dict())
            self._time = float(payload.TimeUnixS)
            self.new_timestep(payload)
        elif self._time == float(payload.TimeUnixS):
            api_endpoint = f"{self.settings.mm_api_root}/sim-timestep/"
            r = requests.post(url=api_endpoint, json=payload.as_dict())
            self.repeated_timestep(payload)

    def new_timestep(self, payload: SimTimestep) -> None:
        # LOGGER.info("New timestep in atn_actor_base")
        raise NotImplementedError

    def repeated_timestep(self, payload: SimTimestep) -> None:
        # LOGGER.info("Timestep received again in atn_actor_base")
        raise NotImplementedError

    def send_heartbeat_to_super(self) -> None:
        self.send_message(
            payload=HeartbeatA_Maker().tuple,
            to_role=GNodeRole.Supervisor,
            to_g_node_alias=self.settings.my_super_alias,
        )

    def time(self) -> float:
        if self.universe_type == UniverseType.Dev:
            return self._time
        else:
            return time.time()

    def time_str(self) -> str:
        return pendulum.from_timestamp(self._time).strftime("%m/%d/%Y, %H:%M")
