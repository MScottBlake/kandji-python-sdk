# GetDeviceLostModeDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**lost_mode** | [**IphoneOrIpadInLostMode200ResponseLostMode**](IphoneOrIpadInLostMode200ResponseLostMode.md) |  | [optional] 

## Example

```python
from kandji.models.get_device_lost_mode_details200_response import GetDeviceLostModeDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceLostModeDetails200Response from a JSON string
get_device_lost_mode_details200_response_instance = GetDeviceLostModeDetails200Response.from_json(json)
# print the JSON string representation of the object
print(GetDeviceLostModeDetails200Response.to_json())

# convert the object into a dict
get_device_lost_mode_details200_response_dict = get_device_lost_mode_details200_response_instance.to_dict()
# create an instance of GetDeviceLostModeDetails200Response from a dict
get_device_lost_mode_details200_response_from_dict = GetDeviceLostModeDetails200Response.from_dict(get_device_lost_mode_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


