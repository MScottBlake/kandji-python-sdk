# DeviceInformationGetDeviceDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_lock** | [**DeviceInformationGetDeviceDetails200ResponseActivationLock**](DeviceInformationGetDeviceDetails200ResponseActivationLock.md) |  | [optional] 
**apple_business_manager** | [**DeviceInformationGetDeviceDetails200ResponseAppleBusinessManager**](DeviceInformationGetDeviceDetails200ResponseAppleBusinessManager.md) |  | [optional] 
**automated_device_enrollment** | [**DeviceInformationGetDeviceDetails200ResponseAutomatedDeviceEnrollment**](DeviceInformationGetDeviceDetails200ResponseAutomatedDeviceEnrollment.md) |  | [optional] 
**cellular** | [**DeviceInformationGetDeviceDetails200ResponseCellular**](DeviceInformationGetDeviceDetails200ResponseCellular.md) |  | [optional] 
**filevault** | [**DeviceInformationGetDeviceDetails200ResponseFilevault**](DeviceInformationGetDeviceDetails200ResponseFilevault.md) |  | [optional] 
**general** | [**DeviceInformationGetDeviceDetails200ResponseGeneral**](DeviceInformationGetDeviceDetails200ResponseGeneral.md) |  | [optional] 
**hardware_overview** | [**DeviceInformationGetDeviceDetails200ResponseHardwareOverview**](DeviceInformationGetDeviceDetails200ResponseHardwareOverview.md) |  | [optional] 
**installed_profiles** | **object** |  | [optional] 
**kandji_agent** | [**DeviceInformationGetDeviceDetails200ResponseKandjiAgent**](DeviceInformationGetDeviceDetails200ResponseKandjiAgent.md) |  | [optional] 
**lost_mode** | [**DeviceInformationGetDeviceDetails200ResponseLostMode**](DeviceInformationGetDeviceDetails200ResponseLostMode.md) |  | [optional] 
**mdm** | [**DeviceInformationGetDeviceDetails200ResponseMdm**](DeviceInformationGetDeviceDetails200ResponseMdm.md) |  | [optional] 
**network** | **object** |  | [optional] 
**recovery_information** | [**DeviceInformationGetDeviceDetails200ResponseRecoveryInformation**](DeviceInformationGetDeviceDetails200ResponseRecoveryInformation.md) |  | [optional] 
**security_information** | [**DeviceInformationGetDeviceDetails200ResponseSecurityInformation**](DeviceInformationGetDeviceDetails200ResponseSecurityInformation.md) |  | [optional] 
**tags** | **object** |  | [optional] 
**users** | [**DeviceInformationGetDeviceDetails200ResponseUsers**](DeviceInformationGetDeviceDetails200ResponseUsers.md) |  | [optional] 
**volumes** | **object** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_details200_response import DeviceInformationGetDeviceDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceDetails200Response from a JSON string
device_information_get_device_details200_response_instance = DeviceInformationGetDeviceDetails200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceDetails200Response.to_json())

# convert the object into a dict
device_information_get_device_details200_response_dict = device_information_get_device_details200_response_instance.to_dict()
# create an instance of DeviceInformationGetDeviceDetails200Response from a dict
device_information_get_device_details200_response_from_dict = DeviceInformationGetDeviceDetails200Response.from_dict(device_information_get_device_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


