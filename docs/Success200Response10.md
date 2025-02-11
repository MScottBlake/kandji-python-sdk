# Success200Response10


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **object** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**cursor** | **str** |  | [optional] 

## Example

```python
from kandji.models.success200_response10 import Success200Response10

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response10 from a JSON string
success200_response10_instance = Success200Response10.from_json(json)
# print the JSON string representation of the object
print(Success200Response10.to_json())

# convert the object into a dict
success200_response10_dict = success200_response10_instance.to_dict()
# create an instance of Success200Response10 from a dict
success200_response10_from_dict = Success200Response10.from_dict(success200_response10_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


