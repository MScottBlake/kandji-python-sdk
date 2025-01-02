# kandji_sdk.LostModeApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_lost_mode**](LostModeApi.md#disable_lost_mode) | **POST** /api/v1/devices/{device_id}/action/disablelostmode | Disable Lost Mode
[**enable_lost_mode**](LostModeApi.md#enable_lost_mode) | **POST** /api/v1/devices/{device_id}/action/enablelostmode | Enable Lost Mode
[**play_lost_mode_sound**](LostModeApi.md#play_lost_mode_sound) | **POST** /api/v1/devices/{device_id}/action/playlostmodesound | Play Lost Mode Sound
[**update_location**](LostModeApi.md#update_location) | **POST** /api/v1/devices/{device_id}/action/updatelocation | Update Location


# **disable_lost_mode**
> disable_lost_mode(device_id)

Disable Lost Mode

<p>This command will send a request to turn off lost mode on iOS and iPadOS.</p> <p>If the command is already pending, the message &quot;<em>Disable lost mode is already pending for this device.</em>&quot; will be in the response.</p>

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
    api_instance = kandji_sdk.LostModeApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Disable Lost Mode
        api_instance.disable_lost_mode(device_id)
    except Exception as e:
        print("Exception when calling LostModeApi->disable_lost_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_lost_mode**
> enable_lost_mode(device_id, body=body)

Enable Lost Mode

<p>This endpoint sends an MDM command to remotely turn on lost mode on iOS and iPadOS.</p> <p>Optionally, a JSON payload can be sent in the request to set a lock message, phone number, and footnote on the target device.</p>

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
    api_instance = kandji_sdk.LostModeApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Enable Lost Mode
        api_instance.enable_lost_mode(device_id, body=body)
    except Exception as e:
        print("Exception when calling LostModeApi->enable_lost_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_lost_mode_sound**
> play_lost_mode_sound(device_id)

Play Lost Mode Sound

<p>This command will tell the target iOS or iPadOS device to play the lost mode sound.</p> <p><strong>Note</strong>: The Lost Mode sound will play for 2 minutes, even if the device is in silent mode. Anyone finding the device can silence the sound by pressing any of its side buttons.</p>

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
    api_instance = kandji_sdk.LostModeApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Play Lost Mode Sound
        api_instance.play_lost_mode_sound(device_id)
    except Exception as e:
        print("Exception when calling LostModeApi->play_lost_mode_sound: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location**
> update_location(device_id)

Update Location

This endpoint sends an MDM command to update the location data on iOS and iPadOS.

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
    api_instance = kandji_sdk.LostModeApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Update Location
        api_instance.update_location(device_id)
    except Exception as e:
        print("Exception when calling LostModeApi->update_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

