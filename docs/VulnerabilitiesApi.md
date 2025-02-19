# kandji.VulnerabilitiesApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vulnerability_description**](VulnerabilitiesApi.md#get_vulnerability_description) | **GET** /api/v1/vulnerability-management/vulnerabilities/{cve_id} | Get Vulnerability Description
[**list_affected_applications**](VulnerabilitiesApi.md#list_affected_applications) | **GET** /api/v1/vulnerability-management/vulnerabilities/{cve_id}/applications | List Affected Applications
[**list_affected_devices**](VulnerabilitiesApi.md#list_affected_devices) | **GET** /api/v1/vulnerability-management/vulnerabilities/{cve_id}/devices | List Affected Devices
[**list_detections**](VulnerabilitiesApi.md#list_detections) | **GET** /api/v1/vulnerability-management/detections | List Detections
[**list_vulnerabilities**](VulnerabilitiesApi.md#list_vulnerabilities) | **GET** /api/v1/vulnerability-management/vulnerabilities | List Vulnerabilities


# **get_vulnerability_description**
> InlineObject35 get_vulnerability_description(cve_id)

Get Vulnerability Description

This endpoint makes a request to retrieve information about a cve and summary information about detections for a tenants fleet.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.inline_object35 import InlineObject35
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

[**InlineObject35**](InlineObject35.md)

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

# **list_affected_applications**
> object list_affected_applications(cve_id, page=page, size=size, sort_by=sort_by, filter=filter)

List Affected Applications

This endpoint makes a request to retrieve a list of applications impacted by a specified <code>cve_id</code> vulnerability for a tenants fleet.

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
    cve_id = 'cve_id_example' # str | 
    page = '' # str | The page number of the response. (optional)
    size = '50' # str | A hard upper limit is set at 50  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. (optional)
    sort_by = 'cve_id' # str | Field to sort by. Example: sort_by=app_name. (optional)
    filter = 'device_serial_number' # str | Filterable columns: blueprint_id updated_at (optional)

    try:
        # List Affected Applications
        api_response = api_instance.list_affected_applications(cve_id, page=page, size=size, sort_by=sort_by, filter=filter)
        print("The response of VulnerabilitiesApi->list_affected_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnerabilitiesApi->list_affected_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**|  | 
 **page** | **str**| The page number of the response. | [optional] 
 **size** | **str**| A hard upper limit is set at 50  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. | [optional] 
 **sort_by** | **str**| Field to sort by. Example: sort_by&#x3D;app_name. | [optional] 
 **filter** | **str**| Filterable columns: blueprint_id updated_at | [optional] 

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

# **list_affected_devices**
> object list_affected_devices(cve_id, page=page, size=size, sort_by=sort_by, filter=filter)

List Affected Devices

This endpoint makes a request to retrieve a list of devices impacted by a specified <code>cve_id</code> vulnerability for a tenants fleet.

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
    cve_id = 'cve_id_example' # str | 
    page = '' # str | The page number of the response. (optional)
    size = '50' # str | A hard upper limit is set at 50  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. (optional)
    sort_by = 'cve_id' # str | Field to sort by. Example: sort_by=app_name. (optional)
    filter = 'device_serial_number' # str | Filterable columns: blueprint_id updated_at (optional)

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
 **filter** | **str**| Filterable columns: blueprint_id updated_at | [optional] 

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

# **list_detections**
> InlineObject33 list_detections(after=after, limit=limit, filter=filter)

List Detections

This endpoint makes a request to retrieve a list of all vulnerability detections across the device fleet.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.inline_object33 import InlineObject33
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
    limit = '300' # str | A hard upper <code>limit</code> is set at 300  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. (optional)
    filter = 'device_serial_number' # str | Can filter on any key attribute within the response. (optional)

    try:
        # List Detections
        api_response = api_instance.list_detections(after=after, limit=limit, filter=filter)
        print("The response of VulnerabilitiesApi->list_detections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnerabilitiesApi->list_detections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Cursor token. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300  records returned per request. If more records are expected, pagination should be used using the URL value returned in the next attribute. Additionally, filters can be added to a request to limit the results. | [optional] 
 **filter** | **str**| Can filter on any key attribute within the response. | [optional] 

### Return type

[**InlineObject33**](InlineObject33.md)

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
> InlineObject34 list_vulnerabilities(page=page, size=size, sort_by=sort_by, filter=filter)

List Vulnerabilities

This endpoint makes a request to retrieve a list of all vulnerabilities grouped by cve.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.inline_object34 import InlineObject34
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
    sort_by = 'cve_id' # str | Field to sort by. Example: sort_by=cve_id. (optional)
    filter = 'device_serial_number' # str | <p>Filterable columns:</p> <p>cve_id app_name severity first_detection_date latest_detection_date</p> (optional)

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
 **sort_by** | **str**| Field to sort by. Example: sort_by&#x3D;cve_id. | [optional] 
 **filter** | **str**| &lt;p&gt;Filterable columns:&lt;/p&gt; &lt;p&gt;cve_id app_name severity first_detection_date latest_detection_date&lt;/p&gt; | [optional] 

### Return type

[**InlineObject34**](InlineObject34.md)

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

