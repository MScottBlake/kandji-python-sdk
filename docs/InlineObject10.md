# InlineObject10


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**InlineObject10General**](InlineObject10General.md) |  | [optional] 
**mdm** | [**InlineObject10Mdm**](InlineObject10Mdm.md) |  | [optional] 
**activation_lock** | [**InlineObject10ActivationLock**](InlineObject10ActivationLock.md) |  | [optional] 
**filevault** | [**InlineObject10Filevault**](InlineObject10Filevault.md) |  | [optional] 
**lost_mode** | [**InlineObject10LostMode**](InlineObject10LostMode.md) |  | [optional] 
**automated_device_enrollment** | [**InlineObject10AutomatedDeviceEnrollment**](InlineObject10AutomatedDeviceEnrollment.md) |  | [optional] 
**kandji_agent** | [**InlineObject10KandjiAgent**](InlineObject10KandjiAgent.md) |  | [optional] 
**hardware_overview** | [**InlineObject10HardwareOverview**](InlineObject10HardwareOverview.md) |  | [optional] 
**volumes** | **object** |  | [optional] 
**network** | **object** |  | [optional] 
**recovery_information** | [**InlineObject10RecoveryInformation**](InlineObject10RecoveryInformation.md) |  | [optional] 
**users** | [**InlineObject10Users**](InlineObject10Users.md) |  | [optional] 
**installed_profiles** | **object** |  | [optional] 
**apple_business_manager** | [**InlineObject10AppleBusinessManager**](InlineObject10AppleBusinessManager.md) |  | [optional] 
**security_information** | [**InlineObject10SecurityInformation**](InlineObject10SecurityInformation.md) |  | [optional] 
**cellular** | [**InlineObject10Cellular**](InlineObject10Cellular.md) |  | [optional] 
**tags** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object10 import InlineObject10

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10 from a JSON string
inline_object10_instance = InlineObject10.from_json(json)
# print the JSON string representation of the object
print(InlineObject10.to_json())

# convert the object into a dict
inline_object10_dict = inline_object10_instance.to_dict()
# create an instance of InlineObject10 from a dict
inline_object10_from_dict = InlineObject10.from_dict(inline_object10_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


