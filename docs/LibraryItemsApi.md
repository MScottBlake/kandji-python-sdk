# kandji.LibraryItemsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_library_item_activity**](LibraryItemsApi.md#get_library_item_activity) | **GET** /api/v1/library/library-items/{library_item_id}/activity | Get Library Item Activity
[**get_library_item_statuses**](LibraryItemsApi.md#get_library_item_statuses) | **GET** /api/v1/library/library-items/{library_item_id}/status | Get Library Item Statuses


# **get_library_item_activity**
> AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response get_library_item_activity(library_item_id, activity_type=activity_type, user_id=user_id, user_email=user_email, limit=limit, offset=offset)

Get Library Item Activity

<p>This endpoint retrieves the activity related to a specific library item. Activity is listed from newest to oldest.</p> <p>To see a delta of the activity events between now and the last request, you can store the newest entry from the previous request and then look for that entry in the next request. Any entry post that will be the delta.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.automated_device_enrollment_integrations_list_ade_devices200_response import AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response
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
    api_instance = kandji.LibraryItemsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    activity_type = 'library_item_assignment_changed' # str | Filter actions by this activity type. Choices are: library_item_created, library_item_edited, library_item_deleted, library_item_duplicated, library_item_assignment_changed (optional)
    user_id = '{user uuid}' # str | Filter actions by this user (id) (optional)
    user_email = 'me@example.com' # str | Filter actions by this user (email) (optional)
    limit = '10' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
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
 **activity_type** | **str**| Filter actions by this activity type. Choices are: library_item_created, library_item_edited, library_item_deleted, library_item_duplicated, library_item_assignment_changed | [optional] 
 **user_id** | **str**| Filter actions by this user (id) | [optional] 
 **user_email** | **str**| Filter actions by this user (email) | [optional] 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 

### Return type

[**AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response**](AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_item_statuses**
> AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response get_library_item_statuses(library_item_id, computer_id=computer_id, limit=limit, offset=offset)

Get Library Item Statuses

<p>This endpoint retrieves the statuses related to a specific library item.</p> <h3 id=&quot;request-parameters&quot;>Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.automated_device_enrollment_integrations_list_ade_devices200_response import AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response
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
    api_instance = kandji.LibraryItemsApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    computer_id = '{device_id}' # str | Query for the status of one device. (optional)
    limit = '300' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results. (optional)
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
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | [optional] 
 **offset** | **str**| Specify the starting record to return | [optional] 

### Return type

[**AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response**](AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

