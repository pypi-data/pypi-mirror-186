from __future__ import annotations
from pydantic import BaseModel
class ReferenceNumberItem(BaseModel):
    Code: str
    Value: str