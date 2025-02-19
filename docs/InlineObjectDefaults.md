# InlineObjectDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from kandji.models.inline_object_defaults import InlineObjectDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObjectDefaults from a JSON string
inline_object_defaults_instance = InlineObjectDefaults.from_json(json)
# print the JSON string representation of the object
print(InlineObjectDefaults.to_json())

# convert the object into a dict
inline_object_defaults_dict = inline_object_defaults_instance.to_dict()
# create an instance of InlineObjectDefaults from a dict
inline_object_defaults_from_dict = InlineObjectDefaults.from_dict(inline_object_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


