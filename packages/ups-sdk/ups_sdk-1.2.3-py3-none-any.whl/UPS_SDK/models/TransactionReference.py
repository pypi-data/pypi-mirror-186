from __future__ import annotations
from pydantic import BaseModel

class TransactionReference(BaseModel):
    CustomerContext: str
    XpciVersion: str