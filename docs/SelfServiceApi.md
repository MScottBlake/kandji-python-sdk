# kandji.SelfServiceApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_self_service_categories**](SelfServiceApi.md#list_self_service_categories) | **GET** /api/v1/self-service/categories | List Self Service Categories


# **list_self_service_categories**
> object list_self_service_categories()

List Self Service Categories

<p>This endpoint retrieves a list of self-service categories and their associated IDs.</p> <p>If you are planning to make a Library item available in Self Service under a specific category, you can call this endpoint to get the category ID and then use that ID when creating or updating the library item via the Kandji API.</p>

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
    api_instance = kandji.SelfServiceApi(api_client)

    try:
        # List Self Service Categories
        api_response = api_instance.list_self_service_categories()
        print("The response of SelfServiceApi->list_self_service_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfServiceApi->list_self_service_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

