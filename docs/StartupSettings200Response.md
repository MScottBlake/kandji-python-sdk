# StartupSettings200Response


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
from kandji.models.startup_settings200_response import StartupSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StartupSettings200Response from a JSON string
startup_settings200_response_instance = StartupSettings200Response.from_json(json)
# print the JSON string representation of the object
print(StartupSettings200Response.to_json())

# convert the object into a dict
startup_settings200_response_dict = startup_settings200_response_instance.to_dict()
# create an instance of StartupSettings200Response from a dict
startup_settings200_response_from_dict = StartupSettings200Response.from_dict(startup_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


