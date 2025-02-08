# kandji.CustomProfilesApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_profile**](CustomProfilesApi.md#create_custom_profile) | **POST** /api/v1/library/custom-profiles | Create Custom Profile
[**delete_custom_profile**](CustomProfilesApi.md#delete_custom_profile) | **DELETE** /api/v1/library/custom-profiles/{library_item_id} | Delete Custom Profile
[**get_custom_profile**](CustomProfilesApi.md#get_custom_profile) | **GET** /api/v1/library/custom-profiles/{library_item_id} | Get Custom Profile
[**list_custom_profiles**](CustomProfilesApi.md#list_custom_profiles) | **GET** /api/v1/library/custom-profiles | List Custom Profiles
[**update_custom_profile**](CustomProfilesApi.md#update_custom_profile) | **PATCH** /api/v1/library/custom-profiles/{library_item_id} | Update Custom Profile


# **create_custom_profile**
> object create_custom_profile(name, file, active)

Create Custom Profile

This request allows you to create a custom profile in the Kandji library.

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
    api_instance = kandji.CustomProfilesApi(api_client)
    name = 'name_example' # str | (Required) The profile name
    file = None # bytearray | (Required) The path to the profile's .mobileconfig file
    active = 'active_example' # str | (Optional, default=true) Whether this library item is active

    try:
        # Create Custom Profile
        api_response = api_instance.create_custom_profile(name, file, active)
        print("The response of CustomProfilesApi->create_custom_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomProfilesApi->create_custom_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| (Required) The profile name | 
 **file** | **bytearray**| (Required) The path to the profile&#39;s .mobileconfig file | 
 **active** | **str**| (Optional, default&#x3D;true) Whether this library item is active | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_profile**
> delete_custom_profile(library_item_id)

Delete Custom Profile

<p>NOTICE: This is permanent so be careful.</p> <p>This endpoint sends a request to delete a specific custom profile from the Kandji library.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p>

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
    api_instance = kandji.CustomProfilesApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Delete Custom Profile
        api_instance.delete_custom_profile(library_item_id)
    except Exception as e:
        print("Exception when calling CustomProfilesApi->delete_custom_profile: %s\n" % e)
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

# **get_custom_profile**
> object get_custom_profile(library_item_id)

Get Custom Profile

<p>This endpoint retrieves details about a specific custom profile from the Kandji library.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p>

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
    api_instance = kandji.CustomProfilesApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Get Custom Profile
        api_response = api_instance.get_custom_profile(library_item_id)
        print("The response of CustomProfilesApi->get_custom_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomProfilesApi->get_custom_profile: %s\n" % e)
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

# **list_custom_profiles**
> object list_custom_profiles(page=page)

List Custom Profiles

This endpoint makes a request to retrieve a list of custom profiles from the Kandji library.

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
    api_instance = kandji.CustomProfilesApi(api_client)
    page = '1' # str | Optional page number. Used when results exceed pagination threshold. A hard upper limit is set at 300 device records returned per request. (optional)

    try:
        # List Custom Profiles
        api_response = api_instance.list_custom_profiles(page=page)
        print("The response of CustomProfilesApi->list_custom_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomProfilesApi->list_custom_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Optional page number. Used when results exceed pagination threshold. A hard upper limit is set at 300 device records returned per request. | [optional] 

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

# **update_custom_profile**
> object update_custom_profile(library_item_id)

Update Custom Profile

<p>This request allows you to update a custom profile in the Kandji library.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p>

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
    api_instance = kandji.CustomProfilesApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Update Custom Profile
        api_response = api_instance.update_custom_profile(library_item_id)
        print("The response of CustomProfilesApi->update_custom_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomProfilesApi->update_custom_profile: %s\n" % e)
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

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

