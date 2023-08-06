from __future__ import annotations
from pydantic import BaseModel
from typing import Optional
from .Address import Address

class ActivityLocation(BaseModel):
    Address: Optional[Address]
    Description: Optional[str]