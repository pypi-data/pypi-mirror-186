from pydantic import BaseModel
from xml.etree import ElementTree as ET
from enum import Enum

class RequestAction(Enum):
    TRACK = "Track"
    
class RequestOption(Enum):
    ACTIVITY = "activity"
    NONE = "none"

class TrackRequest(BaseModel):
    track_type: str
    reference_number_or_tracking_number: str
    
    request_action: RequestAction = RequestAction.TRACK
    request_option: RequestOption = RequestOption.ACTIVITY
    customer_context: str = "Customer Context"
    xpci_version: str = "1.0"
    
    def xml(self) -> ET.Element:
        root = ET.Element("TrackRequest")
        request_el = ET.SubElement(root, "Request")
        transaction_reference_el = ET.SubElement(request_el, "TransactionReference")
        ET.SubElement(transaction_reference_el, "CustomerContext").text = self.customer_context
        ET.SubElement(transaction_reference_el, "XpciVersion").text = self.xpci_version
        ET.SubElement(request_el, "RequestAction").text = self.request_action.value
        ET.SubElement(request_el, "RequestOption").text = self.request_option.value
        track_type_el = ET.SubElement(root, self.track_type)
        ET.SubElement(track_type_el, "Value").text = self.reference_number_or_tracking_number
        
        return root
    