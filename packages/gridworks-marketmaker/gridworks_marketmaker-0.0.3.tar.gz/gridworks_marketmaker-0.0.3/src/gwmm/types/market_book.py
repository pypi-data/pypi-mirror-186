"""Type market.book, version 000"""
import json
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwmm.types.accepted_bid import AcceptedBid
from gwmm.types.accepted_bid import AcceptedBid_Maker
from gwmm.types.market_slot import MarketSlot
from gwmm.types.market_slot import MarketSlot_Maker


class MarketBook(BaseModel):
    """MarketMaker's list of bids for a MarketSlot"""

    Slot: MarketSlot = Field(
        title="MarketSlot the book is for",
    )
    Bids: List[AcceptedBid] = Field(
        title="List of bids in the book",
    )
    TypeName: Literal["market.book"] = "market.book"
    Version: str = "000"

    @validator("Bids")
    def _check_bids(cls, v: List) -> List:
        for elt in v:
            if not isinstance(elt, AcceptedBid):
                raise ValueError(f"elt {elt} of Bids must have type AcceptedBid.")
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        d["Slot"] = self.Slot.as_dict()

        # Recursively call as_dict() for the SubTypes
        bids = []
        for elt in self.Bids:
            bids.append(elt.as_dict())
        d["Bids"] = bids
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class MarketBook_Maker:
    type_name = "market.book"
    version = "000"

    def __init__(self, slot: MarketSlot, bids: List[AcceptedBid]):
        self.tuple = MarketBook(
            Slot=slot,
            Bids=bids,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: MarketBook) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> MarketBook:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> MarketBook:
        d2 = dict(d)
        if "Slot" not in d2.keys():
            raise SchemaError(f"dict {d2} missing Slot")
        if not isinstance(d2["Slot"], dict):
            raise SchemaError(f"d['Slot'] {d2['Slot']} must be a MarketSlot!")
        slot = MarketSlot_Maker.dict_to_tuple(d2["Slot"])
        d2["Slot"] = slot
        if "Bids" not in d2.keys():
            raise SchemaError(f"dict {d2} missing Bids")
        bids = []
        if not isinstance(d2["Bids"], List):
            raise SchemaError("Bids must be a List!")
        for elt in d2["Bids"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"elt {elt} of Bids must be " "AcceptedBid but not even a dict!"
                )
            bids.append(AcceptedBid_Maker.dict_to_tuple(elt))
        d2["Bids"] = bids
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return MarketBook(
            Slot=d2["Slot"],
            Bids=d2["Bids"],
            TypeName=d2["TypeName"],
            Version="000",
        )
