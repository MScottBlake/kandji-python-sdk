# DeviceInformationGetDeviceDetails200ResponseGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_tag** | **str** |  | [optional] 
**assigned_user** | **str** |  | [optional] 
**blueprint_name** | **str** |  | [optional] 
**blueprint_uuid** | **str** |  | [optional] 
**boot_volume** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**first_enrollment** | **str** |  | [optional] 
**last_enrollment** | **str** |  | [optional] 
**last_user** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**supplemental_build_version** | **str** |  | [optional] 
**supplemental_os_version_extra** | **str** |  | [optional] 
**system_version** | **str** |  | [optional] 
**time_since_boot** | **str** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response_general import DeviceInformationGetDeviceDetails200ResponseGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200ResponseGeneral from a JSON string
device_information_get_device_details200_response_general_instance = DeviceInformationGetDeviceDetails200ResponseGeneral.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200ResponseGeneral.to_json())

# convert the object into a dict
device_information_get_device_details200_response_general_dict = device_information_get_device_details200_response_general_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200ResponseGeneral from a dict
device_information_get_device_details200_response_general_from_dict = DeviceInformationGetDeviceDetails200ResponseGeneral.from_dict(device_information_get_device_details200_response_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


