from __future__ import annotations
from pydantic import BaseModel, Field
from .Response import Response
from .Shipment import Shipment
from typing import Any, List

class TrackResponse(BaseModel):
    Response: Response
    Shipments: List[Shipment] = Field(None, alias="Shipment")
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        
        if isinstance(data["Shipment"], dict):
            data["Shipment"] = [data["Shipment"]]
            
        for shipment in data["Shipment"]:
            package = shipment.get("Package")
            
            if isinstance(package["Activity"], dict):
                shipment["Package"]["Activity"] = [shipment["Package"]["Activity"]]
            
            redirect_or_alternate_tracking_number = package.get("Redirect") or package.get("AlternateTrackingNumber")
            if redirect_or_alternate_tracking_number is None:
                
                if isinstance(shipment["ReferenceNumber"], dict):
                    shipment["ReferenceNumber"] = [shipment["ReferenceNumber"]]
            
        super().__init__(**data)