# kandji_python_sdk.LibraryItemsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_library_item_activity**](LibraryItemsApi.md#get_library_item_activity) | **GET** /api/v1/library/library-items/{library_item_id}/activity | Get Library Item Activity
[**get_library_item_statuses**](LibraryItemsApi.md#get_library_item_statuses) | **GET** /api/v1/library/library-items/{library_item_id}/status | Get Library Item Statuses


# **get_library_item_activity**
> object get_library_item_activity(library_item_id, activity_type=activity_type, user_id=user_id, user_email=user_email, limit=limit, offset=offset)

Get Library Item Activity

This endpoint retrieves the activity related to a specific library item. Activity is listed from newest to oldest.   To see a delta of the activity events between now and the last request, you can store the newest entry from the previous request and then look for that entry in the next request. Any entry post that will be the delta.   ### Request Parameters   `library_item_id` (path parameter): The unique identifier of the library item.

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
    api_instance = kandji_python_sdk.LibraryItemsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    activity_type = 'library_item_assignment_changed' # str | Filter actions by this activity type. Choices are: library\\\\\\_item\\\\\\_created, library\\\\\\_item\\\\\\_edited, library\\\\\\_item\\\\\\_deleted, library\\\\\\_item\\\\\\_duplicated, library\\\\\\_item\\\\\\_assignment\\\\\\_changed (optional)
    user_id = '{user uuid}' # str | Filter actions by this user (id) (optional)
    user_email = 'me@example.com' # str | Filter actions by this user (email) (optional)
    limit = '10' # str | A hard upper \\`limit\\` is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\`limit\\` and \\`offset\\` parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '100' # str | Specify the starting record to return (optional)

    try:
        # Get Library Item Activity
        api_response = api_instance.get_library_item_activity(library_item_id, activity_type=activity_type, user_id=user_id, user_email=user_email, limit=limit, offset=offset)
        print("The response of LibraryItemsApi->get_library_item_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryItemsApi->get_library_item_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 
 **activity_type** | **str**| Filter actions by this activity type. Choices are: library\\\\\\_item\\\\\\_created, library\\\\\\_item\\\\\\_edited, library\\\\\\_item\\\\\\_deleted, library\\\\\\_item\\\\\\_duplicated, library\\\\\\_item\\\\\\_assignment\\\\\\_changed | [optional] 
 **user_id** | **str**| Filter actions by this user (id) | [optional] 
 **user_email** | **str**| Filter actions by this user (email) | [optional] 
 **limit** | **str**| A hard upper \\&#x60;limit\\&#x60; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\&#x60;limit\\&#x60; and \\&#x60;offset\\&#x60; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 

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
**200** | OK |  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Allow -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * Via -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * X-Served-By -  <br>  * X-Timer -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_item_statuses**
> object get_library_item_statuses(library_item_id, computer_id=computer_id, limit=limit, offset=offset)

Get Library Item Statuses

This endpoint retrieves the statuses related to a specific library item.   ### Request Parameters   `library_item_id` (path parameter): The unique identifier of the library item.

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
    api_instance = kandji_python_sdk.LibraryItemsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    computer_id = '{device_id}' # str | Query for the status of one device. (optional)
    limit = '300' # str | A hard upper \\`limit\\` is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\`limit\\` and \\`offset\\` parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
    offset = '' # str | Specify the starting record to return (optional)

    try:
        # Get Library Item Statuses
        api_response = api_instance.get_library_item_statuses(library_item_id, computer_id=computer_id, limit=limit, offset=offset)
        print("The response of LibraryItemsApi->get_library_item_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryItemsApi->get_library_item_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 
 **computer_id** | **str**| Query for the status of one device. | [optional] 
 **limit** | **str**| A hard upper \\&#x60;limit\\&#x60; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\&#x60;limit\\&#x60; and \\&#x60;offset\\&#x60; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 

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
**200** | OK |  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Allow -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * Via -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * X-Served-By -  <br>  * X-Timer -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

