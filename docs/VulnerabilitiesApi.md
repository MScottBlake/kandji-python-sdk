# kandji.VulnerabilitiesApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vulnerability_description**](VulnerabilitiesApi.md#get_vulnerability_description) | **GET** /api/v1/vulnerability-management/vulnerabilities/{cve_id} | Get Vulnerability Description
[**list_affected_apps**](VulnerabilitiesApi.md#list_affected_apps) | **GET** /api/v1/vulnerability-management/vulnerabilities/{cve_id}/applications | List Affected Apps
[**list_affected_devices**](VulnerabilitiesApi.md#list_affected_devices) | **GET** /api/v1/vulnerability-management/vulnerabilities/{cve_id}/devices | List Affected Devices
[**list_detections**](VulnerabilitiesApi.md#list_detections) | **GET** /api/v1/vulnerability-management/detections | List Detections
[**list_vulnerabilities**](VulnerabilitiesApi.md#list_vulnerabilities) | **GET** /api/v1/vulnerability-management/vulnerabilities | List Vulnerabilities


# **get_vulnerability_description**
> VulnerabilitiesGetVulnerabilityDescription200Response get_vulnerability_description(cve_id)

Get Vulnerability Description

Retrieve information about a CVE.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.vulnerabilities_get_vulnerability_description200_response import VulnerabilitiesGetVulnerabilityDescription200Response
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
    api_instance = kandji.VulnerabilitiesApi(api_client)
    cve_id = 'cve_id_example' # str | 

    try:
        # Get Vulnerability Description
        api_response = api_instance.get_vulnerability_description(cve_id)
        print("The response of VulnerabilitiesApi->get_vulnerability_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnerabilitiesApi->get_vulnerability_description: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**|  | 

### Return type

[**VulnerabilitiesGetVulnerabilityDescription200Response**](VulnerabilitiesGetVulnerabilityDescription200Response.md)

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

# **list_affected_apps**
> VulnerabilitiesListAffectedApps200Response list_affected_apps(cve_id, page=page, size=size, sort_by=sort_by, filter=filter)

List Affected Apps

This endpoint makes a request to retrieve a list of applications impacted by a specified <code>cve_id</code> vulnerability for a tenants fleet.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.vulnerabilities_list_affected_apps200_response import VulnerabilitiesListAffectedApps200Response
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
    api_instance = kandji.VulnerabilitiesApi(api_client)
    cve_id = 'cve_id_example' # str | 
    page = '' # str | The page number of the response. (optional)
    size = '50' # str | A hard upper limit is set at 50  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. (optional)
    sort_by = 'cve_id' # str | Field to sort by. Example: sort_by=app_name. (optional)
    filter = '{\"created_at\":{\"gte\":\"2025-05-23T17:11:31.816587Z\"}}' # str | <p>Filterable columns:</p> <ul> <li>blueprint_id</li> <li>created_at</li> </ul> (optional)

    try:
        # List Affected Apps
        api_response = api_instance.list_affected_apps(cve_id, page=page, size=size, sort_by=sort_by, filter=filter)
        print("The response of VulnerabilitiesApi->list_affected_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnerabilitiesApi->list_affected_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**|  | 
 **page** | **str**| The page number of the response. | [optional] 
 **size** | **str**| A hard upper limit is set at 50  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. | [optional] 
 **sort_by** | **str**| Field to sort by. Example: sort_by&#x3D;app_name. | [optional] 
 **filter** | **str**| &lt;p&gt;Filterable columns:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;blueprint_id&lt;/li&gt; &lt;li&gt;created_at&lt;/li&gt; &lt;/ul&gt; | [optional] 

### Return type

[**VulnerabilitiesListAffectedApps200Response**](VulnerabilitiesListAffectedApps200Response.md)

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

# **list_affected_devices**
> VulnerabilitiesListAffectedApps200Response list_affected_devices(cve_id, page=page, size=size, sort_by=sort_by, filter=filter)

List Affected Devices

Retrieve a list of devices impacted by a specified <code>cve_id</code> vulnerability for a tenants fleet.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.vulnerabilities_list_affected_apps200_response import VulnerabilitiesListAffectedApps200Response
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
    api_instance = kandji.VulnerabilitiesApi(api_client)
    cve_id = 'cve_id_example' # str | 
    page = '' # str | The page number of the response. (optional)
    size = '50' # str | A hard upper limit is set at 50  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. (optional)
    sort_by = 'cve_id' # str | Field to sort by. Example: sort_by=app_name. (optional)
    filter = '{\"detection_datetime\":{\"gte\":\"2025-05-23T17:11:31.816587Z\"}}' # str | <p>Filterable columns:</p> <ul> <li>blueprint_id</li> <li>detection_datetime</li> </ul> (optional)

    try:
        # List Affected Devices
        api_response = api_instance.list_affected_devices(cve_id, page=page, size=size, sort_by=sort_by, filter=filter)
        print("The response of VulnerabilitiesApi->list_affected_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnerabilitiesApi->list_affected_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**|  | 
 **page** | **str**| The page number of the response. | [optional] 
 **size** | **str**| A hard upper limit is set at 50  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. | [optional] 
 **sort_by** | **str**| Field to sort by. Example: sort_by&#x3D;app_name. | [optional] 
 **filter** | **str**| &lt;p&gt;Filterable columns:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;blueprint_id&lt;/li&gt; &lt;li&gt;detection_datetime&lt;/li&gt; &lt;/ul&gt; | [optional] 

### Return type

[**VulnerabilitiesListAffectedApps200Response**](VulnerabilitiesListAffectedApps200Response.md)

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

# **list_detections**
> VulnerabilitiesListDetections200Response list_detections(after=after, size=size, filter=filter)

List Detections

Retrieve a list of all vulnerability detections across the device fleet.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.vulnerabilities_list_detections200_response import VulnerabilitiesListDetections200Response
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
    api_instance = kandji.VulnerabilitiesApi(api_client)
    after = '' # str | Cursor token. (optional)
    size = '300' # str | A hard upper <code>limit</code> is set at 300  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. (optional)
    filter = '{\"cve_id\":{\"in\":[\"CVE-2024-24795\"]}}' # str | <p>Filter on any key attribute within the response.</p> <ul> <li>device_id</li> <li>device_name</li> <li>device_serial_number</li> <li>device_model</li> <li>device_os_version</li> <li>blueprint_id</li> <li>blueprint_name</li> <li>name</li> <li>path</li> <li>version</li> <li>bundle_id</li> <li>cve_id</li> <li>cve_description</li> <li>cve_link</li> <li>cvss_score</li> <li>cvss_severity</li> <li>detection_datetime</li> <li>cve_published_at</li> <li>cve_modified_at</li> </ul> (optional)

    try:
        # List Detections
        api_response = api_instance.list_detections(after=after, size=size, filter=filter)
        print("The response of VulnerabilitiesApi->list_detections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnerabilitiesApi->list_detections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Cursor token. | [optional] 
 **size** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. | [optional] 
 **filter** | **str**| &lt;p&gt;Filter on any key attribute within the response.&lt;/p&gt; &lt;ul&gt; &lt;li&gt;device_id&lt;/li&gt; &lt;li&gt;device_name&lt;/li&gt; &lt;li&gt;device_serial_number&lt;/li&gt; &lt;li&gt;device_model&lt;/li&gt; &lt;li&gt;device_os_version&lt;/li&gt; &lt;li&gt;blueprint_id&lt;/li&gt; &lt;li&gt;blueprint_name&lt;/li&gt; &lt;li&gt;name&lt;/li&gt; &lt;li&gt;path&lt;/li&gt; &lt;li&gt;version&lt;/li&gt; &lt;li&gt;bundle_id&lt;/li&gt; &lt;li&gt;cve_id&lt;/li&gt; &lt;li&gt;cve_description&lt;/li&gt; &lt;li&gt;cve_link&lt;/li&gt; &lt;li&gt;cvss_score&lt;/li&gt; &lt;li&gt;cvss_severity&lt;/li&gt; &lt;li&gt;detection_datetime&lt;/li&gt; &lt;li&gt;cve_published_at&lt;/li&gt; &lt;li&gt;cve_modified_at&lt;/li&gt; &lt;/ul&gt; | [optional] 

### Return type

[**VulnerabilitiesListDetections200Response**](VulnerabilitiesListDetections200Response.md)

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

# **list_vulnerabilities**
> object list_vulnerabilities(page=page, size=size, sort_by=sort_by, filter=filter)

List Vulnerabilities

Retrieve a list of all vulnerabilities grouped by cve.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
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
    api_instance = kandji.VulnerabilitiesApi(api_client)
    page = '' # str | The page number of the response. (optional)
    size = '50' # str | A hard upper limit is set at 50  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. (optional)
    sort_by = 'cve_id' # str | <p>Field to sort by.</p> <ul> <li>cve_id</li> <li>software (the name of the software)</li> <li>cvss_severity</li> <li>first_detection_date</li> <li>latest_detection_date</li> </ul> (optional)
    filter = '{\"cve_id\":{\"in\":[\"CVE-2024-24795\"]}}' # str | <p>Filterable columns</p> <ul> <li>cve_id</li> <li>app_name</li> <li>severity</li> <li>first_detection_date</li> <li>latest_detection_date</li> </ul> (optional)

    try:
        # List Vulnerabilities
        api_response = api_instance.list_vulnerabilities(page=page, size=size, sort_by=sort_by, filter=filter)
        print("The response of VulnerabilitiesApi->list_vulnerabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnerabilitiesApi->list_vulnerabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The page number of the response. | [optional] 
 **size** | **str**| A hard upper limit is set at 50  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. | [optional] 
 **sort_by** | **str**| &lt;p&gt;Field to sort by.&lt;/p&gt; &lt;ul&gt; &lt;li&gt;cve_id&lt;/li&gt; &lt;li&gt;software (the name of the software)&lt;/li&gt; &lt;li&gt;cvss_severity&lt;/li&gt; &lt;li&gt;first_detection_date&lt;/li&gt; &lt;li&gt;latest_detection_date&lt;/li&gt; &lt;/ul&gt; | [optional] 
 **filter** | **str**| &lt;p&gt;Filterable columns&lt;/p&gt; &lt;ul&gt; &lt;li&gt;cve_id&lt;/li&gt; &lt;li&gt;app_name&lt;/li&gt; &lt;li&gt;severity&lt;/li&gt; &lt;li&gt;first_detection_date&lt;/li&gt; &lt;li&gt;latest_detection_date&lt;/li&gt; &lt;/ul&gt; | [optional] 

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

