# kandji.ThreatsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_behavioral_detections**](ThreatsApi.md#get_behavioral_detections) | **GET** /api/v1/behavioral-detections | Get Behavioral Detections
[**get_threat_details**](ThreatsApi.md#get_threat_details) | **GET** /api/v1/threat-details | Get Threat Details


# **get_behavioral_detections**
> ThreatsGetBehavioralDetections200Response get_behavioral_detections(threat_id=threat_id, classification=classification, status=status, date_range=date_range, detection_date=detection_date, device_id=device_id, malware_family=malware_family, parent_process_name=parent_process_name, target_process_name=target_process_name, informational_tags=informational_tags, term=term, sort_by=sort_by, limit=limit, offset=offset)

Get Behavioral Detections

Get Behavioral Detections.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.threats_get_behavioral_detections200_response import ThreatsGetBehavioralDetections200Response
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
    api_instance = kandji.ThreatsApi(api_client)
    threat_id = '' # str | Filter by a specific threat ID (threat_id=Kandji_BD_0096). (optional)
    classification = '' # str | Filter by threat classification (classification=malicious). (optional)
    status = '' # str | Filter by threat status (threat_status=blocked) (optional)
    date_range = '' # str | Return all records within a specified number of days (Int) (optional)
    detection_date = '' # str | two query params detection_date_from and detection_date_to (optional)
    device_id = '' # str | Search for a specific device by the device id (uuid). (optional)
    malware_family = '' # str | Filter by malware family (malware_family=TrickBot). (optional)
    parent_process_name = '' # str | Filter by parent process (parent_process_name=bash). (optional)
    target_process_name = '' # str | Filter by target process (target_process_name=python). (optional)
    informational_tags = '' # str | Filter by tags (informational_tags=exploit,privilege_escalation). (optional)
    term = '' # str | Search term to filter threat results. Device name, file hash, image path (optional)
    sort_by = 'status' # str | <p>Detections can be sorted by any of the following keys. Prepending a dash (-) to the parameter value will reverse the order of the returned results. ?sort_by=-device_name will order the response by device_name in descending order.</p> <ul> <li>threat_id</li> <li>classification</li> <li>device_name</li> <li>parent_process_name</li> <li>target_process_name</li> <li>detection_date</li> <li>status</li> </ul> (optional)
    limit = '1000' # str | A hard upper <code>limit</code> is set at 1000 records returned per request. If more records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters.  Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Get Behavioral Detections
        api_response = api_instance.get_behavioral_detections(threat_id=threat_id, classification=classification, status=status, date_range=date_range, detection_date=detection_date, device_id=device_id, malware_family=malware_family, parent_process_name=parent_process_name, target_process_name=target_process_name, informational_tags=informational_tags, term=term, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of ThreatsApi->get_behavioral_detections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatsApi->get_behavioral_detections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_id** | **str**| Filter by a specific threat ID (threat_id&#x3D;Kandji_BD_0096). | [optional] 
 **classification** | **str**| Filter by threat classification (classification&#x3D;malicious). | [optional] 
 **status** | **str**| Filter by threat status (threat_status&#x3D;blocked) | [optional] 
 **date_range** | **str**| Return all records within a specified number of days (Int) | [optional] 
 **detection_date** | **str**| two query params detection_date_from and detection_date_to | [optional] 
 **device_id** | **str**| Search for a specific device by the device id (uuid). | [optional] 
 **malware_family** | **str**| Filter by malware family (malware_family&#x3D;TrickBot). | [optional] 
 **parent_process_name** | **str**| Filter by parent process (parent_process_name&#x3D;bash). | [optional] 
 **target_process_name** | **str**| Filter by target process (target_process_name&#x3D;python). | [optional] 
 **informational_tags** | **str**| Filter by tags (informational_tags&#x3D;exploit,privilege_escalation). | [optional] 
 **term** | **str**| Search term to filter threat results. Device name, file hash, image path | [optional] 
 **sort_by** | **str**| &lt;p&gt;Detections can be sorted by any of the following keys. Prepending a dash (-) to the parameter value will reverse the order of the returned results. ?sort_by&#x3D;-device_name will order the response by device_name in descending order.&lt;/p&gt; &lt;ul&gt; &lt;li&gt;threat_id&lt;/li&gt; &lt;li&gt;classification&lt;/li&gt; &lt;li&gt;device_name&lt;/li&gt; &lt;li&gt;parent_process_name&lt;/li&gt; &lt;li&gt;target_process_name&lt;/li&gt; &lt;li&gt;detection_date&lt;/li&gt; &lt;li&gt;status&lt;/li&gt; &lt;/ul&gt; | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 1000 records returned per request. If more records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters.  Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**ThreatsGetBehavioralDetections200Response**](ThreatsGetBehavioralDetections200Response.md)

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

# **get_threat_details**
> ThreatsGetThreatDetails200Response get_threat_details(classification=classification, date_range=date_range, device_id=device_id, status=status, sort_by=sort_by, term=term, limit=limit, offset=offset)

Get Threat Details

Get threat details.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.threats_get_threat_details200_response import ThreatsGetThreatDetails200Response
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
    api_instance = kandji.ThreatsApi(api_client)
    classification = 'malware' # str | Return all records matching a specified classification. The following classification options are available: <code>malware</code> and <code>pup</code>. Leave this parameter empty to return all classification types. (optional)
    date_range = '7' # str | Return all records within a specified number of days. Any positive number of days may be specified. Examples: <code>7</code>, <code>30</code>, <code>60</code>, <code>90</code>, <code>180</code>, or <code>365</code>. (optional)
    device_id = '15fcec08-xxxx-xxxx-xxxx-7c2f950910eb' # str |  (optional)
    status = 'quarantined' # str | Return all records matching a specified status. The following status options are available: <code>quarantined</code>, <code>not_quarantined</code>, or <code>released</code>. Leave this parameter empty to return all status types. (optional)
    sort_by = 'status' # str | <p>Results can be sorted with the following options: </p> <ul> <li>threat_name</li> <li>classification</li> <li>device_name</li> <li>process_name</li> <li>process_owner</li> <li>detection_date</li> <li>status</li> </ul> <p>Prepending a dash (-) to the parameter value will reverse the order of the returned results.</p> <p><code>?sort_by=-device_name</code> will order the response by device_name in descending order.</p> (optional)
    term = 'Chrome' # str | <p>Search term to filter threat results.</p> <p>The response will include anything matching the following fields: <code>device_name</code>, <code>file_hash</code>, and <code>file_path</code>.</p> <p>So if you search for <code>bad file</code>, the results will include anywhere <code>bad file</code> exists in the three fields above.</p> (optional)
    limit = '1000' # str | <p>A hard upper <code>limit</code> is set at 1000 records returned per request. If more records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. </p> <p>Additionally, parameter queries can be added to a request to limit the results.</p> (optional)
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
 **classification** | **str**| Return all records matching a specified classification. The following classification options are available: &lt;code&gt;malware&lt;/code&gt; and &lt;code&gt;pup&lt;/code&gt;. Leave this parameter empty to return all classification types. | [optional] 
 **date_range** | **str**| Return all records within a specified number of days. Any positive number of days may be specified. Examples: &lt;code&gt;7&lt;/code&gt;, &lt;code&gt;30&lt;/code&gt;, &lt;code&gt;60&lt;/code&gt;, &lt;code&gt;90&lt;/code&gt;, &lt;code&gt;180&lt;/code&gt;, or &lt;code&gt;365&lt;/code&gt;. | [optional] 
 **device_id** | **str**|  | [optional] 
 **status** | **str**| Return all records matching a specified status. The following status options are available: &lt;code&gt;quarantined&lt;/code&gt;, &lt;code&gt;not_quarantined&lt;/code&gt;, or &lt;code&gt;released&lt;/code&gt;. Leave this parameter empty to return all status types. | [optional] 
 **sort_by** | **str**| &lt;p&gt;Results can be sorted with the following options: &lt;/p&gt; &lt;ul&gt; &lt;li&gt;threat_name&lt;/li&gt; &lt;li&gt;classification&lt;/li&gt; &lt;li&gt;device_name&lt;/li&gt; &lt;li&gt;process_name&lt;/li&gt; &lt;li&gt;process_owner&lt;/li&gt; &lt;li&gt;detection_date&lt;/li&gt; &lt;li&gt;status&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Prepending a dash (-) to the parameter value will reverse the order of the returned results.&lt;/p&gt; &lt;p&gt;&lt;code&gt;?sort_by&#x3D;-device_name&lt;/code&gt; will order the response by device_name in descending order.&lt;/p&gt; | [optional] 
 **term** | **str**| &lt;p&gt;Search term to filter threat results.&lt;/p&gt; &lt;p&gt;The response will include anything matching the following fields: &lt;code&gt;device_name&lt;/code&gt;, &lt;code&gt;file_hash&lt;/code&gt;, and &lt;code&gt;file_path&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;So if you search for &lt;code&gt;bad file&lt;/code&gt;, the results will include anywhere &lt;code&gt;bad file&lt;/code&gt; exists in the three fields above.&lt;/p&gt; | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 1000 records returned per request. If more records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. &lt;/p&gt; &lt;p&gt;Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt; | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 

### Return type

[**ThreatsGetThreatDetails200Response**](ThreatsGetThreatDetails200Response.md)

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

