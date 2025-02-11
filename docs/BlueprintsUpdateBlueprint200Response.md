# BlueprintsUpdateBlueprint200Response


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
**missing_computers_count** | **int** |  | [optional] 
**enrollment_code** | [**BlueprintsCreateBlueprint201ResponseEnrollmentCode**](BlueprintsCreateBlueprint201ResponseEnrollmentCode.md) |  | [optional] 

## Example

```python
from kandji.models.blueprints_update_blueprint200_response import BlueprintsUpdateBlueprint200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintsUpdateBlueprint200Response from a JSON string
blueprints_update_blueprint200_response_instance = BlueprintsUpdateBlueprint200Response.from_json(json)
# print the JSON string representation of the object
print(BlueprintsUpdateBlueprint200Response.to_json())

# convert the object into a dict
blueprints_update_blueprint200_response_dict = blueprints_update_blueprint200_response_instance.to_dict()
# create an instance of BlueprintsUpdateBlueprint200Response from a dict
blueprints_update_blueprint200_response_from_dict = BlueprintsUpdateBlueprint200Response.from_dict(blueprints_update_blueprint200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


