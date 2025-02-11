# DeviceInformationGetDeviceDetails200ResponseFilevault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filevault_enabled** | **object** |  | [optional] 
**filevault_recoverykey_type** | **str** |  | [optional] 
**filevault_prk_escrowed** | **int** |  | [optional] 
**filevault_next_rotation** | **str** |  | [optional] 
**filevault_regen_required** | **int** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response_filevault import DeviceInformationGetDeviceDetails200ResponseFilevault

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200ResponseFilevault from a JSON string
device_information_get_device_details200_response_filevault_instance = DeviceInformationGetDeviceDetails200ResponseFilevault.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200ResponseFilevault.to_json())

# convert the object into a dict
device_information_get_device_details200_response_filevault_dict = device_information_get_device_details200_response_filevault_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200ResponseFilevault from a dict
device_information_get_device_details200_response_filevault_from_dict = DeviceInformationGetDeviceDetails200ResponseFilevault.from_dict(device_information_get_device_details200_response_filevault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


