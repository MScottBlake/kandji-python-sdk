# InlineObject7


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
**enrollment_code** | [**InlineObject5EnrollmentCode**](InlineObject5EnrollmentCode.md) |  | [optional] 

## Example

```python
from kandji.models.inline_object7 import InlineObject7

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject7 from a JSON string
inline_object7_instance = InlineObject7.from_json(json)
# print the JSON string representation of the object
print(InlineObject7.to_json())

# convert the object into a dict
inline_object7_dict = inline_object7_instance.to_dict()
# create an instance of InlineObject7 from a dict
inline_object7_from_dict = InlineObject7.from_dict(inline_object7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


