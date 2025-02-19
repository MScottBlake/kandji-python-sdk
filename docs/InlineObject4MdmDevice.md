# InlineObject4MdmDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**enrolled_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**enrollment_status** | **int** |  | [optional] 
**deferred_install** | **int** |  | [optional] 
**is_missing** | **int** |  | [optional] 
**is_removed** | **int** |  | [optional] 

## Example

```python
from kandji.models.inline_object4_mdm_device import InlineObject4MdmDevice

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject4MdmDevice from a JSON string
inline_object4_mdm_device_instance = InlineObject4MdmDevice.from_json(json)
# print the JSON string representation of the object
print(InlineObject4MdmDevice.to_json())

# convert the object into a dict
inline_object4_mdm_device_dict = inline_object4_mdm_device_instance.to_dict()
# create an instance of InlineObject4MdmDevice from a dict
inline_object4_mdm_device_from_dict = InlineObject4MdmDevice.from_dict(inline_object4_mdm_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


