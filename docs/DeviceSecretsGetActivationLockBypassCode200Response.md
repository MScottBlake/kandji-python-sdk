# DeviceSecretsGetActivationLockBypassCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_based_albc** | **str** |  | [optional] 
**device_based_albc** | **str** |  | [optional] 

## Example

```python
from kandji.models.device_secrets_get_activation_lock_bypass_code200_response import DeviceSecretsGetActivationLockBypassCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSecretsGetActivationLockBypassCode200Response from a JSON string
device_secrets_get_activation_lock_bypass_code200_response_instance = DeviceSecretsGetActivationLockBypassCode200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceSecretsGetActivationLockBypassCode200Response.to_json())

# convert the object into a dict
device_secrets_get_activation_lock_bypass_code200_response_dict = device_secrets_get_activation_lock_bypass_code200_response_instance.to_dict()
# create an instance of DeviceSecretsGetActivationLockBypassCode200Response from a dict
device_secrets_get_activation_lock_bypass_code200_response_from_dict = DeviceSecretsGetActivationLockBypassCode200Response.from_dict(device_secrets_get_activation_lock_bypass_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


