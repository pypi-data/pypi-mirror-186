from __future__ import annotations
from pydantic import BaseModel
class Message(BaseModel):
    Code: str
    Description: str