from __future__ import annotations
from pydantic import BaseModel
class ReferenceNumber(BaseModel):
    Code: str
    Value: str