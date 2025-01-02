# kandji_sdk.SettingsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licensing**](SettingsApi.md#licensing) | **GET** /api/v1/settings/licensing | Licensing


# **licensing**
> object licensing()

Licensing

Returns Kandji tenant licensing and utilization information.

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
    api_instance = kandji_sdk.SettingsApi(api_client)

    try:
        # Licensing
        api_response = api_instance.licensing()
        print("The response of SettingsApi->licensing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->licensing: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

