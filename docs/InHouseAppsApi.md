# kandji_sdk.InHouseAppsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inhouse_app**](InHouseAppsApi.md#create_inhouse_app) | **POST** /api/v1/library/ipa-apps | Create In-House App
[**delete_inhouse_app**](InHouseAppsApi.md#delete_inhouse_app) | **DELETE** /api/v1/library/ipa-apps/{library_item_id} | Delete In-House App
[**get_inhouse_app**](InHouseAppsApi.md#get_inhouse_app) | **GET** /api/v1/library/ipa-apps/{library_item_id} | Get In-House App
[**list_inhouse_apps**](InHouseAppsApi.md#list_inhouse_apps) | **GET** /api/v1/library/ipa-apps | List In-House Apps
[**update_inhouse_app**](InHouseAppsApi.md#update_inhouse_app) | **PATCH** /api/v1/library/ipa-apps/{library_item_id} | Update In-House App
[**upload_inhouse_app**](InHouseAppsApi.md#upload_inhouse_app) | **POST** /api/v1/library/ipa-apps/upload | Upload In-House App
[**upload_inhouse_app_status**](InHouseAppsApi.md#upload_inhouse_app_status) | **GET** /api/v1/library/ipa-apps/upload/{pending_upload_id}/status | Upload In-House App Status


# **create_inhouse_app**
> create_inhouse_app(content_type, body=body)

Create In-House App

<p>After uploading the .ipa app file to S3, this request allows you to create the In-House App in the Kandji library.</p> <p>You must have already generated a <code>file_key</code> via <code>Create In-House App</code> endpoint and uploaded the file to S3 using a request similar to the <code>Upload In-House App to S3</code> example.</p> <p>The <code>name</code> key can be an arbitrary value used for setting the name of the Library Item as it appears in Kandji</p>

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
    api_instance = kandji_sdk.InHouseAppsApi(api_client)
    content_type = 'application/json' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Create In-House App
        api_instance.create_inhouse_app(content_type, body=body)
    except Exception as e:
        print("Exception when calling InHouseAppsApi->create_inhouse_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inhouse_app**
> delete_inhouse_app(library_item_id)

Delete In-House App

<p>NOTICE: This is permanent so be careful.</p> <p>This endpoint sends a request to delete a specific In-House App Library Item from Kandji.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the Library Item.</p>

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
    api_instance = kandji_sdk.InHouseAppsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Delete In-House App
        api_instance.delete_inhouse_app(library_item_id)
    except Exception as e:
        print("Exception when calling InHouseAppsApi->delete_inhouse_app: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inhouse_app**
> object get_inhouse_app(library_item_id)

Get In-House App

<p>This endpoint retrieves details about a specific In-House App from the Kandji Library.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the Library Item.</p>

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
    api_instance = kandji_sdk.InHouseAppsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Get In-House App
        api_response = api_instance.get_inhouse_app(library_item_id)
        print("The response of InHouseAppsApi->get_inhouse_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InHouseAppsApi->get_inhouse_app: %s\n" % e)
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
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Encoding -  <br>  * Content-Language -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Access-Control-Allow-Origin -  <br>  * Accept-Ranges -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inhouse_apps**
> object list_inhouse_apps(page=page)

List In-House Apps

This endpoint makes a request to retrieve a list of In-House Apps from the Kandji library.

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
    api_instance = kandji_sdk.InHouseAppsApi(api_client)
    page = '1' # str | Optional page number. Used when results exceed pagination threshold. A hard upper <code>limit</code> is set at 300 app records returned per request. (optional)

    try:
        # List In-House Apps
        api_response = api_instance.list_inhouse_apps(page=page)
        print("The response of InHouseAppsApi->list_inhouse_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InHouseAppsApi->list_inhouse_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Optional page number. Used when results exceed pagination threshold. A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 app records returned per request. | [optional] 

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

# **update_inhouse_app**
> update_inhouse_app(library_item_id, content_type, body=body)

Update In-House App

<p>This request allows you to update an existing In-house App in the Kandji library.</p> <p>Must have already generated a <code>file_key</code> via <code>Create In-House App</code> endpoint and uploaded the file to S3 using a request similar to the <code>Upload In-House App to S3</code> example.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p>

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
    api_instance = kandji_sdk.InHouseAppsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    content_type = 'application/json' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update In-House App
        api_instance.update_inhouse_app(library_item_id, content_type, body=body)
    except Exception as e:
        print("Exception when calling InHouseAppsApi->update_inhouse_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 
 **content_type** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_inhouse_app**
> object upload_inhouse_app(content_type, body=body)

Upload In-House App

<p>This request retrieves the S3 upload details needed for uploading the in-house app .ipa file to Amazon S3.</p> <p>Creates a pre-signed <code>post_url</code> to upload a new In-house App to S3.</p> <p>The provided <code>filename</code> will be used to calculate a unique <code>file_key</code> in S3.</p> <p>A separate request will have to be made to the <code>Upload In-House App to S3</code> endpoint to upload the file to S3 directly using the <code>post_url</code> and <code>post_data</code> from the <code>Upload In-House App</code> response.</p> <p>The returned <code>id</code> value can be used to check the upload status in the <code>Upload In-House App Status</code> endpoint after calling the <code>Upload In-House App to S3</code> endpoint.</p>

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
    api_instance = kandji_sdk.InHouseAppsApi(api_client)
    content_type = 'application/json' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Upload In-House App
        api_response = api_instance.upload_inhouse_app(content_type, body=body)
        print("The response of InHouseAppsApi->upload_inhouse_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InHouseAppsApi->upload_inhouse_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Connection -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Language -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Access-Control-Allow-Origin -  <br>  * Accept-Ranges -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_inhouse_app_status**
> object upload_inhouse_app_status(pending_upload_id)

Upload In-House App Status

<p>This endpoint retrieves current upload status of an In-House App .ipa file to Amazon S3 from the <code>Upload In-House App to S3</code> endpoint</p> <p>The app .ipa file has successfully uploaded and is ready for the <code>Create In-House App</code> endpoint when the <code>status</code> returned is <code>VALIDATED</code></p> <p>If the <code>status</code> returned is <code>UPLOADING</code> or VALIDATING, the upload is still being processed. Retry again after 1 second.</p> <p>If the <code>status</code> returned is <code>UPLOAD_FAILED</code> or <code>VALIDATE_FAILED</code> then re-attempt the <code>Upload In-House App to S3</code> endpoint.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>pending_upload_id</code> (path parameter): This should be the <code>id</code> from the <code>Upload to In-House App</code> API response</p>

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
    api_instance = kandji_sdk.InHouseAppsApi(api_client)
    pending_upload_id = 'pending_upload_id_example' # str | 

    try:
        # Upload In-House App Status
        api_response = api_instance.upload_inhouse_app_status(pending_upload_id)
        print("The response of InHouseAppsApi->upload_inhouse_app_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InHouseAppsApi->upload_inhouse_app_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending_upload_id** | **str**|  | 

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

