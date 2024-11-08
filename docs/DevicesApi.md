# kandji_python_sdk.DevicesApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_lost_mode**](DevicesApi.md#cancel_lost_mode) | **DELETE** /api/v1/devices/{device_id}/details/lostmode | Cancel Lost Mode
[**clear_passcode**](DevicesApi.md#clear_passcode) | **POST** /api/v1/devices/{device_id}/action/clearpasscode | Clear Passcode
[**create_device_note**](DevicesApi.md#create_device_note) | **POST** /api/v1/devices/{device_id}/notes | Create Device Note
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /api/v1/devices/{device_id} | Delete Device
[**delete_device_note**](DevicesApi.md#delete_device_note) | **DELETE** /api/v1/devices/{device_id}/notes/{note_id} | Delete Device Note
[**delete_user**](DevicesApi.md#delete_user) | **POST** /api/v1/devices/{device_id}/action/deleteuser | Delete User
[**disable_lost_mode**](DevicesApi.md#disable_lost_mode) | **POST** /api/v1/devices/{device_id}/action/disablelostmode | Disable Lost Mode
[**enable_lost_mode**](DevicesApi.md#enable_lost_mode) | **POST** /api/v1/devices/{device_id}/action/enablelostmode | Enable Lost Mode
[**erase_device**](DevicesApi.md#erase_device) | **POST** /api/v1/devices/{device_id}/action/erase | Erase Device
[**get_activation_lock_bypass_code**](DevicesApi.md#get_activation_lock_bypass_code) | **GET** /api/v1/devices/{device_id}/secrets/bypasscode | Get Activation Lock Bypass Code
[**get_device**](DevicesApi.md#get_device) | **GET** /api/v1/devices/{device_id} | Get Device
[**get_device_activity**](DevicesApi.md#get_device_activity) | **GET** /api/v1/devices/{device_id}/activity | Get Device Activity
[**get_device_apps**](DevicesApi.md#get_device_apps) | **GET** /api/v1/devices/{device_id}/apps | Get Device Apps
[**get_device_commands**](DevicesApi.md#get_device_commands) | **GET** /api/v1/devices/{device_id}/commands | Get Device Commands
[**get_device_details**](DevicesApi.md#get_device_details) | **GET** /api/v1/devices/{device_id}/details | Get Device Details
[**get_device_library_items**](DevicesApi.md#get_device_library_items) | **GET** /api/v1/devices/{device_id}/library-items | Get Device Library Items
[**get_device_lost_mode_details**](DevicesApi.md#get_device_lost_mode_details) | **GET** /api/v1/devices/{device_id}/details/lostmode | Get Device Lost Mode details
[**get_device_notes**](DevicesApi.md#get_device_notes) | **GET** /api/v1/devices/{device_id}/notes | Get Device Notes
[**get_device_parameters**](DevicesApi.md#get_device_parameters) | **GET** /api/v1/devices/{device_id}/parameters | Get Device Parameters
[**get_device_status**](DevicesApi.md#get_device_status) | **GET** /api/v1/devices/{device_id}/status | Get Device Status
[**get_filevault_recovery_key**](DevicesApi.md#get_filevault_recovery_key) | **GET** /api/v1/devices/{device_id}/secrets/filevaultkey | Get FileVault Recovery Key
[**get_recovery_lock_password**](DevicesApi.md#get_recovery_lock_password) | **GET** /api/v1/devices/{device_id}/secrets/recoverypassword | Get Recovery Lock Password
[**get_unlock_pin**](DevicesApi.md#get_unlock_pin) | **GET** /api/v1/devices/{device_id}/secrets/unlockpin | Get Unlock Pin
[**list_devices**](DevicesApi.md#list_devices) | **GET** /api/v1/devices | List Devices
[**lock_device**](DevicesApi.md#lock_device) | **POST** /api/v1/devices/{device_id}/action/lock | Lock Device
[**play_lost_mode_sound**](DevicesApi.md#play_lost_mode_sound) | **POST** /api/v1/devices/{device_id}/action/playlostmodesound | Play Lost Mode Sound
[**reinstall_agent**](DevicesApi.md#reinstall_agent) | **POST** /api/v1/devices/{device_id}/action/reinstallagent | Reinstall Agent
[**remote_desktop**](DevicesApi.md#remote_desktop) | **POST** /api/v1/devices/{device_id}/action/remotedesktop | Remote Desktop
[**renew_mdm_profile**](DevicesApi.md#renew_mdm_profile) | **POST** /api/v1/devices/{device_id}/action/renewmdmprofile | Renew MDM Profile
[**restart_device**](DevicesApi.md#restart_device) | **POST** /api/v1/devices/{device_id}/action/restart | Restart Device
[**retrieve_device_note**](DevicesApi.md#retrieve_device_note) | **GET** /api/v1/devices/{device_id}/notes/{note_id} | Retrieve Device Note
[**send_blankpush**](DevicesApi.md#send_blankpush) | **POST** /api/v1/devices/{device_id}/action/blankpush | Send Blankpush
[**set_name**](DevicesApi.md#set_name) | **POST** /api/v1/devices/{device_id}/action/setname | Set Name
[**shutdown**](DevicesApi.md#shutdown) | **POST** /api/v1/devices/{device_id}/action/shutdown | Shutdown
[**unlock_account**](DevicesApi.md#unlock_account) | **POST** /api/v1/devices/{device_id}/action/unlockaccount | Unlock Account
[**update_device**](DevicesApi.md#update_device) | **PATCH** /api/v1/devices/{device_id} | Update Device
[**update_device_note**](DevicesApi.md#update_device_note) | **PATCH** /api/v1/devices/{device_id}/notes/{note_id} | Update Device Note
[**update_inventory**](DevicesApi.md#update_inventory) | **POST** /api/v1/devices/{device_id}/action/updateinventory | Update Inventory
[**update_location**](DevicesApi.md#update_location) | **POST** /api/v1/devices/{device_id}/action/updatelocation | Update Location


# **cancel_lost_mode**
> cancel_lost_mode(device_id)

Cancel Lost Mode

<p>This endpoint can be used to send a cancelation request if Lost Mode is in an error state for a given iOS or iPadOS device.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Cancel Lost Mode
        api_instance.cancel_lost_mode(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->cancel_lost_mode: %s\n" % e)
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

# **clear_passcode**
> clear_passcode(device_id)

Clear Passcode

<p>This endpoint sends an MDM command to clear a device passcode. Available for iPhone and iPad.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Clear Passcode
        api_instance.clear_passcode(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->clear_passcode: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_note**
> object create_device_note(device_id, body=body)

Create Device Note

<p>This request creates a note for the specified device ID.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Create Device Note
        api_response = api_instance.create_device_note(device_id, body=body)
        print("The response of DevicesApi->create_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_device_note: %s\n" % e)
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

# **delete_device**
> delete_device(device_id)

Delete Device

<p>This endpoint sends an MDM command to delete a device. This will remove the device record from Kandji and send a Remove Management command. For macOS devices, it will also send an uninstall command to the Kandji Agent at the next agent checkin.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Delete Device
        api_instance.delete_device(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_device: %s\n" % e)
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

# **delete_device_note**
> object delete_device_note(device_id, note_id)

Delete Device Note

<p>This request deletes a specified note (Note ID) for the specified Device ID.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    note_id = 'note_id_example' # str | 

    try:
        # Delete Device Note
        api_response = api_instance.delete_device_note(device_id, note_id)
        print("The response of DevicesApi->delete_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_device_note: %s\n" % e)
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

# **delete_user**
> delete_user(device_id, body=body)

Delete User

<p>This endpoint sends an MDM command to delete a local user account on macOS and Shared iPad (Device Supervision via Automated Device Enrollment is required).</p> <p><strong>Request Body Parameters</strong>: application/json</p> <hr /> <p><code>DeleteAllUsers</code> - <code>boolean</code></p> <p><code>ForceDeletion</code> - <code>boolean</code></p> <p><code>UserName</code> - <code>string</code></p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Delete User
        api_instance.delete_user(device_id, body=body)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_user: %s\n" % e)
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

# **disable_lost_mode**
> disable_lost_mode(device_id)

Disable Lost Mode

<p>This command will send a request to turn off lost mode on iOS and iPadOS.</p> <p>If the command is already pending, the message \"<em>Disable lost mode is already pending for this device.</em>\" will be in the response.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Disable Lost Mode
        api_instance.disable_lost_mode(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->disable_lost_mode: %s\n" % e)
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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Enable Lost Mode
        api_instance.enable_lost_mode(device_id, body=body)
    except Exception as e:
        print("Exception when calling DevicesApi->enable_lost_mode: %s\n" % e)
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

<p>This endpoint sends an MDM command to erase the device.</p> <p>iOS 4.0+, iPadOS 4.0+, macOS 10.7+, tvOS 10.2+</p> <p><strong>Request Body Parameters: application/json</strong></p> <div class=\"click-to-expand-wrapper is-table-wrapper\"><table> <thead> <tr> <th>Key</th> <th>Type</th> <th>Description</th> </tr> </thead> <tbody> <tr> <td><code>PIN</code></td> <td><code>string</code></td> <td>The six-character PIN for Find My. This value is available in macOS 10.8 and later.</td> </tr> <tr> <td><code>PreserveDataPlan</code></td> <td><code>boolean</code></td> <td>If true, preserve the data plan on an iPhone or iPad with eSIM functionality, if one exists. This value is available in iOS 11 and later.  <br />  <br />Default: true</td> </tr> <tr> <td><code>DisallowProximitySetup</code></td> <td><code>boolean</code></td> <td>If true, disable Proximity Setup on the next reboot and skip the pane in Setup Assistant. This value is available in iOS 11 and later. Prior to iOS 14, don’t use this option with any other option.  <br />  <br />Default: false</td> </tr> <tr> <td><code>ReturnToService</code></td> <td><code>object</code></td> <td>(iOS 17 and later and iPadOS 17 and later and with Shared iPad ) When sending the erase device command to mobile devices, use this key to enable Return to Service. Include an optional Wi-Fi payload ProfileId to allow the device to connect to a Wi-Fi network automatically after being erased. If a Wi-Fi ProfileId is not provided and the mobile device is not tethered to a Mac to share the network connection, the end-user will be required to select a Wi-Fi network to complete the setup.  <br />  <br />If sent to any macOS computer or to mobile devices on iOS 16 or iPadOS 16 and below, the RTS keys will be ignored, and only the erase device command will be issued to the device.</td> </tr> <tr> <td>- <code>Enabled</code></td> <td><code>boolean</code></td> <td>(Required) If true, the device tries to re-enroll itself automatically after erasure. The user needs to deactivate all activation locks for this feature to work correctly.</td> </tr> <tr> <td>- <code>ProfileId</code></td> <td><code>string</code></td> <td>Profile ID value associated with a Wi-Fi profile payload. This is required when the device doesn’t have ethernet access.</td> </tr> </tbody> </table> </div>

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Erase Device
        api_instance.erase_device(device_id, body=body)
    except Exception as e:
        print("Exception when calling DevicesApi->erase_device: %s\n" % e)
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

# **get_activation_lock_bypass_code**
> object get_activation_lock_bypass_code(device_id)

Get Activation Lock Bypass Code

<p>This request allows you to retrieve the Activation Lock Bypass code.</p> <p>user_based_albc is the user-based Activation Lock bypass code for when Activation Lock is enabled using an personal Apple ID and Find My.</p> <p>device_based_albc is the device-based Activation Lock bypass code for when Activation Lock is enabled by the MDM server.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>device_id</code> (path parameter): The unique identifier of the device.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Activation Lock Bypass Code
        api_response = api_instance.get_activation_lock_bypass_code(device_id)
        print("The response of DevicesApi->get_activation_lock_bypass_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_activation_lock_bypass_code: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> object get_device(device_id)

Get Device

<p>This request returns the high-level information for a specified Device ID.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device
        api_response = api_instance.get_device(device_id)
        print("The response of DevicesApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_activity**
> object get_device_activity(device_id, limit, offset=offset)

Get Device Activity

<p>This request returns the device activity for a specified Device ID.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = '300' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p> 
    offset = '0' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # Get Device Activity
        api_response = api_instance.get_device_activity(device_id, limit, offset=offset)
        print("The response of DevicesApi->get_device_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return&lt;/p&gt;  | [optional] 

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

# **get_device_apps**
> object get_device_apps(device_id)

Get Device Apps

<p>This request returns a list of all installed apps for a specified Device ID.</p> <p>For iPhone and iPad, the preinstalled Apple apps are not reported.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Apps
        api_response = api_instance.get_device_apps(device_id)
        print("The response of DevicesApi->get_device_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_apps: %s\n" % e)
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

# **get_device_commands**
> get_device_commands(device_id, limit, offset=offset)

Get Device Commands

<p>This endpoint sends a request to get information about the commands sent to a given device ID.</p> <h3 id=\"mdm-status-codes\">MDM Status Codes</h3> <ul> <li>1 : Command is Pending</li> <li>2 : Command is running</li> <li>3 : Command completed</li> <li>4 : Command failed</li> <li>5 : Command received \"Not Now\" response</li> </ul> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = '300' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p> 
    offset = 'offset_example' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # Get Device Commands
        api_instance.get_device_commands(device_id, limit, offset=offset)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return&lt;/p&gt;  | [optional] 

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

# **get_device_details**
> object get_device_details(device_id)

Get Device Details

<p>This request returns the device details for a specified Device ID.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Details
        api_response = api_instance.get_device_details(device_id)
        print("The response of DevicesApi->get_device_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_details: %s\n" % e)
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
**200** | OK |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_library_items**
> object get_device_library_items(device_id)

Get Device Library Items

<p>This request gets all library items and their statuses for a specified Device ID</p> <h4 id=\"possible-library-item-status-values\">Possible library item status values</h4> <div class=\"click-to-expand-wrapper is-table-wrapper\"><table> <thead> <tr> <th><strong>Value</strong></th> <th><strong>Type</strong></th> <th><strong>Additional Info</strong></th> </tr> </thead> <tbody> <tr> <td>AVAILABLE</td> <td>string</td> <td>Library item available in Self Service</td> </tr> <tr> <td>CACHED</td> <td>string</td> <td>Library item downloaded for install but not yet installed</td> </tr> <tr> <td>CHANGE_PENDING</td> <td>string</td> <td>Recovery Password library item has changes that have not yet been applied</td> </tr> <tr> <td>DOWNLOADING</td> <td>string</td> <td>Library item downloading</td> </tr> <tr> <td>ERROR</td> <td>string</td> <td>Audit failure</td> </tr> <tr> <td>EXCLUDED</td> <td>string</td> <td>Not in scope for assignment rule</td> </tr> <tr> <td>INCOMPATIBLE</td> <td>string</td> <td>Not compatible with device or OS version</td> </tr> <tr> <td>INSTALLING</td> <td>string</td> <td>Library item installing</td> </tr> <tr> <td>PASS</td> <td>string</td> <td>Device meets requirements</td> </tr> <tr> <td>PENDING</td> <td>string</td> <td>Waiting on device, not yet installed (All library items except for config profiles)</td> </tr> <tr> <td>failed</td> <td>string</td> <td>Configuration profile failed to install</td> </tr> <tr> <td>pending</td> <td>string</td> <td>Waiting on device, Configuration profile not yet installed</td> </tr> <tr> <td>success</td> <td>string</td> <td>Configuration profile installed</td> </tr> </tbody> </table> </div>

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Library Items
        api_response = api_instance.get_device_library_items(device_id)
        print("The response of DevicesApi->get_device_library_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_library_items: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_lost_mode_details**
> object get_device_lost_mode_details(device_id)

Get Device Lost Mode details

<p>This request returns the device lost mode details for a specified Device ID.</p> <p><strong>Note</strong>: Lost Mode is is only available for iOS and iPadOS. For more information, please see this <a href=\"https://support.kandji.io/a/solutions/articles/72000573873\">Kandji support artilcle</a>.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Lost Mode details
        api_response = api_instance.get_device_lost_mode_details(device_id)
        print("The response of DevicesApi->get_device_lost_mode_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_lost_mode_details: %s\n" % e)
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
**200** | OK |  * Content-Type -  <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_notes**
> object get_device_notes(device_id)

Get Device Notes

<p>This request gets all notes for the specified Device ID.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Notes
        api_response = api_instance.get_device_notes(device_id)
        print("The response of DevicesApi->get_device_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_notes: %s\n" % e)
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

# **get_device_parameters**
> object get_device_parameters(device_id)

Get Device Parameters

<p>This request returns the parameters and their statuses for a specified Device ID</p> <p>This endpoint is only applicable to macOS clients.</p> <p>The parameters will be returned as a list of IDs. These IDs can be correlated with the parameter names available here: <a href=\"https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations\">https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations</a></p> <p><strong>Possible parameter status values</strong></p> <div class=\"click-to-expand-wrapper is-table-wrapper\"><table> <thead> <tr> <th><strong>Value</strong></th> <th><strong>Type</strong></th> <th><strong>Additional Info</strong></th> </tr> </thead> <tbody> <tr> <td>ERROR</td> <td>string</td> <td>Audit failure</td> </tr> <tr> <td>INCOMPATIBLE</td> <td>string</td> <td>Not compatible with device or OS version</td> </tr> <tr> <td>PASS</td> <td>string</td> <td>Device meets requirements</td> </tr> <tr> <td>PENDING</td> <td>string</td> <td>Waiting on device. Not yet run.</td> </tr> <tr> <td>REMEDIATED</td> <td>string</td> <td>Parameter remediated</td> </tr> <tr> <td>WARNING</td> <td>string</td> <td>Muted alert</td> </tr> </tbody> </table> </div>

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Parameters
        api_response = api_instance.get_device_parameters(device_id)
        print("The response of DevicesApi->get_device_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_parameters: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_status**
> object get_device_status(device_id)

Get Device Status

<p>This request returns the full status (parameters and library items) for a specified Device ID.</p> <p>The parameters will be returned as a list of IDs. These IDs can be correlated with the parameter names available here: <a href=\"https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations\">https://github.com/kandji-inc/support/wiki/Devices-API---Parameter-Correlations</a></p> <h4 id=\"possible-status-values\">Possible status values</h4> <p><strong>Library items</strong></p> <div class=\"click-to-expand-wrapper is-table-wrapper\"><table> <thead> <tr> <th><strong>Value</strong></th> <th><strong>Type</strong></th> <th><strong>Additional Info</strong></th> </tr> </thead> <tbody> <tr> <td>AVAILABLE</td> <td>string</td> <td>Library item available in Self Service</td> </tr> <tr> <td>ERROR</td> <td>string</td> <td>Audit failure</td> </tr> <tr> <td>EXCLUDED</td> <td>string</td> <td>Not in scope for assignment rule</td> </tr> <tr> <td>INCOMPATIBLE</td> <td>string</td> <td>Not compatible with device or OS version</td> </tr> <tr> <td>PASS</td> <td>string</td> <td>Device meets requirements</td> </tr> <tr> <td>PENDING</td> <td>string</td> <td>Waiting on device, not yet installed (All library items except for config profiles)</td> </tr> <tr> <td>failed</td> <td>string</td> <td>Configuration profile failed to install</td> </tr> <tr> <td>pending</td> <td>string</td> <td>Waiting on device, Configuration profile not yet installed</td> </tr> <tr> <td>success</td> <td>string</td> <td>Configuration profile installed</td> </tr> </tbody> </table> </div><p><strong>Parameters</strong></p> <div class=\"click-to-expand-wrapper is-table-wrapper\"><table> <thead> <tr> <th><strong>Value</strong></th> <th><strong>Type</strong></th> <th><strong>Additional Info</strong></th> </tr> </thead> <tbody> <tr> <td>ERROR</td> <td>string</td> <td>Audit failure</td> </tr> <tr> <td>INCOMPATIBLE</td> <td>string</td> <td>Not compatible with device or OS version</td> </tr> <tr> <td>PASS</td> <td>string</td> <td>Device meets requirements</td> </tr> <tr> <td>PENDING</td> <td>string</td> <td>Waiting on device. Not yet run.</td> </tr> <tr> <td>REMEDIATED</td> <td>string</td> <td>Parameter remediated</td> </tr> <tr> <td>WARNING</td> <td>string</td> <td>Muted alert</td> </tr> </tbody> </table> </div>

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Status
        api_response = api_instance.get_device_status(device_id)
        print("The response of DevicesApi->get_device_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_status: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filevault_recovery_key**
> object get_filevault_recovery_key(device_id)

Get FileVault Recovery Key

<p>This request allows you to retrieve the FileVault Recovery key for a macOS device.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>device_id</code> (path parameter): The unique identifier of the device.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get FileVault Recovery Key
        api_response = api_instance.get_filevault_recovery_key(device_id)
        print("The response of DevicesApi->get_filevault_recovery_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_filevault_recovery_key: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_lock_password**
> object get_recovery_lock_password(device_id)

Get Recovery Lock Password

<p>This request returns the Recovery Lock password for a Mac with an Apple Silicon processor and the legacy EFI firmware password for a Mac with an Intel processor.</p> <p>For more details on setting and managing Recovery passwords, see this <a href=\"https://support.kandji.io/support/solutions/articles/72000560472-configure-the-recovery-password-library-item\">Kandji support article</a>.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>device_id</code> (path parameter): The unique identifier of the device.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Recovery Lock Password
        api_response = api_instance.get_recovery_lock_password(device_id)
        print("The response of DevicesApi->get_recovery_lock_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_recovery_lock_password: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unlock_pin**
> object get_unlock_pin(device_id)

Get Unlock Pin

<p>This request allows you to retrieve the device unlock pin for a macOS device.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>device_id</code> (path parameter): The unique identifier of the device.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Unlock Pin
        api_response = api_instance.get_unlock_pin(device_id)
        print("The response of DevicesApi->get_unlock_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_unlock_pin: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices**
> object list_devices(limit, asset_tag=asset_tag, blueprint_id=blueprint_id, device_id=device_id, device_name=device_name, filevault_enabled=filevault_enabled, mac_address=mac_address, model=model, ordering=ordering, os_version=os_version, platform=platform, serial_number=serial_number, tag_name=tag_name, tag_name_in=tag_name_in, tag_id=tag_id, tag_id_in=tag_id_in, user=user, user_email=user_email, user_id=user_id, user_name=user_name, offset=offset)

List Devices

<p>This request returns a list of devices in a Kandji tenant. Optionally. query parameters can be used to filter results.</p> <p>There is a hard upper limit of 300 results per request. To return addtional results pagination must be used. Pagination examples can be found in the Kandji support <a href=\"https://github.com/kandji-inc/support/tree/main/api-tools/code-examples\">GitHub</a>.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    limit = '300' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p> 
    asset_tag = '23245' # str |  (optional)
    blueprint_id = '91f97957-2353-4f86-a1ab-64d2b044a596' # str | <p>Return results \"containing\" the specified blueprint id</p>  (optional)
    device_id = '2cfeb3ac-3b5d-423e-bcff-e2676a3a32da' # str |  (optional)
    device_name = 'Johnny's MacBook Pro' # str |  (optional)
    filevault_enabled = 'true' # str | <p>Query for devices that either have FileVault on (true) or off (false). This parameter only applies to macOS. </p> <p>An empty list <code>[]</code> will be returned if no devices are found with the given parameter value.</p>  (optional)
    mac_address = '00:0c:29:05:43:b6' # str | <p>Search for a specific device by MAC address </p>  (optional)
    model = 'MacBook Air (M1, 2020)' # str | <p>Return model results \"containing\" the specified model string.</p>  (optional)
    ordering = 'device_id' # str | <p>The <code>ordering</code> parameter can be used to define how the device records are ordered in the response. Prepending a dash (-) to the parameter value will reverse the order of the returned results.</p> <p><code>?ordering=-serial_number</code> will order the response by serial_number in descending order.</p> <p><strong>Possible values</strong></p> <ul> <li><code>asset_tag</code></li> <li><code>blueprint_id</code></li> <li><code>device_id</code></li> <li><code>device_name</code></li> <li><code>last_check_in</code> - agent checkin</li> <li><code>model</code></li> <li><code>platform</code></li> <li><code>os_version</code></li> <li><code>serial_number</code></li> <li><code>user</code></li> </ul> <p>Additionally, multiple values can be combined in a comma separated list to further customize the ordering of the response.</p> <p><code>?ordering=serial_number,platform</code></p>  (optional)
    os_version = '13.2.3' # str | <p>Return all device records with the specified OS version</p>  (optional)
    platform = 'iPad' # str | <p>Return all records matching a specific platform. Possible values:<code>Mac</code>, <code>iPad</code>, <code>iPhone</code>, <code>AppleTV</code></p>  (optional)
    serial_number = 'VMC5qeJ5pDkp' # str | <p>Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned.</p>  (optional)
    tag_name = 'accuhive_01' # str | <p>Return results for given tag name. Case sensitive.</p>  (optional)
    tag_name_in = 'accuhive_01, accuhive_02' # str | <p>Return results for given tag names separate by commas. Case sensitive.</p>  (optional)
    tag_id = '' # str | <p>Search for a tag by its ID. Case sensitive.</p>  (optional)
    tag_id_in = '' # str | <p>Return results for given tag IDs separated by commas. Case sensitive.</p>  (optional)
    user = 'Art Vandelay' # str | <p>Return results \"containing\" the user name</p>  (optional)
    user_email = 'someUser@Kandji.io' # str | <p>Return results \"containing\" search on email address</p>  (optional)
    user_id = '1' # str | <p>\"exact\" match on kandji user ID number</p>  (optional)
    user_name = 'Vandelay' # str | <p>Return results \"containing\" the assigned user Display Name</p>  (optional)
    offset = '0' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # List Devices
        api_response = api_instance.list_devices(limit, asset_tag=asset_tag, blueprint_id=blueprint_id, device_id=device_id, device_name=device_name, filevault_enabled=filevault_enabled, mac_address=mac_address, model=model, ordering=ordering, os_version=os_version, platform=platform, serial_number=serial_number, tag_name=tag_name, tag_name_in=tag_name_in, tag_id=tag_id, tag_id_in=tag_id_in, user=user, user_email=user_email, user_id=user_id, user_name=user_name, offset=offset)
        print("The response of DevicesApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | 
 **asset_tag** | **str**|  | [optional] 
 **blueprint_id** | **str**| &lt;p&gt;Return results \&quot;containing\&quot; the specified blueprint id&lt;/p&gt;  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device_name** | **str**|  | [optional] 
 **filevault_enabled** | **str**| &lt;p&gt;Query for devices that either have FileVault on (true) or off (false). This parameter only applies to macOS. &lt;/p&gt; &lt;p&gt;An empty list &lt;code&gt;[]&lt;/code&gt; will be returned if no devices are found with the given parameter value.&lt;/p&gt;  | [optional] 
 **mac_address** | **str**| &lt;p&gt;Search for a specific device by MAC address &lt;/p&gt;  | [optional] 
 **model** | **str**| &lt;p&gt;Return model results \&quot;containing\&quot; the specified model string.&lt;/p&gt;  | [optional] 
 **ordering** | **str**| &lt;p&gt;The &lt;code&gt;ordering&lt;/code&gt; parameter can be used to define how the device records are ordered in the response. Prepending a dash (-) to the parameter value will reverse the order of the returned results.&lt;/p&gt; &lt;p&gt;&lt;code&gt;?ordering&#x3D;-serial_number&lt;/code&gt; will order the response by serial_number in descending order.&lt;/p&gt; &lt;p&gt;&lt;strong&gt;Possible values&lt;/strong&gt;&lt;/p&gt; &lt;ul&gt; &lt;li&gt;&lt;code&gt;asset_tag&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;blueprint_id&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;device_id&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;device_name&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;last_check_in&lt;/code&gt; - agent checkin&lt;/li&gt; &lt;li&gt;&lt;code&gt;model&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;platform&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;os_version&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;serial_number&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;user&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Additionally, multiple values can be combined in a comma separated list to further customize the ordering of the response.&lt;/p&gt; &lt;p&gt;&lt;code&gt;?ordering&#x3D;serial_number,platform&lt;/code&gt;&lt;/p&gt;  | [optional] 
 **os_version** | **str**| &lt;p&gt;Return all device records with the specified OS version&lt;/p&gt;  | [optional] 
 **platform** | **str**| &lt;p&gt;Return all records matching a specific platform. Possible values:&lt;code&gt;Mac&lt;/code&gt;, &lt;code&gt;iPad&lt;/code&gt;, &lt;code&gt;iPhone&lt;/code&gt;, &lt;code&gt;AppleTV&lt;/code&gt;&lt;/p&gt;  | [optional] 
 **serial_number** | **str**| &lt;p&gt;Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned.&lt;/p&gt;  | [optional] 
 **tag_name** | **str**| &lt;p&gt;Return results for given tag name. Case sensitive.&lt;/p&gt;  | [optional] 
 **tag_name_in** | **str**| &lt;p&gt;Return results for given tag names separate by commas. Case sensitive.&lt;/p&gt;  | [optional] 
 **tag_id** | **str**| &lt;p&gt;Search for a tag by its ID. Case sensitive.&lt;/p&gt;  | [optional] 
 **tag_id_in** | **str**| &lt;p&gt;Return results for given tag IDs separated by commas. Case sensitive.&lt;/p&gt;  | [optional] 
 **user** | **str**| &lt;p&gt;Return results \&quot;containing\&quot; the user name&lt;/p&gt;  | [optional] 
 **user_email** | **str**| &lt;p&gt;Return results \&quot;containing\&quot; search on email address&lt;/p&gt;  | [optional] 
 **user_id** | **str**| &lt;p&gt;\&quot;exact\&quot; match on kandji user ID number&lt;/p&gt;  | [optional] 
 **user_name** | **str**| &lt;p&gt;Return results \&quot;containing\&quot; the assigned user Display Name&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return&lt;/p&gt;  | [optional] 

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

# **lock_device**
> object lock_device(device_id, body=body)

Lock Device

<p>This endpoint sends an MDM command to remotely lock a device.</p> <p>For macOS clients, an unlock PIN will be created, and returned in the response.</p> <blockquote> <p><strong>Caution !!!</strong><br /><em>For a Mac with Apple silicon running a version of macOS before 11.5 will deactivate the Mac. To reactivate, the Mac requires a network connection and authentication by a Secure Token enabled local administrator.</em></p> </blockquote> <p>Optionally, a JSON payload can be sent in the request to set a lock message and phone number on the target device.</p> <p><strong>Note:</strong> For macOS, although the lock message is displayed on all types of Mac computers, the phone number is displayed only on a Mac with Apple silicon.</p> <h4 id=\"response-properties\">Response properties</h4> <div class=\"click-to-expand-wrapper is-table-wrapper\"><table> <thead> <tr> <th>Property</th> <th>Description</th> <th>Type</th> </tr> </thead> <tbody> <tr> <td>PIN</td> <td>Six digit pin code used to unlock a Mac.</td> <td>String</td> </tr> </tbody> </table> </div>

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Lock Device
        api_response = api_instance.lock_device(device_id, body=body)
        print("The response of DevicesApi->lock_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->lock_device: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |
**400** | Bad Request |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_lost_mode_sound**
> play_lost_mode_sound(device_id)

Play Lost Mode Sound

<p>This command will tell the target iOS or iPadOS device to play the lost mode sound.</p> <p><strong>Note</strong>: The Lost Mode sound will play for 2 minutes, even if the device is in silent mode. Anyone finding the device can silence the sound by pressing any of its side buttons.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Play Lost Mode Sound
        api_instance.play_lost_mode_sound(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->play_lost_mode_sound: %s\n" % e)
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

# **reinstall_agent**
> reinstall_agent(device_id)

Reinstall Agent

<p>This endpoint sends an MDM command reinstall the Kandji Agent. Available for macOS devices.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Reinstall Agent
        api_instance.reinstall_agent(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->reinstall_agent: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_desktop**
> remote_desktop(device_id, body=body)

Remote Desktop

<p>This endpoint sends an MDM command to control the Remote Management status on a Mac. This MDM command turns on (or turns off) Remote Management with <em>Observe</em> and <em>Control</em> permissions given to all users*.*</p> <p><strong>Request Body Parameters</strong>: application/json</p> <hr /> <p><code>EnableRemoteDesktop</code> - <code>boolean</code></p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Remote Desktop
        api_instance.remote_desktop(device_id, body=body)
    except Exception as e:
        print("Exception when calling DevicesApi->remote_desktop: %s\n" % e)
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

<p>This endpoint sends an MDM command to re-install the existing root MDM profile for a given device ID. This command will not impact any existing configurations, apps, or profiles.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Renew MDM Profile
        api_instance.renew_mdm_profile(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->renew_mdm_profile: %s\n" % e)
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

<p>This endpoint sends an MDM command to remotely restart a device.</p> <ul> <li><p><code>RebuildKernelCache</code> - If <code>true</code>, the system rebuilds the kernel cache during a device restart. If <code>BootstrapTokenAllowedForAuthentication</code> is <code>true</code> inSecurityInfoResponse.SecurityInfo, the device requests the bootstrap token from MDM before executing this command. This value is available in macOS 11 and later. Default: false</p> </li> <li><p><code>NotifyUser</code> - If <code>true</code>, notifies the user to restart the device at their convenience. Forced restart if the device is at <code>loginwindow</code> with no logged-in users. The user can dismiss the notification and ignore the request. No further notifications display unless you resend the command. This value is available in macOS 11.3 and later. Default: false</p> </li> </ul> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Restart Device
        api_instance.restart_device(device_id, body=body)
    except Exception as e:
        print("Exception when calling DevicesApi->restart_device: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_device_note**
> object retrieve_device_note(device_id, note_id)

Retrieve Device Note

<p>This request retrieves a specified note (Note ID) for the specified Device ID.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    note_id = 'note_id_example' # str | 

    try:
        # Retrieve Device Note
        api_response = api_instance.retrieve_device_note(device_id, note_id)
        print("The response of DevicesApi->retrieve_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->retrieve_device_note: %s\n" % e)
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

# **send_blankpush**
> send_blankpush(device_id)

Send Blankpush

<p>This endpoint sends an MDM command to initiate a blank push.</p> <p><a href=\"https://support.kandji.io/what-is-a-blank-push\">Using the Blank Push command</a></p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Send Blankpush
        api_instance.send_blankpush(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->send_blankpush: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_name**
> set_name(device_id, body=body)

Set Name

<p>This endpoint sends an MDM command to set the device name.</p> <p><strong>Request Body Parameters</strong>: application/json</p> <hr /> <p><code>DeviceName</code> - <code>string</code></p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Set Name
        api_instance.set_name(device_id, body=body)
    except Exception as e:
        print("Exception when calling DevicesApi->set_name: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown**
> shutdown(device_id)

Shutdown

<p>This endpoint sends an MDM command to shutdown a device.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Shutdown
        api_instance.shutdown(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->shutdown: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_account**
> unlock_account(device_id, body=body)

Unlock Account

<p>This endpoint sends an MDM command to unlock a user account that locked by the system because of too many failed password attempts. Available for macOS.</p> <p><strong>Request Body Parameters</strong>: application/json</p> <hr /> <p><code>UserName</code> - <code>string</code></p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Unlock Account
        api_instance.unlock_account(device_id, body=body)
    except Exception as e:
        print("Exception when calling DevicesApi->unlock_account: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> object update_device(device_id, body=body)

Update Device

<p>This request allows you to update device information, such as the assigned blueprint, user, Asset Tag, and Tags. It is not required to use all attributes in a given request. For example if you only want to update the assigned blueprint, you only need to pass the <code>blueprint_id</code> in the request payload.</p> <p><strong>NOTE</strong>: With the introduction of a UUID value for user ID in the <a href=\"https://api-docs.kandji.io/#b107eb0a-b586-414f-bc4c-3d2b304cfd5f\">Users API</a>, the Device PATCH endpoint will support both the depricated user ID integer value and the new user ID UUID value when updating the user assignment for a device. The ability to update user assignment via the integer ID value will be removed starting January 2025.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>device_id</code> (path parameter): The unique identifier of the device.</p> <h3 id=\"additional-information\">Additional information</h3> <p>User ID can be found using the <code>list users</code> API</p> <p>A Blueprint ID can be found using the <code>list blueprints</code> API or in the URL path while on a Blueprint overview page.</p> <p>For example, for this URL <a href=\"https://subdomain.kandji.io/blueprints/6391086e-85a1-4820-813c-f9c75025fff4\">https://subdomain.kandji.io/blueprints/6391086e-85a1-4820-813c-f9c75025fff4</a></p> <p>The Blueprint ID would be <code>6391086e-85a1-4820-813c-f9c75025fff4</code></p> <p>An example script that leverages this API can be found in the <a href=\"https://github.com/kandji-inc/support/tree/main/api-tools/update-device-record\">Kandji Support GitHub</a></p> <h4 id=\"clearing-the-device-asset-tag\">Clearing the device asset tag</h4> <p>To clear a device asset tag, set the <code>asset_tag</code> value to <code>null</code> in the JSON payload.</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code class=\"language-json\">{     \"asset_tag\": null }  </code></pre> <h4 id=\"clearing-the-assigned-user-attribute\">Clearing the assigned user attribute</h4> <p>To clear the assigned user for a given device, set the <code>user</code> value to <code>null</code> in the JSON payload.</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code class=\"language-json\">{     \"user\": null }  </code></pre> <h4 id=\"clearing-all-tags\">Clearing all tags</h4> <p>To clear the assigned tags for a given device, set the <code>tags</code> value to an empty list <code>[]</code> in the JSON payload.</p> <pre class=\"click-to-expand-wrapper is-snippet-wrapper\"><code class=\"language-json\">{     \"tags\": [] }  </code></pre> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update Device
        api_response = api_instance.update_device(device_id, body=body)
        print("The response of DevicesApi->update_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->update_device: %s\n" % e)
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
**200** | OK |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_note**
> object update_device_note(device_id, note_id, authorization, content_type, body=body)

Update Device Note

<p>This request patches a specified note (Note ID) for the specified Device ID.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    note_id = 'note_id_example' # str | 
    authorization = 'Bearer {{API TOKEN}}' # str | 
    content_type = 'application/json' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update Device Note
        api_response = api_instance.update_device_note(device_id, note_id, authorization, content_type, body=body)
        print("The response of DevicesApi->update_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->update_device_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **note_id** | **str**|  | 
 **authorization** | **str**|  | 
 **content_type** | **str**|  | 
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

# **update_inventory**
> update_inventory(device_id)

Update Inventory

<p>This endpoint sends an MDM command to start a check-in for a device, initiating the daily MDM commands and MDM logic.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Update Inventory
        api_instance.update_inventory(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->update_inventory: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location**
> update_location(device_id)

Update Location

<p>This endpoint sends an MDM command to update the location data on iOS and iPadOS.</p> 

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
    api_instance = kandji_python_sdk.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Update Location
        api_instance.update_location(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->update_location: %s\n" % e)
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

