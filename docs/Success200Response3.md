# Success200Response3


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
**missing_computers_count** | **int** |  | [optional] 
**enrollment_code** | [**Success201ResponseEnrollmentCode**](Success201ResponseEnrollmentCode.md) |  | [optional] 

## Example

```python
from kandji.models.success200_response3 import Success200Response3

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response3 from a JSON string
success200_response3_instance = Success200Response3.from_json(json)
# print the JSON string representation of the object
print(Success200Response3.to_json())

# convert the object into a dict
success200_response3_dict = success200_response3_instance.to_dict()
# create an instance of Success200Response3 from a dict
success200_response3_from_dict = Success200Response3.from_dict(success200_response3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


