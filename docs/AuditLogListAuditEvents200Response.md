# AuditLogListAuditEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**previous** | **object** |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from kandji.models.audit_log_list_audit_events200_response import AuditLogListAuditEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogListAuditEvents200Response from a JSON string
audit_log_list_audit_events200_response_instance = AuditLogListAuditEvents200Response.from_json(json)
# print the JSON string representation of the object
print(AuditLogListAuditEvents200Response.to_json())

# convert the object into a dict
audit_log_list_audit_events200_response_dict = audit_log_list_audit_events200_response_instance.to_dict()
# create an instance of AuditLogListAuditEvents200Response from a dict
audit_log_list_audit_events200_response_from_dict = AuditLogListAuditEvents200Response.from_dict(audit_log_list_audit_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


