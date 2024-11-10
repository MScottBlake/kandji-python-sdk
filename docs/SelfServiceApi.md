# kandji_python_sdk.SelfServiceApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_self_service_categories**](SelfServiceApi.md#list_self_service_categories) | **GET** /api/v1/self-service/categories | List Self Service Categories


# **list_self_service_categories**
> object list_self_service_categories()

List Self Service Categories

This endpoint retrieves a list of self\\-service categories and their associated IDs.   If you are planning to make a Library item available in Self Service under a specific category, you can call this endpoint to get the category ID and then use that ID when creating or updating the library item via the Kandji API.

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
    api_instance = kandji_python_sdk.SelfServiceApi(api_client)

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
**200** | OK |  * Allow -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

