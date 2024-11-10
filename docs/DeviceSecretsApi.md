# kandji_python_sdk.DeviceSecretsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activation_lock_bypass_code**](DeviceSecretsApi.md#get_activation_lock_bypass_code) | **GET** /api/v1/devices/{device_id}/secrets/bypasscode | Get Activation Lock Bypass Code
[**get_filevault_recovery_key**](DeviceSecretsApi.md#get_filevault_recovery_key) | **GET** /api/v1/devices/{device_id}/secrets/filevaultkey | Get FileVault Recovery Key
[**get_recovery_lock_password**](DeviceSecretsApi.md#get_recovery_lock_password) | **GET** /api/v1/devices/{device_id}/secrets/recoverypassword | Get Recovery Lock Password
[**get_unlock_pin**](DeviceSecretsApi.md#get_unlock_pin) | **GET** /api/v1/devices/{device_id}/secrets/unlockpin | Get Unlock Pin


# **get_activation_lock_bypass_code**
> object get_activation_lock_bypass_code(device_id)

Get Activation Lock Bypass Code

This request allows you to retrieve the Activation Lock Bypass code.   user\\_based\\_albc is the user\\-based Activation Lock bypass code for when Activation Lock is enabled using an personal Apple ID and Find My.   device\\_based\\_albc is the device\\-based Activation Lock bypass code for when Activation Lock is enabled by the MDM server.   ### Request Parameters   `device_id` (path parameter): The unique identifier of the device.

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
    api_instance = kandji_python_sdk.DeviceSecretsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Activation Lock Bypass Code
        api_response = api_instance.get_activation_lock_bypass_code(device_id)
        print("The response of DeviceSecretsApi->get_activation_lock_bypass_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSecretsApi->get_activation_lock_bypass_code: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filevault_recovery_key**
> object get_filevault_recovery_key(device_id)

Get FileVault Recovery Key

This request allows you to retrieve the FileVault Recovery key for a macOS device.   ### Request Parameters   `device_id` (path parameter): The unique identifier of the device.

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
    api_instance = kandji_python_sdk.DeviceSecretsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get FileVault Recovery Key
        api_response = api_instance.get_filevault_recovery_key(device_id)
        print("The response of DeviceSecretsApi->get_filevault_recovery_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSecretsApi->get_filevault_recovery_key: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_lock_password**
> object get_recovery_lock_password(device_id)

Get Recovery Lock Password

This request returns the Recovery Lock password for a Mac with an Apple Silicon processor and the legacy EFI firmware password for a Mac with an Intel processor.   For more details on setting and managing Recovery passwords, see this [Kandji support article](https://support.kandji.io/support/solutions/articles/72000560472-configure-the-recovery-password-library-item).    ### Request Parameters   `device_id` (path parameter): The unique identifier of the device.

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
    api_instance = kandji_python_sdk.DeviceSecretsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Recovery Lock Password
        api_response = api_instance.get_recovery_lock_password(device_id)
        print("The response of DeviceSecretsApi->get_recovery_lock_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSecretsApi->get_recovery_lock_password: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unlock_pin**
> object get_unlock_pin(device_id)

Get Unlock Pin

This request allows you to retrieve the device unlock pin for a macOS device.   ### Request Parameters   `device_id` (path parameter): The unique identifier of the device.

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
    api_instance = kandji_python_sdk.DeviceSecretsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Unlock Pin
        api_response = api_instance.get_unlock_pin(device_id)
        print("The response of DeviceSecretsApi->get_unlock_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSecretsApi->get_unlock_pin: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

