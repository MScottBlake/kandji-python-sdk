# DeviceInformationGetDeviceDetails200ResponseGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_level** | **str** |  | [optional] 
**asset_tag** | **str** |  | [optional] 
**assigned_user** | **object** |  | [optional] 
**blueprint_name** | **str** |  | [optional] 
**blueprint_uuid** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**enterprise_device_id** | **str** |  | [optional] 
**enterprise_id** | **str** |  | [optional] 
**first_enrollment** | **str** |  | [optional] 
**last_enrollment** | **str** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**os_build** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**security_patch_level** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 

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


