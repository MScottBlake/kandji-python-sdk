# CreateIntegration200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**blueprint** | [**CreateIntegration200ResponseBlueprint**](CreateIntegration200ResponseBlueprint.md) |  | [optional] 
**access_token_expiry** | **str** |  | [optional] 
**server_name** | **str** |  | [optional] 
**server_uuid** | **str** |  | [optional] 
**admin_id** | **str** |  | [optional] 
**org_name** | **str** |  | [optional] 
**org_email** | **str** |  | [optional] 
**org_phone** | **str** |  | [optional] 
**org_address** | **str** |  | [optional] 
**org_type** | **str** |  | [optional] 
**stoken_file_name** | **str** |  | [optional] 
**last_device_sync** | **object** |  | [optional] 
**defaults** | [**CreateIntegration200ResponseDefaults**](CreateIntegration200ResponseDefaults.md) |  | [optional] 
**days_left** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**status_reason** | **object** |  | [optional] 
**status_received_at** | **object** |  | [optional] 
**device_counts** | [**CreateIntegration200ResponseDeviceCounts**](CreateIntegration200ResponseDeviceCounts.md) |  | [optional] 

## Example

```python
from kandji.models.create_integration200_response import CreateIntegration200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIntegration200Response from a JSON string
create_integration200_response_instance = CreateIntegration200Response.from_json(json)
# print the JSON string representation of the object
print(CreateIntegration200Response.to_json())

# convert the object into a dict
create_integration200_response_dict = create_integration200_response_instance.to_dict()
# create an instance of CreateIntegration200Response from a dict
create_integration200_response_from_dict = CreateIntegration200Response.from_dict(create_integration200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


