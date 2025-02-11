# PrismLocalUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**cursor** | **str** |  | [optional] 

## Example

```python
from kandji.models.prism_local_users200_response import PrismLocalUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrismLocalUsers200Response from a JSON string
prism_local_users200_response_instance = PrismLocalUsers200Response.from_json(json)
# print the JSON string representation of the object
print(PrismLocalUsers200Response.to_json())

# convert the object into a dict
prism_local_users200_response_dict = prism_local_users200_response_instance.to_dict()
# create an instance of PrismLocalUsers200Response from a dict
prism_local_users200_response_from_dict = PrismLocalUsers200Response.from_dict(prism_local_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


