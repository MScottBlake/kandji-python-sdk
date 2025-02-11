# Success201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**params** | **object** |  | [optional] 
**enrollment_code** | [**Success201ResponseEnrollmentCode**](Success201ResponseEnrollmentCode.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from kandji.models.success201_response import Success201Response

# TODO update the JSON string below
json = "{}"
# create an instance of Success201Response from a JSON string
success201_response_instance = Success201Response.from_json(json)
# print the JSON string representation of the object
print(Success201Response.to_json())

# convert the object into a dict
success201_response_dict = success201_response_instance.to_dict()
# create an instance of Success201Response from a dict
success201_response_from_dict = Success201Response.from_dict(success201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


