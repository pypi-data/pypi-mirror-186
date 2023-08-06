import random
import time
from functools import lru_cache
from typing import Dict
from typing import List

import dotenv
import pendulum
from aiocache import Cache
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import FileResponse
from gridworks.utils import RestfulResponse
from pydantic import BaseModel
from pydantic import ValidationError

import gwmm.config as config
from gwmm.enums import UniverseType
from gwmm.market_maker import MarketMaker
from gwmm.market_maker_api import MarketMakerApi
from gwmm.types import AtnBid
from gwmm.types import AtnBid_Maker
from gwmm.types import MarketMakerInfo
from gwmm.types import SimTimestep


settings: config.Settings = config.Settings(_env_file=dotenv.find_dotenv())

app = FastAPI()
cache = Cache(
    Cache.REDIS,
    endpoint=f"{settings.redis_endpoint}",
    port=6379,
    namespace="main",
)


class SimTime:
    def __init__(self):
        pass

    async def get_time(self) -> int:
        return await cache.get("time", default=0)

    async def set_time(self, value: int) -> None:
        await cache.set("time", value)


sim_time = SimTime()


mm = MarketMakerApi()


@lru_cache()
def get_settings():
    return mm.settings


@app.get("/", response_model=MarketMakerInfo)
async def main():
    return mm.info


@app.get("/get-time/")
async def get_time():
    time_s = await get_time()
    return {
        "TimeUnixS": time_s,
        "UTC": pendulum.from_timestamp(time_s).to_iso8601_string(),
    }


@app.post(f"/sim-timestep/", response_model=RestfulResponse)
async def set_time(timestep: SimTimestep):
    await sim_time.set_time(timestep.TimeUnixS)
    return RestfulResponse(Note=f"Successfully updated time to {timestep.TimeUnixS}")


@app.post("/atn-bid/", response_model=RestfulResponse)
async def atn_bid_received(
    d: Dict,
):
    try:
        payload = AtnBid_Maker.dict_to_tuple(d)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"{e}")
    time_received = await get_time()

    # HACK for timesteps that are not subsecond:
    time_received -= 120

    ts_ns = int(time_received * 10**9)
    if mm.universe_type == UniverseType.Dev:
        ts_ns += random.uniform(-(10**8), 10**8)
    rr = mm.atn_bid(payload=payload, ts_ns=ts_ns)
    if rr.HttpStatusCode > 200:
        raise HTTPException(
            status_code=rr.HttpStatusCode, detail=f"[{rr.HttpStatusCode}]: {rr.Note}"
        )
    return rr


async def get_time() -> float:
    if mm.universe_type == UniverseType.Dev:
        time_s = await sim_time.get_time()
        return float(time_s)
    return time.time()
