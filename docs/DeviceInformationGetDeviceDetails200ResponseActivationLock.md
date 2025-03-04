# DeviceInformationGetDeviceDetails200ResponseActivationLock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_lock_allowed_while_supervised** | **int** |  | [optional] 
**activation_lock_supported** | **int** |  | [optional] 
**bypass_code_failed** | **int** |  | [optional] 
**device_activation_lock_enabled** | **int** |  | [optional] 
**user_activation_lock_enabled** | **int** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response_activation_lock import DeviceInformationGetDeviceDetails200ResponseActivationLock

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200ResponseActivationLock from a JSON string
device_information_get_device_details200_response_activation_lock_instance = DeviceInformationGetDeviceDetails200ResponseActivationLock.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200ResponseActivationLock.to_json())

# convert the object into a dict
device_information_get_device_details200_response_activation_lock_dict = device_information_get_device_details200_response_activation_lock_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200ResponseActivationLock from a dict
device_information_get_device_details200_response_activation_lock_from_dict = DeviceInformationGetDeviceDetails200ResponseActivationLock.from_dict(device_information_get_device_details200_response_activation_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


