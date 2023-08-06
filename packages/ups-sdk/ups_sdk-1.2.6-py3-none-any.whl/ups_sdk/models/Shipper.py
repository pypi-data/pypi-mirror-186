from __future__ import annotations
from pydantic import BaseModel
from .Address import Address
from typing import Optional

class Shipper(BaseModel):
    ShipperNumber: str
    Address: Optional[Address]