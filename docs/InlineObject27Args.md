# InlineObject27Args


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **object** |  | [optional] 
**columns** | **object** |  | [optional] 
**sort_by** | **str** |  | [optional] 
**blueprint_ids** | **object** |  | [optional] 
**device_families** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object27_args import InlineObject27Args

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject27Args from a JSON string
inline_object27_args_instance = InlineObject27Args.from_json(json)
# print the JSON string representation of the object
print(InlineObject27Args.to_json())

# convert the object into a dict
inline_object27_args_dict = inline_object27_args_instance.to_dict()
# create an instance of InlineObject27Args from a dict
inline_object27_args_from_dict = InlineObject27Args.from_dict(inline_object27_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


