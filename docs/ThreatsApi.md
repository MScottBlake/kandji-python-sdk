# kandji_python_sdk.ThreatsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_threat_details**](ThreatsApi.md#get_threat_details) | **GET** /api/v1/threat-details | Get Threat Details


# **get_threat_details**
> object get_threat_details(classification=classification, date_range=date_range, device_id=device_id, status=status, sort_by=sort_by, term=term, limit=limit, offset=offset)

Get Threat Details

Get threat details.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji_python_sdk
from kandji_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://<sub_domain>.api.kandji.io
# See configuration.py for a list of all supported configuration parameters.
configuration = kandji_python_sdk.Configuration(
    host = "https://<sub_domain>.api.kandji.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Token): bearer
configuration = kandji_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kandji_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kandji_python_sdk.ThreatsApi(api_client)
    classification = 'malware' # str | Return all records matching a specified classification. The following classification options are available: \\`malware\\` and \\`pup\\`. Leave this parameter empty to return all classification types. (optional)
    date_range = '7' # str | Return all records within a specified number of days. Any positive number of days may be specified. Examples: \\`7\\`, \\`30\\`, \\`60\\`, \\`90\\`, \\`180\\`, or \\`365\\`. (optional)
    device_id = '15fcec08-xxxx-xxxx-xxxx-7c2f950910eb' # str |  (optional)
    status = 'quarantined' # str | Return all records matching a specified status. The following status options are available: \\`quarantined\\`, \\`not\\_quarantined\\`, or \\`released\\`. Leave this parameter empty to return all status types. (optional)
    sort_by = 'status' # str | Results can be sorted with the following options:    \\* threat\\\\\\_name \\* classification \\* device\\\\\\_name \\* process\\ \\\\_name \\* process\\\\\\_owner \\* detection\\\\\\_date \\* status    Prepending a dash (\\\\\\-) to the parameter value will reverse the order of the returned results.   \\`?sort\\_by\\=\\-device\\_name\\` will order the response by device\\\\\\_name in descending order. (optional)
    term = 'Chrome' # str | Search term to filter threat results.   The response will include anything matching the following fields: \\`device\\_name\\`, \\ `file\\_hash\\`, and \\`file\\_path\\`.   So if you search for \\`bad file\\`, the results will include anywhere \\`bad file\\` exists in the three fields above. (optional)
    limit = '1000' # str | A hard upper \\`limit\\` is set at 1000 records returned per request. If more records are expected, pagination should be used using the \\`limit\\` and \\`offset\\` parameters.    Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '1' # str | Specify the starting record to return (optional)

    try:
        # Get Threat Details
        api_response = api_instance.get_threat_details(classification=classification, date_range=date_range, device_id=device_id, status=status, sort_by=sort_by, term=term, limit=limit, offset=offset)
        print("The response of ThreatsApi->get_threat_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatsApi->get_threat_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification** | **str**| Return all records matching a specified classification. The following classification options are available: \\&#x60;malware\\&#x60; and \\&#x60;pup\\&#x60;. Leave this parameter empty to return all classification types. | [optional] 
 **date_range** | **str**| Return all records within a specified number of days. Any positive number of days may be specified. Examples: \\&#x60;7\\&#x60;, \\&#x60;30\\&#x60;, \\&#x60;60\\&#x60;, \\&#x60;90\\&#x60;, \\&#x60;180\\&#x60;, or \\&#x60;365\\&#x60;. | [optional] 
 **device_id** | **str**|  | [optional] 
 **status** | **str**| Return all records matching a specified status. The following status options are available: \\&#x60;quarantined\\&#x60;, \\&#x60;not\\_quarantined\\&#x60;, or \\&#x60;released\\&#x60;. Leave this parameter empty to return all status types. | [optional] 
 **sort_by** | **str**| Results can be sorted with the following options:    \\* threat\\\\\\_name \\* classification \\* device\\\\\\_name \\* process\\ \\\\_name \\* process\\\\\\_owner \\* detection\\\\\\_date \\* status    Prepending a dash (\\\\\\-) to the parameter value will reverse the order of the returned results.   \\&#x60;?sort\\_by\\&#x3D;\\-device\\_name\\&#x60; will order the response by device\\\\\\_name in descending order. | [optional] 
 **term** | **str**| Search term to filter threat results.   The response will include anything matching the following fields: \\&#x60;device\\_name\\&#x60;, \\ &#x60;file\\_hash\\&#x60;, and \\&#x60;file\\_path\\&#x60;.   So if you search for \\&#x60;bad file\\&#x60;, the results will include anywhere \\&#x60;bad file\\&#x60; exists in the three fields above. | [optional] 
 **limit** | **str**| A hard upper \\&#x60;limit\\&#x60; is set at 1000 records returned per request. If more records are expected, pagination should be used using the \\&#x60;limit\\&#x60; and \\&#x60;offset\\&#x60; parameters.    Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 

### Return type

**object**

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

