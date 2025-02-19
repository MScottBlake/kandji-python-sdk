# InlineObject9


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**last_check_in** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
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
**lost_mode_status** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object9 import InlineObject9

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject9 from a JSON string
inline_object9_instance = InlineObject9.from_json(json)
# print the JSON string representation of the object
print(InlineObject9.to_json())

# convert the object into a dict
inline_object9_dict = inline_object9_instance.to_dict()
# create an instance of InlineObject9 from a dict
inline_object9_from_dict = InlineObject9.from_dict(inline_object9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


