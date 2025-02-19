# InlineObject8


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
**user** | [**InlineObject8User**](InlineObject8User.md) |  | [optional] 
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
from kandji.models.inline_object8 import InlineObject8

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject8 from a JSON string
inline_object8_instance = InlineObject8.from_json(json)
# print the JSON string representation of the object
print(InlineObject8.to_json())

# convert the object into a dict
inline_object8_dict = inline_object8_instance.to_dict()
# create an instance of InlineObject8 from a dict
inline_object8_from_dict = InlineObject8.from_dict(inline_object8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


