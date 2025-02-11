# IpadApps200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**apps** | **object** |  | [optional] 

## Example

```python
from kandji.models.ipad_apps200_response import IpadApps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IpadApps200Response from a JSON string
ipad_apps200_response_instance = IpadApps200Response.from_json(json)
# print the JSON string representation of the object
print(IpadApps200Response.to_json())

# convert the object into a dict
ipad_apps200_response_dict = ipad_apps200_response_instance.to_dict()
# create an instance of IpadApps200Response from a dict
ipad_apps200_response_from_dict = IpadApps200Response.from_dict(ipad_apps200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


