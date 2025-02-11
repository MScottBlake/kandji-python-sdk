# AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**enrolled_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**enrollment_status** | **int** |  | [optional] 
**deferred_install** | **int** |  | [optional] 
**is_missing** | **int** |  | [optional] 
**is_removed** | **int** |  | [optional] 

## Example

```python
from kandji.models.automated_device_enrollment_integrations_get_ade_device200_response_mdm_device import AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice

# TODO update the JSON string below
json = "{}"
# create an instance of AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice from a JSON string
automated_device_enrollment_integrations_get_ade_device200_response_mdm_device_instance = AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice.from_json(json)
# print the JSON string representation of the object
print(AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice.to_json())

# convert the object into a dict
automated_device_enrollment_integrations_get_ade_device200_response_mdm_device_dict = automated_device_enrollment_integrations_get_ade_device200_response_mdm_device_instance.to_dict()
# create an instance of AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice from a dict
automated_device_enrollment_integrations_get_ade_device200_response_mdm_device_from_dict = AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice.from_dict(automated_device_enrollment_integrations_get_ade_device200_response_mdm_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


