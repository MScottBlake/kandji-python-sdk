# PrismApplications200Response


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
from kandji.models.prism_applications200_response import PrismApplications200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrismApplications200Response from a JSON string
prism_applications200_response_instance = PrismApplications200Response.from_json(json)
# print the JSON string representation of the object
print(PrismApplications200Response.to_json())

# convert the object into a dict
prism_applications200_response_dict = prism_applications200_response_instance.to_dict()
# create an instance of PrismApplications200Response from a dict
prism_applications200_response_from_dict = PrismApplications200Response.from_dict(prism_applications200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


