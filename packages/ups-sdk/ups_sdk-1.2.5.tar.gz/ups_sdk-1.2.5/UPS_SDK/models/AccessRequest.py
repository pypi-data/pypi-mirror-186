from pydantic import BaseModel
from xml.etree import ElementTree as ET

class AccessRequest(BaseModel):
    access_license_number: str
    user_id: str
    password: str
    
    def xml(self) -> ET.Element:
        root = ET.Element("AccessRequest")
        ET.SubElement(root, "AccessLicenseNumber").text = self.access_license_number
        ET.SubElement(root, "UserId").text = self.user_id
        ET.SubElement(root, "Password").text = self.password
        return root
