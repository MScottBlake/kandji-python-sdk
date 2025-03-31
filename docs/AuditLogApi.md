# kandji.AuditLogApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_audit_events**](AuditLogApi.md#list_audit_events) | **GET** /api/v1/audit/events | List audit events


# **list_audit_events**
> AuditLogListAuditEvents200Response list_audit_events(limit, sort_by, start_date=start_date, end_date=end_date, cursor=cursor)

List audit events

<p>List audit log events from the Kandji Activity module.</p>
<p>Returns events related to</p>
<ul>
<li><p>Blueprint and Library Item creation, updates, and deletions (CUD)</p>
</li>
<li><p>Access to sensitive data (such as FileVault keys and recovery keys)</p>
</li>
<li><p>Device lifecycle events (enrollment, deletion, MDM removal, blueprint changes)</p>
</li>
<li><p>User directory events (including directory user deletions)</p>
</li>
<li><p>Administrative actions (tenant owner updates, API token management (CUD))</p>
</li>
<li><p>Admin user management activities</p>
</li>
<li><p>Vulnerability management detections and remediations (for customers with this feature)</p>
</li>
</ul>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.audit_log_list_audit_events200_response import AuditLogListAuditEvents200Response
from kandji.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://<sub_domain>.api.kandji.io
# See configuration.py for a list of all supported configuration parameters.
configuration = kandji.Configuration(
    host = "https://<sub_domain>.api.kandji.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Token): bearer
configuration = kandji.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kandji.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kandji.AuditLogApi(api_client)
    limit = '500' # str | A max upper <code>limit</code> is set at 500 records returned per request. Pagination should be used using the cursor in the <code>next</code> key to request more results. Additionally, parameter queries can be added to a request to filter the results.
    sort_by = '-occurred_at' # str | Sort results by <code>occurred_at</code>, <code>id</code> either ascending (default behavior) or descending(-) order.
    start_date = '2024-11-26T22:58:26.239570Z' # str | Filter by start date in datetime or year-month-day (2024-11-26) formats (optional)
    end_date = '2024-12-06T17:48:41.784439Z' # str | Filter by start date in datetime or year-month-day (2024-12-06) formats (optional)
    cursor = '' # str | You can pass the next cursor as a parameter or use the URL in the next key to get the next page of results or to start from where you left off last. (optional)

    try:
        # List audit events
        api_response = api_instance.list_audit_events(limit, sort_by, start_date=start_date, end_date=end_date, cursor=cursor)
        print("The response of AuditLogApi->list_audit_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->list_audit_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| A max upper &lt;code&gt;limit&lt;/code&gt; is set at 500 records returned per request. Pagination should be used using the cursor in the &lt;code&gt;next&lt;/code&gt; key to request more results. Additionally, parameter queries can be added to a request to filter the results. | 
 **sort_by** | **str**| Sort results by &lt;code&gt;occurred_at&lt;/code&gt;, &lt;code&gt;id&lt;/code&gt; either ascending (default behavior) or descending(-) order. | 
 **start_date** | **str**| Filter by start date in datetime or year-month-day (2024-11-26) formats | [optional] 
 **end_date** | **str**| Filter by start date in datetime or year-month-day (2024-12-06) formats | [optional] 
 **cursor** | **str**| You can pass the next cursor as a parameter or use the URL in the next key to get the next page of results or to start from where you left off last. | [optional] 

### Return type

[**AuditLogListAuditEvents200Response**](AuditLogListAuditEvents200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

