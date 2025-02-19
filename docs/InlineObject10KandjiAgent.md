# InlineObject10KandjiAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_installed** | **str** |  | [optional] 
**install_date** | **str** |  | [optional] 
**last_check_in** | **str** |  | [optional] 
**agent_version** | **str** |  | [optional] 

## Example

```python
from kandji.models.inline_object10_kandji_agent import InlineObject10KandjiAgent

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject10KandjiAgent from a JSON string
inline_object10_kandji_agent_instance = InlineObject10KandjiAgent.from_json(json)
# print the JSON string representation of the object
print(InlineObject10KandjiAgent.to_json())

# convert the object into a dict
inline_object10_kandji_agent_dict = inline_object10_kandji_agent_instance.to_dict()
# create an instance of InlineObject10KandjiAgent from a dict
inline_object10_kandji_agent_from_dict = InlineObject10KandjiAgent.from_dict(inline_object10_kandji_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


