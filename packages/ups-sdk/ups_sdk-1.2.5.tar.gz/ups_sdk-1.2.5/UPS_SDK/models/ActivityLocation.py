from __future__ import annotations
from pydantic import BaseModel
from typing import Optional
from UPS_SDK.models.Address import Address

class ActivityLocation(BaseModel):
    Address: Optional[Address]
    Description: Optional[str]