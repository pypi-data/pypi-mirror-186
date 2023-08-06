import requests, urllib3, xmltodict, json
from httpx import AsyncClient
from dataclasses import dataclass
from xml.etree import ElementTree
from ups_sdk.models import AccessRequest, TrackRequest, TrackResponse, TrackError
urllib3.disable_warnings()

@dataclass
class UPSApi:
    access_request: AccessRequest
    host: str = "https://onlinetools.ups.com/ups.app/xml/Track"
    
    @staticmethod
    def __create_response(text: str) -> TrackResponse:
        xpars = xmltodict.parse(text, dict_constructor=dict)
        track_response: dict = json.loads(json.dumps(xpars))["TrackResponse"]
        
        if "Error" in track_response["Response"].keys():
            raise TrackError(**track_response["Response"]["Error"])
        
        response = TrackResponse(**track_response)
        
        return response
    
    def prepare_request_data(self, track_request: TrackRequest) -> str:
        xml_data = ""
        xml_data += ElementTree.tostring(self.access_request.xml()).decode("utf-8")
        xml_data += ElementTree.tostring(track_request.xml()).decode("utf-8")
        return xml_data
    
    def get_package(self, track_request: TrackRequest):
        response = requests.post(self.host, self.prepare_request_data(track_request), verify=False)
        return self.__create_response(response.text)

    async def async_get_package(self, async_client: AsyncClient, track_request: TrackRequest):
        response = await async_client.post(self.host, data=self.prepare_request_data(track_request))
        return self.__create_response(response.text)