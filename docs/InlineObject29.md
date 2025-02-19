# InlineObject29


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**args** | [**InlineObject27Args**](InlineObject27Args.md) |  | [optional] 
**error_msg** | **object** |  | [optional] 
**path** | **str** |  | [optional] 
**signed_url** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.inline_object29 import InlineObject29

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject29 from a JSON string
inline_object29_instance = InlineObject29.from_json(json)
# print the JSON string representation of the object
print(InlineObject29.to_json())

# convert the object into a dict
inline_object29_dict = inline_object29_instance.to_dict()
# create an instance of InlineObject29 from a dict
inline_object29_from_dict = InlineObject29.from_dict(inline_object29_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


