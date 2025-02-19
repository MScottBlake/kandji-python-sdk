# InlineObject23


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **object** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**cursor** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object23 import InlineObject23

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject23 from a JSON string
inline_object23_instance = InlineObject23.from_json(json)
# print the JSON string representation of the object
print(InlineObject23.to_json())

# convert the object into a dict
inline_object23_dict = inline_object23_instance.to_dict()
# create an instance of InlineObject23 from a dict
inline_object23_from_dict = InlineObject23.from_dict(inline_object23_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


