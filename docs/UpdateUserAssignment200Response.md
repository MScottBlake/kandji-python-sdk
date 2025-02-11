# UpdateUserAssignment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blueprint_id** | **str** |  | [optional] 
**mdm_device** | [**Success200Response1MdmDevice**](Success200Response1MdmDevice.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**dep_account** | [**Success200Response1DepAccount**](Success200Response1DepAccount.md) |  | [optional] 
**asset_tag** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**device_assigned_by** | **str** |  | [optional] 
**device_assigned_date** | **str** |  | [optional] 
**device_family** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**profile_assign_time** | **str** |  | [optional] 
**profile_push_time** | **str** |  | [optional] 
**profile_status** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_assignment_status** | **str** |  | [optional] 
**failed_assignment_attempts** | **int** |  | [optional] 
**assignment_status_received_at** | **str** |  | [optional] 
**blueprint** | **str** |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from kandji.models.update_user_assignment200_response import UpdateUserAssignment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserAssignment200Response from a JSON string
update_user_assignment200_response_instance = UpdateUserAssignment200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateUserAssignment200Response.to_json())

# convert the object into a dict
update_user_assignment200_response_dict = update_user_assignment200_response_instance.to_dict()
# create an instance of UpdateUserAssignment200Response from a dict
update_user_assignment200_response_from_dict = UpdateUserAssignment200Response.from_dict(update_user_assignment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


