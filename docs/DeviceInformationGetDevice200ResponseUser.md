# DeviceInformationGetDevice200ResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_archived** | **int** |  | [optional] 

## Example

```python
from kandji.models.device_information_get_device200_response_user import DeviceInformationGetDevice200ResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInformationGetDevice200ResponseUser from a JSON string
device_information_get_device200_response_user_instance = DeviceInformationGetDevice200ResponseUser.from_json(json)
# print the JSON string representation of the object
print(DeviceInformationGetDevice200ResponseUser.to_json())

# convert the object into a dict
device_information_get_device200_response_user_dict = device_information_get_device200_response_user_instance.to_dict()
# create an instance of DeviceInformationGetDevice200ResponseUser from a dict
device_information_get_device200_response_user_from_dict = DeviceInformationGetDevice200ResponseUser.from_dict(device_information_get_device200_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


