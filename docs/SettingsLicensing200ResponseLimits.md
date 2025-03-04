# SettingsLicensing200ResponseLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_devices** | **int** |  | [optional] 
**max_devices_per_platform** | [**SettingsLicensing200ResponseLimitsMaxDevicesPerPlatform**](SettingsLicensing200ResponseLimitsMaxDevicesPerPlatform.md) |  | [optional] 
**plan_type** | **str** |  | [optional] 

## Example

```python
from kandji.models.settings_licensing200_response_limits import SettingsLicensing200ResponseLimits

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsLicensing200ResponseLimits from a JSON string
settings_licensing200_response_limits_instance = SettingsLicensing200ResponseLimits.from_json(json)
# print the JSON string representation of the object
print(SettingsLicensing200ResponseLimits.to_json())

# convert the object into a dict
settings_licensing200_response_limits_dict = settings_licensing200_response_limits_instance.to_dict()
# create an instance of SettingsLicensing200ResponseLimits from a dict
settings_licensing200_response_limits_from_dict = SettingsLicensing200ResponseLimits.from_dict(settings_licensing200_response_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


