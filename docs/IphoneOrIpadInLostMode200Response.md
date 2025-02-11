# IphoneOrIpadInLostMode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**IphoneOrIpadInLostMode200ResponseGeneral**](IphoneOrIpadInLostMode200ResponseGeneral.md) |  | [optional] 
**mdm** | [**IphoneOrIpadInLostMode200ResponseMdm**](IphoneOrIpadInLostMode200ResponseMdm.md) |  | [optional] 
**activation_lock** | [**IphoneOrIpadInLostMode200ResponseActivationLock**](IphoneOrIpadInLostMode200ResponseActivationLock.md) |  | [optional] 
**filevault** | [**IphoneOrIpadInLostMode200ResponseFilevault**](IphoneOrIpadInLostMode200ResponseFilevault.md) |  | [optional] 
**lost_mode** | [**IphoneOrIpadInLostMode200ResponseLostMode**](IphoneOrIpadInLostMode200ResponseLostMode.md) |  | [optional] 
**automated_device_enrollment** | [**IphoneOrIpadInLostMode200ResponseAutomatedDeviceEnrollment**](IphoneOrIpadInLostMode200ResponseAutomatedDeviceEnrollment.md) |  | [optional] 
**kandji_agent** | [**IphoneOrIpadInLostMode200ResponseKandjiAgent**](IphoneOrIpadInLostMode200ResponseKandjiAgent.md) |  | [optional] 
**hardware_overview** | [**IphoneOrIpadInLostMode200ResponseHardwareOverview**](IphoneOrIpadInLostMode200ResponseHardwareOverview.md) |  | [optional] 
**volumes** | **object** |  | [optional] 
**network** | **object** |  | [optional] 
**recovery_information** | [**IphoneOrIpadInLostMode200ResponseRecoveryInformation**](IphoneOrIpadInLostMode200ResponseRecoveryInformation.md) |  | [optional] 
**users** | [**IphoneOrIpadInLostMode200ResponseUsers**](IphoneOrIpadInLostMode200ResponseUsers.md) |  | [optional] 
**installed_profiles** | **object** |  | [optional] 
**apple_business_manager** | [**IphoneOrIpadInLostMode200ResponseAppleBusinessManager**](IphoneOrIpadInLostMode200ResponseAppleBusinessManager.md) |  | [optional] 
**security_information** | [**IphoneOrIpadInLostMode200ResponseSecurityInformation**](IphoneOrIpadInLostMode200ResponseSecurityInformation.md) |  | [optional] 
**cellular** | [**IphoneOrIpadInLostMode200ResponseCellular**](IphoneOrIpadInLostMode200ResponseCellular.md) |  | [optional] 
**tags** | **object** |  | [optional] 

## Example

```python
from kandji.models.iphone_or_ipad_in_lost_mode200_response import IphoneOrIpadInLostMode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IphoneOrIpadInLostMode200Response from a JSON string
iphone_or_ipad_in_lost_mode200_response_instance = IphoneOrIpadInLostMode200Response.from_json(json)
# print the JSON string representation of the object
print(IphoneOrIpadInLostMode200Response.to_json())

# convert the object into a dict
iphone_or_ipad_in_lost_mode200_response_dict = iphone_or_ipad_in_lost_mode200_response_instance.to_dict()
# create an instance of IphoneOrIpadInLostMode200Response from a dict
iphone_or_ipad_in_lost_mode200_response_from_dict = IphoneOrIpadInLostMode200Response.from_dict(iphone_or_ipad_in_lost_mode200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


