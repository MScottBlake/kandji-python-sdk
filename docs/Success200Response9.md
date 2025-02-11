# Success200Response9


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
from kandji.models.success200_response9 import Success200Response9

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response9 from a JSON string
success200_response9_instance = Success200Response9.from_json(json)
# print the JSON string representation of the object
print(Success200Response9.to_json())

# convert the object into a dict
success200_response9_dict = success200_response9_instance.to_dict()
# create an instance of Success200Response9 from a dict
success200_response9_from_dict = Success200Response9.from_dict(success200_response9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


