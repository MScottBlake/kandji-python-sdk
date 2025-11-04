# DeviceInformationGetDevice200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_installed** | **int** |  | [optional] 
**agent_version** | **str** |  | [optional] 
**api_level** | **str** |  | [optional] 
**asset_tag** | **str** |  | [optional] 
**blueprint_id** | **str** |  | [optional] 
**blueprint_name** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**first_enrollment** | **str** |  | [optional] 
**full_software_version** | **str** |  | [optional] 
**is_missing** | **int** |  | [optional] 
**is_removed** | **int** |  | [optional] 
**last_check_in** | **str** |  | [optional] 
**last_enrollment** | **str** |  | [optional] 
**lost_mode_status** | **str** |  | [optional] 
**mdm_enabled** | **int** |  | [optional] 
**model** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**security_patch_level** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**supplemental_build_version** | **str** |  | [optional] 
**supplemental_os_version_extra** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 
**user** | [**DeviceInformationGetDevice200ResponseUser**](DeviceInformationGetDevice200ResponseUser.md) |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device200_response import DeviceInformationGetDevice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDevice200Response from a JSON string
device_information_get_device200_response_instance = DeviceInformationGetDevice200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDevice200Response.to_json())

# convert the object into a dict
device_information_get_device200_response_dict = device_information_get_device200_response_instance.to_dict()
# create an instance of DeviceInformationGetDevice200Response from a dict
device_information_get_device200_response_from_dict = DeviceInformationGetDevice200Response.from_dict(device_information_get_device200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


