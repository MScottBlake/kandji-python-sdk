# PrismDeviceInformation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**cursor** | **object** |  | [optional] 

## Example

```python
from kandji.models.prism_device_information200_response import PrismDeviceInformation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrismDeviceInformation200Response from a JSON string
prism_device_information200_response_instance = PrismDeviceInformation200Response.from_json(json)
# print the JSON string representation of the object
print(PrismDeviceInformation200Response.to_json())

# convert the object into a dict
prism_device_information200_response_dict = prism_device_information200_response_instance.to_dict()
# create an instance of PrismDeviceInformation200Response from a dict
prism_device_information200_response_from_dict = PrismDeviceInformation200Response.from_dict(prism_device_information200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


