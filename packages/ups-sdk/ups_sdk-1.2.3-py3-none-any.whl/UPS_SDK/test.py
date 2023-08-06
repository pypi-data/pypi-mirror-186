from unittest import TestCase
import unittest
from main import UPSApi
from UPS_SDK.models import TrackResponse
from UPS_SDK.models import TrackError
from UPS_SDK.models import TrackType
from models.AccessRequest import AccessRequest
from models.TrackRequest import TrackRequest

class GetPackageTest(TestCase):
    WRONG_TRACKING_NUMBER = "1Z89RA79045600675612"
    CORRECT_TRACKING_NUMBER = "1Z89RA790456006756"
    
    def test_correct_package(self):
        correct_request = TrackRequest(
            track_type=TrackType.ByTrackingNumber, reference_number_or_tracking_number=self.CORRECT_TRACKING_NUMBER
        )
        correct_package = api.get_package(track_request=correct_request)
        self.assertIsInstance(correct_package, TrackResponse, "Correct Package Is Instance TrackResponse Object")
        
    def test_wrong_package(self):
        wrong_request = TrackRequest(
            track_type=TrackType.ByTrackingNumber, reference_number_or_tracking_number=self.WRONG_TRACKING_NUMBER
        )
        self.assertRaises(TrackError, api.get_package, track_request=wrong_request)
    
ACCESS_LICENSE_NUMBER = "0D9B373178F57052"
USER_ID = "BUZV"
PASSWORD = "Falkel.2021"
api = UPSApi(access_request=AccessRequest(access_license_number=ACCESS_LICENSE_NUMBER, user_id=USER_ID, password=PASSWORD))
unittest.main()