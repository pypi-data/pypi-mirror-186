from __future__ import annotations
from pydantic import BaseModel
from .UnitOfMeasurement import UnitOfMeasurement
class PackageWeight(BaseModel):
    UnitOfMeasurement: UnitOfMeasurement
    Weight: str