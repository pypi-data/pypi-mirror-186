""" Supervisor """
import logging
import traceback
from typing import Optional

import pendulum
from gridworks.actor_base import ActorBase

from gwmm.config import SupervisorSettings
from gwmm.enums import GNodeRole
from gwmm.types import HeartbeatA
from gwmm.types import HeartbeatA_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class Supervisor(ActorBase):
    def __init__(self, settings: SupervisorSettings):
        super().__init__(settings=settings)  # type: ignore

        self.latest_time_unix_s: Optional[int] = None

    ########################
    # Sends
    ########################

    def prepare_for_death(self) -> None:
        self.actor_main_stopped = True

    ########################
    # Receives
    ########################

    def route_message(
        self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA
    ) -> None:
        if payload.TypeName == HeartbeatA_Maker.type_name:
            try:
                self.heartbeat_a_received(from_alias, from_role, payload)
            except:
                LOGGER.warning("Error in g_node_ready_received")
                LOGGER.warning(traceback.format_exc(True))
        else:
            LOGGER.info(f"Does not process TypeName {payload.TypeName}")
            return

    def heartbeat_a_received(
        self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA
    ) -> None:
        LOGGER.warning(
            f"Received heartbeat from {from_alias} of role {from_role.value}"
        )

    def time_utc_str(self) -> str:
        if self.latest_time_unix_s is None:
            return ""
        return pendulum.from_timestamp(self.latest_time_unix_s).strftime(
            "%m/%d/%Y, %H:%M"
        )
