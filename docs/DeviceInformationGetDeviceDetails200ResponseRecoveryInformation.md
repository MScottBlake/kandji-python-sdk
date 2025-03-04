# DeviceInformationGetDeviceDetails200ResponseRecoveryInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firmware_password_exist** | **int** |  | [optional] 
**firmware_password_pending** | **int** |  | [optional] 
**password_rotation_scheduled** | **object** |  | [optional] 
**recovery_lock_enabled** | **int** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response_recovery_information import DeviceInformationGetDeviceDetails200ResponseRecoveryInformation

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200ResponseRecoveryInformation from a JSON string
device_information_get_device_details200_response_recovery_information_instance = DeviceInformationGetDeviceDetails200ResponseRecoveryInformation.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200ResponseRecoveryInformation.to_json())

# convert the object into a dict
device_information_get_device_details200_response_recovery_information_dict = device_information_get_device_details200_response_recovery_information_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200ResponseRecoveryInformation from a dict
device_information_get_device_details200_response_recovery_information_from_dict = DeviceInformationGetDeviceDetails200ResponseRecoveryInformation.from_dict(device_information_get_device_details200_response_recovery_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


