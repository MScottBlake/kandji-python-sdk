# GetDeviceCommands200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**commands** | [**GetDeviceActivity200ResponseActivity**](GetDeviceActivity200ResponseActivity.md) |  | [optional] 

## Example

```python
from kandji.models.get_device_commands200_response import GetDeviceCommands200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceCommands200Response from a JSON string
get_device_commands200_response_instance = GetDeviceCommands200Response.from_json(json)
# print the JSON string representation of the object
print(GetDeviceCommands200Response.to_json())

# convert the object into a dict
get_device_commands200_response_dict = get_device_commands200_response_instance.to_dict()
# create an instance of GetDeviceCommands200Response from a dict
get_device_commands200_response_from_dict = GetDeviceCommands200Response.from_dict(get_device_commands200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


