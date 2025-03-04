# PrismActivationLock200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **object** |  | [optional] 
**data** | **object** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **object** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrismActivationLock200Response from a JSON string
prism_activation_lock200_response_instance = PrismActivationLock200Response.from_json(json)
# print the JSON string representation of the object
print(PrismActivationLock200Response.to_json())

# convert the object into a dict
prism_activation_lock200_response_dict = prism_activation_lock200_response_instance.to_dict()
# create an instance of PrismActivationLock200Response from a dict
prism_activation_lock200_response_from_dict = PrismActivationLock200Response.from_dict(prism_activation_lock200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


