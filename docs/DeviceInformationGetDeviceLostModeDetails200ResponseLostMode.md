# DeviceInformationGetDeviceLostModeDetails200ResponseLostMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_status** | **str** |  | [optional] 
**disable_status_at** | **str** |  | [optional] 
**disabled_by** | **str** |  | [optional] 
**enable_status_at** | **str** |  | [optional] 
**enabled_by** | **str** |  | [optional] 
**last_location** | [**DeviceInformationGetDeviceLostModeDetails200ResponseLostModeLastLocation**](DeviceInformationGetDeviceLostModeDetails200ResponseLostModeLastLocation.md) |  | [optional] 
**last_location_at** | **str** |  | [optional] 
**last_location_status** | **str** |  | [optional] 
**last_location_status_at** | **str** |  | [optional] 
**lock_screen_footnote** | **str** |  | [optional] 
**lock_screen_message** | **str** |  | [optional] 
**lock_screen_phone_number** | **str** |  | [optional] 
**lost_mode_status** | **str** |  | [optional] 
**sound_status** | **str** |  | [optional] 
**sound_status_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device_lost_mode_details200_response_lost_mode import DeviceInformationGetDeviceLostModeDetails200ResponseLostMode

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDeviceLostModeDetails200ResponseLostMode from a JSON string
device_information_get_device_lost_mode_details200_response_lost_mode_instance = DeviceInformationGetDeviceLostModeDetails200ResponseLostMode.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDeviceLostModeDetails200ResponseLostMode.to_json())

# convert the object into a dict
device_information_get_device_lost_mode_details200_response_lost_mode_dict = device_information_get_device_lost_mode_details200_response_lost_mode_instance.to_dict()
# create an instance of DeviceInformationGetDeviceLostModeDetails200ResponseLostMode from a dict
device_information_get_device_lost_mode_details200_response_lost_mode_from_dict = DeviceInformationGetDeviceLostModeDetails200ResponseLostMode.from_dict(device_information_get_device_lost_mode_details200_response_lost_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


