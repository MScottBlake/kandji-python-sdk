# ExampleExportStatusCheck200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**args** | [**DeviceInfoForAllIpads200ResponseArgs**](DeviceInfoForAllIpads200ResponseArgs.md) |  | [optional] 
**error_msg** | **object** |  | [optional] 
**path** | **str** |  | [optional] 
**signed_url** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.example_export_status_check200_response import ExampleExportStatusCheck200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleExportStatusCheck200Response from a JSON string
example_export_status_check200_response_instance = ExampleExportStatusCheck200Response.from_json(json)
# print the JSON string representation of the object
print(ExampleExportStatusCheck200Response.to_json())

# convert the object into a dict
example_export_status_check200_response_dict = example_export_status_check200_response_instance.to_dict()
# create an instance of ExampleExportStatusCheck200Response from a dict
example_export_status_check200_response_from_dict = ExampleExportStatusCheck200Response.from_dict(example_export_status_check200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


