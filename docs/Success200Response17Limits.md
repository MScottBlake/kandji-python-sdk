# Success200Response17Limits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_type** | **str** |  | [optional] 
**max_devices** | **int** |  | [optional] 
**max_devices_per_platform** | [**Success200Response17LimitsMaxDevicesPerPlatform**](Success200Response17LimitsMaxDevicesPerPlatform.md) |  | [optional] 

## Example

```python
from kandji.models.success200_response17_limits import Success200Response17Limits

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response17Limits from a JSON string
success200_response17_limits_instance = Success200Response17Limits.from_json(json)
# print the JSON string representation of the object
print(Success200Response17Limits.to_json())

# convert the object into a dict
success200_response17_limits_dict = success200_response17_limits_instance.to_dict()
# create an instance of Success200Response17Limits from a dict
success200_response17_limits_from_dict = Success200Response17Limits.from_dict(success200_response17_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


