# kandji.PrismApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activation_lock**](PrismApi.md#activation_lock) | **GET** /api/v1/prism/activation_lock | Activation lock
[**application_firewall**](PrismApi.md#application_firewall) | **GET** /api/v1/prism/application_firewall | Application firewall
[**applications**](PrismApi.md#applications) | **GET** /api/v1/prism/apps | Applications
[**certificates**](PrismApi.md#certificates) | **GET** /api/v1/prism/certificates | Certificates
[**count**](PrismApi.md#count) | **GET** /api/v1/prism/count | Count
[**desktop_and_screensaver**](PrismApi.md#desktop_and_screensaver) | **GET** /api/v1/prism/desktop_and_screensaver | Desktop and Screensaver
[**device_information**](PrismApi.md#device_information) | **GET** /api/v1/prism/device_information | Device information
[**filevault**](PrismApi.md#filevault) | **GET** /api/v1/prism/filevault | FileVault
[**gatekeeper_and_xprotect**](PrismApi.md#gatekeeper_and_xprotect) | **GET** /api/v1/prism/gatekeeper_and_xprotect | Gatekeeper and XProtect
[**get_category_export**](PrismApi.md#get_category_export) | **GET** /api/v1/prism/export/{export_id} | Get category export
[**installed_profiles**](PrismApi.md#installed_profiles) | **GET** /api/v1/prism/installed_profiles | Installed profiles
[**kernel_extensions**](PrismApi.md#kernel_extensions) | **GET** /api/v1/prism/kernel_extensions | Kernel Extensions
[**launch_agents_and_daemons**](PrismApi.md#launch_agents_and_daemons) | **GET** /api/v1/prism/launch_agents_and_daemons | Launch Agents and Daemons
[**local_users**](PrismApi.md#local_users) | **GET** /api/v1/prism/local_users | Local users
[**request_category_export**](PrismApi.md#request_category_export) | **POST** /api/v1/prism/export | Request category export
[**startup_settings**](PrismApi.md#startup_settings) | **GET** /api/v1/prism/startup_settings | Startup settings
[**system_extensions**](PrismApi.md#system_extensions) | **GET** /api/v1/prism/system_extensions | System Extensions
[**transparency_database**](PrismApi.md#transparency_database) | **GET** /api/v1/prism/transparency_database | Transparency database


# **activation_lock**
> PrismActivationLock200Response activation_lock(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Activation lock

Get activation lock attributes for devices.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Activation lock
        api_response = api_instance.activation_lock(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->activation_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->activation_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * X-Served-By -  <br>  * X-Timer -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_firewall**
> PrismActivationLock200Response application_firewall(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Application firewall

Get Application Firewall details for macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Application firewall
        api_response = api_instance.application_firewall(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->application_firewall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->application_firewall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications**
> PrismApplications200Response applications(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Applications

Get the applications installed on macOS, iOS, iPadOS, and tvOS devices.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_applications200_response import PrismApplications200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '{\"name\":{\"not_in\":[\"Okta Verify\"]},\"device__name\":{\"not_in\":[\"testuser’s MacBook Air\"]}}' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Applications
        api_response = api_instance.applications(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismApplications200Response**](PrismApplications200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * X-Served-By -  <br>  * X-Timer -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificates**
> PrismActivationLock200Response certificates(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Certificates

Get certificate details.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Certificates
        api_response = api_instance.certificates(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * X-Served-By -  <br>  * X-Timer -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count**
> PrismCount200Response count(category)

Count

<p>Get the total record count for the specified Prism category.</p>
<p>If a category contains spaces substitute the spaces for underscores (&quot;_&quot;) when using the API query.</p>
<p>Example: <code>Device information</code> becomes <code>device_information</code>.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_count200_response import PrismCount200Response
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
    api_instance = kandji.PrismApi(api_client)
    category = 'apps' # str | <p>Return the count of records for the specified category.  If a category contains spaces substitute the spaces for underscores (&quot;_&quot;) when using the API query.</p> <p>Examples: apps device_information kernel_extensions system_extensions</p>

    try:
        # Count
        api_response = api_instance.count(category)
        print("The response of PrismApi->count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| &lt;p&gt;Return the count of records for the specified category.  If a category contains spaces substitute the spaces for underscores (&amp;quot;_&amp;quot;) when using the API query.&lt;/p&gt; &lt;p&gt;Examples: apps device_information kernel_extensions system_extensions&lt;/p&gt; | 

### Return type

[**PrismCount200Response**](PrismCount200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **desktop_and_screensaver**
> PrismActivationLock200Response desktop_and_screensaver(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Desktop and Screensaver

Get Desktop and Screensaver details for macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Desktop and Screensaver
        api_response = api_instance.desktop_and_screensaver(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->desktop_and_screensaver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->desktop_and_screensaver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_information**
> PrismDeviceInformation200Response device_information(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset, body=body)

Device information

Get attributes about devices.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_device_information200_response import PrismDeviceInformation200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = '14afabf2-7599-47af-a942-bf7f0b8fedf8' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '{\"device__name\":{\"in\":[\"testusers\'s MacBook Air\"]},\"updated_at\":{\"gte\":\"2023-09-03T04:00:00.000Z\",\"lte\":\"2023-09-04T04:00:00.000Z\"}}' # str | <p>JSON schema object containing one or more key value pairs.</p> <p>Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p> (optional)
    sort_by = 'serial_number' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return (optional)
    body = {} # str |  (optional)

    try:
        # Device information
        api_response = api_instance.device_information(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset, body=body)
        print("The response of PrismApi->device_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->device_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs.&lt;/p&gt; &lt;p&gt;Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt; | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 
 **body** | **str**|  | [optional] 

### Return type

[**PrismDeviceInformation200Response**](PrismDeviceInformation200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filevault**
> PrismDeviceInformation200Response filevault(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

FileVault

Get FileVault information for macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_device_information200_response import PrismDeviceInformation200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return (optional)

    try:
        # FileVault
        api_response = api_instance.filevault(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->filevault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->filevault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 

### Return type

[**PrismDeviceInformation200Response**](PrismDeviceInformation200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gatekeeper_and_xprotect**
> PrismActivationLock200Response gatekeeper_and_xprotect(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Gatekeeper and XProtect

Get Gatekeeper and XProtect attributes for macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac' # str | Results are limited to Mac only as Gatekeeper and XProtect are not applicable for other platfroms. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return (optional)

    try:
        # Gatekeeper and XProtect
        api_response = api_instance.gatekeeper_and_xprotect(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->gatekeeper_and_xprotect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->gatekeeper_and_xprotect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Results are limited to Mac only as Gatekeeper and XProtect are not applicable for other platfroms. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_export**
> PrismGetCategoryExport200Response get_category_export(export_id)

Get category export

<p>Get an export request's status. To download the export, use the <code>signed_url</code>. This will download a CSV file containing the exported category information.</p>
<h3 id=&quot;request-parameters&quot;>Request Parameters</h3>
<p>export_id (path parameter): The unique identifier of the the export job.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_get_category_export200_response import PrismGetCategoryExport200Response
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
    api_instance = kandji.PrismApi(api_client)
    export_id = 'export_id_example' # str | 

    try:
        # Get category export
        api_response = api_instance.get_category_export(export_id)
        print("The response of PrismApi->get_category_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->get_category_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**|  | 

### Return type

[**PrismGetCategoryExport200Response**](PrismGetCategoryExport200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installed_profiles**
> PrismActivationLock200Response installed_profiles(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Installed profiles

Get Installed Profiles attributes for macOS, iOS, iPadOS, and tvOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Installed profiles
        api_response = api_instance.installed_profiles(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->installed_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->installed_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kernel_extensions**
> PrismActivationLock200Response kernel_extensions(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Kernel Extensions

Get Kernel Extension attributes for macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | SON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Kernel Extensions
        api_response = api_instance.kernel_extensions(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->kernel_extensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->kernel_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| SON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_agents_and_daemons**
> PrismActivationLock200Response launch_agents_and_daemons(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Launch Agents and Daemons

Get Launch Agents and Daemons installed on macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Launch Agents and Daemons
        api_response = api_instance.launch_agents_and_daemons(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->launch_agents_and_daemons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->launch_agents_and_daemons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_users**
> PrismLocalUsers200Response local_users(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Local users

Get Local Users detials for macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_local_users200_response import PrismLocalUsers200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Local users
        api_response = api_instance.local_users(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->local_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->local_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismLocalUsers200Response**](PrismLocalUsers200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_category_export**
> PrismRequestCategoryExport200Response request_category_export(body=body)

Request category export

<p>Request export of a category. The <code>id</code> key is used when checking the export status using the <em>Request category export</em> endpoint.</p>
<p><strong>Request Body Parameters: application/json</strong></p>
<div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>
<thead>
<tr>
<th>Key</th>
<th>Type</th>
<th>Possible value(s)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>blueprint_ids</code></td>
<td><code>array</code></td>
<td><code>[&quot;string&quot;, &quot;string&quot;, &quot;string&quot;]</code></td>
<td>List of one or more comma separate blueprint IDs.</td>
</tr>
<tr>
<td><code>category</code></td>
<td><code>string</code></td>
<td><code>apps</code> ,  <br /><code>activation_lock</code> ,  <br /><code>desktop_and_screensaver</code> ,  <br /><code>device_information</code> ,  <br /><code>gatekeeper_and_xprotect</code> ,  <br /><code>installed_profiles</code> ,  <br /><code>kernel_extensions</code> ,  <br /><code>local_users</code> ,  <br /><code>launch_agents_and_daemons</code> ,  <br /><code>system_extensions</code> ,  <br /><code>startup_settings</code> ,  <br /><code>transparency_database</code></td>
<td>Only one category per export reqest.</td>
</tr>
<tr>
<td><code>device_families</code></td>
<td><code>array</code></td>
<td><code>[&quot;Mac&quot;, &quot;iPhone&quot;, &quot;iPad&quot;, &quot;tvOS&quot;]</code></td>
<td>List of one or more comma separted string values for device families.</td>
</tr>
<tr>
<td><code>filter</code></td>
<td><code>object</code></td>
<td><code>{&quot;apple_silicon&quot;: {&quot;eq&quot;: true}, &quot;device__name&quot;: {&quot;like&quot;: [&quot;this&quot;, &quot;or_this&quot;]}}</code></td>
<td>JSON schema object containing one or more key value pairs.  <br />  <br /><strong>Note</strong>: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</td>
</tr>
<tr>
<td><code>sort_by</code></td>
<td><code>string</code></td>
<td></td>
<td>Sort results by the name of a given response body key in either ascending (default behavior) or descending(`-`) order.</td>
</tr>
</tbody>
</table>
</div>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_request_category_export200_response import PrismRequestCategoryExport200Response
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
    api_instance = kandji.PrismApi(api_client)
    body = {"blueprint_ids":["string","string","string"],"category":"device_information","device_families":["Mac"],"filter":{},"sort_by":"device__nam"} # str |  (optional)

    try:
        # Request category export
        api_response = api_instance.request_category_export(body=body)
        print("The response of PrismApi->request_category_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->request_category_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

[**PrismRequestCategoryExport200Response**](PrismRequestCategoryExport200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |
**400** | Bad Request |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **startup_settings**
> PrismActivationLock200Response startup_settings(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Startup settings

Get Startup settings for macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return (optional)

    try:
        # Startup settings
        api_response = api_instance.startup_settings(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->startup_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->startup_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_extensions**
> PrismActivationLock200Response system_extensions(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

System Extensions

Get System Extension attributes for macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # System Extensions
        api_response = api_instance.system_extensions(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->system_extensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->system_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transparency_database**
> PrismActivationLock200Response transparency_database(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Transparency database

Get Transparency Database (TCC) attributes for macOS.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
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
    api_instance = kandji.PrismApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | Filter results by one or more blueprint IDs separated by commas. (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | Filter results by one or more device families separate by commas. (optional)
    filter = '' # str | JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. (optional)
    sort_by = '' # str | Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order. (optional)
    limit = '' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return. (optional)

    try:
        # Transparency database
        api_response = api_instance.transparency_database(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of PrismApi->transparency_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrismApi->transparency_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| Filter results by one or more blueprint IDs separated by commas. | [optional] 
 **device_families** | **str**| Filter results by one or more device families separate by commas. | [optional] 
 **filter** | **str**| JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc. | [optional] 
 **sort_by** | **str**| Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order. | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return. | [optional] 

### Return type

[**PrismActivationLock200Response**](PrismActivationLock200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

