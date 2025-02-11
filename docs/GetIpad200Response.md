# GetIpad200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**supplemental_build_version** | **str** |  | [optional] 
**supplemental_os_version_extra** | **str** |  | [optional] 
**last_check_in** | **str** |  | [optional] 
**user** | [**GetIpad200ResponseUser**](GetIpad200ResponseUser.md) |  | [optional] 
**asset_tag** | **str** |  | [optional] 
**blueprint_id** | **str** |  | [optional] 
**mdm_enabled** | **int** |  | [optional] 
**agent_installed** | **int** |  | [optional] 
**is_missing** | **int** |  | [optional] 
**is_removed** | **int** |  | [optional] 
**agent_version** | **str** |  | [optional] 
**first_enrollment** | **str** |  | [optional] 
**last_enrollment** | **str** |  | [optional] 
**blueprint_name** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 

## Example

```python
from kandji.models.get_ipad200_response import GetIpad200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIpad200Response from a JSON string
get_ipad200_response_instance = GetIpad200Response.from_json(json)
# print the JSON string representation of the object
print(GetIpad200Response.to_json())

# convert the object into a dict
get_ipad200_response_dict = get_ipad200_response_instance.to_dict()
# create an instance of GetIpad200Response from a dict
get_ipad200_response_from_dict = GetIpad200Response.from_dict(get_ipad200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


