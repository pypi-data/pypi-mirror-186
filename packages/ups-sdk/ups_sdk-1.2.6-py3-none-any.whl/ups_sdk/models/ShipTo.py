from __future__ import annotations
from pydantic import BaseModel
from .Address import Address
class ShipTo(BaseModel):
    Address: Address