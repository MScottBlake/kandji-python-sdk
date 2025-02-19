# InlineObject32


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **object** |  | [optional] 
**previous** | **object** |  | [optional] 
**malware_count** | **int** |  | [optional] 
**pup_count** | **int** |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object32 import InlineObject32

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject32 from a JSON string
inline_object32_instance = InlineObject32.from_json(json)
# print the JSON string representation of the object
print(InlineObject32.to_json())

# convert the object into a dict
inline_object32_dict = inline_object32_instance.to_dict()
# create an instance of InlineObject32 from a dict
inline_object32_from_dict = InlineObject32.from_dict(inline_object32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


