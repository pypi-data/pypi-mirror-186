"""Type market.maker.info, version 000"""
import json
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwmm.types.market_type_gt import MarketTypeGt
from gwmm.types.market_type_gt import MarketTypeGt_Maker


class MarketMakerInfo(BaseModel):
    """ """

    GNodeAlias: str = Field(
        title="GNodeAlias",
    )
    MarketTypeList: List[MarketTypeGt] = Field(
        title="MarketTypeList",
    )
    SampleMarketName: str = Field(
        title="SampleMarketName",
    )
    SampleMarketSlotName: str = Field(
        title="SampleMarketSlotName",
    )
    TypeName: Literal["market.maker.info"] = "market.maker.info"
    Version: str = "000"

    @validator("GNodeAlias")
    def _check_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(f"GNodeAlias failed LeftRightDot format validation: {e}")
        return v

    @validator("MarketTypeList")
    def _check_market_type_list(cls, v: List) -> List:
        for elt in v:
            if not isinstance(elt, MarketTypeGt):
                raise ValueError(
                    f"elt {elt} of MarketTypeList must have type MarketTypeGt."
                )
        return v

    @validator("SampleMarketSlotName")
    def _check_sample_market_slot_name(cls, v: str) -> str:
        try:
            check_is_market_slot_name_lrd_format(v)
        except ValueError as e:
            raise ValueError(
                f"SampleMarketSlotName failed MarketSlotNameLrdFormat format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()

        # Recursively call as_dict() for the SubTypes
        market_type_list = []
        for elt in self.MarketTypeList:
            market_type_list.append(elt.as_dict())
        d["MarketTypeList"] = market_type_list
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class MarketMakerInfo_Maker:
    type_name = "market.maker.info"
    version = "000"

    def __init__(
        self,
        g_node_alias: str,
        market_type_list: List[MarketTypeGt],
        sample_market_name: str,
        sample_market_slot_name: str,
    ):
        self.tuple = MarketMakerInfo(
            GNodeAlias=g_node_alias,
            MarketTypeList=market_type_list,
            SampleMarketName=sample_market_name,
            SampleMarketSlotName=sample_market_slot_name,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: MarketMakerInfo) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> MarketMakerInfo:
        """
        Given a serialized JSON type object, returns the Python class object
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> MarketMakerInfo:
        d2 = dict(d)
        if "GNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GNodeAlias")
        if "MarketTypeList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MarketTypeList")
        market_type_list = []
        if not isinstance(d2["MarketTypeList"], List):
            raise SchemaError("MarketTypeList must be a List!")
        for elt in d2["MarketTypeList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"elt {elt} of MarketTypeList must be "
                    "MarketTypeGt but not even a dict!"
                )
            market_type_list.append(MarketTypeGt_Maker.dict_to_tuple(elt))
        d2["MarketTypeList"] = market_type_list
        if "SampleMarketName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SampleMarketName")
        if "SampleMarketSlotName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SampleMarketSlotName")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return MarketMakerInfo(
            GNodeAlias=d2["GNodeAlias"],
            MarketTypeList=d2["MarketTypeList"],
            SampleMarketName=d2["SampleMarketName"],
            SampleMarketSlotName=d2["SampleMarketSlotName"],
            TypeName=d2["TypeName"],
            Version="000",
        )
