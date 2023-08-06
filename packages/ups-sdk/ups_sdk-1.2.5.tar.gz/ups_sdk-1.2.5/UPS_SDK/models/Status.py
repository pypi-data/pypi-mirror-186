from __future__ import annotations
from pydantic import BaseModel
from UPS_SDK.models.StatusType import StatusType
from UPS_SDK.models.StatusCode import StatusCode
class Status(BaseModel):
    StatusType: StatusType
    StatusCode: StatusCode