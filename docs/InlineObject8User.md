# InlineObject8User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_archived** | **int** |  | [optional] 

## Example

```python
from kandji.models.inline_object8_user import InlineObject8User

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject8User from a JSON string
inline_object8_user_instance = InlineObject8User.from_json(json)
# print the JSON string representation of the object
print(InlineObject8User.to_json())

# convert the object into a dict
inline_object8_user_dict = inline_object8_user_instance.to_dict()
# create an instance of InlineObject8User from a dict
inline_object8_user_from_dict = InlineObject8User.from_dict(inline_object8_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


