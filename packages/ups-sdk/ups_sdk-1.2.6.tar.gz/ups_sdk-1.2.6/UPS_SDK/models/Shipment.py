from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional
from .Package import Package
from .ShipTo import ShipTo
from .Shipper import Shipper
from .ReferenceNumberItem import ReferenceNumberItem
from .Service import Service
from .ShipmentWeight import ShipmentWeight

class Shipment(BaseModel):
    Shipper: Shipper
    ShipTo: ShipTo
    ShipmentWeight: Optional[ShipmentWeight]
    Service: Service
    ReferenceNumbers: Optional[List[ReferenceNumberItem]] = Field(None, alias="ReferenceNumber")
    ShipmentIdentificationNumber: str
    PickupDate: str
    ScheduledDeliveryDate: Optional[str]
    Package: Package
    
    @staticmethod
    def delivered_date_to_str(date: datetime, description: str):
        
        pass
    
    @property
    def delivered_date(self) -> Optional[datetime]:
        last_activity = self.Package.AllActivity[0]
        if self.Package.is_delivered:
            return last_activity.get_date
        return None
    
    @property
    def scheduled_delivery_date(self):
        date = None
        if self.Package.RescheduledDeliveryDate is not None :
            date = datetime.strptime(self.Package.RescheduledDeliveryDate, "%Y%m%d")
        elif self.ScheduledDeliveryDate is not None:
            date = datetime.strptime(self.ScheduledDeliveryDate, "%Y%m%d")
        return date
    
    
    
        