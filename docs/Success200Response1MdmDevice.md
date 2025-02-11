# Success200Response1MdmDevice


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
from kandji.models.success200_response1_mdm_device import Success200Response1MdmDevice

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response1MdmDevice from a JSON string
success200_response1_mdm_device_instance = Success200Response1MdmDevice.from_json(json)
# print the JSON string representation of the object
print(Success200Response1MdmDevice.to_json())

# convert the object into a dict
success200_response1_mdm_device_dict = success200_response1_mdm_device_instance.to_dict()
# create an instance of Success200Response1MdmDevice from a dict
success200_response1_mdm_device_from_dict = Success200Response1MdmDevice.from_dict(success200_response1_mdm_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


