# DeviceInformationGetDeviceStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**library_items** | **object** |  | [optional] 
**parameters** | **object** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_status200_response import DeviceInformationGetDeviceStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceStatus200Response from a JSON string
device_information_get_device_status200_response_instance = DeviceInformationGetDeviceStatus200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceStatus200Response.to_json())

# convert the object into a dict
device_information_get_device_status200_response_dict = device_information_get_device_status200_response_instance.to_dict()
# create an instance of DeviceInformationGetDeviceStatus200Response from a dict
device_information_get_device_status200_response_from_dict = DeviceInformationGetDeviceStatus200Response.from_dict(device_information_get_device_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


