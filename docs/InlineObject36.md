# InlineObject36


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**previous** | **object** |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object36 import InlineObject36

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject36 from a JSON string
inline_object36_instance = InlineObject36.from_json(json)
# print the JSON string representation of the object
print(InlineObject36.to_json())

# convert the object into a dict
inline_object36_dict = inline_object36_instance.to_dict()
# create an instance of InlineObject36 from a dict
inline_object36_from_dict = InlineObject36.from_dict(inline_object36_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


