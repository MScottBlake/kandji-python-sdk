# DeviceInformationGetDeviceDetails200ResponseKandjiAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_installed** | **str** |  | [optional] 
**agent_version** | **str** |  | [optional] 
**install_date** | **str** |  | [optional] 
**last_check_in** | **str** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response_kandji_agent import DeviceInformationGetDeviceDetails200ResponseKandjiAgent

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200ResponseKandjiAgent from a JSON string
device_information_get_device_details200_response_kandji_agent_instance = DeviceInformationGetDeviceDetails200ResponseKandjiAgent.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200ResponseKandjiAgent.to_json())

# convert the object into a dict
device_information_get_device_details200_response_kandji_agent_dict = device_information_get_device_details200_response_kandji_agent_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200ResponseKandjiAgent from a dict
device_information_get_device_details200_response_kandji_agent_from_dict = DeviceInformationGetDeviceDetails200ResponseKandjiAgent.from_dict(device_information_get_device_details200_response_kandji_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


