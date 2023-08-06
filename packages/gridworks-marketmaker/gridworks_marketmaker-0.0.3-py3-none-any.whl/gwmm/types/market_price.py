"""Type market.price, version 000"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from fastapi_utils.enums import StrEnum
from gridworks.errors import SchemaError
from gridworks.message import as_enum
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwmm.enums import MarketPriceUnit


class MarketPriceUnit000SchemaEnum:
    enum_name: str = "market.price.unit.000"
    symbols: List[str] = [
        "00000000",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class MarketPriceUnit000(StrEnum):
    USDPerMWh = auto()

    @classmethod
    def default(cls) -> "MarketPriceUnit000":
        return cls.USDPerMWh

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class MarketPriceUnitMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> MarketPriceUnit:
        if not MarketPriceUnit000SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to MarketPriceUnit000 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, MarketPriceUnit, MarketPriceUnit.default())

    @classmethod
    def local_to_type(cls, market_price_unit: MarketPriceUnit) -> str:
        if not isinstance(market_price_unit, MarketPriceUnit):
            raise SchemaError(f"{market_price_unit} must be of type {MarketPriceUnit}")
        versioned_enum = as_enum(
            market_price_unit, MarketPriceUnit000, MarketPriceUnit000.default()
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, MarketPriceUnit000] = {
        "00000000": MarketPriceUnit000.USDPerMWh,
    }

    versioned_enum_to_type_dict: Dict[MarketPriceUnit000, str] = {
        MarketPriceUnit000.USDPerMWh: "00000000",
    }


class MarketPrice(BaseModel):
    """ """

    ValueTimes1000: int = Field(
        title="ValueTimes1000",
    )
    Unit: MarketPriceUnit = Field(
        title="Unit",
    )
    TypeName: Literal["market.price"] = "market.price"
    Version: str = "000"

    @validator("Unit")
    def _check_unit(cls, v: MarketPriceUnit) -> MarketPriceUnit:
        return as_enum(v, MarketPriceUnit, MarketPriceUnit.USDPerMWh)

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["Unit"]
        Unit = as_enum(self.Unit, MarketPriceUnit, MarketPriceUnit.default())
        d["UnitGtEnumSymbol"] = MarketPriceUnitMap.local_to_type(Unit)
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class MarketPrice_Maker:
    type_name = "market.price"
    version = "000"

    def __init__(self, value_times1000: int, unit: MarketPriceUnit):
        self.tuple = MarketPrice(
            ValueTimes1000=value_times1000,
            Unit=unit,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: MarketPrice) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> MarketPrice:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> MarketPrice:
        d2 = dict(d)
        if "ValueTimes1000" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValueTimes1000")
        if "UnitGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing UnitGtEnumSymbol")
        if d2["UnitGtEnumSymbol"] in MarketPriceUnit000SchemaEnum.symbols:
            d2["Unit"] = MarketPriceUnitMap.type_to_local(d2["UnitGtEnumSymbol"])
        else:
            d2["Unit"] = MarketPriceUnit.default()
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return MarketPrice(
            ValueTimes1000=d2["ValueTimes1000"],
            Unit=d2["Unit"],
            TypeName=d2["TypeName"],
            Version="000",
        )
