# PrismApplicationFirewall200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **object** |  | [optional] 
**data** | **object** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **object** |  | [optional] 

## Example

```python
from kandji.models.prism_application_firewall200_response import PrismApplicationFirewall200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrismApplicationFirewall200Response from a JSON string
prism_application_firewall200_response_instance = PrismApplicationFirewall200Response.from_json(json)
# print the JSON string representation of the object
print(PrismApplicationFirewall200Response.to_json())

# convert the object into a dict
prism_application_firewall200_response_dict = prism_application_firewall200_response_instance.to_dict()
# create an instance of PrismApplicationFirewall200Response from a dict
prism_application_firewall200_response_from_dict = PrismApplicationFirewall200Response.from_dict(prism_application_firewall200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


