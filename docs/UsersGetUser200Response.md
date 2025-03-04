# UsersGetUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** |  | [optional] 
**archived** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**department** | **object** |  | [optional] 
**deprecated_user_id** | **str** |  | [optional] 
**device_count** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**integration** | [**UsersGetUser200ResponseIntegration**](UsersGetUser200ResponseIntegration.md) |  | [optional] 
**job_title** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.users_get_user200_response import UsersGetUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersGetUser200Response from a JSON string
users_get_user200_response_instance = UsersGetUser200Response.from_json(json)
# print the JSON string representation of the object
print(UsersGetUser200Response.to_json())

# convert the object into a dict
users_get_user200_response_dict = users_get_user200_response_instance.to_dict()
# create an instance of UsersGetUser200Response from a dict
users_get_user200_response_from_dict = UsersGetUser200Response.from_dict(users_get_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


