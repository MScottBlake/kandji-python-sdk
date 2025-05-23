# kandji.DeviceInformationApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_lost_mode**](DeviceInformationApi.md#cancel_lost_mode) | **DELETE** /api/v1/devices/{device_id}/details/lostmode | Cancel Lost Mode
[**get_device**](DeviceInformationApi.md#get_device) | **GET** /api/v1/devices/{device_id} | Get Device
[**get_device_activity**](DeviceInformationApi.md#get_device_activity) | **GET** /api/v1/devices/{device_id}/activity | Get Device Activity
[**get_device_apps**](DeviceInformationApi.md#get_device_apps) | **GET** /api/v1/devices/{device_id}/apps | Get Device Apps
[**get_device_details**](DeviceInformationApi.md#get_device_details) | **GET** /api/v1/devices/{device_id}/details | Get Device Details
[**get_device_library_items**](DeviceInformationApi.md#get_device_library_items) | **GET** /api/v1/devices/{device_id}/library-items | Get Device Library Items
[**get_device_lost_mode_details**](DeviceInformationApi.md#get_device_lost_mode_details) | **GET** /api/v1/devices/{device_id}/details/lostmode | Get Device Lost Mode details
[**get_device_parameters**](DeviceInformationApi.md#get_device_parameters) | **GET** /api/v1/devices/{device_id}/parameters | Get Device Parameters
[**get_device_status**](DeviceInformationApi.md#get_device_status) | **GET** /api/v1/devices/{device_id}/status | Get Device Status
[**list_devices**](DeviceInformationApi.md#list_devices) | **GET** /api/v1/devices | List Devices
[**update_device**](DeviceInformationApi.md#update_device) | **PATCH** /api/v1/devices/{device_id} | Update Device


# **cancel_lost_mode**
> cancel_lost_mode(device_id)

Cancel Lost Mode

This endpoint can be used to send a cancelation request if Lost Mode is in an error state for a given iOS or iPadOS device.

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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Cancel Lost Mode
        api_instance.cancel_lost_mode(device_id)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->cancel_lost_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> DeviceInformationGetDevice200Response get_device(device_id)

Get Device

This request returns the high-level information for a specified Device ID.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_information_get_device200_response import DeviceInformationGetDevice200Response
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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device
        api_response = api_instance.get_device(device_id)
        print("The response of DeviceInformationApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->get_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceInformationGetDevice200Response**](DeviceInformationGetDevice200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_activity**
> DeviceInformationGetDeviceActivity200Response get_device_activity(device_id, limit, offset=offset)

Get Device Activity

This request returns the device activity for a specified Device ID.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_information_get_device_activity200_response import DeviceInformationGetDeviceActivity200Response
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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = '300' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.
    offset = '0' # str | Specify the starting record to return (optional)

    try:
        # Get Device Activity
        api_response = api_instance.get_device_activity(device_id, limit, offset=offset)
        print("The response of DeviceInformationApi->get_device_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->get_device_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | 
 **offset** | **str**| Specify the starting record to return | [optional] 

### Return type

[**DeviceInformationGetDeviceActivity200Response**](DeviceInformationGetDeviceActivity200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_apps**
> DeviceInformationGetDeviceApps200Response get_device_apps(device_id)

Get Device Apps

<p>This request returns a list of all installed apps for a specified Device ID.</p>
<p>For iPhone and iPad, the preinstalled Apple apps are not reported.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_information_get_device_apps200_response import DeviceInformationGetDeviceApps200Response
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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Apps
        api_response = api_instance.get_device_apps(device_id)
        print("The response of DeviceInformationApi->get_device_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->get_device_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceInformationGetDeviceApps200Response**](DeviceInformationGetDeviceApps200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Link -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Total-Count -  <br>  * X-Total-Pages -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_details**
> DeviceInformationGetDeviceDetails200Response get_device_details(device_id)

Get Device Details

This request returns the device details for a specified Device ID.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_information_get_device_details200_response import DeviceInformationGetDeviceDetails200Response
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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Details
        api_response = api_instance.get_device_details(device_id)
        print("The response of DeviceInformationApi->get_device_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->get_device_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceInformationGetDeviceDetails200Response**](DeviceInformationGetDeviceDetails200Response.md)

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

# **get_device_library_items**
> DeviceInformationGetDeviceLibraryItems200Response get_device_library_items(device_id)

Get Device Library Items

<p>This request gets all library items and their statuses for a specified Device ID</p>
<h4 id=&quot;possible-library-item-status-values&quot;>Possible library item status values</h4>
<div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>
<thead>
<tr>
<th><strong>Value</strong></th>
<th><strong>Type</strong></th>
<th><strong>Additional Info</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>AVAILABLE</td>
<td>string</td>
<td>Library item available in Self Service</td>
</tr>
<tr>
<td>CACHED</td>
<td>string</td>
<td>Library item downloaded for install but not yet installed</td>
</tr>
<tr>
<td>CHANGE_PENDING</td>
<td>string</td>
<td>Recovery Password library item has changes that have not yet been applied</td>
</tr>
<tr>
<td>DOWNLOADING</td>
<td>string</td>
<td>Library item downloading</td>
</tr>
<tr>
<td>ERROR</td>
<td>string</td>
<td>Audit failure</td>
</tr>
<tr>
<td>EXCLUDED</td>
<td>string</td>
<td>Not in scope for assignment rule</td>
</tr>
<tr>
<td>INCOMPATIBLE</td>
<td>string</td>
<td>Not compatible with device or OS version</td>
</tr>
<tr>
<td>INSTALLING</td>
<td>string</td>
<td>Library item installing</td>
</tr>
<tr>
<td>PASS</td>
<td>string</td>
<td>Device meets requirements</td>
</tr>
<tr>
<td>PENDING</td>
<td>string</td>
<td>Waiting on device, not yet installed (All library items except for config profiles)</td>
</tr>
<tr>
<td>failed</td>
<td>string</td>
<td>Configuration profile failed to install</td>
</tr>
<tr>
<td>pending</td>
<td>string</td>
<td>Waiting on device, Configuration profile not yet installed</td>
</tr>
<tr>
<td>success</td>
<td>string</td>
<td>Configuration profile installed</td>
</tr>
</tbody>
</table>
</div>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_information_get_device_library_items200_response import DeviceInformationGetDeviceLibraryItems200Response
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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Library Items
        api_response = api_instance.get_device_library_items(device_id)
        print("The response of DeviceInformationApi->get_device_library_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->get_device_library_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceInformationGetDeviceLibraryItems200Response**](DeviceInformationGetDeviceLibraryItems200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_lost_mode_details**
> DeviceInformationGetDeviceLostModeDetails200Response get_device_lost_mode_details(device_id)

Get Device Lost Mode details

<p>This request returns the device lost mode details for a specified Device ID.</p>
<p><strong>Note</strong>: Lost Mode is is only available for iOS and iPadOS. For more information, please see this <a href=&quot;https://support.kandji.io/a/solutions/articles/72000573873&quot;>Kandji support artilcle</a>.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_information_get_device_lost_mode_details200_response import DeviceInformationGetDeviceLostModeDetails200Response
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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Lost Mode details
        api_response = api_instance.get_device_lost_mode_details(device_id)
        print("The response of DeviceInformationApi->get_device_lost_mode_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->get_device_lost_mode_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceInformationGetDeviceLostModeDetails200Response**](DeviceInformationGetDeviceLostModeDetails200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type -  <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_parameters**
> DeviceInformationGetDeviceParameters200Response get_device_parameters(device_id)

Get Device Parameters

<p>This request returns the parameters and their statuses for a specified Device ID</p>
<p>This endpoint is only applicable to macOS clients.</p>
<p>The parameters will be returned as a list of IDs. These IDs can be correlated with the parameter names available here: <a href=&quot;https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations&quot;>https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations</a></p>
<p><strong>Possible parameter status values</strong></p>
<div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>
<thead>
<tr>
<th><strong>Value</strong></th>
<th><strong>Type</strong></th>
<th><strong>Additional Info</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>ERROR</td>
<td>string</td>
<td>Audit failure</td>
</tr>
<tr>
<td>INCOMPATIBLE</td>
<td>string</td>
<td>Not compatible with device or OS version</td>
</tr>
<tr>
<td>PASS</td>
<td>string</td>
<td>Device meets requirements</td>
</tr>
<tr>
<td>PENDING</td>
<td>string</td>
<td>Waiting on device. Not yet run.</td>
</tr>
<tr>
<td>REMEDIATED</td>
<td>string</td>
<td>Parameter remediated</td>
</tr>
<tr>
<td>WARNING</td>
<td>string</td>
<td>Muted alert</td>
</tr>
</tbody>
</table>
</div>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_information_get_device_parameters200_response import DeviceInformationGetDeviceParameters200Response
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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Parameters
        api_response = api_instance.get_device_parameters(device_id)
        print("The response of DeviceInformationApi->get_device_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->get_device_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceInformationGetDeviceParameters200Response**](DeviceInformationGetDeviceParameters200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_status**
> DeviceInformationGetDeviceStatus200Response get_device_status(device_id)

Get Device Status

<p>This request returns the full status (parameters and library items) for a specified Device ID.</p>
<p>The parameters will be returned as a list of IDs. These IDs can be correlated with the parameter names available here: <a href=&quot;https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations&quot;>https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations</a></p>
<h4 id=&quot;possible-status-values&quot;>Possible status values</h4>
<p><strong>Library items</strong></p>
<div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>
<thead>
<tr>
<th><strong>Value</strong></th>
<th><strong>Type</strong></th>
<th><strong>Additional Info</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>AVAILABLE</td>
<td>string</td>
<td>Library item available in Self Service</td>
</tr>
<tr>
<td>ERROR</td>
<td>string</td>
<td>Audit failure</td>
</tr>
<tr>
<td>EXCLUDED</td>
<td>string</td>
<td>Not in scope for assignment rule</td>
</tr>
<tr>
<td>INCOMPATIBLE</td>
<td>string</td>
<td>Not compatible with device or OS version</td>
</tr>
<tr>
<td>PASS</td>
<td>string</td>
<td>Device meets requirements</td>
</tr>
<tr>
<td>PENDING</td>
<td>string</td>
<td>Waiting on device, not yet installed (All library items except for config profiles)</td>
</tr>
<tr>
<td>failed</td>
<td>string</td>
<td>Configuration profile failed to install</td>
</tr>
<tr>
<td>pending</td>
<td>string</td>
<td>Waiting on device, Configuration profile not yet installed</td>
</tr>
<tr>
<td>success</td>
<td>string</td>
<td>Configuration profile installed</td>
</tr>
</tbody>
</table>
</div><p><strong>Parameters</strong></p>
<div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>
<thead>
<tr>
<th><strong>Value</strong></th>
<th><strong>Type</strong></th>
<th><strong>Additional Info</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>ERROR</td>
<td>string</td>
<td>Audit failure</td>
</tr>
<tr>
<td>INCOMPATIBLE</td>
<td>string</td>
<td>Not compatible with device or OS version</td>
</tr>
<tr>
<td>PASS</td>
<td>string</td>
<td>Device meets requirements</td>
</tr>
<tr>
<td>PENDING</td>
<td>string</td>
<td>Waiting on device. Not yet run.</td>
</tr>
<tr>
<td>REMEDIATED</td>
<td>string</td>
<td>Parameter remediated</td>
</tr>
<tr>
<td>WARNING</td>
<td>string</td>
<td>Muted alert</td>
</tr>
</tbody>
</table>
</div>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_information_get_device_status200_response import DeviceInformationGetDeviceStatus200Response
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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Status
        api_response = api_instance.get_device_status(device_id)
        print("The response of DeviceInformationApi->get_device_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->get_device_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceInformationGetDeviceStatus200Response**](DeviceInformationGetDeviceStatus200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices**
> object list_devices(limit, asset_tag=asset_tag, blueprint_id=blueprint_id, device_id=device_id, device_name=device_name, filevault_enabled=filevault_enabled, mac_address=mac_address, model=model, ordering=ordering, os_version=os_version, platform=platform, serial_number=serial_number, tag_name=tag_name, tag_name_in=tag_name_in, tag_id=tag_id, tag_id_in=tag_id_in, user=user, user_email=user_email, user_email_exact=user_email_exact, user_id=user_id, user_name=user_name, offset=offset)

List Devices

<p>This request returns a list of devices in a Kandji tenant. Optionally. query parameters can be used to filter results.</p>
<p>There is a hard upper limit of 300 results per request. To return addtional results pagination must be used. Pagination examples can be found in the Kandji support <a href=&quot;https://github.com/kandji-inc/support/tree/main/api-tools/code-examples&quot;>GitHub</a>.</p>

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
    api_instance = kandji.DeviceInformationApi(api_client)
    limit = '300' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.
    asset_tag = '23245' # str |  (optional)
    blueprint_id = '91f97957-2353-4f86-a1ab-64d2b044a596' # str | Return results &quot;containing&quot; the specified blueprint id (optional)
    device_id = '2cfeb3ac-3b5d-423e-bcff-e2676a3a32da' # str |  (optional)
    device_name = 'Johnny\'s MacBook Pro' # str |  (optional)
    filevault_enabled = 'true' # str | <p>Query for devices that either have FileVault on (true) or off (false). This parameter only applies to macOS. </p> <p>An empty list <code>[]</code> will be returned if no devices are found with the given parameter value.</p> (optional)
    mac_address = '00:0c:29:05:43:b6' # str | Search for a specific device by MAC address (optional)
    model = 'MacBook Air (M1, 2020)' # str | Return model results &quot;containing&quot; the specified model string. (optional)
    ordering = 'device_id' # str | <p>The <code>ordering</code> parameter can be used to define how the device records are ordered in the response. Prepending a dash (-) to the parameter value will reverse the order of the returned results.</p> <p><code>?ordering=-serial_number</code> will order the response by serial_number in descending order.</p> <p><strong>Possible values</strong></p> <ul> <li><code>asset_tag</code></li> <li><code>blueprint_id</code></li> <li><code>device_id</code></li> <li><code>device_name</code></li> <li><code>last_check_in</code> - agent checkin</li> <li><code>model</code></li> <li><code>platform</code></li> <li><code>os_version</code></li> <li><code>serial_number</code></li> <li><code>user</code></li> </ul> <p>Additionally, multiple values can be combined in a comma separated list to further customize the ordering of the response.</p> <p><code>?ordering=serial_number,platform</code></p> (optional)
    os_version = '13.2.3' # str | Return all device records containing the specified OS version (optional)
    platform = 'iPad' # str | Return all records matching a specific platform. Possible values:<code>Mac</code>, <code>iPad</code>, <code>iPhone</code>, <code>AppleTV</code> (optional)
    serial_number = 'VMC5qeJ5pDkp' # str | Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned. (optional)
    tag_name = 'accuhive_01' # str | Return results for given tag name. Case sensitive. (optional)
    tag_name_in = 'accuhive_01, accuhive_02' # str | Return results for given tag names separate by commas. Case sensitive. (optional)
    tag_id = '' # str | Search for a tag by its ID. Case sensitive. (optional)
    tag_id_in = '' # str | Return results for given tag IDs separated by commas. Case sensitive. (optional)
    user = 'Art Vandelay' # str | Return results &quot;containing&quot; the user name (optional)
    user_email = 'someUser@Kandji.io' # str | Return results &quot;containing&quot; search on email address (optional)
    user_email_exact = 'someUser@Kandji.io' # str | Return results &quot;matching&quot; the specified email address (optional)
    user_id = '5344c996-8823-4b37-8d6e-8515fc7c3a0a' # str | &quot;exact&quot; match on kandji user ID (example: 5344c996-8823-4b37-8d6e-8515fc7c3a0a) (optional)
    user_name = 'Vandelay' # str | Return results &quot;containing&quot; the assigned user Display Name (optional)
    offset = '0' # str | Specify the starting record to return (optional)

    try:
        # List Devices
        api_response = api_instance.list_devices(limit, asset_tag=asset_tag, blueprint_id=blueprint_id, device_id=device_id, device_name=device_name, filevault_enabled=filevault_enabled, mac_address=mac_address, model=model, ordering=ordering, os_version=os_version, platform=platform, serial_number=serial_number, tag_name=tag_name, tag_name_in=tag_name_in, tag_id=tag_id, tag_id_in=tag_id_in, user=user, user_email=user_email, user_email_exact=user_email_exact, user_id=user_id, user_name=user_name, offset=offset)
        print("The response of DeviceInformationApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | 
 **asset_tag** | **str**|  | [optional] 
 **blueprint_id** | **str**| Return results &amp;quot;containing&amp;quot; the specified blueprint id | [optional] 
 **device_id** | **str**|  | [optional] 
 **device_name** | **str**|  | [optional] 
 **filevault_enabled** | **str**| &lt;p&gt;Query for devices that either have FileVault on (true) or off (false). This parameter only applies to macOS. &lt;/p&gt; &lt;p&gt;An empty list &lt;code&gt;[]&lt;/code&gt; will be returned if no devices are found with the given parameter value.&lt;/p&gt; | [optional] 
 **mac_address** | **str**| Search for a specific device by MAC address | [optional] 
 **model** | **str**| Return model results &amp;quot;containing&amp;quot; the specified model string. | [optional] 
 **ordering** | **str**| &lt;p&gt;The &lt;code&gt;ordering&lt;/code&gt; parameter can be used to define how the device records are ordered in the response. Prepending a dash (-) to the parameter value will reverse the order of the returned results.&lt;/p&gt; &lt;p&gt;&lt;code&gt;?ordering&#x3D;-serial_number&lt;/code&gt; will order the response by serial_number in descending order.&lt;/p&gt; &lt;p&gt;&lt;strong&gt;Possible values&lt;/strong&gt;&lt;/p&gt; &lt;ul&gt; &lt;li&gt;&lt;code&gt;asset_tag&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;blueprint_id&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;device_id&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;device_name&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;last_check_in&lt;/code&gt; - agent checkin&lt;/li&gt; &lt;li&gt;&lt;code&gt;model&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;platform&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;os_version&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;serial_number&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;user&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Additionally, multiple values can be combined in a comma separated list to further customize the ordering of the response.&lt;/p&gt; &lt;p&gt;&lt;code&gt;?ordering&#x3D;serial_number,platform&lt;/code&gt;&lt;/p&gt; | [optional] 
 **os_version** | **str**| Return all device records containing the specified OS version | [optional] 
 **platform** | **str**| Return all records matching a specific platform. Possible values:&lt;code&gt;Mac&lt;/code&gt;, &lt;code&gt;iPad&lt;/code&gt;, &lt;code&gt;iPhone&lt;/code&gt;, &lt;code&gt;AppleTV&lt;/code&gt; | [optional] 
 **serial_number** | **str**| Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned. | [optional] 
 **tag_name** | **str**| Return results for given tag name. Case sensitive. | [optional] 
 **tag_name_in** | **str**| Return results for given tag names separate by commas. Case sensitive. | [optional] 
 **tag_id** | **str**| Search for a tag by its ID. Case sensitive. | [optional] 
 **tag_id_in** | **str**| Return results for given tag IDs separated by commas. Case sensitive. | [optional] 
 **user** | **str**| Return results &amp;quot;containing&amp;quot; the user name | [optional] 
 **user_email** | **str**| Return results &amp;quot;containing&amp;quot; search on email address | [optional] 
 **user_email_exact** | **str**| Return results &amp;quot;matching&amp;quot; the specified email address | [optional] 
 **user_id** | **str**| &amp;quot;exact&amp;quot; match on kandji user ID (example: 5344c996-8823-4b37-8d6e-8515fc7c3a0a) | [optional] 
 **user_name** | **str**| Return results &amp;quot;containing&amp;quot; the assigned user Display Name | [optional] 
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

# **update_device**
> DeviceInformationUpdateDevice200Response update_device(device_id, body=body)

Update Device

<p>This request allows you to update device information, such as the assigned blueprint, user, Asset Tag, and Tags. It is not required to use all attributes in a given request. For example if you only want to update the assigned blueprint, you only need to pass the <code>blueprint_id</code> in the request payload.</p>
<p><strong>NOTE</strong>: With the introduction of a UUID value for user ID in the <a href=&quot;https://api-docs.kandji.io/#b107eb0a-b586-414f-bc4c-3d2b304cfd5f&quot;>Users API</a>, the Device PATCH endpoint will support both the depricated user ID integer value and the new user ID UUID value when updating the user assignment for a device. The ability to update user assignment via the integer ID value will be removed starting January 2025.</p>
<h3 id=&quot;request-parameters&quot;>Request Parameters</h3>
<p><code>device_id</code> (path parameter): The unique identifier of the device.</p>
<h3 id=&quot;additional-information&quot;>Additional information</h3>
<p>User ID can be found using the <code>list users</code> API</p>
<p>A Blueprint ID can be found using the <code>list blueprints</code> API or in the URL path while on a Blueprint overview page.</p>
<p>For example, for this URL <a href=&quot;https://subdomain.kandji.io/blueprints/6391086e-85a1-4820-813c-f9c75025fff4&quot;>https://subdomain.kandji.io/blueprints/6391086e-85a1-4820-813c-f9c75025fff4</a></p>
<p>The Blueprint ID would be <code>6391086e-85a1-4820-813c-f9c75025fff4</code></p>
<p>An example script that leverages this API can be found in the <a href=&quot;https://github.com/kandji-inc/support/tree/main/api-tools/update-device-record&quot;>Kandji Support GitHub</a></p>
<h4 id=&quot;clearing-the-device-asset-tag&quot;>Clearing the device asset tag</h4>
<p>To clear a device asset tag, set the <code>asset_tag</code> value to <code>null</code> in the JSON payload.</p>
<pre class=&quot;click-to-expand-wrapper is-snippet-wrapper&quot;><code class=&quot;language-json&quot;>{
    &quot;asset_tag&quot;: null
}

</code></pre>
<h4 id=&quot;clearing-the-assigned-user-attribute&quot;>Clearing the assigned user attribute</h4>
<p>To clear the assigned user for a given device, set the <code>user</code> value to <code>null</code> in the JSON payload.</p>
<pre class=&quot;click-to-expand-wrapper is-snippet-wrapper&quot;><code class=&quot;language-json&quot;>{
    &quot;user&quot;: null
}

</code></pre>
<h4 id=&quot;clearing-all-tags&quot;>Clearing all tags</h4>
<p>To clear the assigned tags for a given device, set the <code>tags</code> value to an empty list <code>[]</code> in the JSON payload.</p>
<pre class=&quot;click-to-expand-wrapper is-snippet-wrapper&quot;><code class=&quot;language-json&quot;>{
    &quot;tags&quot;: []
}

</code></pre>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_information_update_device200_response import DeviceInformationUpdateDevice200Response
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
    api_instance = kandji.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 
    body = {"asset_tag":"1040","blueprint_id":"be1a4d67-91d8-4d19-a927-c8be6e77b6b2","tags":["tag1","tag2","tag3","tag4","tag5"],"user":"5344c996-8823-4b37-8d6e-8515fc7c3a0a"} # str |  (optional)

    try:
        # Update Device
        api_response = api_instance.update_device(device_id, body=body)
        print("The response of DeviceInformationApi->update_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->update_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**DeviceInformationUpdateDevice200Response**](DeviceInformationUpdateDevice200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

