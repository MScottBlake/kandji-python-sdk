# Success200Response2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**params** | **object** |  | [optional] 
**computers_count** | **int** |  | [optional] 
**enrollment_code** | [**Success201ResponseEnrollmentCode**](Success201ResponseEnrollmentCode.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from kandji.models.success200_response2 import Success200Response2

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response2 from a JSON string
success200_response2_instance = Success200Response2.from_json(json)
# print the JSON string representation of the object
print(Success200Response2.to_json())

# convert the object into a dict
success200_response2_dict = success200_response2_instance.to_dict()
# create an instance of Success200Response2 from a dict
success200_response2_from_dict = Success200Response2.from_dict(success200_response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


