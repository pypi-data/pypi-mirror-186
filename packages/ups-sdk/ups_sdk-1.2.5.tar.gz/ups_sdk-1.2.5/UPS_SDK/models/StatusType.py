from __future__ import annotations
from pydantic import BaseModel
class StatusType(BaseModel):
    Code: str
    Description: str