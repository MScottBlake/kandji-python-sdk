# InlineObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**blueprint** | [**InlineObjectBlueprint**](InlineObjectBlueprint.md) |  | [optional] 
**access_token_expiry** | **str** |  | [optional] 
**server_name** | **str** |  | [optional] 
**server_uuid** | **str** |  | [optional] 
**admin_id** | **str** |  | [optional] 
**org_name** | **str** |  | [optional] 
**org_email** | **str** |  | [optional] 
**org_phone** | **str** |  | [optional] 
**org_address** | **str** |  | [optional] 
**org_type** | **str** |  | [optional] 
**stoken_file_name** | **str** |  | [optional] 
**last_device_sync** | **object** |  | [optional] 
**defaults** | [**InlineObjectDefaults**](InlineObjectDefaults.md) |  | [optional] 
**days_left** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**status_reason** | **object** |  | [optional] 
**status_received_at** | **object** |  | [optional] 
**device_counts** | [**InlineObjectDeviceCounts**](InlineObjectDeviceCounts.md) |  | [optional] 

## Example

```python
from kandji.models.inline_object import InlineObject

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject from a JSON string
inline_object_instance = InlineObject.from_json(json)
# print the JSON string representation of the object
print(InlineObject.to_json())

# convert the object into a dict
inline_object_dict = inline_object_instance.to_dict()
# create an instance of InlineObject from a dict
inline_object_from_dict = InlineObject.from_dict(inline_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


