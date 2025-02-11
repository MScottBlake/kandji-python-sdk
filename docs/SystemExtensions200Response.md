# SystemExtensions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **object** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**cursor** | **object** |  | [optional] 

## Example

```python
from kandji.models.system_extensions200_response import SystemExtensions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemExtensions200Response from a JSON string
system_extensions200_response_instance = SystemExtensions200Response.from_json(json)
# print the JSON string representation of the object
print(SystemExtensions200Response.to_json())

# convert the object into a dict
system_extensions200_response_dict = system_extensions200_response_instance.to_dict()
# create an instance of SystemExtensions200Response from a dict
system_extensions200_response_from_dict = SystemExtensions200Response.from_dict(system_extensions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


