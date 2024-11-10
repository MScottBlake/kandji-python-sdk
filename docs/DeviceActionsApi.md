# kandji_python_sdk.DeviceActionsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_passcode**](DeviceActionsApi.md#clear_passcode) | **POST** /api/v1/devices/{device_id}/action/clearpasscode | Clear Passcode
[**delete_device**](DeviceActionsApi.md#delete_device) | **DELETE** /api/v1/devices/{device_id} | Delete Device
[**delete_user**](DeviceActionsApi.md#delete_user) | **POST** /api/v1/devices/{device_id}/action/deleteuser | Delete User
[**erase_device**](DeviceActionsApi.md#erase_device) | **POST** /api/v1/devices/{device_id}/action/erase | Erase Device
[**get_device_commands**](DeviceActionsApi.md#get_device_commands) | **GET** /api/v1/devices/{device_id}/commands | Get Device Commands
[**lock_device**](DeviceActionsApi.md#lock_device) | **POST** /api/v1/devices/{device_id}/action/lock | Lock Device
[**reinstall_agent**](DeviceActionsApi.md#reinstall_agent) | **POST** /api/v1/devices/{device_id}/action/reinstallagent | Reinstall Agent
[**remote_desktop**](DeviceActionsApi.md#remote_desktop) | **POST** /api/v1/devices/{device_id}/action/remotedesktop | Remote Desktop
[**renew_mdm_profile**](DeviceActionsApi.md#renew_mdm_profile) | **POST** /api/v1/devices/{device_id}/action/renewmdmprofile | Renew MDM Profile
[**restart_device**](DeviceActionsApi.md#restart_device) | **POST** /api/v1/devices/{device_id}/action/restart | Restart Device
[**send_blankpush**](DeviceActionsApi.md#send_blankpush) | **POST** /api/v1/devices/{device_id}/action/blankpush | Send Blankpush
[**set_name**](DeviceActionsApi.md#set_name) | **POST** /api/v1/devices/{device_id}/action/setname | Set Name
[**shutdown**](DeviceActionsApi.md#shutdown) | **POST** /api/v1/devices/{device_id}/action/shutdown | Shutdown
[**unlock_account**](DeviceActionsApi.md#unlock_account) | **POST** /api/v1/devices/{device_id}/action/unlockaccount | Unlock Account
[**update_inventory**](DeviceActionsApi.md#update_inventory) | **POST** /api/v1/devices/{device_id}/action/updateinventory | Update Inventory


# **clear_passcode**
> clear_passcode(device_id)

Clear Passcode

This endpoint sends an MDM command to clear a device passcode. Available for iPhone and iPad.

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Clear Passcode
        api_instance.clear_passcode(device_id)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->clear_passcode: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> delete_device(device_id)

Delete Device

This endpoint sends an MDM command to delete a device. This will remove the device record from Kandji and send a Remove Management command. For macOS devices, it will also send an uninstall command to the Kandji Agent at the next agent checkin.

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Delete Device
        api_instance.delete_device(device_id)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->delete_device: %s\n" % e)
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(device_id, body=body)

Delete User

This endpoint sends an MDM command to delete a local user account on macOS and Shared iPad (Device Supervision via Automated Device Enrollment is required).   **Request Body Parameters**: application/json      ---   `DeleteAllUsers` \\- `boolean`   `ForceDeletion` \\- `boolean`    `UserName` \\- `string`

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Delete User
        api_instance.delete_user(device_id, body=body)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->delete_user: %s\n" % e)
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

# **erase_device**
> erase_device(device_id, body=body)

Erase Device

This endpoint sends an MDM command to erase the device.    iOS 4\\.0\\+, iPadOS 4\\.0\\+, macOS 10\\.7\\+, tvOS 10\\.2\\+   **Request Body Parameters: application/json**     | Key | Type | Description |  | --- | --- | --- | | `PIN` | `string` | The six\\-character PIN for Find My. This value is available in macOS 10\\.8 and later. | | `PreserveDataPlan` | `boolean` | If true, preserve the data plan on an iPhone or iPad with eSIM functionality, if one exists. This value is available in iOS 11 and later.  Default: true | | `DisallowProximitySetup` | `boolean` | If true, disable Proximity Setup on the next reboot and skip the pane in Setup Assistant. This value is available in iOS 11 and later. Prior to iOS 14, don’t use this option with any other option.  Default: false | | `ReturnToService` | `object` | (iOS 17 and later and iPadOS 17 and later and with Shared iPad ) When sending the erase device command to mobile devices, use this key to enable Return to Service. Include an optional Wi\\-Fi payload ProfileId to allow the device to connect to a Wi\\-Fi network automatically after being erased. If a Wi\\ -Fi ProfileId is not provided and the mobile device is not tethered to a Mac to share the network connection, the end\\-user will be required to select a Wi\\-Fi network to complete the setup.  If sent to any macOS computer or to mobile devices on iOS 16 or iPadOS 16 and below, the RTS keys will be ignored, and only the erase device command will be issued to the device. | | \\- `Enabled` | `boolean` | (Required) If true, the device tries to re\\-enroll itself automatically after erasure. The user needs to deactivate all activation locks for this feature to work correctly. | | \\- `ProfileId` | `string` | Profile ID value associated with a Wi\\-Fi profile payload. This is required when the device doesn’t have ethernet access. |

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Erase Device
        api_instance.erase_device(device_id, body=body)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->erase_device: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_commands**
> get_device_commands(device_id, limit, offset=offset)

Get Device Commands

This endpoint sends a request to get information about the commands sent to a given device ID.   ### MDM Status Codes   * 1 : Command is Pending * 2 : Command is running * 3 : Command completed * 4 : Command failed * 5 : Command received 'Not Now' response

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = '300' # str | A hard upper \\`limit\\` is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\`limit\\` and \\`offset\\` parameters. Additionally, parameter queries can be added to a request to limit the results.
    offset = 'offset_example' # str | Specify the starting record to return (optional)

    try:
        # Get Device Commands
        api_instance.get_device_commands(device_id, limit, offset=offset)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->get_device_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **limit** | **str**| A hard upper \\&#x60;limit\\&#x60; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the \\&#x60;limit\\&#x60; and \\&#x60;offset\\&#x60; parameters. Additionally, parameter queries can be added to a request to limit the results. | 
 **offset** | **str**| Specify the starting record to return | [optional] 

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
**200** | OK |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_device**
> object lock_device(device_id, body=body)

Lock Device

This endpoint sends an MDM command to remotely lock a device.    For macOS clients, an unlock PIN will be created, and returned in the response.    > **Caution !!!**   > *For a Mac with Apple silicon running a version of macOS before 11\\.5 will deactivate the Mac. To reactivate, the Mac requires a network connection and authentication by a Secure Token enabled local administrator.*   Optionally, a JSON payload can be sent in the request to set a lock message and phone number on the target device.   **Note:** For macOS, although the lock message is displayed on all types of Mac computers, the phone number is displayed only on a Mac with Apple silicon.   #### Response properties     | Property | Description | Type | | --- | --- | --- | | PIN | Six digit pin code used to unlock a Mac. | String |

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Lock Device
        api_response = api_instance.lock_device(device_id, body=body)
        print("The response of DeviceActionsApi->lock_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->lock_device: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |
**400** | Bad Request |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reinstall_agent**
> reinstall_agent(device_id)

Reinstall Agent

This endpoint sends an MDM command reinstall the Kandji Agent. Available for macOS devices.

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Reinstall Agent
        api_instance.reinstall_agent(device_id)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->reinstall_agent: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_desktop**
> remote_desktop(device_id, body=body)

Remote Desktop

This endpoint sends an MDM command to control the Remote Management status on a Mac. This MDM command turns on (or turns off) Remote Management with *Observe* and *Control* permissions given to all users\\*.\\*   **Request Body Parameters**: application/json     ---   `EnableRemoteDesktop` \\- `boolean`

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Remote Desktop
        api_instance.remote_desktop(device_id, body=body)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->remote_desktop: %s\n" % e)
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

# **renew_mdm_profile**
> renew_mdm_profile(device_id)

Renew MDM Profile

This endpoint sends an MDM command to re\\-install the existing root MDM profile for a given device ID. This command will not impact any existing configurations, apps, or profiles.

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Renew MDM Profile
        api_instance.renew_mdm_profile(device_id)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->renew_mdm_profile: %s\n" % e)
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

# **restart_device**
> restart_device(device_id, body=body)

Restart Device

This endpoint sends an MDM command to remotely restart a device.    * `RebuildKernelCache` \\- If `true`, the system rebuilds the kernel cache during a device restart. If `BootstrapTokenAllowedForAuthentication` is `true` inSecurityInfoResponse.SecurityInfo, the device requests the bootstrap token from MDM before executing this command. This value is available in macOS 11 and later. Default: false * `NotifyUser` \\- If `true`, notifies the user to restart the device at their convenience. Forced restart if the device is at `loginwindow` with no logged\\-in users. The user can dismiss the notification and ignore the request. No further notifications display unless you resend the command. This value is available in macOS 11\\.3 and later. Default: false

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Restart Device
        api_instance.restart_device(device_id, body=body)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->restart_device: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_blankpush**
> send_blankpush(device_id)

Send Blankpush

This endpoint sends an MDM command to initiate a blank push.    [Using the Blank Push command](https://support.kandji.io/what-is-a-blank-push)

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Send Blankpush
        api_instance.send_blankpush(device_id)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->send_blankpush: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_name**
> set_name(device_id, body=body)

Set Name

This endpoint sends an MDM command to set the device name.    **Request Body Parameters**: application/json     ---   `DeviceName` \\- `string`

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Set Name
        api_instance.set_name(device_id, body=body)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->set_name: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown**
> shutdown(device_id)

Shutdown

This endpoint sends an MDM command to shutdown a device.

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Shutdown
        api_instance.shutdown(device_id)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->shutdown: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_account**
> unlock_account(device_id, body=body)

Unlock Account

This endpoint sends an MDM command to unlock a user account that locked by the system because of too many failed password attempts. Available for macOS.   **Request Body Parameters**: application/json     ---    `UserName` \\- `string`

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Unlock Account
        api_instance.unlock_account(device_id, body=body)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->unlock_account: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory**
> update_inventory(device_id)

Update Inventory

This endpoint sends an MDM command to start a check\\-in for a device, initiating the daily MDM commands and MDM logic.

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
    api_instance = kandji_python_sdk.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Update Inventory
        api_instance.update_inventory(device_id)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->update_inventory: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

