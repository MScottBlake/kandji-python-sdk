# kandji.DeviceActionsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_passcode**](DeviceActionsApi.md#clear_passcode) | **POST** /api/v1/devices/{device_id}/action/clearpasscode | Clear Passcode
[**delete_device**](DeviceActionsApi.md#delete_device) | **DELETE** /api/v1/devices/{device_id} | Delete Device
[**delete_user**](DeviceActionsApi.md#delete_user) | **POST** /api/v1/devices/{device_id}/action/deleteuser | Delete User
[**erase_device**](DeviceActionsApi.md#erase_device) | **POST** /api/v1/devices/{device_id}/action/erase | Erase Device
[**get_device_commands**](DeviceActionsApi.md#get_device_commands) | **GET** /api/v1/devices/{device_id}/commands | Get Device Commands
[**lock_device**](DeviceActionsApi.md#lock_device) | **POST** /api/v1/devices/{device_id}/action/lock | Lock Device
[**perform_daily_checkin**](DeviceActionsApi.md#perform_daily_checkin) | **POST** /api/v1/devices/{device_id}/action/dailycheckin | Perform Daily Check-in
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
    api_instance = kandji.DeviceActionsApi(api_client)
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

<p>This endpoint deletes a device, which will remove the device record and unenroll the device from MDM.</p>
<p>For macOS and Windows devices, the agent will automatically uninstall on the next agent checkin.</p>

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
    api_instance = kandji.DeviceActionsApi(api_client)
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

<p>This endpoint sends an MDM command to delete a local user account on macOS and Shared iPad (Device Supervision via Automated Device Enrollment is required).</p>
<p><strong>Request Body Parameters</strong>: application/json</p>
<hr />
<p><code>DeleteAllUsers</code> - <code>boolean</code></p>
<p><code>ForceDeletion</code> - <code>boolean</code></p>
<p><code>UserName</code> - <code>string</code></p>

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
    api_instance = kandji.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = {"DeleteAllUsers":false,"ForceDeletion":false,"UserName":"testuser"} # str |  (optional)

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

<p>This endpoint sends an MDM command to erase a device.</p>
<p><strong>Request Body Parameters: application/json</strong></p>
<div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>
<thead>
<tr>
<th>Key</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>PIN</code></td>
<td><code>string</code></td>
<td>The six-character PIN for Find My. This value is available in macOS 10.8 and later.  <br />  <br />Note: This value will be ignored for iOS, iPadOS, and tvOS devices.</td>
</tr>
<tr>
<td><code>PreserveDataPlan</code></td>
<td><code>boolean</code></td>
<td>If true, preserve the data plan on an iPhone or iPad with eSIM functionality, if one exists. This value is available in iOS 11 and later.  <br />  <br />Default: true</td>
</tr>
<tr>
<td><code>DisallowProximitySetup</code></td>
<td><code>boolean</code></td>
<td>If true, disable Proximity Setup on the next reboot and skip the pane in Setup Assistant. This value is available in iOS 11 and later. Prior to iOS 14, don’t use this option with any other option.  <br />  <br />Default: false</td>
</tr>
<tr>
<td><code>ReturnToService</code></td>
<td><code>object</code></td>
<td>(iOS 17 and later and iPadOS 17 and later and with Shared iPad ) When sending the erase device command to mobile devices, use this key to enable Return to Service. Include an optional Wi-Fi payload ProfileId to allow the device to connect to a Wi-Fi network automatically after being erased. If a Wi-Fi ProfileId is not provided and the mobile device is not tethered to a Mac to share the network connection, the end-user will be required to select a Wi-Fi network to complete the setup.  <br />  <br />If sent to any macOS computer or to mobile devices on iOS 16 or iPadOS 16 and below, the RTS keys will be ignored, and only the erase device command will be issued to the device.</td>
</tr>
<tr>
<td>- <code>Enabled</code></td>
<td><code>boolean</code></td>
<td>(Required) If true, the device tries to re-enroll itself automatically after erasure. The user needs to deactivate all activation locks for this feature to work correctly.</td>
</tr>
<tr>
<td>- <code>ProfileId</code></td>
<td><code>string</code></td>
<td>Profile ID value associated with a Wi-Fi profile payload. This is required when the device doesn’t have ethernet access.</td>
</tr>
<tr>
<td><code>erase_mode</code></td>
<td><code>string</code></td>
<td>For Windows devices, the following modes are supported:  <br />  <br /><code>WIPE</code> - Equivalent to running Reset this PC &gt; Remove everything from the Settings app, with Clean Data set to No and Delete Files set to Yes.  <br />  <br /><code>WIPE_CLOUD</code> - Perform a cloud-based remote wipe on the device.  <br />  <br /><code>WIPE_PROTECTED</code> - Performs a remote wipe on the device and fully cleans the internal drive. In some device configurations, this command may leave the device unable to boot. This is similar to WIPE but cannot be circumvented by power cycling the device.</td>
</tr>
<tr>
<td><code>erase_flags</code></td>
<td><code>string</code></td>
<td>Optional erase options for Android devices, provided as a single comma separated list of the following strings:  <br />  <br /><code>WIPE_EXTERNAL_STORAGE</code> - Additionally wipe the device's external storage (such as SD cards).  <br />  <br /><code>WIPE_ESIMS</code> - For company-owned devices, this removes all eSIMs from the device when the device is wiped.  <br />  <br />Example value:  <br /><code>WIPE_EXTERNAL_STORAGE,WIPE_ESIMS</code></td>
</tr>
</tbody>
</table>
</div>

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
    api_instance = kandji.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = {"DisallowProximitySetup":false,"PIN":"123456","PreserveDataPlan":true,"ReturnToService":{"Enabled":false,"ProfileId":""}} # str |  (optional)

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
> DeviceActionsGetDeviceCommands200Response get_device_commands(device_id, limit, offset=offset)

Get Device Commands

<p>This endpoint sends a request to get information about the commands sent to a given Apple device.</p>
<h3 id=&quot;mdm-status-codes&quot;>MDM Status Codes</h3>
<ul>
<li><p>1 : Command is Pending</p>
</li>
<li><p>2 : Command is running</p>
</li>
<li><p>3 : Command completed</p>
</li>
<li><p>4 : Command failed</p>
</li>
<li><p>5 : Command received &quot;Not Now&quot; response</p>
</li>
</ul>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_actions_get_device_commands200_response import DeviceActionsGetDeviceCommands200Response
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
    api_instance = kandji.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = '300' # str | A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.
    offset = '' # str | Specify the starting record to return (optional)

    try:
        # Get Device Commands
        api_response = api_instance.get_device_commands(device_id, limit, offset=offset)
        print("The response of DeviceActionsApi->get_device_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->get_device_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **limit** | **str**| A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results. | 
 **offset** | **str**| Specify the starting record to return | [optional] 

### Return type

[**DeviceActionsGetDeviceCommands200Response**](DeviceActionsGetDeviceCommands200Response.md)

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
> DeviceActionsLockDevice200Response lock_device(device_id, body=body)

Lock Device

<p>This endpoint sends an MDM command to remotely lock an Apple or Android device.</p>
<p>For macOS clients, an unlock PIN will be created, and returned in the response.</p>
<blockquote>
<p><strong>Caution !!!</strong><br /><em>For a Mac with Apple silicon running a version of macOS before 11.5 will deactivate the Mac. To reactivate, the Mac requires a network connection and authentication by a Secure Token enabled local administrator.</em> </p>
</blockquote>
<p>Optionally, a JSON payload can be sent in the request to set a lock message and phone number on the target Mac.</p>
<p><strong>Note:</strong> For macOS, although the lock message is displayed on all types of Mac computers, the phone number is displayed only on a Mac with Apple silicon.</p>
<h4 id=&quot;response-properties&quot;>Response properties</h4>
<div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>
<thead>
<tr>
<th>Property</th>
<th>Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>PIN</td>
<td>Six digit pin code used to unlock a Mac.</td>
<td>String</td>
</tr>
</tbody>
</table>
</div>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.device_actions_lock_device200_response import DeviceActionsLockDevice200Response
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
    api_instance = kandji.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = {"Message":"This device is locked!","PhoneNumber":"1234567890"} # str |  (optional)

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

[**DeviceActionsLockDevice200Response**](DeviceActionsLockDevice200Response.md)

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

# **perform_daily_checkin**
> perform_daily_checkin(device_id)

Perform Daily Check-in

This endpoint runs the daily MDM commands and MDM logic for Apple devices and initiates a full daily CSP sync for Windows devices.

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
    api_instance = kandji.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Perform Daily Check-in
        api_instance.perform_daily_checkin(device_id)
    except Exception as e:
        print("Exception when calling DeviceActionsApi->perform_daily_checkin: %s\n" % e)
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

# **reinstall_agent**
> reinstall_agent(device_id)

Reinstall Agent

This endpoint sends an MDM command reinstall the Kandji Agent on macOS devices.

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
    api_instance = kandji.DeviceActionsApi(api_client)
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

<p>This endpoint sends an MDM command to control the Remote Management status on a Mac. This MDM command turns on (or turns off) Remote Management with <em>Observe</em> and <em>Control</em> permissions given to all users*.*</p>
<p><strong>Request Body Parameters</strong>: application/json</p>
<hr />
<p><code>EnableRemoteDesktop</code> - <code>boolean</code></p>

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
    api_instance = kandji.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = {"EnableRemoteDesktop":true} # str |  (optional)

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

This endpoint sends an MDM command to re-install the existing root MDM profile for a given Apple device. This command will not impact any existing configurations, apps, or profiles.

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
    api_instance = kandji.DeviceActionsApi(api_client)
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

<p>This endpoint sends an MDM command to remotely restart an iPhone, iPad, Apple TV, or Mac.</p>
<ul>
<li><p><code>RebuildKernelCache</code> - If <code>true</code>, the system rebuilds the kernel cache during a device restart. If <code>BootstrapTokenAllowedForAuthentication</code> is <code>true</code> inSecurityInfoResponse.SecurityInfo, the device requests the bootstrap token from MDM before executing this command. This value is available in macOS 11 and later. Default: false</p>
</li>
<li><p><code>NotifyUser</code> - If <code>true</code>, notifies the user to restart the device at their convenience. Forced restart if the device is at <code>loginwindow</code> with no logged-in users. The user can dismiss the notification and ignore the request. No further notifications display unless you resend the command. This value is available in macOS 11.3 and later. Default: false</p>
</li>
</ul>

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
    api_instance = kandji.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = {"NotifyUser":false,"RebuildKernelCache":false} # str |  (optional)

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

<p>This endpoint sends an MDM command to initiate a blank push for an Apple device.</p>
<p><a href=&quot;https://support.kandji.io/what-is-a-blank-push&quot;>Using the Blank Push command</a></p>

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
    api_instance = kandji.DeviceActionsApi(api_client)
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

<p>This endpoint sends an MDM command to set the device name for an Apple device.</p>
<p><strong>Request Body Parameters</strong>: application/json</p>
<hr />
<p><code>DeviceName</code> - <code>string</code></p>

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
    api_instance = kandji.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = {"DeviceName":"Test Mac Mini"} # str |  (optional)

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

This endpoint sends an MDM command to shutdown an iPhone, iPad, or Mac.

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
    api_instance = kandji.DeviceActionsApi(api_client)
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

<p>This endpoint sends an MDM command to unlock a user account that locked by the system because of too many failed password attempts. Available for Mac.</p>
<p><strong>Request Body Parameters</strong>: application/json</p>
<hr />
<p><code>UserName</code> - <code>string</code></p>

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
    api_instance = kandji.DeviceActionsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = {"UserName":"LocalUserToUnlock"} # str |  (optional)

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

<p>This endpoint runs the daily MDM commands and MDM logic for Apple devices.</p>
<p><strong>Note:</strong> The newer <code>dailycheckin</code> endpoint can be used instead and also supports Windows devices.</p>

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
    api_instance = kandji.DeviceActionsApi(api_client)
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

