from __future__ import annotations
from pydantic import BaseModel
from UPS_SDK.models.UnitOfMeasurement import UnitOfMeasurement
class ShipmentWeight(BaseModel):
    UnitOfMeasurement: UnitOfMeasurement
    Weight: str
