# InlineObject10Users


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regular_users** | **object** |  | [optional] 
**system_users** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object10_users import InlineObject10Users

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10Users from a JSON string
inline_object10_users_instance = InlineObject10Users.from_json(json)
# print the JSON string representation of the object
print(InlineObject10Users.to_json())

# convert the object into a dict
inline_object10_users_dict = inline_object10_users_instance.to_dict()
# create an instance of InlineObject10Users from a dict
inline_object10_users_from_dict = InlineObject10Users.from_dict(inline_object10_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


