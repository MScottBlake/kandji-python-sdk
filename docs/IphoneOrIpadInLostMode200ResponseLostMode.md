# IphoneOrIpadInLostMode200ResponseLostMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lost_mode_status** | **str** |  | [optional] 
**enabled_by** | **str** |  | [optional] 
**enable_status_at** | **str** |  | [optional] 
**lock_screen_message** | **str** |  | [optional] 
**lock_screen_phone_number** | **str** |  | [optional] 
**lock_screen_footnote** | **str** |  | [optional] 
**disable_status** | **str** |  | [optional] 
**disabled_by** | **str** |  | [optional] 
**disable_status_at** | **str** |  | [optional] 
**last_location_status** | **str** |  | [optional] 
**last_location_status_at** | **str** |  | [optional] 
**last_location** | [**IphoneOrIpadInLostMode200ResponseLostModeLastLocation**](IphoneOrIpadInLostMode200ResponseLostModeLastLocation.md) |  | [optional] 
**last_location_at** | **str** |  | [optional] 
**sound_status** | **str** |  | [optional] 
**sound_status_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.iphone_or_ipad_in_lost_mode200_response_lost_mode import IphoneOrIpadInLostMode200ResponseLostMode

# TODO update the JSON string below
json = "{}"
# create an instance of IphoneOrIpadInLostMode200ResponseLostMode from a JSON string
iphone_or_ipad_in_lost_mode200_response_lost_mode_instance = IphoneOrIpadInLostMode200ResponseLostMode.from_json(json)
# print the JSON string representation of the object
print(IphoneOrIpadInLostMode200ResponseLostMode.to_json())

# convert the object into a dict
iphone_or_ipad_in_lost_mode200_response_lost_mode_dict = iphone_or_ipad_in_lost_mode200_response_lost_mode_instance.to_dict()
# create an instance of IphoneOrIpadInLostMode200ResponseLostMode from a dict
iphone_or_ipad_in_lost_mode200_response_lost_mode_from_dict = IphoneOrIpadInLostMode200ResponseLostMode.from_dict(iphone_or_ipad_in_lost_mode200_response_lost_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


