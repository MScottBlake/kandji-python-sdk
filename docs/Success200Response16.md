# Success200Response16


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** |  | [optional] 
**archived** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**department** | **object** |  | [optional] 
**deprecated_user_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**integration** | [**Success200Response16Integration**](Success200Response16Integration.md) |  | [optional] 
**job_title** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**device_count** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.success200_response16 import Success200Response16

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response16 from a JSON string
success200_response16_instance = Success200Response16.from_json(json)
# print the JSON string representation of the object
print(Success200Response16.to_json())

# convert the object into a dict
success200_response16_dict = success200_response16_instance.to_dict()
# create an instance of Success200Response16 from a dict
success200_response16_from_dict = Success200Response16.from_dict(success200_response16_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


