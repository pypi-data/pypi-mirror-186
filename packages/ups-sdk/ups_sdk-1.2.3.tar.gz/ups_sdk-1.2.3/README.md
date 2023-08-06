# UPS-Sdk
 UPS-SDK Package is an application assistant that you can use to track your ups packages.

# Basic Usage:
from ups_sdk import UPSApi, TrackRequest, AccessRequest, TrackError, TrackType

access_license_number = "UPS_ACCESS_LICENSE_NUMBER"

user_id = "UPS_USER_ID"

password = "UPS_PASSWORD"

access_request = AccessRequest(access_license_number=access_license_number, user_id=user_id, password=password)

ups = UPSApi(access_request=access_request)

reference_number_or_tracking_number = "UPS_TRACKING_NUMBER"

track_request = TrackRequest(track_type=TrackType.ByTrackingNumber, reference_number_or_tracking_number=reference_number_or_tracking_number)

track_response = ups.get_package(track_request=track_request)

shipment = track_response.Shipment

