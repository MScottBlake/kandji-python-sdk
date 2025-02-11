# DeviceInformationGetDeviceDetails200ResponseMdm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mdm_enabled** | **str** |  | [optional] 
**supervised** | **str** |  | [optional] 
**install_date** | **str** |  | [optional] 
**last_check_in** | **str** |  | [optional] 
**mdm_enabled_user** | **object** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response_mdm import DeviceInformationGetDeviceDetails200ResponseMdm

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200ResponseMdm from a JSON string
device_information_get_device_details200_response_mdm_instance = DeviceInformationGetDeviceDetails200ResponseMdm.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200ResponseMdm.to_json())

# convert the object into a dict
device_information_get_device_details200_response_mdm_dict = device_information_get_device_details200_response_mdm_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200ResponseMdm from a dict
device_information_get_device_details200_response_mdm_from_dict = DeviceInformationGetDeviceDetails200ResponseMdm.from_dict(device_information_get_device_details200_response_mdm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


