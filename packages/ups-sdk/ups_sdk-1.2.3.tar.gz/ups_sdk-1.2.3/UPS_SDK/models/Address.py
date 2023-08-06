from __future__ import annotations
from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    City: Optional[str] = None
    StateProvinceCode: Optional[str] = None
    CountryCode: str
    PostalCode: Optional[str] = None
    AddressLine1: Optional[str] = None