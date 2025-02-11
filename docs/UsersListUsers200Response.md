# UsersListUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**previous** | **object** |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from kandji.models.users_list_users200_response import UsersListUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersListUsers200Response from a JSON string
users_list_users200_response_instance = UsersListUsers200Response.from_json(json)
# print the JSON string representation of the object
print(UsersListUsers200Response.to_json())

# convert the object into a dict
users_list_users200_response_dict = users_list_users200_response_instance.to_dict()
# create an instance of UsersListUsers200Response from a dict
users_list_users200_response_from_dict = UsersListUsers200Response.from_dict(users_list_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


