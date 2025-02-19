# InlineObject4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blueprint_id** | **str** |  | [optional] 
**mdm_device** | [**InlineObject4MdmDevice**](InlineObject4MdmDevice.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**dep_account** | [**InlineObject4DepAccount**](InlineObject4DepAccount.md) |  | [optional] 
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
from kandji.models.inline_object4 import InlineObject4

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject4 from a JSON string
inline_object4_instance = InlineObject4.from_json(json)
# print the JSON string representation of the object
print(InlineObject4.to_json())

# convert the object into a dict
inline_object4_dict = inline_object4_instance.to_dict()
# create an instance of InlineObject4 from a dict
inline_object4_from_dict = InlineObject4.from_dict(inline_object4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


