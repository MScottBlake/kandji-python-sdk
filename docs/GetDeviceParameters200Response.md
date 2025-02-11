# GetDeviceParameters200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**parameters** | **object** |  | [optional] 

## Example

```python
from kandji.models.get_device_parameters200_response import GetDeviceParameters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceParameters200Response from a JSON string
get_device_parameters200_response_instance = GetDeviceParameters200Response.from_json(json)
# print the JSON string representation of the object
print(GetDeviceParameters200Response.to_json())

# convert the object into a dict
get_device_parameters200_response_dict = get_device_parameters200_response_instance.to_dict()
# create an instance of GetDeviceParameters200Response from a dict
get_device_parameters200_response_from_dict = GetDeviceParameters200Response.from_dict(get_device_parameters200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


