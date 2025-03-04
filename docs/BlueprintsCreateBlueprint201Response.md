# BlueprintsCreateBlueprint201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_code** | [**BlueprintsCreateBlueprint201ResponseEnrollmentCode**](BlueprintsCreateBlueprint201ResponseEnrollmentCode.md) |  | [optional] 
**icon** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**params** | **object** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from kandji.models.blueprints_create_blueprint201_response import BlueprintsCreateBlueprint201Response

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintsCreateBlueprint201Response from a JSON string
blueprints_create_blueprint201_response_instance = BlueprintsCreateBlueprint201Response.from_json(json)
# print the JSON string representation of the object
print(BlueprintsCreateBlueprint201Response.to_json())

# convert the object into a dict
blueprints_create_blueprint201_response_dict = blueprints_create_blueprint201_response_instance.to_dict()
# create an instance of BlueprintsCreateBlueprint201Response from a dict
blueprints_create_blueprint201_response_from_dict = BlueprintsCreateBlueprint201Response.from_dict(blueprints_create_blueprint201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


