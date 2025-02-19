# InlineObject10Cellular


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_roaming** | **int** |  | [optional] 
**data_roaming** | **int** |  | [optional] 
**cellular_technology** | **int** |  | [optional] 
**subscriptions** | **object** |  | [optional] 

## Example

```python
from kandji.models.inline_object10_cellular import InlineObject10Cellular

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10Cellular from a JSON string
inline_object10_cellular_instance = InlineObject10Cellular.from_json(json)
# print the JSON string representation of the object
print(InlineObject10Cellular.to_json())

# convert the object into a dict
inline_object10_cellular_dict = inline_object10_cellular_instance.to_dict()
# create an instance of InlineObject10Cellular from a dict
inline_object10_cellular_from_dict = InlineObject10Cellular.from_dict(inline_object10_cellular_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


