# AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_expiry** | **str** |  | [optional] 
**admin_id** | **str** |  | [optional] 
**blueprint** | [**AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200ResponseBlueprint**](AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200ResponseBlueprint.md) |  | [optional] 
**days_left** | **int** |  | [optional] 
**defaults** | [**AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200ResponseDefaults**](AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200ResponseDefaults.md) |  | [optional] 
**device_counts** | [**AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200ResponseDeviceCounts**](AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200ResponseDeviceCounts.md) |  | [optional] 
**id** | **str** |  | [optional] 
**last_device_sync** | **object** |  | [optional] 
**org_address** | **str** |  | [optional] 
**org_email** | **str** |  | [optional] 
**org_name** | **str** |  | [optional] 
**org_phone** | **str** |  | [optional] 
**org_type** | **str** |  | [optional] 
**server_name** | **str** |  | [optional] 
**server_uuid** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_reason** | **object** |  | [optional] 
**status_received_at** | **object** |  | [optional] 
**stoken_file_name** | **str** |  | [optional] 

## Example

```python
from kandji.models.automated_device_enrollment_integrations_create_ade_integration200_response import AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response from a JSON string
automated_device_enrollment_integrations_create_ade_integration200_response_instance = AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response.from_json(json)
# print the JSON string representation of the object
print(AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response.to_json())

# convert the object into a dict
automated_device_enrollment_integrations_create_ade_integration200_response_dict = automated_device_enrollment_integrations_create_ade_integration200_response_instance.to_dict()
# create an instance of AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response from a dict
automated_device_enrollment_integrations_create_ade_integration200_response_from_dict = AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response.from_dict(automated_device_enrollment_integrations_create_ade_integration200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


