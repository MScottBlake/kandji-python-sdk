# EdrStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**library_items** | **object** |  | [optional] 

## Example

```python
from kandji.models.edr_status200_response import EdrStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EdrStatus200Response from a JSON string
edr_status200_response_instance = EdrStatus200Response.from_json(json)
# print the JSON string representation of the object
print(EdrStatus200Response.to_json())

# convert the object into a dict
edr_status200_response_dict = edr_status200_response_instance.to_dict()
# create an instance of EdrStatus200Response from a dict
edr_status200_response_from_dict = EdrStatus200Response.from_dict(edr_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


