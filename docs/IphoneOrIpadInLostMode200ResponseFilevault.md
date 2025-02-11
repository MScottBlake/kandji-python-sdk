# IphoneOrIpadInLostMode200ResponseFilevault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filevault_enabled** | **object** |  | [optional] 
**filevault_recoverykey_type** | **str** |  | [optional] 
**filevault_prk_escrowed** | **int** |  | [optional] 
**filevault_next_rotation** | **str** |  | [optional] 
**filevault_regen_required** | **int** |  | [optional] 

## Example

```python
from kandji.models.iphone_or_ipad_in_lost_mode200_response_filevault import IphoneOrIpadInLostMode200ResponseFilevault

# TODO update the JSON string below
json = "{}"
# create an instance of IphoneOrIpadInLostMode200ResponseFilevault from a JSON string
iphone_or_ipad_in_lost_mode200_response_filevault_instance = IphoneOrIpadInLostMode200ResponseFilevault.from_json(json)
# print the JSON string representation of the object
print(IphoneOrIpadInLostMode200ResponseFilevault.to_json())

# convert the object into a dict
iphone_or_ipad_in_lost_mode200_response_filevault_dict = iphone_or_ipad_in_lost_mode200_response_filevault_instance.to_dict()
# create an instance of IphoneOrIpadInLostMode200ResponseFilevault from a dict
iphone_or_ipad_in_lost_mode200_response_filevault_from_dict = IphoneOrIpadInLostMode200ResponseFilevault.from_dict(iphone_or_ipad_in_lost_mode200_response_filevault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


