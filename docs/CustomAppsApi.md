# kandji_python_sdk.CustomAppsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_app**](CustomAppsApi.md#create_custom_app) | **POST** /api/v1/library/custom-apps | Create Custom App
[**delete_custom_app**](CustomAppsApi.md#delete_custom_app) | **DELETE** /api/v1/library/custom-apps/{library_item_id} | Delete Custom App
[**get_custom_app**](CustomAppsApi.md#get_custom_app) | **GET** /api/v1/library/custom-apps/{library_item_id} | Get Custom App
[**list_custom_apps**](CustomAppsApi.md#list_custom_apps) | **GET** /api/v1/library/custom-apps | List Custom Apps
[**update_custom_app**](CustomAppsApi.md#update_custom_app) | **PATCH** /api/v1/library/custom-apps/{library_item_id} | Update Custom App
[**upload_custom_app**](CustomAppsApi.md#upload_custom_app) | **POST** /api/v1/library/custom-apps/upload | Upload Custom App


# **create_custom_app**
> object create_custom_app(file_key, install_enforcement, install_type, name, self_service_category_id, self_service_recommended, show_in_self_service)

Create Custom App

This request allows you to create a custom app in the Kandji library.    Must have already generated a `file_key` via `Create custom app` endpoint and uploaded the file to S3 using a request similar to the `Upload to S3` example.

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
    api_instance = kandji_python_sdk.CustomAppsApi(api_client)
    file_key = 'file_key_example' # str | (Required) The S3 key from the `Upload Custom App` endpont used to upload the custom app file.
    install_enforcement = 'install_enforcement_example' # str | (Required) Options are install\\\\_once, continuously\\\\_enforce, no\\\\_enforcement
    install_type = 'install_type_example' # str | (Required) Options are package, zip, image
    name = 'name_example' # str | (Required) The name for this Custom App
    self_service_category_id = 'self_service_category_id_example' # str | (Required for show\\\\_in\\\\_self\\\\_service\\\\=true) Self Service Category (by ID) to display app in
    self_service_recommended = 'self_service_recommended_example' # str | (Optional, default\\\\=false) Adds recommended flag to app in Self Service
    show_in_self_service = 'show_in_self_service_example' # str | (Optional, default\\\\=false) Displays this app in Self Service

    try:
        # Create Custom App
        api_response = api_instance.create_custom_app(file_key, install_enforcement, install_type, name, self_service_category_id, self_service_recommended, show_in_self_service)
        print("The response of CustomAppsApi->create_custom_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAppsApi->create_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_key** | **str**| (Required) The S3 key from the &#x60;Upload Custom App&#x60; endpont used to upload the custom app file. | 
 **install_enforcement** | **str**| (Required) Options are install\\\\_once, continuously\\\\_enforce, no\\\\_enforcement | 
 **install_type** | **str**| (Required) Options are package, zip, image | 
 **name** | **str**| (Required) The name for this Custom App | 
 **self_service_category_id** | **str**| (Required for show\\\\_in\\\\_self\\\\_service\\\\&#x3D;true) Self Service Category (by ID) to display app in | 
 **self_service_recommended** | **str**| (Optional, default\\\\&#x3D;false) Adds recommended flag to app in Self Service | 
 **show_in_self_service** | **str**| (Optional, default\\\\&#x3D;false) Displays this app in Self Service | 

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
**201** | Created |  * Allow -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_app**
> delete_custom_app(library_item_id)

Delete Custom App

NOTICE: This is permanent so be careful.   This endpoint sends a request to delete a specific custom app from the Kandji library.   ### Request Parameters   `library_item_id` (path parameter): The unique identifier of the library item.

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
    api_instance = kandji_python_sdk.CustomAppsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Delete Custom App
        api_instance.delete_custom_app(library_item_id)
    except Exception as e:
        print("Exception when calling CustomAppsApi->delete_custom_app: %s\n" % e)
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
**204** | No Content |  * Allow -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  |
**404** | Not Found |  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * Via -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * X-Served-By -  <br>  * X-Timer -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_app**
> object get_custom_app(library_item_id)

Get Custom App

This endpoint retrieves details about a specific custom app from the Kandji library.   ### Request Parameters   `library_item_id` (path parameter): The unique identifier of the library item.

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
    api_instance = kandji_python_sdk.CustomAppsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Get Custom App
        api_response = api_instance.get_custom_app(library_item_id)
        print("The response of CustomAppsApi->get_custom_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAppsApi->get_custom_app: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_apps**
> object list_custom_apps(page=page)

List Custom Apps

This endpoint makes a request to retrieve a list of custom apps from the Kandji library.

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
    api_instance = kandji_python_sdk.CustomAppsApi(api_client)
    page = '1' # str | Optional page number. Used when results exceed pagination threshold. A hard upper \\`limit\\` is set at 300 device records returned per request. (optional)

    try:
        # List Custom Apps
        api_response = api_instance.list_custom_apps(page=page)
        print("The response of CustomAppsApi->list_custom_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAppsApi->list_custom_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Optional page number. Used when results exceed pagination threshold. A hard upper \\&#x60;limit\\&#x60; is set at 300 device records returned per request. | [optional] 

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
**200** | OK |  * Allow -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_app**
> object update_custom_app(library_item_id, active, name)

Update Custom App

This request allows you to update a custom app in the Kandji library.    Must have already generated a `file_key` via `Create custom app` endpoint and uploaded the file to S3 using a request similar to the `Upload to S3` example.   ### Request Parameters   `library_item_id` (path parameter): The unique identifier of the library item.

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
    api_instance = kandji_python_sdk.CustomAppsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    active = 'active_example' # str | (Optional, default\\\\=true) Whether this Custom App is active and installable
    name = 'name_example' # str | Renaming a Custom App

    try:
        # Update Custom App
        api_response = api_instance.update_custom_app(library_item_id, active, name)
        print("The response of CustomAppsApi->update_custom_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAppsApi->update_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 
 **active** | **str**| (Optional, default\\\\&#x3D;true) Whether this Custom App is active and installable | 
 **name** | **str**| Renaming a Custom App | 

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
**200** | OK |  * Allow -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_custom_app**
> upload_custom_app(body=body)

Upload Custom App

This request retrieves the S3 upload details need for uploading the app to Amazon S3\\.   Creates a pre\\-signed `post_url` to upload a new Custom App to S3\\.   The provided `name` will be used to calculate a unique `file_key` in S3\\.   A separate request will have to be made to the `Upload to S3` endpoint to upload the file to S3 directly using the `post_url` and `post_data` from the `Upload Custom App` response.

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
    api_instance = kandji_python_sdk.CustomAppsApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Upload Custom App
        api_instance.upload_custom_app(body=body)
    except Exception as e:
        print("Exception when calling CustomAppsApi->upload_custom_app: %s\n" % e)
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
**201** | Created |  * Allow -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

