from __future__ import annotations
import datetime
from typing import Optional
from pydantic import BaseModel
from .ActivityLocation import ActivityLocation
from .Status import Status
from .Address import Address

class ActivityItem(BaseModel):
    ActivityLocation: Optional[ActivityLocation]
    Status: Status
    Date: str
    Time: str
    GMTDate: str
    GMTTime: str
    GMTOffset: str
    
    @property
    def description(self) -> str:
        return self.Status.StatusType.Description
    
    @property
    def city(self) -> str:
        return self.ActivityLocation.Address.City
    
    @property
    def address(self) -> Address:
        return self.ActivityLocation.Address
    
    @property
    def status_code(self) -> str:
        return self.Status.StatusCode.Code
    
    @property
    def get_date(self) -> datetime.datetime:
        full_datetime = f"{self.Date} - {self.Time}"
        return datetime.datetime.strptime(full_datetime, "%Y%m%d - %H%M%S")