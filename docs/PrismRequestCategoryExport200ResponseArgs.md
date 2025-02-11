# PrismRequestCategoryExport200ResponseArgs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **object** |  | [optional] 
**columns** | **object** |  | [optional] 
**sort_by** | **str** |  | [optional] 
**blueprint_ids** | **object** |  | [optional] 
**device_families** | **object** |  | [optional] 

## Example

```python
from kandji.models.prism_request_category_export200_response_args import PrismRequestCategoryExport200ResponseArgs

# TODO update the JSON string below
json = "{}"
# create an instance of PrismRequestCategoryExport200ResponseArgs from a JSON string
prism_request_category_export200_response_args_instance = PrismRequestCategoryExport200ResponseArgs.from_json(json)
# print the JSON string representation of the object
print(PrismRequestCategoryExport200ResponseArgs.to_json())

# convert the object into a dict
prism_request_category_export200_response_args_dict = prism_request_category_export200_response_args_instance.to_dict()
# create an instance of PrismRequestCategoryExport200ResponseArgs from a dict
prism_request_category_export200_response_args_from_dict = PrismRequestCategoryExport200ResponseArgs.from_dict(prism_request_category_export200_response_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


