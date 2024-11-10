# kandji_python_sdk.DeviceInformationApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_lost_mode**](DeviceInformationApi.md#cancel_lost_mode) | **DELETE** /api/v1/devices/{device_id}/details/lostmode | Cancel Lost Mode
[**get_device_activity**](DeviceInformationApi.md#get_device_activity) | **GET** /api/v1/devices/{device_id}/activity | Get Device Activity
[**get_device_apps**](DeviceInformationApi.md#get_device_apps) | **GET** /api/v1/devices/{device_id}/apps | Get Device Apps
[**get_device_details**](DeviceInformationApi.md#get_device_details) | **GET** /api/v1/devices/{device_id}/details | Get Device Details
[**get_device_library_items**](DeviceInformationApi.md#get_device_library_items) | **GET** /api/v1/devices/{device_id}/library-items | Get Device Library Items
[**get_device_lost_mode_details**](DeviceInformationApi.md#get_device_lost_mode_details) | **GET** /api/v1/devices/{device_id}/details/lostmode | Get Device Lost Mode details
[**get_device_parameters**](DeviceInformationApi.md#get_device_parameters) | **GET** /api/v1/devices/{device_id}/parameters | Get Device Parameters
[**get_device_status**](DeviceInformationApi.md#get_device_status) | **GET** /api/v1/devices/{device_id}/status | Get Device Status
[**list_devices**](DeviceInformationApi.md#list_devices) | **GET** /api/v1/devices | List Devices


# **cancel_lost_mode**
> cancel_lost_mode(device_id)

Cancel Lost Mode

This endpoint can be used to send a cancelation request if Lost Mode is in an error state for a given iOS or iPadOS device.

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
    api_instance = kandji_python_sdk.DeviceInformationApi(api_client)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_activity**
> object get_device_activity(device_id, limit, offset=offset)

Get Device Activity

This request returns the device activity for a specified Device ID.

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
    api_instance = kandji_python_sdk.DeviceInformationApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = '300' # str | A hard upper \\`limit\\` is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\`limit\\` and \\`offset\\` parameters. Additionally, parameter queries can be added to a request to limit the results.
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
 **limit** | **str**| A hard upper \\&#x60;limit\\&#x60; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\&#x60;limit\\&#x60; and \\&#x60;offset\\&#x60; parameters. Additionally, parameter queries can be added to a request to limit the results. | 
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_apps**
> object get_device_apps(device_id)

Get Device Apps

This request returns a list of all installed apps for a specified Device ID.   For iPhone and iPad, the preinstalled Apple apps are not reported.

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
    api_instance = kandji_python_sdk.DeviceInformationApi(api_client)
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

**object**

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
> object get_device_details(device_id)

Get Device Details

This request returns the device details for a specified Device ID.

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
    api_instance = kandji_python_sdk.DeviceInformationApi(api_client)
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

# **get_device_library_items**
> object get_device_library_items(device_id)

Get Device Library Items

This request gets all library items and their statuses for a specified Device ID   #### Possible library item status values     | **Value** | **Type** | **Additional Info** | | --- | --- | --- | | AVAILABLE | string | Library item available in Self Service | | CACHED | string | Library item downloaded for install but not yet installed | | CHANGE\\_PENDING | string | Recovery Password library item has changes that have not yet been applied | | DOWNLOADING | string | Library item downloading | | ERROR | string | Audit failure | | EXCLUDED | string | Not in scope for assignment rule |  | INCOMPATIBLE | string | Not compatible with device or OS version | | INSTALLING | string | Library item installing | | PASS | string | Device meets requirements | | PENDING | string | Waiting on device, not yet installed (All library items except for config profiles) | | failed | string | Configuration profile failed to install | | pending | string | Waiting on device, Configuration profile not yet installed | | success | string | Configuration profile installed |

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
    api_instance = kandji_python_sdk.DeviceInformationApi(api_client)
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

**object**

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
> object get_device_lost_mode_details(device_id)

Get Device Lost Mode details

This request returns the device lost mode details for a specified Device ID.   **Note**: Lost Mode is is only available for iOS and iPadOS. For more information, please see this [Kandji support artilcle](https://support.kandji.io/a/solutions/articles/72000573873).

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
    api_instance = kandji_python_sdk.DeviceInformationApi(api_client)
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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_parameters**
> object get_device_parameters(device_id)

Get Device Parameters

This request returns the parameters and their statuses for a specified Device ID   This endpoint is only applicable to macOS clients.   The parameters will be returned as a list of IDs. These IDs can be correlated with the parameter names available here: [https://github.com/kandji\\-inc/support/wiki/Devices\\ -API\\-\\-\\-Parameter\\-Correlations](https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations)    **Possible parameter status values**     | **Value** | **Type** | **Additional Info** | | --- | --- | --- | | ERROR | string | Audit failure | | INCOMPATIBLE | string | Not compatible with device or OS version |  | PASS | string | Device meets requirements | | PENDING | string | Waiting on device. Not yet run. | | REMEDIATED | string | Parameter remediated |  | WARNING | string | Muted alert |

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
    api_instance = kandji_python_sdk.DeviceInformationApi(api_client)
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

**object**

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
> object get_device_status(device_id)

Get Device Status

This request returns the full status (parameters and library items) for a specified Device ID.   The parameters will be returned as a list of IDs. These IDs can be correlated with the parameter names available here: [https://github.com/kandji\\-inc/support/wiki/Devices\\-API\\-\\-\\-Parameter\\ -Correlations](https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations)    #### Possible status values   **Library items**     | **Value** | **Type** | **Additional Info** | | --- | --- | --- | | AVAILABLE | string | Library item available in Self Service | | ERROR | string | Audit failure | | EXCLUDED | string | Not in scope for assignment rule | | INCOMPATIBLE | string | Not compatible with device or OS version | | PASS | string | Device meets requirements | | PENDING | string | Waiting on device, not yet installed (All library items except for config profiles) | | failed | string | Configuration profile failed to install | | pending | string | Waiting on device, Configuration profile not yet installed | | success | string | Configuration profile installed |   **Parameters**     | **Value** | **Type** | **Additional Info** | | --- | --- | --- | | ERROR | string | Audit failure | | INCOMPATIBLE | string | Not compatible with device or OS version | | PASS | string | Device meets requirements | | PENDING | string | Waiting on device. Not yet run. | | REMEDIATED | string | Parameter remediated | | WARNING | string | Muted alert |

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
    api_instance = kandji_python_sdk.DeviceInformationApi(api_client)
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

**object**

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
> object list_devices(limit, asset_tag=asset_tag, blueprint_id=blueprint_id, device_id=device_id, device_name=device_name, filevault_enabled=filevault_enabled, mac_address=mac_address, model=model, ordering=ordering, os_version=os_version, platform=platform, serial_number=serial_number, tag_name=tag_name, tag_name_in=tag_name_in, tag_id=tag_id, tag_id_in=tag_id_in, user=user, user_email=user_email, user_id=user_id, user_name=user_name, offset=offset)

List Devices

This request returns a list of devices in a Kandji tenant. Optionally. query parameters can be used to filter results.   There is a hard upper limit of 300 results per request. To return addtional results pagination must be used. Pagination examples can be found in the Kandji support [GitHub](https://github.com/kandji-inc/support/tree/main/api-tools/code-examples).

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
    api_instance = kandji_python_sdk.DeviceInformationApi(api_client)
    limit = '300' # str | A hard upper \\`limit\\` is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\`limit\\` and \\`offset\\` parameters. Additionally, parameter queries can be added to a request to limit the results.
    asset_tag = '23245' # str |  (optional)
    blueprint_id = '91f97957-2353-4f86-a1ab-64d2b044a596' # str | Return results 'containing' the specified blueprint id (optional)
    device_id = '2cfeb3ac-3b5d-423e-bcff-e2676a3a32da' # str |  (optional)
    device_name = 'Johnny's MacBook Pro' # str |  (optional)
    filevault_enabled = 'true' # str | Query for devices that either have FileVault on (true) or off (false). This parameter only applies to macOS.    An empty list \\`\\ []\\` will be returned if no devices are found with the given parameter value. (optional)
    mac_address = '00:0c:29:05:43:b6' # str | Search for a specific device by MAC address (optional)
    model = 'MacBook Air (M1, 2020)' # str | Return model results 'containing' the specified model string. (optional)
    ordering = 'device_id' # str | The \\`ordering\\` parameter can be used to define how the device records are ordered in the response. Prepending a dash (\\\\\\-) to the parameter value will reverse the order of the returned results.   \\ `?ordering\\=\\-serial\\_number\\` will order the response by serial\\\\ \\_number in descending order.   \\*\\*Possible values\\*\\*   \\ * \\`asset\\_tag\\` \\* \\`blueprint\\_id\\` \\* \\`device\\_id\\` \\ * \\`device\\_name\\` \\* \\`last\\_check\\_in\\` \\\\\\- agent checkin  \\* \\`model\\` \\* \\`platform\\` \\* \\`os\\_version\\` \\* \\`serial\\ _number\\` \\* \\`user\\`   Additionally, multiple values can be combined in a comma separated list to further customize the ordering of the response.   \\`?ordering\\=serial\\_number,platform\\` (optional)
    os_version = '13.2.3' # str | Return all device records with the specified OS version (optional)
    platform = 'iPad' # str | Return all records matching a specific platform. Possible values:\\`Mac\\`, \\`iPad\\`, \\`iPhone\\`, \\`AppleTV\\` (optional)
    serial_number = 'VMC5qeJ5pDkp' # str | Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned. (optional)
    tag_name = 'accuhive_01' # str | Return results for given tag name. Case sensitive. (optional)
    tag_name_in = 'accuhive_01, accuhive_02' # str | Return results for given tag names separate by commas. Case sensitive. (optional)
    tag_id = '' # str | Search for a tag by its ID. Case sensitive. (optional)
    tag_id_in = '' # str | Return results for given tag IDs separated by commas. Case sensitive. (optional)
    user = 'Art Vandelay' # str | Return results 'containing' the user name (optional)
    user_email = 'someUser@Kandji.io' # str | Return results 'containing' search on email address (optional)
    user_id = '1' # str | 'exact' match on kandji user ID number (optional)
    user_name = 'Vandelay' # str | Return results 'containing' the assigned user Display Name (optional)
    offset = '0' # str | Specify the starting record to return (optional)

    try:
        # List Devices
        api_response = api_instance.list_devices(limit, asset_tag=asset_tag, blueprint_id=blueprint_id, device_id=device_id, device_name=device_name, filevault_enabled=filevault_enabled, mac_address=mac_address, model=model, ordering=ordering, os_version=os_version, platform=platform, serial_number=serial_number, tag_name=tag_name, tag_name_in=tag_name_in, tag_id=tag_id, tag_id_in=tag_id_in, user=user, user_email=user_email, user_id=user_id, user_name=user_name, offset=offset)
        print("The response of DeviceInformationApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInformationApi->list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| A hard upper \\&#x60;limit\\&#x60; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\&#x60;limit\\&#x60; and \\&#x60;offset\\&#x60; parameters. Additionally, parameter queries can be added to a request to limit the results. | 
 **asset_tag** | **str**|  | [optional] 
 **blueprint_id** | **str**| Return results &#39;containing&#39; the specified blueprint id | [optional] 
 **device_id** | **str**|  | [optional] 
 **device_name** | **str**|  | [optional] 
 **filevault_enabled** | **str**| Query for devices that either have FileVault on (true) or off (false). This parameter only applies to macOS.    An empty list \\&#x60;\\ []\\&#x60; will be returned if no devices are found with the given parameter value. | [optional] 
 **mac_address** | **str**| Search for a specific device by MAC address | [optional] 
 **model** | **str**| Return model results &#39;containing&#39; the specified model string. | [optional] 
 **ordering** | **str**| The \\&#x60;ordering\\&#x60; parameter can be used to define how the device records are ordered in the response. Prepending a dash (\\\\\\-) to the parameter value will reverse the order of the returned results.   \\ &#x60;?ordering\\&#x3D;\\-serial\\_number\\&#x60; will order the response by serial\\\\ \\_number in descending order.   \\*\\*Possible values\\*\\*   \\ * \\&#x60;asset\\_tag\\&#x60; \\* \\&#x60;blueprint\\_id\\&#x60; \\* \\&#x60;device\\_id\\&#x60; \\ * \\&#x60;device\\_name\\&#x60; \\* \\&#x60;last\\_check\\_in\\&#x60; \\\\\\- agent checkin  \\* \\&#x60;model\\&#x60; \\* \\&#x60;platform\\&#x60; \\* \\&#x60;os\\_version\\&#x60; \\* \\&#x60;serial\\ _number\\&#x60; \\* \\&#x60;user\\&#x60;   Additionally, multiple values can be combined in a comma separated list to further customize the ordering of the response.   \\&#x60;?ordering\\&#x3D;serial\\_number,platform\\&#x60; | [optional] 
 **os_version** | **str**| Return all device records with the specified OS version | [optional] 
 **platform** | **str**| Return all records matching a specific platform. Possible values:\\&#x60;Mac\\&#x60;, \\&#x60;iPad\\&#x60;, \\&#x60;iPhone\\&#x60;, \\&#x60;AppleTV\\&#x60; | [optional] 
 **serial_number** | **str**| Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned. | [optional] 
 **tag_name** | **str**| Return results for given tag name. Case sensitive. | [optional] 
 **tag_name_in** | **str**| Return results for given tag names separate by commas. Case sensitive. | [optional] 
 **tag_id** | **str**| Search for a tag by its ID. Case sensitive. | [optional] 
 **tag_id_in** | **str**| Return results for given tag IDs separated by commas. Case sensitive. | [optional] 
 **user** | **str**| Return results &#39;containing&#39; the user name | [optional] 
 **user_email** | **str**| Return results &#39;containing&#39; search on email address | [optional] 
 **user_id** | **str**| &#39;exact&#39; match on kandji user ID number | [optional] 
 **user_name** | **str**| Return results &#39;containing&#39; the assigned user Display Name | [optional] 
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

