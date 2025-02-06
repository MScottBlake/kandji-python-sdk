# kandji_sdk.CustomAppsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_apps_create_custom_app**](CustomAppsApi.md#custom_apps_create_custom_app) | **POST** /api/v1/library/custom-apps | Create Custom App
[**custom_apps_delete_custom_app**](CustomAppsApi.md#custom_apps_delete_custom_app) | **DELETE** /api/v1/library/custom-apps/{library_item_id} | Delete Custom App
[**custom_apps_get_custom_app**](CustomAppsApi.md#custom_apps_get_custom_app) | **GET** /api/v1/library/custom-apps/{library_item_id} | Get Custom App
[**custom_apps_list_custom_apps**](CustomAppsApi.md#custom_apps_list_custom_apps) | **GET** /api/v1/library/custom-apps | List Custom Apps
[**custom_apps_update_custom_app**](CustomAppsApi.md#custom_apps_update_custom_app) | **PATCH** /api/v1/library/custom-apps/{library_item_id} | Update Custom App
[**custom_apps_upload_custom_app**](CustomAppsApi.md#custom_apps_upload_custom_app) | **POST** /api/v1/library/custom-apps/upload | Upload Custom App


# **custom_apps_create_custom_app**
> object custom_apps_create_custom_app(name, file_key, install_type, install_enforcement, show_in_self_service, self_service_category_id, self_service_recommended)

Create Custom App

<p>This request allows you to create a custom app in the Kandji library.</p> <p>Must have already generated a <code>file_key</code> via <code>Create custom app</code> endpoint and uploaded the file to S3 using a request similar to the <code>Upload to S3</code> example.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji_sdk
from kandji_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://<sub_domain>.api.kandji.io
# See configuration.py for a list of all supported configuration parameters.
configuration = kandji_sdk.Configuration(
    host = "https://<sub_domain>.api.kandji.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Token): bearer
configuration = kandji_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kandji_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kandji_sdk.CustomAppsApi(api_client)
    name = 'name_example' # str | (Required) The name for this Custom App
    file_key = 'file_key_example' # str | (Required) The S3 key from the <code>Upload Custom App</code> endpont used to upload the custom app file.
    install_type = 'install_type_example' # str | (Required) Options are package, zip, image
    install_enforcement = 'install_enforcement_example' # str | (Required) Options are install_once, continuously_enforce, no_enforcement
    show_in_self_service = 'show_in_self_service_example' # str | (Optional, default=false) Displays this app in Self Service
    self_service_category_id = 'self_service_category_id_example' # str | (Required for show_in_self_service=true) Self Service Category (by ID) to display app in
    self_service_recommended = 'self_service_recommended_example' # str | (Optional, default=false) Adds recommended flag to app in Self Service

    try:
        # Create Custom App
        api_response = api_instance.custom_apps_create_custom_app(name, file_key, install_type, install_enforcement, show_in_self_service, self_service_category_id, self_service_recommended)
        print("The response of CustomAppsApi->custom_apps_create_custom_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAppsApi->custom_apps_create_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| (Required) The name for this Custom App | 
 **file_key** | **str**| (Required) The S3 key from the &lt;code&gt;Upload Custom App&lt;/code&gt; endpont used to upload the custom app file. | 
 **install_type** | **str**| (Required) Options are package, zip, image | 
 **install_enforcement** | **str**| (Required) Options are install_once, continuously_enforce, no_enforcement | 
 **show_in_self_service** | **str**| (Optional, default&#x3D;false) Displays this app in Self Service | 
 **self_service_category_id** | **str**| (Required for show_in_self_service&#x3D;true) Self Service Category (by ID) to display app in | 
 **self_service_recommended** | **str**| (Optional, default&#x3D;false) Adds recommended flag to app in Self Service | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_apps_delete_custom_app**
> custom_apps_delete_custom_app(library_item_id)

Delete Custom App

<p>NOTICE: This is permanent so be careful.</p> <p>This endpoint sends a request to delete a specific custom app from the Kandji library.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji_sdk
from kandji_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://<sub_domain>.api.kandji.io
# See configuration.py for a list of all supported configuration parameters.
configuration = kandji_sdk.Configuration(
    host = "https://<sub_domain>.api.kandji.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Token): bearer
configuration = kandji_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kandji_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kandji_sdk.CustomAppsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Delete Custom App
        api_instance.custom_apps_delete_custom_app(library_item_id)
    except Exception as e:
        print("Exception when calling CustomAppsApi->custom_apps_delete_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * Date -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |
**404** | Not Found |  * Connection -  <br>  * Content-Type -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_apps_get_custom_app**
> object custom_apps_get_custom_app(library_item_id)

Get Custom App

<p>This endpoint retrieves details about a specific custom app from the Kandji library.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji_sdk
from kandji_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://<sub_domain>.api.kandji.io
# See configuration.py for a list of all supported configuration parameters.
configuration = kandji_sdk.Configuration(
    host = "https://<sub_domain>.api.kandji.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Token): bearer
configuration = kandji_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kandji_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kandji_sdk.CustomAppsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Get Custom App
        api_response = api_instance.custom_apps_get_custom_app(library_item_id)
        print("The response of CustomAppsApi->custom_apps_get_custom_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAppsApi->custom_apps_get_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_apps_list_custom_apps**
> object custom_apps_list_custom_apps(page=page)

List Custom Apps

This endpoint makes a request to retrieve a list of custom apps from the Kandji library.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji_sdk
from kandji_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://<sub_domain>.api.kandji.io
# See configuration.py for a list of all supported configuration parameters.
configuration = kandji_sdk.Configuration(
    host = "https://<sub_domain>.api.kandji.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Token): bearer
configuration = kandji_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kandji_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kandji_sdk.CustomAppsApi(api_client)
    page = '1' # str | Optional page number. Used when results exceed pagination threshold. A hard upper <code>limit</code> is set at 300 device records returned per request. (optional)

    try:
        # List Custom Apps
        api_response = api_instance.custom_apps_list_custom_apps(page=page)
        print("The response of CustomAppsApi->custom_apps_list_custom_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAppsApi->custom_apps_list_custom_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Optional page number. Used when results exceed pagination threshold. A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_apps_update_custom_app**
> object custom_apps_update_custom_app(library_item_id, name, active)

Update Custom App

<p>This request allows you to update a custom app in the Kandji library.</p> <p>Must have already generated a <code>file_key</code> via <code>Create custom app</code> endpoint and uploaded the file to S3 using a request similar to the <code>Upload to S3</code> example.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji_sdk
from kandji_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://<sub_domain>.api.kandji.io
# See configuration.py for a list of all supported configuration parameters.
configuration = kandji_sdk.Configuration(
    host = "https://<sub_domain>.api.kandji.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Token): bearer
configuration = kandji_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kandji_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kandji_sdk.CustomAppsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    name = 'name_example' # str | Renaming a Custom App
    active = 'active_example' # str | (Optional, default=true) Whether this Custom App is active and installable

    try:
        # Update Custom App
        api_response = api_instance.custom_apps_update_custom_app(library_item_id, name, active)
        print("The response of CustomAppsApi->custom_apps_update_custom_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAppsApi->custom_apps_update_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 
 **name** | **str**| Renaming a Custom App | 
 **active** | **str**| (Optional, default&#x3D;true) Whether this Custom App is active and installable | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_apps_upload_custom_app**
> custom_apps_upload_custom_app(body=body)

Upload Custom App

<p>This request retrieves the S3 upload details need for uploading the app to Amazon S3.</p> <p>Creates a pre-signed <code>post_url</code> to upload a new Custom App to S3.</p> <p>The provided <code>name</code> will be used to calculate a unique <code>file_key</code> in S3.</p> <p>A separate request will have to be made to the <code>Upload to S3</code> endpoint to upload the file to S3 directly using the <code>post_url</code> and <code>post_data</code> from the <code>Upload Custom App</code> response.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji_sdk
from kandji_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://<sub_domain>.api.kandji.io
# See configuration.py for a list of all supported configuration parameters.
configuration = kandji_sdk.Configuration(
    host = "https://<sub_domain>.api.kandji.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Token): bearer
configuration = kandji_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kandji_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kandji_sdk.CustomAppsApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Upload Custom App
        api_instance.custom_apps_upload_custom_app(body=body)
    except Exception as e:
        print("Exception when calling CustomAppsApi->custom_apps_upload_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

