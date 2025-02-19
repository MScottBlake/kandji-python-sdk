# InlineObject10Filevault


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
from kandji.models.inline_object10_filevault import InlineObject10Filevault

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10Filevault from a JSON string
inline_object10_filevault_instance = InlineObject10Filevault.from_json(json)
# print the JSON string representation of the object
print(InlineObject10Filevault.to_json())

# convert the object into a dict
inline_object10_filevault_dict = inline_object10_filevault_instance.to_dict()
# create an instance of InlineObject10Filevault from a dict
inline_object10_filevault_from_dict = InlineObject10Filevault.from_dict(inline_object10_filevault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


