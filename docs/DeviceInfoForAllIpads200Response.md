# DeviceInfoForAllIpads200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**args** | [**DeviceInfoForAllIpads200ResponseArgs**](DeviceInfoForAllIpads200ResponseArgs.md) |  | [optional] 
**error_msg** | **object** |  | [optional] 
**path** | **object** |  | [optional] 
**signed_url** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from kandji.models.device_info_for_all_ipads200_response import DeviceInfoForAllIpads200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfoForAllIpads200Response from a JSON string
device_info_for_all_ipads200_response_instance = DeviceInfoForAllIpads200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceInfoForAllIpads200Response.to_json())

# convert the object into a dict
device_info_for_all_ipads200_response_dict = device_info_for_all_ipads200_response_instance.to_dict()
# create an instance of DeviceInfoForAllIpads200Response from a dict
device_info_for_all_ipads200_response_from_dict = DeviceInfoForAllIpads200Response.from_dict(device_info_for_all_ipads200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


