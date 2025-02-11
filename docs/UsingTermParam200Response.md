# UsingTermParam200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **object** |  | [optional] 
**previous** | **object** |  | [optional] 
**malware_count** | **int** |  | [optional] 
**pup_count** | **int** |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from kandji.models.using_term_param200_response import UsingTermParam200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsingTermParam200Response from a JSON string
using_term_param200_response_instance = UsingTermParam200Response.from_json(json)
# print the JSON string representation of the object
print(UsingTermParam200Response.to_json())

# convert the object into a dict
using_term_param200_response_dict = using_term_param200_response_instance.to_dict()
# create an instance of UsingTermParam200Response from a dict
using_term_param200_response_from_dict = UsingTermParam200Response.from_dict(using_term_param200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


