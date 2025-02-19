# InlineObject10Mdm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mdm_enabled** | **str** |  | [optional] 
**supervised** | **str** |  | [optional] 
**install_date** | **str** |  | [optional] 
**last_check_in** | **str** |  | [optional] 
**mdm_enabled_user** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object10_mdm import InlineObject10Mdm

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10Mdm from a JSON string
inline_object10_mdm_instance = InlineObject10Mdm.from_json(json)
# print the JSON string representation of the object
print(InlineObject10Mdm.to_json())

# convert the object into a dict
inline_object10_mdm_dict = inline_object10_mdm_instance.to_dict()
# create an instance of InlineObject10Mdm from a dict
inline_object10_mdm_from_dict = InlineObject10Mdm.from_dict(inline_object10_mdm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


