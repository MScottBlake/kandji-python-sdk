# PrismGetCategoryExport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**args** | [**PrismRequestCategoryExport200ResponseArgs**](PrismRequestCategoryExport200ResponseArgs.md) |  | [optional] 
**error_msg** | **object** |  | [optional] 
**path** | **str** |  | [optional] 
**signed_url** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.prism_get_category_export200_response import PrismGetCategoryExport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrismGetCategoryExport200Response from a JSON string
prism_get_category_export200_response_instance = PrismGetCategoryExport200Response.from_json(json)
# print the JSON string representation of the object
print(PrismGetCategoryExport200Response.to_json())

# convert the object into a dict
prism_get_category_export200_response_dict = prism_get_category_export200_response_instance.to_dict()
# create an instance of PrismGetCategoryExport200Response from a dict
prism_get_category_export200_response_from_dict = PrismGetCategoryExport200Response.from_dict(prism_get_category_export200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


