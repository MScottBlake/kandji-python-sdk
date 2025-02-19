# InlineObject38


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**InlineObject38Counts**](InlineObject38Counts.md) |  | [optional] 
**limits** | [**InlineObject38Limits**](InlineObject38Limits.md) |  | [optional] 
**tenant_over_license_limit** | **int** |  | [optional] 

## Example

```python
from kandji.models.inline_object38 import InlineObject38

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject38 from a JSON string
inline_object38_instance = InlineObject38.from_json(json)
# print the JSON string representation of the object
print(InlineObject38.to_json())

# convert the object into a dict
inline_object38_dict = inline_object38_instance.to_dict()
# create an instance of InlineObject38 from a dict
inline_object38_from_dict = InlineObject38.from_dict(inline_object38_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


