# DeviceInformationGetDeviceDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cellular** | [**DeviceInformationGetDeviceDetails200ResponseCellular**](DeviceInformationGetDeviceDetails200ResponseCellular.md) |  | [optional] 
**general** | [**DeviceInformationGetDeviceDetails200ResponseGeneral**](DeviceInformationGetDeviceDetails200ResponseGeneral.md) |  | [optional] 
**hardware** | [**DeviceInformationGetDeviceDetails200ResponseHardware**](DeviceInformationGetDeviceDetails200ResponseHardware.md) |  | [optional] 
**management** | [**DeviceInformationGetDeviceDetails200ResponseManagement**](DeviceInformationGetDeviceDetails200ResponseManagement.md) |  | [optional] 
**security** | [**DeviceInformationGetDeviceDetails200ResponseSecurity**](DeviceInformationGetDeviceDetails200ResponseSecurity.md) |  | [optional] 
**tags** | **object** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response import DeviceInformationGetDeviceDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200Response from a JSON string
device_information_get_device_details200_response_instance = DeviceInformationGetDeviceDetails200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200Response.to_json())

# convert the object into a dict
device_information_get_device_details200_response_dict = device_information_get_device_details200_response_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200Response from a dict
device_information_get_device_details200_response_from_dict = DeviceInformationGetDeviceDetails200Response.from_dict(device_information_get_device_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


