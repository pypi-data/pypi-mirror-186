from __future__ import annotations
from pydantic import BaseModel
from .StatusType import StatusType
from .StatusCode import StatusCode
class Status(BaseModel):
    StatusType: StatusType
    StatusCode: StatusCode