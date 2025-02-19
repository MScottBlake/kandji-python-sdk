# InlineObjectBlueprint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from kandji.models.inline_object_blueprint import InlineObjectBlueprint

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObjectBlueprint from a JSON string
inline_object_blueprint_instance = InlineObjectBlueprint.from_json(json)
# print the JSON string representation of the object
print(InlineObjectBlueprint.to_json())

# convert the object into a dict
inline_object_blueprint_dict = inline_object_blueprint_instance.to_dict()
# create an instance of InlineObjectBlueprint from a dict
inline_object_blueprint_from_dict = InlineObjectBlueprint.from_dict(inline_object_blueprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


