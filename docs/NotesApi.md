# kandji_sdk.NotesApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notes_create_device_note**](NotesApi.md#notes_create_device_note) | **POST** /api/v1/devices/{device_id}/notes | Create Device Note
[**notes_delete_device_note**](NotesApi.md#notes_delete_device_note) | **DELETE** /api/v1/devices/{device_id}/notes/{note_id} | Delete Device Note
[**notes_get_device_notes**](NotesApi.md#notes_get_device_notes) | **GET** /api/v1/devices/{device_id}/notes | Get Device Notes
[**notes_retrieve_device_note**](NotesApi.md#notes_retrieve_device_note) | **GET** /api/v1/devices/{device_id}/notes/{note_id} | Retrieve Device Note
[**notes_update_device_note**](NotesApi.md#notes_update_device_note) | **PATCH** /api/v1/devices/{device_id}/notes/{note_id} | Update Device Note


# **notes_create_device_note**
> object notes_create_device_note(device_id, body=body)

Create Device Note

This request creates a note for the specified device ID.

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
    api_instance = kandji_sdk.NotesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Create Device Note
        api_response = api_instance.notes_create_device_note(device_id, body=body)
        print("The response of NotesApi->notes_create_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_create_device_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_delete_device_note**
> object notes_delete_device_note(device_id, note_id)

Delete Device Note

This request deletes a specified note (Note ID) for the specified Device ID.

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
    api_instance = kandji_sdk.NotesApi(api_client)
    device_id = 'device_id_example' # str | 
    note_id = 'note_id_example' # str | 

    try:
        # Delete Device Note
        api_response = api_instance.notes_delete_device_note(device_id, note_id)
        print("The response of NotesApi->notes_delete_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_delete_device_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **note_id** | **str**|  | 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_get_device_notes**
> object notes_get_device_notes(device_id)

Get Device Notes

This request gets all notes for the specified Device ID.

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
    api_instance = kandji_sdk.NotesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Notes
        api_response = api_instance.notes_get_device_notes(device_id)
        print("The response of NotesApi->notes_get_device_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_get_device_notes: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * X-Total-Count -  <br>  * X-Total-Pages -  <br>  * Link -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_retrieve_device_note**
> object notes_retrieve_device_note(device_id, note_id)

Retrieve Device Note

This request retrieves a specified note (Note ID) for the specified Device ID.

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
    api_instance = kandji_sdk.NotesApi(api_client)
    device_id = 'device_id_example' # str | 
    note_id = 'note_id_example' # str | 

    try:
        # Retrieve Device Note
        api_response = api_instance.notes_retrieve_device_note(device_id, note_id)
        print("The response of NotesApi->notes_retrieve_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_retrieve_device_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **note_id** | **str**|  | 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_update_device_note**
> object notes_update_device_note(device_id, note_id, body=body)

Update Device Note

This request patches a specified note (Note ID) for the specified Device ID.

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
    api_instance = kandji_sdk.NotesApi(api_client)
    device_id = 'device_id_example' # str | 
    note_id = 'note_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update Device Note
        api_response = api_instance.notes_update_device_note(device_id, note_id, body=body)
        print("The response of NotesApi->notes_update_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_update_device_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **note_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

