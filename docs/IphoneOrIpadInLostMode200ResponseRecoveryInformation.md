# IphoneOrIpadInLostMode200ResponseRecoveryInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_lock_enabled** | **int** |  | [optional] 
**firmware_password_exist** | **int** |  | [optional] 
**firmware_password_pending** | **int** |  | [optional] 
**password_rotation_scheduled** | **object** |  | [optional] 

## Example

```python
from kandji.models.iphone_or_ipad_in_lost_mode200_response_recovery_information import IphoneOrIpadInLostMode200ResponseRecoveryInformation

# TODO update the JSON string below
json = "{}"
# create an instance of IphoneOrIpadInLostMode200ResponseRecoveryInformation from a JSON string
iphone_or_ipad_in_lost_mode200_response_recovery_information_instance = IphoneOrIpadInLostMode200ResponseRecoveryInformation.from_json(json)
# print the JSON string representation of the object
print(IphoneOrIpadInLostMode200ResponseRecoveryInformation.to_json())

# convert the object into a dict
iphone_or_ipad_in_lost_mode200_response_recovery_information_dict = iphone_or_ipad_in_lost_mode200_response_recovery_information_instance.to_dict()
# create an instance of IphoneOrIpadInLostMode200ResponseRecoveryInformation from a dict
iphone_or_ipad_in_lost_mode200_response_recovery_information_from_dict = IphoneOrIpadInLostMode200ResponseRecoveryInformation.from_dict(iphone_or_ipad_in_lost_mode200_response_recovery_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


