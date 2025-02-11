# CreateIntegration200ResponseBlueprint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from kandji.models.create_integration200_response_blueprint import CreateIntegration200ResponseBlueprint

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIntegration200ResponseBlueprint from a JSON string
create_integration200_response_blueprint_instance = CreateIntegration200ResponseBlueprint.from_json(json)
# print the JSON string representation of the object
print(CreateIntegration200ResponseBlueprint.to_json())

# convert the object into a dict
create_integration200_response_blueprint_dict = create_integration200_response_blueprint_instance.to_dict()
# create an instance of CreateIntegration200ResponseBlueprint from a dict
create_integration200_response_blueprint_from_dict = CreateIntegration200ResponseBlueprint.from_dict(create_integration200_response_blueprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


