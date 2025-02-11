# DeviceInfoForAllIpads200ResponseArgs


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
from kandji.models.device_info_for_all_ipads200_response_args import DeviceInfoForAllIpads200ResponseArgs

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfoForAllIpads200ResponseArgs from a JSON string
device_info_for_all_ipads200_response_args_instance = DeviceInfoForAllIpads200ResponseArgs.from_json(json)
# print the JSON string representation of the object
print(DeviceInfoForAllIpads200ResponseArgs.to_json())

# convert the object into a dict
device_info_for_all_ipads200_response_args_dict = device_info_for_all_ipads200_response_args_instance.to_dict()
# create an instance of DeviceInfoForAllIpads200ResponseArgs from a dict
device_info_for_all_ipads200_response_args_from_dict = DeviceInfoForAllIpads200ResponseArgs.from_dict(device_info_for_all_ipads200_response_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


