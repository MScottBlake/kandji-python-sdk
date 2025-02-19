# InlineObject10AppleBusinessManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**device_family** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**device_assigned_date** | **str** |  | [optional] 
**device_assigned_by** | **str** |  | [optional] 

## Example

```python
from kandji.models.inline_object10_apple_business_manager import InlineObject10AppleBusinessManager

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10AppleBusinessManager from a JSON string
inline_object10_apple_business_manager_instance = InlineObject10AppleBusinessManager.from_json(json)
# print the JSON string representation of the object
print(InlineObject10AppleBusinessManager.to_json())

# convert the object into a dict
inline_object10_apple_business_manager_dict = inline_object10_apple_business_manager_instance.to_dict()
# create an instance of InlineObject10AppleBusinessManager from a dict
inline_object10_apple_business_manager_from_dict = InlineObject10AppleBusinessManager.from_dict(inline_object10_apple_business_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


