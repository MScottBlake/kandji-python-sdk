# PrismRequestCategoryExport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**args** | [**PrismRequestCategoryExport200ResponseArgs**](PrismRequestCategoryExport200ResponseArgs.md) |  | [optional] 
**error_msg** | **object** |  | [optional] 
**path** | **object** |  | [optional] 
**signed_url** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.prism_request_category_export200_response import PrismRequestCategoryExport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrismRequestCategoryExport200Response from a JSON string
prism_request_category_export200_response_instance = PrismRequestCategoryExport200Response.from_json(json)
# print the JSON string representation of the object
print(PrismRequestCategoryExport200Response.to_json())

# convert the object into a dict
prism_request_category_export200_response_dict = prism_request_category_export200_response_instance.to_dict()
# create an instance of PrismRequestCategoryExport200Response from a dict
prism_request_category_export200_response_from_dict = PrismRequestCategoryExport200Response.from_dict(prism_request_category_export200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


