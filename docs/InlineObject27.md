# InlineObject27


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**args** | [**InlineObject27Args**](InlineObject27Args.md) |  | [optional] 
**error_msg** | **object** |  | [optional] 
**path** | **object** |  | [optional] 
**signed_url** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.inline_object27 import InlineObject27

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject27 from a JSON string
inline_object27_instance = InlineObject27.from_json(json)
# print the JSON string representation of the object
print(InlineObject27.to_json())

# convert the object into a dict
inline_object27_dict = inline_object27_instance.to_dict()
# create an instance of InlineObject27 from a dict
inline_object27_from_dict = InlineObject27.from_dict(inline_object27_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


