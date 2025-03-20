# ThreatsGetBehavioralDetections200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**malicious_count** | **int** |  | [optional] 
**next** | **object** |  | [optional] 
**previous** | **object** |  | [optional] 
**results** | **object** |  | [optional] 
**suspicious_count** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from kandji.models.threats_get_behavioral_detections200_response import ThreatsGetBehavioralDetections200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatsGetBehavioralDetections200Response from a JSON string
threats_get_behavioral_detections200_response_instance = ThreatsGetBehavioralDetections200Response.from_json(json)
# print the JSON string representation of the object
print(ThreatsGetBehavioralDetections200Response.to_json())

# convert the object into a dict
threats_get_behavioral_detections200_response_dict = threats_get_behavioral_detections200_response_instance.to_dict()
# create an instance of ThreatsGetBehavioralDetections200Response from a dict
threats_get_behavioral_detections200_response_from_dict = ThreatsGetBehavioralDetections200Response.from_dict(threats_get_behavioral_detections200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


