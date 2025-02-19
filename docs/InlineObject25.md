# InlineObject25


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**cursor** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object25 import InlineObject25

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject25 from a JSON string
inline_object25_instance = InlineObject25.from_json(json)
# print the JSON string representation of the object
print(InlineObject25.to_json())

# convert the object into a dict
inline_object25_dict = inline_object25_instance.to_dict()
# create an instance of InlineObject25 from a dict
inline_object25_from_dict = InlineObject25.from_dict(inline_object25_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


