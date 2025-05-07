# VulnerabilitiesListAffectedApps200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**results** | **object** |  | [optional] 
**size** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from kandji.models.vulnerabilities_list_affected_apps200_response import VulnerabilitiesListAffectedApps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VulnerabilitiesListAffectedApps200Response from a JSON string
vulnerabilities_list_affected_apps200_response_instance = VulnerabilitiesListAffectedApps200Response.from_json(json)
# print the JSON string representation of the object
print(VulnerabilitiesListAffectedApps200Response.to_json())

# convert the object into a dict
vulnerabilities_list_affected_apps200_response_dict = vulnerabilities_list_affected_apps200_response_instance.to_dict()
# create an instance of VulnerabilitiesListAffectedApps200Response from a dict
vulnerabilities_list_affected_apps200_response_from_dict = VulnerabilitiesListAffectedApps200Response.from_dict(vulnerabilities_list_affected_apps200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


