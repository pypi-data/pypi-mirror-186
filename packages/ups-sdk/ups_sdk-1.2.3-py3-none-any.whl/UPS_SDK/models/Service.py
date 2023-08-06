from __future__ import annotations
from pydantic import BaseModel
class Service(BaseModel):
    Code: str
    Description: str