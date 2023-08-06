"""Settings for a MarketMaker, readable from environment and/or from env files."""

import pendulum
from gridworks.gw_config import AlgoApiSecrets
from gridworks.gw_config import GNodeSettings
from gridworks.gw_config import Public
from gridworks.gw_config import SupervisorSettings
from pydantic import BaseSettings
from pydantic import SecretStr


class MarketMakerSettings(GNodeSettings):
    g_node_alias: str = "d1.isone.ver.keene"
    g_node_role_value: str = "MarketMaker"
    my_super_alias: str = "d1.super3"
    g_node_id: str = "575f374f-8533-4733-baf7-91146c607445"
    g_node_instance_id: str = "0d96fcb9-ce50-4441-bec0-c0c5141318c9"
    mm_api_root: str = "http://localhost:7997"
    sk: SecretStr = SecretStr(
        "EG/l78fTcnkeyHjnPVJZZ3w7jFUHJfyGGPrfKk3VAgcWLMtg6fubxEe3gNIQvHTn9QpxSYevCuQoRGYjz9I8yg=="
    )

    # addr "CYWMWYHJ7ON4IR5XQDJBBPDU472QU4KJQ6XQVZBIIRTCHT6SHTFNHEAVC4"
    class Config:
        env_prefix = "MM_"
        env_nested_delimiter = "__"


DEFAULT_ENV_FILE = ".env"
