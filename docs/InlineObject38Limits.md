# InlineObject38Limits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_type** | **str** |  | [optional] 
**max_devices** | **int** |  | [optional] 
**max_devices_per_platform** | [**InlineObject38LimitsMaxDevicesPerPlatform**](InlineObject38LimitsMaxDevicesPerPlatform.md) |  | [optional] 

## Example

```python
from kandji.models.inline_object38_limits import InlineObject38Limits

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject38Limits from a JSON string
inline_object38_limits_instance = InlineObject38Limits.from_json(json)
# print the JSON string representation of the object
print(InlineObject38Limits.to_json())

# convert the object into a dict
inline_object38_limits_dict = inline_object38_limits_instance.to_dict()
# create an instance of InlineObject38Limits from a dict
inline_object38_limits_from_dict = InlineObject38Limits.from_dict(inline_object38_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


