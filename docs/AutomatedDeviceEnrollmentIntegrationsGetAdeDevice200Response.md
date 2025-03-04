# AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_tag** | **str** |  | [optional] 
**assignment_status_received_at** | **str** |  | [optional] 
**blueprint** | **str** |  | [optional] 
**blueprint_id** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**dep_account** | [**AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseDepAccount**](AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseDepAccount.md) |  | [optional] 
**description** | **str** |  | [optional] 
**device_assigned_by** | **str** |  | [optional] 
**device_assigned_date** | **str** |  | [optional] 
**device_family** | **str** |  | [optional] 
**failed_assignment_attempts** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**last_assignment_status** | **str** |  | [optional] 
**mdm_device** | [**AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice**](AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice.md) |  | [optional] 
**model** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**profile_assign_time** | **str** |  | [optional] 
**profile_push_time** | **str** |  | [optional] 
**profile_status** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from kandji.models.automated_device_enrollment_integrations_get_ade_device200_response import AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response from a JSON string
automated_device_enrollment_integrations_get_ade_device200_response_instance = AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response.from_json(json)
# print the JSON string representation of the object
print(AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response.to_json())

# convert the object into a dict
automated_device_enrollment_integrations_get_ade_device200_response_dict = automated_device_enrollment_integrations_get_ade_device200_response_instance.to_dict()
# create an instance of AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response from a dict
automated_device_enrollment_integrations_get_ade_device200_response_from_dict = AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response.from_dict(automated_device_enrollment_integrations_get_ade_device200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


