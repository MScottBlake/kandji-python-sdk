# ThreatsGetThreatDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**malware_count** | **int** |  | [optional] 
**next** | **object** |  | [optional] 
**previous** | **object** |  | [optional] 
**pup_count** | **int** |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from kandji.models.threats_get_threat_details200_response import ThreatsGetThreatDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatsGetThreatDetails200Response from a JSON string
threats_get_threat_details200_response_instance = ThreatsGetThreatDetails200Response.from_json(json)
# print the JSON string representation of the object
print(ThreatsGetThreatDetails200Response.to_json())

# convert the object into a dict
threats_get_threat_details200_response_dict = threats_get_threat_details200_response_instance.to_dict()
# create an instance of ThreatsGetThreatDetails200Response from a dict
threats_get_threat_details200_response_from_dict = ThreatsGetThreatDetails200Response.from_dict(threats_get_threat_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


