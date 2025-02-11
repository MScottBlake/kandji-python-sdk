# SettingsLicensing200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**SettingsLicensing200ResponseCounts**](SettingsLicensing200ResponseCounts.md) |  | [optional] 
**limits** | [**SettingsLicensing200ResponseLimits**](SettingsLicensing200ResponseLimits.md) |  | [optional] 
**tenant_over_license_limit** | **int** |  | [optional] 

## Example

```python
from kandji.models.settings_licensing200_response import SettingsLicensing200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsLicensing200Response from a JSON string
settings_licensing200_response_instance = SettingsLicensing200Response.from_json(json)
# print the JSON string representation of the object
print(SettingsLicensing200Response.to_json())

# convert the object into a dict
settings_licensing200_response_dict = settings_licensing200_response_instance.to_dict()
# create an instance of SettingsLicensing200Response from a dict
settings_licensing200_response_from_dict = SettingsLicensing200Response.from_dict(settings_licensing200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


