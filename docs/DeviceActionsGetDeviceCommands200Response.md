# DeviceActionsGetDeviceCommands200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**commands** | [**AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response**](AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response.md) |  | [optional] 

## Example

```python
from kandji.models.device_actions_get_device_commands200_response import DeviceActionsGetDeviceCommands200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceActionsGetDeviceCommands200Response from a JSON string
device_actions_get_device_commands200_response_instance = DeviceActionsGetDeviceCommands200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceActionsGetDeviceCommands200Response.to_json())

# convert the object into a dict
device_actions_get_device_commands200_response_dict = device_actions_get_device_commands200_response_instance.to_dict()
# create an instance of DeviceActionsGetDeviceCommands200Response from a dict
device_actions_get_device_commands200_response_from_dict = DeviceActionsGetDeviceCommands200Response.from_dict(device_actions_get_device_commands200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


