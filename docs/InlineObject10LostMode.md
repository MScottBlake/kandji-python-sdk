# InlineObject10LostMode


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
**last_location** | [**InlineObject10LostModeLastLocation**](InlineObject10LostModeLastLocation.md) |  | [optional] 
**last_location_at** | **str** |  | [optional] 
**sound_status** | **str** |  | [optional] 
**sound_status_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.inline_object10_lost_mode import InlineObject10LostMode

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10LostMode from a JSON string
inline_object10_lost_mode_instance = InlineObject10LostMode.from_json(json)
# print the JSON string representation of the object
print(InlineObject10LostMode.to_json())

# convert the object into a dict
inline_object10_lost_mode_dict = inline_object10_lost_mode_instance.to_dict()
# create an instance of InlineObject10LostMode from a dict
inline_object10_lost_mode_from_dict = InlineObject10LostMode.from_dict(inline_object10_lost_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


