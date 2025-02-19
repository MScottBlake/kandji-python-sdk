# InlineObject10ActivationLock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_code_failed** | **int** |  | [optional] 
**user_activation_lock_enabled** | **int** |  | [optional] 
**device_activation_lock_enabled** | **int** |  | [optional] 
**activation_lock_allowed_while_supervised** | **int** |  | [optional] 
**activation_lock_supported** | **int** |  | [optional] 

## Example

```python
from kandji.models.inline_object10_activation_lock import InlineObject10ActivationLock

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10ActivationLock from a JSON string
inline_object10_activation_lock_instance = InlineObject10ActivationLock.from_json(json)
# print the JSON string representation of the object
print(InlineObject10ActivationLock.to_json())

# convert the object into a dict
inline_object10_activation_lock_dict = inline_object10_activation_lock_instance.to_dict()
# create an instance of InlineObject10ActivationLock from a dict
inline_object10_activation_lock_from_dict = InlineObject10ActivationLock.from_dict(inline_object10_activation_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


