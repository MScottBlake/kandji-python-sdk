# TagsCreateTag201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from kandji.models.tags_create_tag201_response import TagsCreateTag201Response

# TODO update the JSON string below
json = "{}"
# create an instance of TagsCreateTag201Response from a JSON string
tags_create_tag201_response_instance = TagsCreateTag201Response.from_json(json)
# print the JSON string representation of the object
print(TagsCreateTag201Response.to_json())

# convert the object into a dict
tags_create_tag201_response_dict = tags_create_tag201_response_instance.to_dict()
# create an instance of TagsCreateTag201Response from a dict
tags_create_tag201_response_from_dict = TagsCreateTag201Response.from_dict(tags_create_tag201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


