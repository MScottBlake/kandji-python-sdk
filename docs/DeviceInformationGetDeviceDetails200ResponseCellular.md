# DeviceInformationGetDeviceDetails200ResponseCellular


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_roaming** | **int** |  | [optional] 
**data_roaming** | **int** |  | [optional] 
**cellular_technology** | **int** |  | [optional] 
**subscriptions** | **object** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response_cellular import DeviceInformationGetDeviceDetails200ResponseCellular

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200ResponseCellular from a JSON string
device_information_get_device_details200_response_cellular_instance = DeviceInformationGetDeviceDetails200ResponseCellular.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200ResponseCellular.to_json())

# convert the object into a dict
device_information_get_device_details200_response_cellular_dict = device_information_get_device_details200_response_cellular_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200ResponseCellular from a dict
device_information_get_device_details200_response_cellular_from_dict = DeviceInformationGetDeviceDetails200ResponseCellular.from_dict(device_information_get_device_details200_response_cellular_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


