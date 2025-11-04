# DeviceInformationGetDeviceDetails200ResponseHardware


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_capacity** | **str** |  | [optional] 
**total_capacity** | **str** |  | [optional] 
**total_ram** | **str** |  | [optional] 
**wifi_mac_address** | **str** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response_hardware import DeviceInformationGetDeviceDetails200ResponseHardware

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200ResponseHardware from a JSON string
device_information_get_device_details200_response_hardware_instance = DeviceInformationGetDeviceDetails200ResponseHardware.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200ResponseHardware.to_json())

# convert the object into a dict
device_information_get_device_details200_response_hardware_dict = device_information_get_device_details200_response_hardware_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200ResponseHardware from a dict
device_information_get_device_details200_response_hardware_from_dict = DeviceInformationGetDeviceDetails200ResponseHardware.from_dict(device_information_get_device_details200_response_hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


