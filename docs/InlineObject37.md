# InlineObject37


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** |  | [optional] 
**archived** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**department** | **object** |  | [optional] 
**deprecated_user_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**integration** | [**InlineObject37Integration**](InlineObject37Integration.md) |  | [optional] 
**job_title** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**device_count** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.inline_object37 import InlineObject37

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject37 from a JSON string
inline_object37_instance = InlineObject37.from_json(json)
# print the JSON string representation of the object
print(InlineObject37.to_json())

# convert the object into a dict
inline_object37_dict = inline_object37_instance.to_dict()
# create an instance of InlineObject37 from a dict
inline_object37_from_dict = InlineObject37.from_dict(inline_object37_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


