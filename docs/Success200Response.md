# Success200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **object** |  | [optional] 
**previous** | **object** |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from kandji.models.success200_response import Success200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response from a JSON string
success200_response_instance = Success200Response.from_json(json)
# print the JSON string representation of the object
print(Success200Response.to_json())

# convert the object into a dict
success200_response_dict = success200_response_instance.to_dict()
# create an instance of Success200Response from a dict
success200_response_from_dict = Success200Response.from_dict(success200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


