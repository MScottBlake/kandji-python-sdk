# TransparencyDatabase200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **object** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**cursor** | **object** |  | [optional] 

## Example

```python
from kandji.models.transparency_database200_response import TransparencyDatabase200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TransparencyDatabase200Response from a JSON string
transparency_database200_response_instance = TransparencyDatabase200Response.from_json(json)
# print the JSON string representation of the object
print(TransparencyDatabase200Response.to_json())

# convert the object into a dict
transparency_database200_response_dict = transparency_database200_response_instance.to_dict()
# create an instance of TransparencyDatabase200Response from a dict
transparency_database200_response_from_dict = TransparencyDatabase200Response.from_dict(transparency_database200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


