# kandji_python_sdk.DefaultApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activation_lock**](DefaultApi.md#activation_lock) | **GET** /api/v1/prism/activation_lock | Activation lock
[**application_firewall**](DefaultApi.md#application_firewall) | **GET** /api/v1/prism/application_firewall | Application firewall
[**applications**](DefaultApi.md#applications) | **GET** /api/v1/prism/apps | Applications
[**assign_library_item**](DefaultApi.md#assign_library_item) | **POST** /api/v1/blueprints/{blueprint_id}/assign-library-item | Assign Library Item
[**cancel_lost_mode**](DefaultApi.md#cancel_lost_mode) | **DELETE** /api/v1/devices/{device_id}/details/lostmode | Cancel Lost Mode
[**certificates**](DefaultApi.md#certificates) | **GET** /api/v1/prism/certificates | Certificates
[**clear_passcode**](DefaultApi.md#clear_passcode) | **POST** /api/v1/devices/{device_id}/action/clearpasscode | Clear Passcode
[**count**](DefaultApi.md#count) | **GET** /api/v1/prism/count | Count
[**create_ade_integration**](DefaultApi.md#create_ade_integration) | **POST** /api/v1/integrations/apple/ade/ | Create ADE integration
[**create_blueprint**](DefaultApi.md#create_blueprint) | **POST** /api/v1/blueprints | Create Blueprint
[**create_custom_app**](DefaultApi.md#create_custom_app) | **POST** /api/v1/library/custom-apps | Create Custom App
[**create_custom_profile**](DefaultApi.md#create_custom_profile) | **POST** /api/v1/library/custom-profiles | Create Custom Profile
[**create_custom_script**](DefaultApi.md#create_custom_script) | **POST** /api/v1/library/custom-scripts | Create Custom Script
[**create_device_note**](DefaultApi.md#create_device_note) | **POST** /api/v1/devices/{device_id}/notes | Create Device Note
[**create_tag**](DefaultApi.md#create_tag) | **POST** /api/v1/tags | Create Tag
[**delete_ade_integration**](DefaultApi.md#delete_ade_integration) | **DELETE** /api/v1/integrations/apple/ade/{ade_token_id} | Delete ADE integration
[**delete_blueprint**](DefaultApi.md#delete_blueprint) | **DELETE** /api/v1/blueprints/{blueprint_id} | Delete Blueprint
[**delete_custom_app**](DefaultApi.md#delete_custom_app) | **DELETE** /api/v1/library/custom-apps/{library_item_id} | Delete Custom App
[**delete_custom_profile**](DefaultApi.md#delete_custom_profile) | **DELETE** /api/v1/library/custom-profiles/{library_item_id} | Delete Custom Profile
[**delete_custom_script**](DefaultApi.md#delete_custom_script) | **DELETE** /api/v1/library/custom-scripts/{library_item_id} | Delete Custom Script
[**delete_device**](DefaultApi.md#delete_device) | **DELETE** /api/v1/devices/{device_id} | Delete Device
[**delete_device_note**](DefaultApi.md#delete_device_note) | **DELETE** /api/v1/devices/{device_id}/notes/{note_id} | Delete Device Note
[**delete_tag**](DefaultApi.md#delete_tag) | **DELETE** /api/v1/tags/{tag_id} | Delete Tag
[**delete_user**](DefaultApi.md#delete_user) | **POST** /api/v1/devices/{device_id}/action/deleteuser | Delete User
[**desktop_and_screensaver**](DefaultApi.md#desktop_and_screensaver) | **GET** /api/v1/prism/desktop_and_screensaver | Desktop and Screensaver
[**device_information**](DefaultApi.md#device_information) | **GET** /api/v1/prism/device_information | Device information
[**disable_lost_mode**](DefaultApi.md#disable_lost_mode) | **POST** /api/v1/devices/{device_id}/action/disablelostmode | Disable Lost Mode
[**download_ade_public_key**](DefaultApi.md#download_ade_public_key) | **GET** /api/v1/integrations/apple/ade/public_key/ | Download ADE public key
[**enable_lost_mode**](DefaultApi.md#enable_lost_mode) | **POST** /api/v1/devices/{device_id}/action/enablelostmode | Enable Lost Mode
[**erase_device**](DefaultApi.md#erase_device) | **POST** /api/v1/devices/{device_id}/action/erase | Erase Device
[**filevault**](DefaultApi.md#filevault) | **GET** /api/v1/prism/filevault | FileVault
[**gatekeeper_and_xprotect**](DefaultApi.md#gatekeeper_and_xprotect) | **GET** /api/v1/prism/gatekeeper_and_xprotect | Gatekeeper and XProtect
[**get_activation_lock_bypass_code**](DefaultApi.md#get_activation_lock_bypass_code) | **GET** /api/v1/devices/{device_id}/secrets/bypasscode | Get Activation Lock Bypass Code
[**get_ade_device**](DefaultApi.md#get_ade_device) | **GET** /api/v1/integrations/apple/ade/devices/{device_id} | Get ADE device
[**get_ade_integration**](DefaultApi.md#get_ade_integration) | **GET** /api/v1/integrations/apple/ade/{ade_token_id} | Get ADE integration
[**get_blueprint**](DefaultApi.md#get_blueprint) | **GET** /api/v1/blueprints/{blueprint_id} | Get Blueprint
[**get_blueprint_templates**](DefaultApi.md#get_blueprint_templates) | **GET** /api/v1/blueprints/templates/ | Get Blueprint Templates
[**get_category_export**](DefaultApi.md#get_category_export) | **GET** /api/v1/prism/export/{export_id} | Get category export
[**get_custom_app**](DefaultApi.md#get_custom_app) | **GET** /api/v1/library/custom-apps/{library_item_id} | Get Custom App
[**get_custom_profile**](DefaultApi.md#get_custom_profile) | **GET** /api/v1/library/custom-profiles/{library_item_id} | Get Custom Profile
[**get_custom_script**](DefaultApi.md#get_custom_script) | **GET** /api/v1/library/custom-scripts/{library_item_id} | Get Custom Script
[**get_device**](DefaultApi.md#get_device) | **GET** /api/v1/devices/{device_id} | Get Device
[**get_device_activity**](DefaultApi.md#get_device_activity) | **GET** /api/v1/devices/{device_id}/activity | Get Device Activity
[**get_device_apps**](DefaultApi.md#get_device_apps) | **GET** /api/v1/devices/{device_id}/apps | Get Device Apps
[**get_device_commands**](DefaultApi.md#get_device_commands) | **GET** /api/v1/devices/{device_id}/commands | Get Device Commands
[**get_device_details**](DefaultApi.md#get_device_details) | **GET** /api/v1/devices/{device_id}/details | Get Device Details
[**get_device_library_items**](DefaultApi.md#get_device_library_items) | **GET** /api/v1/devices/{device_id}/library-items | Get Device Library Items
[**get_device_lost_mode_details**](DefaultApi.md#get_device_lost_mode_details) | **GET** /api/v1/devices/{device_id}/details/lostmode | Get Device Lost Mode details
[**get_device_notes**](DefaultApi.md#get_device_notes) | **GET** /api/v1/devices/{device_id}/notes | Get Device Notes
[**get_device_parameters**](DefaultApi.md#get_device_parameters) | **GET** /api/v1/devices/{device_id}/parameters | Get Device Parameters
[**get_device_status**](DefaultApi.md#get_device_status) | **GET** /api/v1/devices/{device_id}/status | Get Device Status
[**get_filevault_recovery_key**](DefaultApi.md#get_filevault_recovery_key) | **GET** /api/v1/devices/{device_id}/secrets/filevaultkey | Get FileVault Recovery Key
[**get_library_item_activity**](DefaultApi.md#get_library_item_activity) | **GET** /api/v1/library/library-items/{library_item_id}/activity | Get Library Item Activity
[**get_library_item_statuses**](DefaultApi.md#get_library_item_statuses) | **GET** /api/v1/library/library-items/{library_item_id}/status | Get Library Item Statuses
[**get_manual_enrollment_profile**](DefaultApi.md#get_manual_enrollment_profile) | **GET** /api/v1/blueprints/{blueprint_id}/ota-enrollment-profile | Get Manual Enrollment Profile
[**get_recovery_lock_password**](DefaultApi.md#get_recovery_lock_password) | **GET** /api/v1/devices/{device_id}/secrets/recoverypassword | Get Recovery Lock Password
[**get_tags**](DefaultApi.md#get_tags) | **GET** /api/v1/tags | Get Tags
[**get_threat_details**](DefaultApi.md#get_threat_details) | **GET** /api/v1/threat-details | Get Threat Details
[**get_unlock_pin**](DefaultApi.md#get_unlock_pin) | **GET** /api/v1/devices/{device_id}/secrets/unlockpin | Get Unlock Pin
[**get_user**](DefaultApi.md#get_user) | **GET** /api/v1/users/{user_id} | Get User
[**installed_profiles**](DefaultApi.md#installed_profiles) | **GET** /api/v1/prism/installed_profiles | Installed profiles
[**kernel_extensions**](DefaultApi.md#kernel_extensions) | **GET** /api/v1/prism/kernel_extensions | Kernel Extensions
[**launch_agents_and_daemons**](DefaultApi.md#launch_agents_and_daemons) | **GET** /api/v1/prism/launch_agents_and_daemons | Launch Agents and Daemons
[**licensing**](DefaultApi.md#licensing) | **GET** /api/v1/settings/licensing | Licensing
[**list_ade_devices**](DefaultApi.md#list_ade_devices) | **GET** /api/v1/integrations/apple/ade/devices | List ADE devices
[**list_ade_integrations**](DefaultApi.md#list_ade_integrations) | **GET** /api/v1/integrations/apple/ade | List ADE integrations
[**list_blueprints**](DefaultApi.md#list_blueprints) | **GET** /api/v1/blueprints | List Blueprints
[**list_custom_apps**](DefaultApi.md#list_custom_apps) | **GET** /api/v1/library/custom-apps | List Custom Apps
[**list_custom_profiles**](DefaultApi.md#list_custom_profiles) | **GET** /api/v1/library/custom-profiles | List Custom Profiles
[**list_custom_scripts**](DefaultApi.md#list_custom_scripts) | **GET** /api/v1/library/custom-scripts | List Custom Scripts
[**list_devices**](DefaultApi.md#list_devices) | **GET** /api/v1/devices | List Devices
[**list_devices_associated_to_ade_token**](DefaultApi.md#list_devices_associated_to_ade_token) | **GET** /api/v1/integrations/apple/ade/{ade_token_id}/devices | List devices associated to ADE token
[**list_library_items**](DefaultApi.md#list_library_items) | **GET** /api/v1/blueprints/{blueprint_id}/list-library-items | List Library Items
[**list_self_service_categories**](DefaultApi.md#list_self_service_categories) | **GET** /api/v1/self-service/categories | List Self Service Categories
[**list_users**](DefaultApi.md#list_users) | **GET** /api/v1/users | List Users
[**local_users**](DefaultApi.md#local_users) | **GET** /api/v1/prism/local_users | Local users
[**lock_device**](DefaultApi.md#lock_device) | **POST** /api/v1/devices/{device_id}/action/lock | Lock Device
[**play_lost_mode_sound**](DefaultApi.md#play_lost_mode_sound) | **POST** /api/v1/devices/{device_id}/action/playlostmodesound | Play Lost Mode Sound
[**reinstall_agent**](DefaultApi.md#reinstall_agent) | **POST** /api/v1/devices/{device_id}/action/reinstallagent | Reinstall Agent
[**remote_desktop**](DefaultApi.md#remote_desktop) | **POST** /api/v1/devices/{device_id}/action/remotedesktop | Remote Desktop
[**remove_library_item**](DefaultApi.md#remove_library_item) | **POST** /api/v1/blueprints/{blueprint_id}/remove-library-item | Remove Library Item
[**renew_ade_integration**](DefaultApi.md#renew_ade_integration) | **POST** /api/v1/integrations/apple/ade/{ade_token_id}/renew | Renew ADE integration
[**renew_mdm_profile**](DefaultApi.md#renew_mdm_profile) | **POST** /api/v1/devices/{device_id}/action/renewmdmprofile | Renew MDM Profile
[**request_category_export**](DefaultApi.md#request_category_export) | **POST** /api/v1/prism/export | Request category export
[**restart_device**](DefaultApi.md#restart_device) | **POST** /api/v1/devices/{device_id}/action/restart | Restart Device
[**retrieve_device_note**](DefaultApi.md#retrieve_device_note) | **GET** /api/v1/devices/{device_id}/notes/{note_id} | Retrieve Device Note
[**send_blankpush**](DefaultApi.md#send_blankpush) | **POST** /api/v1/devices/{device_id}/action/blankpush | Send Blankpush
[**set_name**](DefaultApi.md#set_name) | **POST** /api/v1/devices/{device_id}/action/setname | Set Name
[**shutdown**](DefaultApi.md#shutdown) | **POST** /api/v1/devices/{device_id}/action/shutdown | Shutdown
[**startup_settings**](DefaultApi.md#startup_settings) | **GET** /api/v1/prism/startup_settings | Startup settings
[**system_extensions**](DefaultApi.md#system_extensions) | **GET** /api/v1/prism/system_extensions | System Extensions
[**transparency_database**](DefaultApi.md#transparency_database) | **GET** /api/v1/prism/transparency_database | Transparency database
[**unlock_account**](DefaultApi.md#unlock_account) | **POST** /api/v1/devices/{device_id}/action/unlockaccount | Unlock Account
[**update_ade_device**](DefaultApi.md#update_ade_device) | **PATCH** /api/v1/integrations/apple/ade/devices/{device_id} | Update ADE device
[**update_ade_integration**](DefaultApi.md#update_ade_integration) | **PATCH** /api/v1/integrations/apple/ade/{ade_token_id} | Update ADE integration
[**update_blueprint**](DefaultApi.md#update_blueprint) | **PATCH** /api/v1/blueprints/{blueprint_id} | Update Blueprint
[**update_custom_app**](DefaultApi.md#update_custom_app) | **PATCH** /api/v1/library/custom-apps/{library_item_id} | Update Custom App
[**update_custom_profile**](DefaultApi.md#update_custom_profile) | **PATCH** /api/v1/library/custom-profiles/{library_item_id} | Update Custom Profile
[**update_custom_script**](DefaultApi.md#update_custom_script) | **PATCH** /api/v1/library/custom-scripts/{library_item_id} | Update Custom Script
[**update_device**](DefaultApi.md#update_device) | **PATCH** /api/v1/devices/{device_id} | Update Device
[**update_device_note**](DefaultApi.md#update_device_note) | **PATCH** /api/v1/devices/{device_id}/notes/{note_id} | Update Device Note
[**update_inventory**](DefaultApi.md#update_inventory) | **POST** /api/v1/devices/{device_id}/action/updateinventory | Update Inventory
[**update_location**](DefaultApi.md#update_location) | **POST** /api/v1/devices/{device_id}/action/updatelocation | Update Location
[**update_tag**](DefaultApi.md#update_tag) | **PATCH** /api/v1/tags/{tag_id} | Update Tag
[**upload_custom_app**](DefaultApi.md#upload_custom_app) | **POST** /api/v1/library/custom-apps/upload | Upload Custom App


# **activation_lock**
> activation_lock(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Activation lock

<p>Get activation lock attributes for devices.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Activation lock
        api_instance.activation_lock(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
    except Exception as e:
        print("Exception when calling DefaultApi->activation_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_firewall**
> object application_firewall(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Application firewall

<p>Get Application Firewall details for macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Application firewall
        api_response = api_instance.application_firewall(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->application_firewall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->application_firewall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications**
> object applications(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Applications

<p>Get the applications installed on macOS, iOS, iPadOS, and tvOS devices.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '{\"name\":{\"not_in\":[\"Okta Verify\"]},\"device__name\":{\"not_in\":[\"testuser’s MacBook Air\"]}}' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Applications
        api_response = api_instance.applications(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_library_item**
> object assign_library_item(blueprint_id, body=body)

Assign Library Item

<p>This endpoint allows assigning a library item to a specific blueprint (classic and maps). The response will include a list of library item IDs assigned to the blueprint.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>blueprint_id</code> (path parameter): The unique identifier of the blueprint.</p> <h3 id=\"request-body\">Request Body</h3> <ul> <li><p><code>library_item_id</code> (string, required)</p> </li> <li><p><code>assignment_node_id</code> (string, required for maps)</p> <ul> <li>Note: To find the assignment_node_id, view the map in a browser. Then, on your keyboard, press and hold the Option ⌥ key. Each node ID remains fixed for the lifespan of the node on the map.</li> </ul> </li> </ul> <h3 id=\"error-responses\">Error responses</h3> <div class=\"click-to-expand-wrapper is-table-wrapper\"><table> <thead> <tr> <th><strong>Code</strong></th> <th><strong>Body</strong></th> </tr> </thead> <tbody> <tr> <td>400 - Bad Request</td> <td>Bad Request</td> </tr> <tr> <td></td> <td>\"Library Item already exists on Blueprint\"</td> </tr> <tr> <td></td> <td>\"Library Item already exists in Assignment Node\"</td> </tr> <tr> <td></td> <td>\"assignment_node_id cannot be provided for Classic Blueprint\"</td> </tr> <tr> <td></td> <td>\"Must provide assignment_node_id for Assignment Map Blueprint\"</td> </tr> </tbody> </table> </div>

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Assign Library Item
        api_response = api_instance.assign_library_item(blueprint_id, body=body)
        print("The response of DefaultApi->assign_library_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->assign_library_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 
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
**200** | OK |  * Date -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Cancel Lost Mode
        api_instance.cancel_lost_mode(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_lost_mode: %s\n" % e)
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

# **certificates**
> object certificates(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Certificates

<p>Get certificate details.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Certificates
        api_response = api_instance.certificates(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Clear Passcode
        api_instance.clear_passcode(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->clear_passcode: %s\n" % e)
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

# **count**
> object count(category)

Count

<p>Get the total record count for the specified Prism category.</p> <p>If a category contains spaces substitute the spaces for underscores (\"_\") when using the API query.</p> <p>Example: <code>Device information</code> becomes <code>device_information</code>.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    category = 'apps' # str | <p>Return the count of records for the specified category.  If a category contains spaces substitute the spaces for underscores (\"_\") when using the API query.</p> <p>Examples: apps device_information kernel_extensions system_extensions</p> 

    try:
        # Count
        api_response = api_instance.count(category)
        print("The response of DefaultApi->count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| &lt;p&gt;Return the count of records for the specified category.  If a category contains spaces substitute the spaces for underscores (\&quot;_\&quot;) when using the API query.&lt;/p&gt; &lt;p&gt;Examples: apps device_information kernel_extensions system_extensions&lt;/p&gt;  | 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ade_integration**
> object create_ade_integration(blueprint_id, phone, email, file)

Create ADE integration

<p>This request will create a new ADE integration.</p> <p>The default <code>blueprint_id</code>, <code>phone</code> number, <code>email</code> address, and MDM server token <code>file</code> downloaded from ABM are required and must be sent in the request.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    phone = 'phone_example' # str | 
    email = 'email_example' # str | 
    file = None # bytearray | <p>This is the MDM server token file(.p7m) download from ABM. Once downloaded from ABM, the file can be uploaded via API.</p> 

    try:
        # Create ADE integration
        api_response = api_instance.create_ade_integration(blueprint_id, phone, email, file)
        print("The response of DefaultApi->create_ade_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_ade_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 
 **phone** | **str**|  | 
 **email** | **str**|  | 
 **file** | **bytearray**| &lt;p&gt;This is the MDM server token file(.p7m) download from ABM. Once downloaded from ABM, the file can be uploaded via API.&lt;/p&gt;  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_blueprint**
> object create_blueprint(name, enrollment_code_is_active, enrollment_code_code, source_type, source_id, type)

Create Blueprint

<p>This request creates a new empty Blueprint or a new Blueprint from a template. The keys <code>name</code> and <code>enrollment_code</code> <code>is_active</code> are required, and the blueprint name key must be unique from the existing blueprint names in the Kandji tenant.</p> <p>optionally, <code>type: map</code> can be used when creating a new Assignment Map blueprint.</p> <p>Note: If cloning an existing blueprint,`type` value and the type of sourced (`source.id`) blueprint must match and `source.type` value must be set to `blueprint`.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    name = 'name_example' # str | <p>(required) Set the name of the Blueprint. The name provided must be unique.</p> 
    enrollment_code_is_active = 'enrollment_code_is_active_example' # str | <p>(required) Enable or Disable the Blueprint for manual device enrollment from the enrollment portal</p> 
    enrollment_code_code = 'enrollment_code_code_example' # str | <p>Optionally, set the enrollment code of the Blueprint. This key is not required. If an enrollment code is not supplied in the payload body, it will be randomly generated. The enrollment code will be returned in the response and visible in the Web app.</p> 
    source_type = 'source_type_example' # str | <p>Set the source to create the blueprint from. Possible options: <code>template</code> and <code>blueprint</code>.</p> 
    source_id = 'source_id_example' # str | <p>Set either the source template ID, or the source Blueprint ID to clone an existing template or blueprint.</p> 
    type = 'type_example' # str | <p>Choose the type of blueprint to create. Options: <code>classic</code> or <code>map</code></p> 

    try:
        # Create Blueprint
        api_response = api_instance.create_blueprint(name, enrollment_code_is_active, enrollment_code_code, source_type, source_id, type)
        print("The response of DefaultApi->create_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| &lt;p&gt;(required) Set the name of the Blueprint. The name provided must be unique.&lt;/p&gt;  | 
 **enrollment_code_is_active** | **str**| &lt;p&gt;(required) Enable or Disable the Blueprint for manual device enrollment from the enrollment portal&lt;/p&gt;  | 
 **enrollment_code_code** | **str**| &lt;p&gt;Optionally, set the enrollment code of the Blueprint. This key is not required. If an enrollment code is not supplied in the payload body, it will be randomly generated. The enrollment code will be returned in the response and visible in the Web app.&lt;/p&gt;  | 
 **source_type** | **str**| &lt;p&gt;Set the source to create the blueprint from. Possible options: &lt;code&gt;template&lt;/code&gt; and &lt;code&gt;blueprint&lt;/code&gt;.&lt;/p&gt;  | 
 **source_id** | **str**| &lt;p&gt;Set either the source template ID, or the source Blueprint ID to clone an existing template or blueprint.&lt;/p&gt;  | 
 **type** | **str**| &lt;p&gt;Choose the type of blueprint to create. Options: &lt;code&gt;classic&lt;/code&gt; or &lt;code&gt;map&lt;/code&gt;&lt;/p&gt;  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Content-Type -  <br>  |
**400** | Bad Request |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_app**
> object create_custom_app(name, file_key, install_type, install_enforcement, show_in_self_service, self_service_category_id, self_service_recommended)

Create Custom App

<p>This request allows you to create a custom app in the Kandji library.</p> <p>Must have already generated a <code>file_key</code> via <code>Create custom app</code> endpoint and uploaded the file to S3 using a request similar to the <code>Upload to S3</code> example.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    name = 'name_example' # str | <p>(Required) The name for this Custom App</p> 
    file_key = 'file_key_example' # str | <p>(Required) The S3 key from the <code>Upload Custom App</code> endpont used to upload the custom app file.</p> 
    install_type = 'install_type_example' # str | <p>(Required) Options are package, zip, image</p> 
    install_enforcement = 'install_enforcement_example' # str | <p>(Required) Options are install_once, continuously_enforce, no_enforcement</p> 
    show_in_self_service = 'show_in_self_service_example' # str | <p>(Optional, default=false) Displays this app in Self Service</p> 
    self_service_category_id = 'self_service_category_id_example' # str | <p>(Required for show_in_self_service=true) Self Service Category (by ID) to display app in</p> 
    self_service_recommended = 'self_service_recommended_example' # str | <p>(Optional, default=false) Adds recommended flag to app in Self Service</p> 

    try:
        # Create Custom App
        api_response = api_instance.create_custom_app(name, file_key, install_type, install_enforcement, show_in_self_service, self_service_category_id, self_service_recommended)
        print("The response of DefaultApi->create_custom_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| &lt;p&gt;(Required) The name for this Custom App&lt;/p&gt;  | 
 **file_key** | **str**| &lt;p&gt;(Required) The S3 key from the &lt;code&gt;Upload Custom App&lt;/code&gt; endpont used to upload the custom app file.&lt;/p&gt;  | 
 **install_type** | **str**| &lt;p&gt;(Required) Options are package, zip, image&lt;/p&gt;  | 
 **install_enforcement** | **str**| &lt;p&gt;(Required) Options are install_once, continuously_enforce, no_enforcement&lt;/p&gt;  | 
 **show_in_self_service** | **str**| &lt;p&gt;(Optional, default&#x3D;false) Displays this app in Self Service&lt;/p&gt;  | 
 **self_service_category_id** | **str**| &lt;p&gt;(Required for show_in_self_service&#x3D;true) Self Service Category (by ID) to display app in&lt;/p&gt;  | 
 **self_service_recommended** | **str**| &lt;p&gt;(Optional, default&#x3D;false) Adds recommended flag to app in Self Service&lt;/p&gt;  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_profile**
> object create_custom_profile(name, file, active)

Create Custom Profile

<p>This request allows you to create a custom profile in the Kandji library.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    name = 'name_example' # str | <p>(Required) The profile name</p> 
    file = None # bytearray | <p>(Required) The path to the profile's .mobileconfig file</p> 
    active = 'active_example' # str | <p>(Optional, default=true) Whether this library item is active</p> 

    try:
        # Create Custom Profile
        api_response = api_instance.create_custom_profile(name, file, active)
        print("The response of DefaultApi->create_custom_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_custom_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| &lt;p&gt;(Required) The profile name&lt;/p&gt;  | 
 **file** | **bytearray**| &lt;p&gt;(Required) The path to the profile&#39;s .mobileconfig file&lt;/p&gt;  | 
 **active** | **str**| &lt;p&gt;(Optional, default&#x3D;true) Whether this library item is active&lt;/p&gt;  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_script**
> object create_custom_script(body=body)

Create Custom Script

<p>This request allows you to create a custom script in the Kandji library.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Create Custom Script
        api_response = api_instance.create_custom_script(body=body)
        print("The response of DefaultApi->create_custom_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_custom_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Create Device Note
        api_response = api_instance.create_device_note(device_id, body=body)
        print("The response of DefaultApi->create_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_device_note: %s\n" % e)
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

# **create_tag**
> object create_tag(body=body)

Create Tag

<p>Create a tag. Can only create one tag per request.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Create Tag
        api_response = api_instance.create_tag(body=body)
        print("The response of DefaultApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** | Created |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ade_integration**
> delete_ade_integration(ade_token_id)

Delete ADE integration

<h1 id=\"warning\"><strong>WARNING!</strong></h1> <p>This is a HIGHLY destructive action.</p> <p>Deleting an ADE token will unassign the associated device records from Kandji. For currently enrolled devices that were assigned to Kandji via the delete ADE integration will not be impacted until they are wiped and reprovisioned. This action is essentially the same as removing an ADE token from MDM and then adding it back.</p> <p>If applicable, be sure to reassign the device records in ABM.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 

    try:
        # Delete ADE integration
        api_instance.delete_ade_integration(ade_token_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_ade_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ade_token_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * Date -  <br>  * Connection -  <br>  * Set-Cookie -  <br>  * Allow -  <br>  * Content-Security-Policy -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Xss-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blueprint**
> delete_blueprint(blueprint_id)

Delete Blueprint

<h1 id=\"warning\"><strong>WARNING!</strong></h1> <p>This is a HIGHLY destructive action.</p> <p>Deleting a Blueprint will un-manage ALL devices assigned to the Blueprint.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>blueprint_id</code> (path parameter): The unique identifier of the blueprint.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 

    try:
        # Delete Blueprint
        api_instance.delete_blueprint(blueprint_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 

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

# **delete_custom_app**
> delete_custom_app(library_item_id)

Delete Custom App

<p>NOTICE: This is permanent so be careful.</p> <p>This endpoint sends a request to delete a specific custom app from the Kandji library.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Delete Custom App
        api_instance.delete_custom_app(library_item_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * Date -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |
**404** | Not Found |  * Connection -  <br>  * Content-Type -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_profile**
> delete_custom_profile(library_item_id)

Delete Custom Profile

<p>NOTICE: This is permanent so be careful.</p> <p>This endpoint sends a request to delete a specific custom profile from the Kandji library.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Delete Custom Profile
        api_instance.delete_custom_profile(library_item_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_custom_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * Date -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |
**404** | Not Found |  * Connection -  <br>  * Content-Type -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_script**
> delete_custom_script(library_item_id)

Delete Custom Script

<p>NOTICE: This is permanent so be careful.</p> <p>This endpoint sends a request to delete a specific custom scripts from the Kandji library.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Delete Custom Script
        api_instance.delete_custom_script(library_item_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_custom_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * Date -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |
**404** | Not Found |  * Connection -  <br>  * Content-Type -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Delete Device
        api_instance.delete_device(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_device: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    note_id = 'note_id_example' # str | 

    try:
        # Delete Device Note
        api_response = api_instance.delete_device_note(device_id, note_id)
        print("The response of DefaultApi->delete_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_device_note: %s\n" % e)
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

# **delete_tag**
> delete_tag(tag_id)

Delete Tag

<p>Delete a tag.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>tag_id</code> (path parameter): The unique identifier of the tag.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    tag_id = 'tag_id_example' # str | 

    try:
        # Delete Tag
        api_instance.delete_tag(tag_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**|  | 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Delete User
        api_instance.delete_user(device_id, body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
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

# **desktop_and_screensaver**
> object desktop_and_screensaver(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Desktop and Screensaver

<p>Get Desktop and Screensaver details for macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Desktop and Screensaver
        api_response = api_instance.desktop_and_screensaver(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->desktop_and_screensaver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->desktop_and_screensaver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_information**
> object device_information(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset, body=body)

Device information

<p>Get attributes about devices.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = '14afabf2-7599-47af-a942-bf7f0b8fedf8' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '{\"device__name\":{\"in\":[\"testusers's MacBook Air\"]},\"updated_at\":{\"gte\":\"2023-09-03T04:00:00.000Z\",\"lte\":\"2023-09-04T04:00:00.000Z\"}}' # str | <p>JSON schema object containing one or more key value pairs.</p> <p>Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = 'serial_number' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return</p>  (optional)
    body = 'body_example' # str |  (optional)

    try:
        # Device information
        api_response = api_instance.device_information(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset, body=body)
        print("The response of DefaultApi->device_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->device_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs.&lt;/p&gt; &lt;p&gt;Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return&lt;/p&gt;  | [optional] 
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Disable Lost Mode
        api_instance.disable_lost_mode(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->disable_lost_mode: %s\n" % e)
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

# **download_ade_public_key**
> str download_ade_public_key()

Download ADE public key

<p>This request returns the public key used to create an MDM server connection in Apple Business Manager.</p> <p>The encoded information needs to be saved to a file with the <code>.pem</code> format and then uploaded to ABM.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)

    try:
        # Download ADE public key
        api_response = api_instance.download_ade_public_key()
        print("The response of DefaultApi->download_ade_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_ade_public_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-x509-ca-cert

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Set-Cookie -  <br>  * Allow -  <br>  * Content-Security-Policy -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Xss-Protection -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Enable Lost Mode
        api_instance.enable_lost_mode(device_id, body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->enable_lost_mode: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Erase Device
        api_instance.erase_device(device_id, body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->erase_device: %s\n" % e)
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

# **filevault**
> object filevault(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

FileVault

<p>Get FileVault information for macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # FileVault
        api_response = api_instance.filevault(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->filevault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->filevault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gatekeeper_and_xprotect**
> object gatekeeper_and_xprotect(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Gatekeeper and XProtect

<p>Get Gatekeeper and XProtect attributes for macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac' # str | <p>Results are limited to Mac only as Gatekeeper and XProtect are not applicable for other platfroms.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # Gatekeeper and XProtect
        api_response = api_instance.gatekeeper_and_xprotect(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->gatekeeper_and_xprotect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->gatekeeper_and_xprotect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Results are limited to Mac only as Gatekeeper and XProtect are not applicable for other platfroms.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Activation Lock Bypass Code
        api_response = api_instance.get_activation_lock_bypass_code(device_id)
        print("The response of DefaultApi->get_activation_lock_bypass_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_activation_lock_bypass_code: %s\n" % e)
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

# **get_ade_device**
> object get_ade_device(device_id)

Get ADE device

<p>Get information about a specific Automated Device Enrollment device.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get ADE device
        api_response = api_instance.get_ade_device(device_id)
        print("The response of DefaultApi->get_ade_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ade_device: %s\n" % e)
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

# **get_ade_integration**
> get_ade_integration(ade_token_id)

Get ADE integration

<p>This request returns a specific ADE integration based on the <code>ade_token_id</code> passed.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 

    try:
        # Get ADE integration
        api_instance.get_ade_integration(ade_token_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ade_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ade_token_id** | **str**|  | 

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

# **get_blueprint**
> get_blueprint(blueprint_id)

Get Blueprint

<p>This request returns information about a specific blueprint based on blueprint ID.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>blueprint_id</code> (path parameter): The unique identifier of the blueprint.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 

    try:
        # Get Blueprint
        api_instance.get_blueprint(blueprint_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blueprint_templates**
> get_blueprint_templates(limit=limit, offset=offset)

Get Blueprint Templates



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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    limit = '100' # str | <p>Number of results to return per page.</p>  (optional)
    offset = '400' # str | <p>The initial index from which to return the results.</p>  (optional)

    try:
        # Get Blueprint Templates
        api_instance.get_blueprint_templates(limit=limit, offset=offset)
    except Exception as e:
        print("Exception when calling DefaultApi->get_blueprint_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| &lt;p&gt;Number of results to return per page.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;The initial index from which to return the results.&lt;/p&gt;  | [optional] 

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

# **get_category_export**
> object get_category_export(export_id)

Get category export

<p>Get an export request's status. To download the export, use the <code>signed_url</code>. This will download a CSV file containing the exported category information.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p>export_id (path parameter): The unique identifier of the the export job.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    export_id = 'export_id_example' # str | 

    try:
        # Get category export
        api_response = api_instance.get_category_export(export_id)
        print("The response of DefaultApi->get_category_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_category_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**|  | 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_app**
> object get_custom_app(library_item_id)

Get Custom App

<p>This endpoint retrieves details about a specific custom app from the Kandji library.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Get Custom App
        api_response = api_instance.get_custom_app(library_item_id)
        print("The response of DefaultApi->get_custom_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 

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

# **get_custom_profile**
> object get_custom_profile(library_item_id)

Get Custom Profile

<p>This endpoint retrieves details about a specific custom profile from the Kandji library.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Get Custom Profile
        api_response = api_instance.get_custom_profile(library_item_id)
        print("The response of DefaultApi->get_custom_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_custom_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 

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

# **get_custom_script**
> object get_custom_script(library_item_id)

Get Custom Script

<p>This endpoint retrieves details about a specific custom script from the Kandji library.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Get Custom Script
        api_response = api_instance.get_custom_script(library_item_id)
        print("The response of DefaultApi->get_custom_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_custom_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device
        api_response = api_instance.get_device(device_id)
        print("The response of DefaultApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = '300' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p> 
    offset = '0' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # Get Device Activity
        api_response = api_instance.get_device_activity(device_id, limit, offset=offset)
        print("The response of DefaultApi->get_device_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device_activity: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Apps
        api_response = api_instance.get_device_apps(device_id)
        print("The response of DefaultApi->get_device_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device_apps: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = '300' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p> 
    offset = 'offset_example' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # Get Device Commands
        api_instance.get_device_commands(device_id, limit, offset=offset)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device_commands: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Details
        api_response = api_instance.get_device_details(device_id)
        print("The response of DefaultApi->get_device_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device_details: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Library Items
        api_response = api_instance.get_device_library_items(device_id)
        print("The response of DefaultApi->get_device_library_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device_library_items: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Lost Mode details
        api_response = api_instance.get_device_lost_mode_details(device_id)
        print("The response of DefaultApi->get_device_lost_mode_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device_lost_mode_details: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Notes
        api_response = api_instance.get_device_notes(device_id)
        print("The response of DefaultApi->get_device_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device_notes: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Parameters
        api_response = api_instance.get_device_parameters(device_id)
        print("The response of DefaultApi->get_device_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device_parameters: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device Status
        api_response = api_instance.get_device_status(device_id)
        print("The response of DefaultApi->get_device_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_device_status: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get FileVault Recovery Key
        api_response = api_instance.get_filevault_recovery_key(device_id)
        print("The response of DefaultApi->get_filevault_recovery_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_filevault_recovery_key: %s\n" % e)
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

# **get_library_item_activity**
> object get_library_item_activity(library_item_id, activity_type=activity_type, user_id=user_id, user_email=user_email, limit=limit, offset=offset)

Get Library Item Activity

<p>This endpoint retrieves the activity related to a specific library item. Activity is listed from newest to oldest.</p> <p>To see a delta of the activity events between now and the last request, you can store the newest entry from the previous request and then look for that entry in the next request. Any entry post that will be the delta.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    activity_type = 'library_item_assignment_changed' # str | <p>Filter actions by this activity type. Choices are: library_item_created, library_item_edited, library_item_deleted, library_item_duplicated, library_item_assignment_changed</p>  (optional)
    user_id = '{user uuid}' # str | <p>Filter actions by this user (id)</p>  (optional)
    user_email = 'me@example.com' # str | <p>Filter actions by this user (email)</p>  (optional)
    limit = '10' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '100' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # Get Library Item Activity
        api_response = api_instance.get_library_item_activity(library_item_id, activity_type=activity_type, user_id=user_id, user_email=user_email, limit=limit, offset=offset)
        print("The response of DefaultApi->get_library_item_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_library_item_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 
 **activity_type** | **str**| &lt;p&gt;Filter actions by this activity type. Choices are: library_item_created, library_item_edited, library_item_deleted, library_item_duplicated, library_item_assignment_changed&lt;/p&gt;  | [optional] 
 **user_id** | **str**| &lt;p&gt;Filter actions by this user (id)&lt;/p&gt;  | [optional] 
 **user_email** | **str**| &lt;p&gt;Filter actions by this user (email)&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_item_statuses**
> object get_library_item_statuses(library_item_id, computer_id=computer_id, limit=limit, offset=offset)

Get Library Item Statuses

<p>This endpoint retrieves the statuses related to a specific library item.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    computer_id = '{device_id}' # str | <p>Query for the status of one device.</p>  (optional)
    limit = '300' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # Get Library Item Statuses
        api_response = api_instance.get_library_item_statuses(library_item_id, computer_id=computer_id, limit=limit, offset=offset)
        print("The response of DefaultApi->get_library_item_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_library_item_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 
 **computer_id** | **str**| &lt;p&gt;Query for the status of one device.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_enrollment_profile**
> str get_manual_enrollment_profile(blueprint_id, sso=sso)

Get Manual Enrollment Profile

<p>This request returns the manual enrollment profile (.mobileconfig file) for a specified Blueprint.</p> <p>This request will return the enrollment profile even if \"Require Authentication\" is configured for the Blueprint in Manual Enrollment.</p> <p>The enrollment profile will be returned in raw form with response headers:</p> <ul> <li><p><code>Content-Type</code> = <code>application/x-apple-aspen-config</code></p> </li> <li><p><code>Content-Disposition</code> = <code>attachment;filename=kandji-enroll.mobileconfig</code></p> </li> </ul> <p>An optional query parameter <code>sso=true</code> can be used to return a URL for SSO authentication instead. If this query parameter is used for a Blueprint that does not require authentication, then the enrollment profile will be returned.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>blueprint_id</code> (path parameter): The unique identifier of the blueprint.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    sso = 'true' # str | <p>Use the <code>sso</code> query parameter, set to <code>true</code>, to return a URL instead of the manual enrollment profile. This parameter should only be used for blueprints in which \"Require Authentication\" is configured for Manual Enrollment. The returned URL must be used to authenticate via SSO to receive an enrollment profile. </p>  (optional)

    try:
        # Get Manual Enrollment Profile
        api_response = api_instance.get_manual_enrollment_profile(blueprint_id, sso=sso)
        print("The response of DefaultApi->get_manual_enrollment_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_manual_enrollment_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 
 **sso** | **str**| &lt;p&gt;Use the &lt;code&gt;sso&lt;/code&gt; query parameter, set to &lt;code&gt;true&lt;/code&gt;, to return a URL instead of the manual enrollment profile. This parameter should only be used for blueprints in which \&quot;Require Authentication\&quot; is configured for Manual Enrollment. The returned URL must be used to authenticate via SSO to receive an enrollment profile. &lt;/p&gt;  | [optional] 

### Return type

**str**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-apple-aspen-config

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Connection -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Disposition -  <br>  * Content-Language -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Recovery Lock Password
        api_response = api_instance.get_recovery_lock_password(device_id)
        print("The response of DefaultApi->get_recovery_lock_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_recovery_lock_password: %s\n" % e)
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

# **get_tags**
> object get_tags(search)

Get Tags

<p>Return configured tags.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    search = 'accuhive' # str | <p>Return resultes containing a given tag search string.</p> 

    try:
        # Get Tags
        api_response = api_instance.get_tags(search)
        print("The response of DefaultApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| &lt;p&gt;Return resultes containing a given tag search string.&lt;/p&gt;  | 

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

# **get_threat_details**
> object get_threat_details(classification=classification, date_range=date_range, device_id=device_id, status=status, sort_by=sort_by, term=term, limit=limit, offset=offset)

Get Threat Details

<p>Get threat details.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    classification = 'malware' # str | <p>Return all records matching a specified classification. The following classification options are available: <code>malware</code> and <code>pup</code>. Leave this parameter empty to return all classification types.</p>  (optional)
    date_range = '7' # str | <p>Return all records within a specified number of days. Any positive number of days may be specified. Examples: <code>7</code>, <code>30</code>, <code>60</code>, <code>90</code>, <code>180</code>, or <code>365</code>.</p>  (optional)
    device_id = '15fcec08-xxxx-xxxx-xxxx-7c2f950910eb' # str |  (optional)
    status = 'quarantined' # str | <p>Return all records matching a specified status. The following status options are available: <code>quarantined</code>, <code>not_quarantined</code>, or <code>released</code>. Leave this parameter empty to return all status types.</p>  (optional)
    sort_by = 'status' # str | <p>Results can be sorted with the following options: </p> <ul> <li>threat_name</li> <li>classification</li> <li>device_name</li> <li>process_name</li> <li>process_owner</li> <li>detection_date</li> <li>status</li> </ul> <p>Prepending a dash (-) to the parameter value will reverse the order of the returned results.</p> <p><code>?sort_by=-device_name</code> will order the response by device_name in descending order.</p>  (optional)
    term = 'Chrome' # str | <p>Search term to filter threat results.</p> <p>The response will include anything matching the following fields: <code>device_name</code>, <code>file_hash</code>, and <code>file_path</code>.</p> <p>So if you search for <code>bad file</code>, the results will include anywhere <code>bad file</code> exists in the three fields above.</p>  (optional)
    limit = '1000' # str | <p>A hard upper <code>limit</code> is set at 1000 records returned per request. If more records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. </p> <p>Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '1' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # Get Threat Details
        api_response = api_instance.get_threat_details(classification=classification, date_range=date_range, device_id=device_id, status=status, sort_by=sort_by, term=term, limit=limit, offset=offset)
        print("The response of DefaultApi->get_threat_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_threat_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification** | **str**| &lt;p&gt;Return all records matching a specified classification. The following classification options are available: &lt;code&gt;malware&lt;/code&gt; and &lt;code&gt;pup&lt;/code&gt;. Leave this parameter empty to return all classification types.&lt;/p&gt;  | [optional] 
 **date_range** | **str**| &lt;p&gt;Return all records within a specified number of days. Any positive number of days may be specified. Examples: &lt;code&gt;7&lt;/code&gt;, &lt;code&gt;30&lt;/code&gt;, &lt;code&gt;60&lt;/code&gt;, &lt;code&gt;90&lt;/code&gt;, &lt;code&gt;180&lt;/code&gt;, or &lt;code&gt;365&lt;/code&gt;.&lt;/p&gt;  | [optional] 
 **device_id** | **str**|  | [optional] 
 **status** | **str**| &lt;p&gt;Return all records matching a specified status. The following status options are available: &lt;code&gt;quarantined&lt;/code&gt;, &lt;code&gt;not_quarantined&lt;/code&gt;, or &lt;code&gt;released&lt;/code&gt;. Leave this parameter empty to return all status types.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Results can be sorted with the following options: &lt;/p&gt; &lt;ul&gt; &lt;li&gt;threat_name&lt;/li&gt; &lt;li&gt;classification&lt;/li&gt; &lt;li&gt;device_name&lt;/li&gt; &lt;li&gt;process_name&lt;/li&gt; &lt;li&gt;process_owner&lt;/li&gt; &lt;li&gt;detection_date&lt;/li&gt; &lt;li&gt;status&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Prepending a dash (-) to the parameter value will reverse the order of the returned results.&lt;/p&gt; &lt;p&gt;&lt;code&gt;?sort_by&#x3D;-device_name&lt;/code&gt; will order the response by device_name in descending order.&lt;/p&gt;  | [optional] 
 **term** | **str**| &lt;p&gt;Search term to filter threat results.&lt;/p&gt; &lt;p&gt;The response will include anything matching the following fields: &lt;code&gt;device_name&lt;/code&gt;, &lt;code&gt;file_hash&lt;/code&gt;, and &lt;code&gt;file_path&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;So if you search for &lt;code&gt;bad file&lt;/code&gt;, the results will include anywhere &lt;code&gt;bad file&lt;/code&gt; exists in the three fields above.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 1000 records returned per request. If more records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. &lt;/p&gt; &lt;p&gt;Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Unlock Pin
        api_response = api_instance.get_unlock_pin(device_id)
        print("The response of DefaultApi->get_unlock_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_unlock_pin: %s\n" % e)
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

# **get_user**
> object get_user(user_id)

Get User

<p>This endpoint makes a request to retrieve a specified user directory integration user by id.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p>user_id (path parameter): The unique identifier of the user directory integration user.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User
        api_response = api_instance.get_user(user_id)
        print("The response of DefaultApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

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

# **installed_profiles**
> object installed_profiles(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Installed profiles

<p>Get Installed Profiles attributes for macOS, iOS, iPadOS, and tvOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Installed profiles
        api_response = api_instance.installed_profiles(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->installed_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->installed_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kernel_extensions**
> object kernel_extensions(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Kernel Extensions

<p>Get Kernel Extension attributes for macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>SON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Kernel Extensions
        api_response = api_instance.kernel_extensions(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->kernel_extensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kernel_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;SON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_agents_and_daemons**
> object launch_agents_and_daemons(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Launch Agents and Daemons

<p>Get Launch Agents and Daemons installed on macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Launch Agents and Daemons
        api_response = api_instance.launch_agents_and_daemons(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->launch_agents_and_daemons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->launch_agents_and_daemons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licensing**
> object licensing()

Licensing

<p>Returns Kandji tenant licensing and utilization information.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)

    try:
        # Licensing
        api_response = api_instance.licensing()
        print("The response of DefaultApi->licensing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->licensing: %s\n" % e)
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

# **list_ade_devices**
> object list_ade_devices(blueprint_id=blueprint_id, user_id=user_id, dep_account=dep_account, device_family=device_family, model=model, os=os, profile_status=profile_status, serial_number=serial_number, page=page)

List ADE devices

<p>Get a list of Automated Device Enrollment devices.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_id = 'fce0cc58-caa5-40d2-a0d7-a0b257127ec5' # str | <p>Return results \"containing\" the specified blueprint id</p>  (optional)
    user_id = '8136' # str | <p>\"exact\" match on kandji user ID number</p>  (optional)
    dep_account = '' # str | <p>The ADE token UUID</p>  (optional)
    device_family = '' # str | <p>Mac, iPhone, iPad, AppleTV, iPod</p>  (optional)
    model = 'MacBook Air' # str | <p>Return model results \"containing\" the specified model string. - \"iPad (8th Generation)\", \"MacBook Air\"</p>  (optional)
    os = '' # str | <p>OSX, iOS, tvOS</p>  (optional)
    profile_status = '' # str | <p>The automated device enrollment profile assignment status - assigned, empty, pushed, removed</p>  (optional)
    serial_number = '' # str | <p>Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned.</p>  (optional)
    page = '1' # str | <p>Use the <code>page</code> parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the <code>next</code> and <code>previous</code> key attributes in the response can be used to request the next page of results or return to the previous page.</p>  (optional)

    try:
        # List ADE devices
        api_response = api_instance.list_ade_devices(blueprint_id=blueprint_id, user_id=user_id, dep_account=dep_account, device_family=device_family, model=model, os=os, profile_status=profile_status, serial_number=serial_number, page=page)
        print("The response of DefaultApi->list_ade_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_ade_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**| &lt;p&gt;Return results \&quot;containing\&quot; the specified blueprint id&lt;/p&gt;  | [optional] 
 **user_id** | **str**| &lt;p&gt;\&quot;exact\&quot; match on kandji user ID number&lt;/p&gt;  | [optional] 
 **dep_account** | **str**| &lt;p&gt;The ADE token UUID&lt;/p&gt;  | [optional] 
 **device_family** | **str**| &lt;p&gt;Mac, iPhone, iPad, AppleTV, iPod&lt;/p&gt;  | [optional] 
 **model** | **str**| &lt;p&gt;Return model results \&quot;containing\&quot; the specified model string. - \&quot;iPad (8th Generation)\&quot;, \&quot;MacBook Air\&quot;&lt;/p&gt;  | [optional] 
 **os** | **str**| &lt;p&gt;OSX, iOS, tvOS&lt;/p&gt;  | [optional] 
 **profile_status** | **str**| &lt;p&gt;The automated device enrollment profile assignment status - assigned, empty, pushed, removed&lt;/p&gt;  | [optional] 
 **serial_number** | **str**| &lt;p&gt;Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned.&lt;/p&gt;  | [optional] 
 **page** | **str**| &lt;p&gt;Use the &lt;code&gt;page&lt;/code&gt; parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the &lt;code&gt;next&lt;/code&gt; and &lt;code&gt;previous&lt;/code&gt; key attributes in the response can be used to request the next page of results or return to the previous page.&lt;/p&gt;  | [optional] 

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
**400** | Bad Request |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ade_integrations**
> list_ade_integrations()

List ADE integrations

<p>This request returns a list of configured ADE integrations.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)

    try:
        # List ADE integrations
        api_instance.list_ade_integrations()
    except Exception as e:
        print("Exception when calling DefaultApi->list_ade_integrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **list_blueprints**
> object list_blueprints(id=id, id__in=id__in, name=name, limit=limit, offset=offset)

List Blueprints

<p>This request returns a list of a blueprint records in the Kandji tenant. Optional query parameters can be specified to filter the results.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    id = '97e4e175-1631-43f6-a02b-33fd1c748ab8' # str | <p>Look up a specific Blueprint by its ID</p>  (optional)
    id__in = '11f4eb9a-10ed-4c3d-a7c1-fb87f95743fb,6391086e-85a1-4820-813c-f9c75025fff4' # str | <p>Specify a list of Blueprint IDs to limit the results to.  Multiple values may be separated by commas. There is a double underscore (<code>__</code>) between id and in</p>  (optional)
    name = 'testing_blueprint' # str | <p>Return Blueprint names \"containing\" the specified search string.</p>  (optional)
    limit = '100' # str | <p>Number of results to return per page.</p>  (optional)
    offset = '400' # str | <p>The initial index from which to return the results.</p>  (optional)

    try:
        # List Blueprints
        api_response = api_instance.list_blueprints(id=id, id__in=id__in, name=name, limit=limit, offset=offset)
        print("The response of DefaultApi->list_blueprints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_blueprints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| &lt;p&gt;Look up a specific Blueprint by its ID&lt;/p&gt;  | [optional] 
 **id__in** | **str**| &lt;p&gt;Specify a list of Blueprint IDs to limit the results to.  Multiple values may be separated by commas. There is a double underscore (&lt;code&gt;__&lt;/code&gt;) between id and in&lt;/p&gt;  | [optional] 
 **name** | **str**| &lt;p&gt;Return Blueprint names \&quot;containing\&quot; the specified search string.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;Number of results to return per page.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;The initial index from which to return the results.&lt;/p&gt;  | [optional] 

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

# **list_custom_apps**
> object list_custom_apps(page=page)

List Custom Apps

<p>This endpoint makes a request to retrieve a list of custom apps from the Kandji library.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    page = '1' # str | <p>Optional page number. Used when results exceed pagination threshold. A hard upper <code>limit</code> is set at 300 device records returned per request.</p>  (optional)

    try:
        # List Custom Apps
        api_response = api_instance.list_custom_apps(page=page)
        print("The response of DefaultApi->list_custom_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_custom_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| &lt;p&gt;Optional page number. Used when results exceed pagination threshold. A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request.&lt;/p&gt;  | [optional] 

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

# **list_custom_profiles**
> object list_custom_profiles(page=page)

List Custom Profiles

<p>This endpoint makes a request to retrieve a list of custom profiles from the Kandji library.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    page = '1' # str | <p>Optional page number (when results exceed pagination threshold)</p>  (optional)

    try:
        # List Custom Profiles
        api_response = api_instance.list_custom_profiles(page=page)
        print("The response of DefaultApi->list_custom_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_custom_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| &lt;p&gt;Optional page number (when results exceed pagination threshold)&lt;/p&gt;  | [optional] 

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

# **list_custom_scripts**
> object list_custom_scripts(page=page)

List Custom Scripts

<p>This endpoint makes a request to retrieve a list of custom scripts from the Kandji library.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    page = '1' # str | <p>Optional page number (when results exceed pagination threshold)</p>  (optional)

    try:
        # List Custom Scripts
        api_response = api_instance.list_custom_scripts(page=page)
        print("The response of DefaultApi->list_custom_scripts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_custom_scripts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| &lt;p&gt;Optional page number (when results exceed pagination threshold)&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
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
        print("The response of DefaultApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_devices: %s\n" % e)
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

# **list_devices_associated_to_ade_token**
> object list_devices_associated_to_ade_token(ade_token_id, page=page)

List devices associated to ADE token

<p>This request returns a list of devices associated with a specified <code>ade_token_id</code> as well as their enrollment status.</p> <p>When the <code>mdm_device</code> key value is <code>null</code>, this can be taken as an indication that the device is awaiting enrollment into Kandji.</p> <p>When data is present within the mdm_device dictionary, you can reference the <code>device_id</code> as the ID of the enrolled device record.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 
    page = '1' # str | <p>Use the <code>page</code> parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the <code>next</code> and <code>previous</code> key attributes in the response can be used to request the next page of results or return to the previous page.</p>  (optional)

    try:
        # List devices associated to ADE token
        api_response = api_instance.list_devices_associated_to_ade_token(ade_token_id, page=page)
        print("The response of DefaultApi->list_devices_associated_to_ade_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_devices_associated_to_ade_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ade_token_id** | **str**|  | 
 **page** | **str**| &lt;p&gt;Use the &lt;code&gt;page&lt;/code&gt; parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the &lt;code&gt;next&lt;/code&gt; and &lt;code&gt;previous&lt;/code&gt; key attributes in the response can be used to request the next page of results or return to the previous page.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Set-Cookie -  <br>  * Allow -  <br>  * Content-Security-Policy -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Xss-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_library_items**
> object list_library_items(blueprint_id)

List Library Items

<p>This API endpoint retrieves a list of library items associated with a specific blueprint. (classic and maps). Requires that the blueprint ID is passed as a path parameter in the URL.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>blueprint_id</code> (path parameter): The unique identifier of the blueprint.</p> <h3 id=\"response-fields\">Response fields</h3> <ul> <li><p><code>count</code> (int): The total count of library items.</p> </li> <li><p><code>next</code> (str): The URL for the next page of results, if available. If not available will value will be <code>null</code>.</p> </li> <li><p><code>previous</code> (str): The URL for the previous page of results, if available. If not available will value will be <code>null</code>.</p> </li> <li><p><code>results</code> (object): An array containing objects with the following fields:</p> <ul> <li><p><code>id</code> (str): The ID of the library item.</p> </li> <li><p><code>name</code> (str): The name of the library item.</p> </li> </ul> </li> </ul> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 

    try:
        # List Library Items
        api_response = api_instance.list_library_items(blueprint_id)
        print("The response of DefaultApi->list_library_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_library_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 

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
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_self_service_categories**
> object list_self_service_categories()

List Self Service Categories

<p>This endpoint retrieves a list of self-service categories and their associated IDs.</p> <p>If you are planning to make a Library item available in Self Service under a specific category, you can call this endpoint to get the category ID and then use that ID when creating or updating the library item via the Kandji API.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)

    try:
        # List Self Service Categories
        api_response = api_instance.list_self_service_categories()
        print("The response of DefaultApi->list_self_service_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_self_service_categories: %s\n" % e)
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

# **list_users**
> object list_users(email=email, id=id, integration_id=integration_id, archived=archived)

List Users

<p>This endpoint makes a request to retrieve a list of users from user directory integrations.</p> <p>A maximum of 300 records are returned per request, and pagination can be performed leveraging the URLs provided in the <code>next</code> and <code>previous</code> keys in the response. If there are no more results available, the respective key will be <code>null</code>.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    email = 'test_user_01@accuhive.io' # str | <p>Returns users with email addresses containing the provided string.</p>  (optional)
    id = '69c009ca-1f78-4bdf-bb93-08d6d39041db' # str | <p>Search for a user matching the provided UUID value.</p>  (optional)
    integration_id = 'f7461096-4ef9-43aa-88e9-ca1967ba0b38' # str | <p>Search for a integration matching the provided UUID value.</p>  (optional)
    archived = 'false' # str | <p>Return only users that are either archived (true) or not archived (false). Archived users are users that appear in the Kandji Users module under the Archived tab. </p>  (optional)

    try:
        # List Users
        api_response = api_instance.list_users(email=email, id=id, integration_id=integration_id, archived=archived)
        print("The response of DefaultApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| &lt;p&gt;Returns users with email addresses containing the provided string.&lt;/p&gt;  | [optional] 
 **id** | **str**| &lt;p&gt;Search for a user matching the provided UUID value.&lt;/p&gt;  | [optional] 
 **integration_id** | **str**| &lt;p&gt;Search for a integration matching the provided UUID value.&lt;/p&gt;  | [optional] 
 **archived** | **str**| &lt;p&gt;Return only users that are either archived (true) or not archived (false). Archived users are users that appear in the Kandji Users module under the Archived tab. &lt;/p&gt;  | [optional] 

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

# **local_users**
> object local_users(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Local users

<p>Get Local Users detials for macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Local users
        api_response = api_instance.local_users(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->local_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->local_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Lock Device
        api_response = api_instance.lock_device(device_id, body=body)
        print("The response of DefaultApi->lock_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->lock_device: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Play Lost Mode Sound
        api_instance.play_lost_mode_sound(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->play_lost_mode_sound: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Reinstall Agent
        api_instance.reinstall_agent(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->reinstall_agent: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Remote Desktop
        api_instance.remote_desktop(device_id, body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->remote_desktop: %s\n" % e)
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

# **remove_library_item**
> object remove_library_item(blueprint_id, body=body)

Remove Library Item

<p>This endpoint allows removing a library item from a specific blueprint (classic and maps). The response will include a list of library item IDs assigned to the blueprint.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>blueprint_id</code> (path parameter): The unique identifier of the blueprint.</p> <h3 id=\"request-body\">Request Body</h3> <ul> <li><p><code>library_item_id</code> (string, required)</p> </li> <li><p><code>assignment_node_id</code> (string, required for maps)</p> </li> </ul> <h3 id=\"error-responses\">Error responses</h3> <div class=\"click-to-expand-wrapper is-table-wrapper\"><table> <thead> <tr> <th><strong>Code</strong></th> <th><strong>Body</strong></th> </tr> </thead> <tbody> <tr> <td>400 - Bad Request</td> <td>Bad Request</td> </tr> <tr> <td></td> <td>\"assignment_node_id cannot be provided for Classic Blueprint\"</td> </tr> <tr> <td></td> <td>\"Must provide assignment_node_id for Assignment Map Blueprint\"</td> </tr> <tr> <td></td> <td>\"Library Item does not exist on Blueprint\"</td> </tr> <tr> <td></td> <td>\"Library Item does not exist in Assignment Node\"</td> </tr> </tbody> </table> </div>

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Remove Library Item
        api_response = api_instance.remove_library_item(blueprint_id, body=body)
        print("The response of DefaultApi->remove_library_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->remove_library_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 
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
**200** | OK |  * Date -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_ade_integration**
> renew_ade_integration(ade_token_id, blueprint_id, phone, email, file)

Renew ADE integration

<p>This request will renew an existing ADE integration.</p> <p>The default <code>blueprint_id</code>, <code>phone</code> number, <code>email</code> address, and MDM server token <code>file</code> from the associated MDM server in ABM are required and must be sent in the request.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 
    blueprint_id = 'blueprint_id_example' # str | 
    phone = 'phone_example' # str | 
    email = 'email_example' # str | 
    file = None # bytearray | <p>This is the MDM server token file(.p7m) download from ABM. Once downloaded from ABM, the file can be uploaded via API.</p> 

    try:
        # Renew ADE integration
        api_instance.renew_ade_integration(ade_token_id, blueprint_id, phone, email, file)
    except Exception as e:
        print("Exception when calling DefaultApi->renew_ade_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ade_token_id** | **str**|  | 
 **blueprint_id** | **str**|  | 
 **phone** | **str**|  | 
 **email** | **str**|  | 
 **file** | **bytearray**| &lt;p&gt;This is the MDM server token file(.p7m) download from ABM. Once downloaded from ABM, the file can be uploaded via API.&lt;/p&gt;  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Renew MDM Profile
        api_instance.renew_mdm_profile(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->renew_mdm_profile: %s\n" % e)
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

# **request_category_export**
> object request_category_export(body=body)

Request category export

<p>Request export of a category. The <code>id</code> key is used when checking the export status using the <em>Request category export</em> endpoint.</p> <p><strong>Request Body Parameters: application/json</strong></p> <div class=\"click-to-expand-wrapper is-table-wrapper\"><table> <thead> <tr> <th>Key</th> <th>Type</th> <th>Possible value(s)</th> <th>Description</th> </tr> </thead> <tbody> <tr> <td><code>blueprint_ids</code></td> <td><code>array</code></td> <td><code>[\"string\", \"string\", \"string\"]</code></td> <td>List of one or more comma separate blueprint IDs.</td> </tr> <tr> <td><code>category</code></td> <td><code>string</code></td> <td><code>apps</code> ,  <br /><code>activation_lock</code> ,  <br /><code>desktop_and_screensaver</code> ,  <br /><code>device_information</code> ,  <br /><code>gatekeeper_and_xprotect</code> ,  <br /><code>installed_profiles</code> ,  <br /><code>kernel_extensions</code> ,  <br /><code>local_users</code> ,  <br /><code>launch_agents_and_daemons</code> ,  <br /><code>system_extensions</code> ,  <br /><code>startup_settings</code> ,  <br /><code>transparency_database</code></td> <td>Only one category per export reqest.</td> </tr> <tr> <td><code>device_families</code></td> <td><code>array</code></td> <td><code>[\"Mac\", \"iPhone\", \"iPad\", \"tvOS\"]</code></td> <td>List of one or more comma separted string values for device families.</td> </tr> <tr> <td><code>filter</code></td> <td><code>object</code></td> <td><code>{\"apple_silicon\": {\"eq\": true}, \"device__name\": {\"like\": [\"this\", \"or_this\"]}}</code></td> <td>JSON schema object containing one or more key value pairs.  <br />  <br /><strong>Note</strong>: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</td> </tr> <tr> <td><code>sort_by</code></td> <td><code>string</code></td> <td></td> <td>Sort results by the name of a given response body key in either ascending (default behavior) or descending(`-`) order.</td> </tr> </tbody> </table> </div>

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Request category export
        api_response = api_instance.request_category_export(body=body)
        print("The response of DefaultApi->request_category_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->request_category_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |
**400** | Bad Request |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Restart Device
        api_instance.restart_device(device_id, body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->restart_device: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    note_id = 'note_id_example' # str | 

    try:
        # Retrieve Device Note
        api_response = api_instance.retrieve_device_note(device_id, note_id)
        print("The response of DefaultApi->retrieve_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->retrieve_device_note: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Send Blankpush
        api_instance.send_blankpush(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->send_blankpush: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Set Name
        api_instance.set_name(device_id, body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->set_name: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Shutdown
        api_instance.shutdown(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->shutdown: %s\n" % e)
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

# **startup_settings**
> object startup_settings(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Startup settings

<p>Get Startup settings for macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return</p>  (optional)

    try:
        # Startup settings
        api_response = api_instance.startup_settings(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->startup_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->startup_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_extensions**
> object system_extensions(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

System Extensions

<p>Get System Extension attributes for macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # System Extensions
        api_response = api_instance.system_extensions(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->system_extensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->system_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transparency_database**
> object transparency_database(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)

Transparency database

<p>Get Transparency Database (TCC) attributes for macOS.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_ids = 'blueprint_id, blueprint_id,blueprint_id' # str | <p>Filter results by one or more blueprint IDs separated by commas.</p>  (optional)
    device_families = 'Mac,iPhone,iPad,tvOS' # str | <p>Filter results by one or more device families separate by commas.</p>  (optional)
    filter = '' # str | <p>JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.</p>  (optional)
    sort_by = '' # str | <p>Sort results by the name of a given response body key in either ascending (default behavior) or descending(<code>-</code>) order.</p>  (optional)
    limit = '' # str | <p>A hard upper <code>limit</code> is set at 300 device records returned per request. If more device records are expected, pagination should be used using the <code>limit</code> and <code>offset</code> parameters. Additionally, parameter queries can be added to a request to limit the results.</p>  (optional)
    offset = '' # str | <p>Specify the starting record to return.</p>  (optional)

    try:
        # Transparency database
        api_response = api_instance.transparency_database(blueprint_ids=blueprint_ids, device_families=device_families, filter=filter, sort_by=sort_by, limit=limit, offset=offset)
        print("The response of DefaultApi->transparency_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->transparency_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_ids** | **str**| &lt;p&gt;Filter results by one or more blueprint IDs separated by commas.&lt;/p&gt;  | [optional] 
 **device_families** | **str**| &lt;p&gt;Filter results by one or more device families separate by commas.&lt;/p&gt;  | [optional] 
 **filter** | **str**| &lt;p&gt;JSON schema object containing one or more key value pairs. Note: For detailed information on fiters, see the Filters section at the begining of the Visibility API endpoints in this doc.&lt;/p&gt;  | [optional] 
 **sort_by** | **str**| &lt;p&gt;Sort results by the name of a given response body key in either ascending (default behavior) or descending(&lt;code&gt;-&lt;/code&gt;) order.&lt;/p&gt;  | [optional] 
 **limit** | **str**| &lt;p&gt;A hard upper &lt;code&gt;limit&lt;/code&gt; is set at 300 device records returned per request. If more device records are expected, pagination should be used using the &lt;code&gt;limit&lt;/code&gt; and &lt;code&gt;offset&lt;/code&gt; parameters. Additionally, parameter queries can be added to a request to limit the results.&lt;/p&gt;  | [optional] 
 **offset** | **str**| &lt;p&gt;Specify the starting record to return.&lt;/p&gt;  | [optional] 

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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Access-Control-Allow-Origin -  <br>  * Content-Encoding -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Server -  <br>  * Via -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Unlock Account
        api_instance.unlock_account(device_id, body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->unlock_account: %s\n" % e)
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

# **update_ade_device**
> object update_ade_device(device_id, body=body)

Update ADE device

<p>Update a specific Automated Device Enrollment device's blueprint assignment, user assignment, and asset tag.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>device_id</code> (path parameter): The unique identifier of the device.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update ADE device
        api_response = api_instance.update_ade_device(device_id, body=body)
        print("The response of DefaultApi->update_ade_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_ade_device: %s\n" % e)
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

# **update_ade_integration**
> update_ade_integration(ade_token_id, body=body)

Update ADE integration

<p>This request will update the default blueprint, phone number, and email address in an existing ADE integration.</p> <p>The default <code>blueprint_id</code>, <code>phone</code> number, and <code>email</code> address must be sent in the request.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update ADE integration
        api_instance.update_ade_integration(ade_token_id, body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->update_ade_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ade_token_id** | **str**|  | 
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

# **update_blueprint**
> object update_blueprint(blueprint_id, name, description, enrollment_code_code, enrollment_code_is_active)

Update Blueprint

<p>This requests allows updating of the name, icon, icon color, description, enrollment code, and active status on an existing blueprint.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>blueprint_id</code> (path parameter): The unique identifier of the blueprint.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    name = 'name_example' # str | <p>Update the name of the Blueprint</p> 
    description = 'description_example' # str | <p>Update the description of the Blueprint </p> 
    enrollment_code_code = 'enrollment_code_code_example' # str | <p>Update the enrollment code of the Blueprint </p> 
    enrollment_code_is_active = 'enrollment_code_is_active_example' # str | <p>Disable the Blueprint for manual device enrollment from the enrollment portal.</p> 

    try:
        # Update Blueprint
        api_response = api_instance.update_blueprint(blueprint_id, name, description, enrollment_code_code, enrollment_code_is_active)
        print("The response of DefaultApi->update_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 
 **name** | **str**| &lt;p&gt;Update the name of the Blueprint&lt;/p&gt;  | 
 **description** | **str**| &lt;p&gt;Update the description of the Blueprint &lt;/p&gt;  | 
 **enrollment_code_code** | **str**| &lt;p&gt;Update the enrollment code of the Blueprint &lt;/p&gt;  | 
 **enrollment_code_is_active** | **str**| &lt;p&gt;Disable the Blueprint for manual device enrollment from the enrollment portal.&lt;/p&gt;  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_app**
> object update_custom_app(library_item_id, name, active)

Update Custom App

<p>This request allows you to update a custom app in the Kandji library.</p> <p>Must have already generated a <code>file_key</code> via <code>Create custom app</code> endpoint and uploaded the file to S3 using a request similar to the <code>Upload to S3</code> example.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    name = 'name_example' # str | <p>Renaming a Custom App</p> 
    active = 'active_example' # str | <p>(Optional, default=true) Whether this Custom App is active and installable</p> 

    try:
        # Update Custom App
        api_response = api_instance.update_custom_app(library_item_id, name, active)
        print("The response of DefaultApi->update_custom_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 
 **name** | **str**| &lt;p&gt;Renaming a Custom App&lt;/p&gt;  | 
 **active** | **str**| &lt;p&gt;(Optional, default&#x3D;true) Whether this Custom App is active and installable&lt;/p&gt;  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_profile**
> object update_custom_profile(library_item_id)

Update Custom Profile

<p>This request allows you to update a custom profile in the Kandji library.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>library_item_id</code> (path parameter): The unique identifier of the library item.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 

    try:
        # Update Custom Profile
        api_response = api_instance.update_custom_profile(library_item_id)
        print("The response of DefaultApi->update_custom_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_custom_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_script**
> object update_custom_script(library_item_id, body=body)

Update Custom Script

<p>This request allows you to update a custom script in the Kandji library.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    library_item_id = 'library_item_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update Custom Script
        api_response = api_instance.update_custom_script(library_item_id, body=body)
        print("The response of DefaultApi->update_custom_script:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_custom_script: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update Device
        api_response = api_instance.update_device(device_id, body=body)
        print("The response of DefaultApi->update_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_device: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 
    note_id = 'note_id_example' # str | 
    authorization = 'Bearer {{API TOKEN}}' # str | 
    content_type = 'application/json' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update Device Note
        api_response = api_instance.update_device_note(device_id, note_id, authorization, content_type, body=body)
        print("The response of DefaultApi->update_device_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_device_note: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Update Inventory
        api_instance.update_inventory(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->update_inventory: %s\n" % e)
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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Update Location
        api_instance.update_location(device_id)
    except Exception as e:
        print("Exception when calling DefaultApi->update_location: %s\n" % e)
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

# **update_tag**
> object update_tag(tag_id, body=body)

Update Tag

<p>Update tag name.</p> <h3 id=\"request-parameters\">Request Parameters</h3> <p><code>tag_id</code> (path parameter): The unique identifier of the tag.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    tag_id = 'tag_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update Tag
        api_response = api_instance.update_tag(tag_id, body=body)
        print("The response of DefaultApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**|  | 
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

# **upload_custom_app**
> upload_custom_app(body=body)

Upload Custom App

<p>This request retrieves the S3 upload details need for uploading the app to Amazon S3.</p> <p>Creates a pre-signed <code>post_url</code> to upload a new Custom App to S3.</p> <p>The provided <code>name</code> will be used to calculate a unique <code>file_key</code> in S3.</p> <p>A separate request will have to be made to the <code>Upload to S3</code> endpoint to upload the file to S3 directly using the <code>post_url</code> and <code>post_data</code> from the <code>Upload Custom App</code> response.</p> 

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
    api_instance = kandji_python_sdk.DefaultApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Upload Custom App
        api_instance.upload_custom_app(body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_custom_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** | Created |  * Date -  <br>  * Server -  <br>  * Content-Type -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

