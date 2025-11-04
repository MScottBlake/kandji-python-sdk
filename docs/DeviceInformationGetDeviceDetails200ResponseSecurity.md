# DeviceInformationGetDeviceDetails200ResponseSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android_debug_bridge_enabled** | **object** |  | [optional] 
**developer_mode_enabled** | **object** |  | [optional] 
**device_posture** | **str** |  | [optional] 
**encryption_status** | **str** |  | [optional] 
**has_google_play_protect** | **int** |  | [optional] 
**has_passcode** | **int** |  | [optional] 
**is_encrypted** | **int** |  | [optional] 
**unknown_app_sources_enabled** | **object** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response_security import DeviceInformationGetDeviceDetails200ResponseSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200ResponseSecurity from a JSON string
device_information_get_device_details200_response_security_instance = DeviceInformationGetDeviceDetails200ResponseSecurity.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200ResponseSecurity.to_json())

# convert the object into a dict
device_information_get_device_details200_response_security_dict = device_information_get_device_details200_response_security_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200ResponseSecurity from a dict
device_information_get_device_details200_response_security_from_dict = DeviceInformationGetDeviceDetails200ResponseSecurity.from_dict(device_information_get_device_details200_response_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


