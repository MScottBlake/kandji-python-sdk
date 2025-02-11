# EdrStatus200Response1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **object** |  | [optional] 
**previous** | **object** |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from kandji.models.edr_status200_response1 import EdrStatus200Response1

# TODO update the JSON string below
json = "{}"
# create an instance of EdrStatus200Response1 from a JSON string
edr_status200_response1_instance = EdrStatus200Response1.from_json(json)
# print the JSON string representation of the object
print(EdrStatus200Response1.to_json())

# convert the object into a dict
edr_status200_response1_dict = edr_status200_response1_instance.to_dict()
# create an instance of EdrStatus200Response1 from a dict
edr_status200_response1_from_dict = EdrStatus200Response1.from_dict(edr_status200_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


