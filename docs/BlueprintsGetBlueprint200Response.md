# BlueprintsGetBlueprint200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**params** | **object** |  | [optional] 
**computers_count** | **int** |  | [optional] 
**enrollment_code** | [**BlueprintsCreateBlueprint201ResponseEnrollmentCode**](BlueprintsCreateBlueprint201ResponseEnrollmentCode.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from kandji.models.blueprints_get_blueprint200_response import BlueprintsGetBlueprint200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintsGetBlueprint200Response from a JSON string
blueprints_get_blueprint200_response_instance = BlueprintsGetBlueprint200Response.from_json(json)
# print the JSON string representation of the object
print(BlueprintsGetBlueprint200Response.to_json())

# convert the object into a dict
blueprints_get_blueprint200_response_dict = blueprints_get_blueprint200_response_instance.to_dict()
# create an instance of BlueprintsGetBlueprint200Response from a dict
blueprints_get_blueprint200_response_from_dict = BlueprintsGetBlueprint200Response.from_dict(blueprints_get_blueprint200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


