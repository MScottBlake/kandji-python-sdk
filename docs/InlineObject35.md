# InlineObject35


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_id** | **str** |  | [optional] 
**cve_description** | **str** |  | [optional] 
**cve_link** | **str** |  | [optional] 
**cvss_score** | **float** |  | [optional] 
**kev_score** | **int** |  | [optional] 
**cvss_severity** | **str** |  | [optional] 
**cve_published_on** | **str** |  | [optional] 
**cve_updated_on** | **str** |  | [optional] 
**devices_impacted** | **int** |  | [optional] 
**first_detection_date** | **str** |  | [optional] 

## Example

```python
from kandji.models.inline_object35 import InlineObject35

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject35 from a JSON string
inline_object35_instance = InlineObject35.from_json(json)
# print the JSON string representation of the object
print(InlineObject35.to_json())

# convert the object into a dict
inline_object35_dict = inline_object35_instance.to_dict()
# create an instance of InlineObject35 from a dict
inline_object35_from_dict = InlineObject35.from_dict(inline_object35_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


