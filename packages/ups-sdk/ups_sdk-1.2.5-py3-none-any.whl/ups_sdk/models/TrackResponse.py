from __future__ import annotations
from pydantic import BaseModel
from UPS_SDK.models.Response import Response
from UPS_SDK.models.Shipment import Shipment
from typing import Any

class TrackResponse(BaseModel):
    Response: Response
    Shipment: Shipment
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        if isinstance(data["Shipment"]["Package"]["Activity"], dict):
            data['Shipment']["Package"]["Activity"] = [data["Shipment"]["Package"]["Activity"]]
        if isinstance(data["Shipment"]["ReferenceNumber"], dict):
            data["Shipment"]["ReferenceNumber"] = [data['Shipment']["ReferenceNumber"]]
            
        super().__init__(**data)