# Success200Response17


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**Success200Response17Counts**](Success200Response17Counts.md) |  | [optional] 
**limits** | [**Success200Response17Limits**](Success200Response17Limits.md) |  | [optional] 
**tenant_over_license_limit** | **int** |  | [optional] 

## Example

```python
from kandji.models.success200_response17 import Success200Response17

# TODO update the JSON string below
json = "{}"
# create an instance of Success200Response17 from a JSON string
success200_response17_instance = Success200Response17.from_json(json)
# print the JSON string representation of the object
print(Success200Response17.to_json())

# convert the object into a dict
success200_response17_dict = success200_response17_instance.to_dict()
# create an instance of Success200Response17 from a dict
success200_response17_from_dict = Success200Response17.from_dict(success200_response17_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


