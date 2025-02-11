# CreateIntegration200ResponseDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from kandji.models.create_integration200_response_defaults import CreateIntegration200ResponseDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIntegration200ResponseDefaults from a JSON string
create_integration200_response_defaults_instance = CreateIntegration200ResponseDefaults.from_json(json)
# print the JSON string representation of the object
print(CreateIntegration200ResponseDefaults.to_json())

# convert the object into a dict
create_integration200_response_defaults_dict = create_integration200_response_defaults_instance.to_dict()
# create an instance of CreateIntegration200ResponseDefaults from a dict
create_integration200_response_defaults_from_dict = CreateIntegration200ResponseDefaults.from_dict(create_integration200_response_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


