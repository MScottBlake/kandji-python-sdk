# GetDevicesInABlueprintSortedBySerialNumber200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**cursor** | **object** |  | [optional] 

## Example

```python
from kandji.models.get_devices_in_a_blueprint_sorted_by_serial_number200_response import GetDevicesInABlueprintSortedBySerialNumber200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevicesInABlueprintSortedBySerialNumber200Response from a JSON string
get_devices_in_a_blueprint_sorted_by_serial_number200_response_instance = GetDevicesInABlueprintSortedBySerialNumber200Response.from_json(json)
# print the JSON string representation of the object
print(GetDevicesInABlueprintSortedBySerialNumber200Response.to_json())

# convert the object into a dict
get_devices_in_a_blueprint_sorted_by_serial_number200_response_dict = get_devices_in_a_blueprint_sorted_by_serial_number200_response_instance.to_dict()
# create an instance of GetDevicesInABlueprintSortedBySerialNumber200Response from a dict
get_devices_in_a_blueprint_sorted_by_serial_number200_response_from_dict = GetDevicesInABlueprintSortedBySerialNumber200Response.from_dict(get_devices_in_a_blueprint_sorted_by_serial_number200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


