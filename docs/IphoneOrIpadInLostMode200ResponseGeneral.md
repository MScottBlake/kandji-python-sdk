# IphoneOrIpadInLostMode200ResponseGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**last_enrollment** | **str** |  | [optional] 
**first_enrollment** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**supplemental_build_version** | **str** |  | [optional] 
**supplemental_os_version_extra** | **str** |  | [optional] 
**system_version** | **str** |  | [optional] 
**boot_volume** | **str** |  | [optional] 
**time_since_boot** | **str** |  | [optional] 
**last_user** | **str** |  | [optional] 
**asset_tag** | **str** |  | [optional] 
**assigned_user** | **str** |  | [optional] 
**blueprint_name** | **str** |  | [optional] 
**blueprint_uuid** | **str** |  | [optional] 

## Example

```python
from kandji.models.iphone_or_ipad_in_lost_mode200_response_general import IphoneOrIpadInLostMode200ResponseGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of IphoneOrIpadInLostMode200ResponseGeneral from a JSON string
iphone_or_ipad_in_lost_mode200_response_general_instance = IphoneOrIpadInLostMode200ResponseGeneral.from_json(json)
# print the JSON string representation of the object
print(IphoneOrIpadInLostMode200ResponseGeneral.to_json())

# convert the object into a dict
iphone_or_ipad_in_lost_mode200_response_general_dict = iphone_or_ipad_in_lost_mode200_response_general_instance.to_dict()
# create an instance of IphoneOrIpadInLostMode200ResponseGeneral from a dict
iphone_or_ipad_in_lost_mode200_response_general_from_dict = IphoneOrIpadInLostMode200ResponseGeneral.from_dict(iphone_or_ipad_in_lost_mode200_response_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


