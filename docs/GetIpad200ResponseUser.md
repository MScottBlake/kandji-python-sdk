# GetIpad200ResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_archived** | **int** |  | [optional] 

## Example

```python
from kandji.models.get_ipad200_response_user import GetIpad200ResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of GetIpad200ResponseUser from a JSON string
get_ipad200_response_user_instance = GetIpad200ResponseUser.from_json(json)
# print the JSON string representation of the object
print(GetIpad200ResponseUser.to_json())

# convert the object into a dict
get_ipad200_response_user_dict = get_ipad200_response_user_instance.to_dict()
# create an instance of GetIpad200ResponseUser from a dict
get_ipad200_response_user_from_dict = GetIpad200ResponseUser.from_dict(get_ipad200_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


