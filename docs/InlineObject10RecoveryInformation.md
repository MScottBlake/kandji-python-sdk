# InlineObject10RecoveryInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_lock_enabled** | **int** |  | [optional] 
**firmware_password_exist** | **int** |  | [optional] 
**firmware_password_pending** | **int** |  | [optional] 
**password_rotation_scheduled** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object10_recovery_information import InlineObject10RecoveryInformation

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10RecoveryInformation from a JSON string
inline_object10_recovery_information_instance = InlineObject10RecoveryInformation.from_json(json)
# print the JSON string representation of the object
print(InlineObject10RecoveryInformation.to_json())

# convert the object into a dict
inline_object10_recovery_information_dict = inline_object10_recovery_information_instance.to_dict()
# create an instance of InlineObject10RecoveryInformation from a dict
inline_object10_recovery_information_from_dict = InlineObject10RecoveryInformation.from_dict(inline_object10_recovery_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


