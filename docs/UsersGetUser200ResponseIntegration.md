# UsersGetUser200ResponseIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from kandji.models.users_get_user200_response_integration import UsersGetUser200ResponseIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of UsersGetUser200ResponseIntegration from a JSON string
users_get_user200_response_integration_instance = UsersGetUser200ResponseIntegration.from_json(json)
# print the JSON string representation of the object
print(UsersGetUser200ResponseIntegration.to_json())

# convert the object into a dict
users_get_user200_response_integration_dict = users_get_user200_response_integration_instance.to_dict()
# create an instance of UsersGetUser200ResponseIntegration from a dict
users_get_user200_response_integration_from_dict = UsersGetUser200ResponseIntegration.from_dict(users_get_user200_response_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


