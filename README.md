# kandji-sdk
<html><head></head><body><h1 id=&quot;welcome-to-the-kandji-api-documentation&quot;>Welcome to the Kandji API Documentation</h1>
<p>You can find your API URL in Settings &gt; Access. The API URL will follow the below formats.</p>
<ul>
<li><p>US - <code>https://SubDomain.api.kandji.io</code></p>
</li>
<li><p>EU - <code>https://SubDomain.api.eu.kandji.io</code></p>
</li>
</ul>
<p>For information on how to obtain an API token, please refer to the following support article.</p>
<p><a href=&quot;https://support.kandji.io/api&quot;>https://support.kandji.io/api</a></p>
<h4 id=&quot;rate-limit&quot;>Rate Limit</h4>
<p>The Kandji API currently has an API rate limit of 10,000 requests per hour per customer.</p>
<h4 id=&quot;request-methods&quot;>Request Methods</h4>
<p>HTTP request methods supported by the Kandji API.</p>
<div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>
<thead>
<tr>
<th>Method</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>The <code>GET</code> method requests a representation of the specified resource.</td>
</tr>
<tr>
<td>POST</td>
<td>The <code>POST</code> method submits an entity to the specified resource.</td>
</tr>
<tr>
<td>PATCH</td>
<td>The <code>PATCH</code> method applies partial modifications to a resource.</td>
</tr>
<tr>
<td>DELETE</td>
<td>The <code>DELETE</code> method deletes the specified resource.</td>
</tr>
</tbody>
</table>
</div><h4 id=&quot;response-codes&quot;>Response codes</h4>
<p>Not all response codes apply to every endpoint.</p>
<div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>
<thead>
<tr>
<th>Code</th>
<th>Response</th>
</tr>
</thead>
<tbody>
<tr>
<td>200</td>
<td>OK</td>
</tr>
<tr>
<td>201</td>
<td>Created</td>
</tr>
<tr>
<td>204</td>
<td>No content</td>
</tr>
<tr>
<td></td>
<td>Typical response when sending the DELETE method.</td>
</tr>
<tr>
<td>400</td>
<td>Bad Request</td>
</tr>
<tr>
<td></td>
<td>&quot;Command already running&quot; - The command may already be running in a <em>Pending</em> state waiting on the device.</td>
</tr>
<tr>
<td></td>
<td>&quot;Command is not allowed for current device&quot; - The command may not be compatible with the target device.</td>
</tr>
<tr>
<td></td>
<td>&quot;JSON parse error - Expecting ',' delimiter: line 3 column 2 (char 65)&quot;</td>
</tr>
<tr>
<td>401</td>
<td>Unauthorized</td>
</tr>
<tr>
<td></td>
<td>This error can occur if the token is incorrect, was revoked, or the token has expired.</td>
</tr>
<tr>
<td>403</td>
<td>Forbidden</td>
</tr>
<tr>
<td></td>
<td>The request was understood but cannot be authorized.</td>
</tr>
<tr>
<td>404</td>
<td>Not found</td>
</tr>
<tr>
<td></td>
<td>Unable to locate the resource in the Kandji tenant.</td>
</tr>
<tr>
<td>415</td>
<td>Unsupported Media Type</td>
</tr>
<tr>
<td></td>
<td>The request contains a media type which the server or resource does not support.</td>
</tr>
<tr>
<td>500</td>
<td>Internal server error</td>
</tr>
<tr>
<td>503</td>
<td>Service unavailable</td>
</tr>
<tr>
<td></td>
<td>This error can occur if a file upload is still being processed via the custom apps API.</td>
</tr>
</tbody>
</table>
</div><h4 id=&quot;data-structure&quot;>Data structure</h4>
<p>The API returns all structured responses in JSON schema format.</p>
<h4 id=&quot;examples&quot;>Examples</h4>
<p>Code examples using the API can be found in the Kandji support <a href=&quot;https://github.com/kandji-inc/support/tree/main/api-tools&quot;>GitHub</a>.</p>
</body></html>

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/MScottBlake/kandji-openapi](https://github.com/MScottBlake/kandji-openapi)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/MScottBlake/kandji-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/MScottBlake/kandji-python-sdk.git`)

Then import the package:
```python
import kandji_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kandji_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = kandji_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    phone = 'phone_example' # str | 
    email = 'email_example' # str | 
    file = None # bytearray | This is the MDM server token file(.p7m) download from ABM. Once downloaded from ABM, the file can be uploaded via API.

    try:
        # Create ADE integration
        api_response = api_instance.create_ade_integration(blueprint_id, phone, email, file)
        print("The response of AutomatedDeviceEnrollmentIntegrationsApi->create_ade_integration:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->create_ade_integration: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://<sub_domain>.api.kandji.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutomatedDeviceEnrollmentIntegrationsApi* | [**create_ade_integration**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#create_ade_integration) | **POST** /api/v1/integrations/apple/ade/ | Create ADE integration
*AutomatedDeviceEnrollmentIntegrationsApi* | [**delete_ade_integration**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#delete_ade_integration) | **DELETE** /api/v1/integrations/apple/ade/{ade_token_id} | Delete ADE integration
*AutomatedDeviceEnrollmentIntegrationsApi* | [**download_ade_public_key**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#download_ade_public_key) | **GET** /api/v1/integrations/apple/ade/public_key/ | Download ADE public key
*AutomatedDeviceEnrollmentIntegrationsApi* | [**get_ade_device**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#get_ade_device) | **GET** /api/v1/integrations/apple/ade/devices/{device_id} | Get ADE device
*AutomatedDeviceEnrollmentIntegrationsApi* | [**get_ade_integration**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#get_ade_integration) | **GET** /api/v1/integrations/apple/ade/{ade_token_id} | Get ADE integration
*AutomatedDeviceEnrollmentIntegrationsApi* | [**list_ade_devices**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#list_ade_devices) | **GET** /api/v1/integrations/apple/ade/devices | List ADE devices
*AutomatedDeviceEnrollmentIntegrationsApi* | [**list_ade_integrations**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#list_ade_integrations) | **GET** /api/v1/integrations/apple/ade | List ADE integrations
*AutomatedDeviceEnrollmentIntegrationsApi* | [**list_devices_associated_to_ade_token**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#list_devices_associated_to_ade_token) | **GET** /api/v1/integrations/apple/ade/{ade_token_id}/devices | List devices associated to ADE token
*AutomatedDeviceEnrollmentIntegrationsApi* | [**renew_ade_integration**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#renew_ade_integration) | **POST** /api/v1/integrations/apple/ade/{ade_token_id}/renew | Renew ADE integration
*AutomatedDeviceEnrollmentIntegrationsApi* | [**update_ade_device**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#update_ade_device) | **PATCH** /api/v1/integrations/apple/ade/devices/{device_id} | Update ADE device
*AutomatedDeviceEnrollmentIntegrationsApi* | [**update_ade_integration**](docs/AutomatedDeviceEnrollmentIntegrationsApi.md#update_ade_integration) | **PATCH** /api/v1/integrations/apple/ade/{ade_token_id} | Update ADE integration
*BlueprintsApi* | [**assign_library_item**](docs/BlueprintsApi.md#assign_library_item) | **POST** /api/v1/blueprints/{blueprint_id}/assign-library-item | Assign Library Item
*BlueprintsApi* | [**create_blueprint**](docs/BlueprintsApi.md#create_blueprint) | **POST** /api/v1/blueprints | Create Blueprint
*BlueprintsApi* | [**delete_blueprint**](docs/BlueprintsApi.md#delete_blueprint) | **DELETE** /api/v1/blueprints/{blueprint_id} | Delete Blueprint
*BlueprintsApi* | [**get_blueprint**](docs/BlueprintsApi.md#get_blueprint) | **GET** /api/v1/blueprints/{blueprint_id} | Get Blueprint
*BlueprintsApi* | [**get_blueprint_templates**](docs/BlueprintsApi.md#get_blueprint_templates) | **GET** /api/v1/blueprints/templates/ | Get Blueprint Templates
*BlueprintsApi* | [**get_manual_enrollment_profile**](docs/BlueprintsApi.md#get_manual_enrollment_profile) | **GET** /api/v1/blueprints/{blueprint_id}/ota-enrollment-profile | Get Manual Enrollment Profile
*BlueprintsApi* | [**list_blueprints**](docs/BlueprintsApi.md#list_blueprints) | **GET** /api/v1/blueprints | List Blueprints
*BlueprintsApi* | [**list_library_items**](docs/BlueprintsApi.md#list_library_items) | **GET** /api/v1/blueprints/{blueprint_id}/list-library-items | List Library Items
*BlueprintsApi* | [**remove_library_item**](docs/BlueprintsApi.md#remove_library_item) | **POST** /api/v1/blueprints/{blueprint_id}/remove-library-item | Remove Library Item
*BlueprintsApi* | [**update_blueprint**](docs/BlueprintsApi.md#update_blueprint) | **PATCH** /api/v1/blueprints/{blueprint_id} | Update Blueprint
*CustomAppsApi* | [**create_custom_app**](docs/CustomAppsApi.md#create_custom_app) | **POST** /api/v1/library/custom-apps | Create Custom App
*CustomAppsApi* | [**delete_custom_app**](docs/CustomAppsApi.md#delete_custom_app) | **DELETE** /api/v1/library/custom-apps/{library_item_id} | Delete Custom App
*CustomAppsApi* | [**get_custom_app**](docs/CustomAppsApi.md#get_custom_app) | **GET** /api/v1/library/custom-apps/{library_item_id} | Get Custom App
*CustomAppsApi* | [**list_custom_apps**](docs/CustomAppsApi.md#list_custom_apps) | **GET** /api/v1/library/custom-apps | List Custom Apps
*CustomAppsApi* | [**update_custom_app**](docs/CustomAppsApi.md#update_custom_app) | **PATCH** /api/v1/library/custom-apps/{library_item_id} | Update Custom App
*CustomAppsApi* | [**upload_custom_app**](docs/CustomAppsApi.md#upload_custom_app) | **POST** /api/v1/library/custom-apps/upload | Upload Custom App
*CustomProfilesApi* | [**create_custom_profile**](docs/CustomProfilesApi.md#create_custom_profile) | **POST** /api/v1/library/custom-profiles | Create Custom Profile
*CustomProfilesApi* | [**delete_custom_profile**](docs/CustomProfilesApi.md#delete_custom_profile) | **DELETE** /api/v1/library/custom-profiles/{library_item_id} | Delete Custom Profile
*CustomProfilesApi* | [**get_custom_profile**](docs/CustomProfilesApi.md#get_custom_profile) | **GET** /api/v1/library/custom-profiles/{library_item_id} | Get Custom Profile
*CustomProfilesApi* | [**list_custom_profiles**](docs/CustomProfilesApi.md#list_custom_profiles) | **GET** /api/v1/library/custom-profiles | List Custom Profiles
*CustomProfilesApi* | [**update_custom_profile**](docs/CustomProfilesApi.md#update_custom_profile) | **PATCH** /api/v1/library/custom-profiles/{library_item_id} | Update Custom Profile
*CustomScriptsApi* | [**create_custom_script**](docs/CustomScriptsApi.md#create_custom_script) | **POST** /api/v1/library/custom-scripts | Create Custom Script
*CustomScriptsApi* | [**delete_custom_script**](docs/CustomScriptsApi.md#delete_custom_script) | **DELETE** /api/v1/library/custom-scripts/{library_item_id} | Delete Custom Script
*CustomScriptsApi* | [**get_custom_script**](docs/CustomScriptsApi.md#get_custom_script) | **GET** /api/v1/library/custom-scripts/{library_item_id} | Get Custom Script
*CustomScriptsApi* | [**list_custom_scripts**](docs/CustomScriptsApi.md#list_custom_scripts) | **GET** /api/v1/library/custom-scripts | List Custom Scripts
*CustomScriptsApi* | [**update_custom_script**](docs/CustomScriptsApi.md#update_custom_script) | **PATCH** /api/v1/library/custom-scripts/{library_item_id} | Update Custom Script
*DeviceActionsApi* | [**clear_passcode**](docs/DeviceActionsApi.md#clear_passcode) | **POST** /api/v1/devices/{device_id}/action/clearpasscode | Clear Passcode
*DeviceActionsApi* | [**delete_device**](docs/DeviceActionsApi.md#delete_device) | **DELETE** /api/v1/devices/{device_id} | Delete Device
*DeviceActionsApi* | [**delete_user**](docs/DeviceActionsApi.md#delete_user) | **POST** /api/v1/devices/{device_id}/action/deleteuser | Delete User
*DeviceActionsApi* | [**erase_device**](docs/DeviceActionsApi.md#erase_device) | **POST** /api/v1/devices/{device_id}/action/erase | Erase Device
*DeviceActionsApi* | [**get_device_commands**](docs/DeviceActionsApi.md#get_device_commands) | **GET** /api/v1/devices/{device_id}/commands | Get Device Commands
*DeviceActionsApi* | [**lock_device**](docs/DeviceActionsApi.md#lock_device) | **POST** /api/v1/devices/{device_id}/action/lock | Lock Device
*DeviceActionsApi* | [**reinstall_agent**](docs/DeviceActionsApi.md#reinstall_agent) | **POST** /api/v1/devices/{device_id}/action/reinstallagent | Reinstall Agent
*DeviceActionsApi* | [**remote_desktop**](docs/DeviceActionsApi.md#remote_desktop) | **POST** /api/v1/devices/{device_id}/action/remotedesktop | Remote Desktop
*DeviceActionsApi* | [**renew_mdm_profile**](docs/DeviceActionsApi.md#renew_mdm_profile) | **POST** /api/v1/devices/{device_id}/action/renewmdmprofile | Renew MDM Profile
*DeviceActionsApi* | [**restart_device**](docs/DeviceActionsApi.md#restart_device) | **POST** /api/v1/devices/{device_id}/action/restart | Restart Device
*DeviceActionsApi* | [**send_blankpush**](docs/DeviceActionsApi.md#send_blankpush) | **POST** /api/v1/devices/{device_id}/action/blankpush | Send Blankpush
*DeviceActionsApi* | [**set_name**](docs/DeviceActionsApi.md#set_name) | **POST** /api/v1/devices/{device_id}/action/setname | Set Name
*DeviceActionsApi* | [**shutdown**](docs/DeviceActionsApi.md#shutdown) | **POST** /api/v1/devices/{device_id}/action/shutdown | Shutdown
*DeviceActionsApi* | [**unlock_account**](docs/DeviceActionsApi.md#unlock_account) | **POST** /api/v1/devices/{device_id}/action/unlockaccount | Unlock Account
*DeviceActionsApi* | [**update_inventory**](docs/DeviceActionsApi.md#update_inventory) | **POST** /api/v1/devices/{device_id}/action/updateinventory | Update Inventory
*DeviceInformationApi* | [**cancel_lost_mode**](docs/DeviceInformationApi.md#cancel_lost_mode) | **DELETE** /api/v1/devices/{device_id}/details/lostmode | Cancel Lost Mode
*DeviceInformationApi* | [**get_device_activity**](docs/DeviceInformationApi.md#get_device_activity) | **GET** /api/v1/devices/{device_id}/activity | Get Device Activity
*DeviceInformationApi* | [**get_device_apps**](docs/DeviceInformationApi.md#get_device_apps) | **GET** /api/v1/devices/{device_id}/apps | Get Device Apps
*DeviceInformationApi* | [**get_device_details**](docs/DeviceInformationApi.md#get_device_details) | **GET** /api/v1/devices/{device_id}/details | Get Device Details
*DeviceInformationApi* | [**get_device_library_items**](docs/DeviceInformationApi.md#get_device_library_items) | **GET** /api/v1/devices/{device_id}/library-items | Get Device Library Items
*DeviceInformationApi* | [**get_device_lost_mode_details**](docs/DeviceInformationApi.md#get_device_lost_mode_details) | **GET** /api/v1/devices/{device_id}/details/lostmode | Get Device Lost Mode details
*DeviceInformationApi* | [**get_device_parameters**](docs/DeviceInformationApi.md#get_device_parameters) | **GET** /api/v1/devices/{device_id}/parameters | Get Device Parameters
*DeviceInformationApi* | [**get_device_status**](docs/DeviceInformationApi.md#get_device_status) | **GET** /api/v1/devices/{device_id}/status | Get Device Status
*DeviceInformationApi* | [**list_devices**](docs/DeviceInformationApi.md#list_devices) | **GET** /api/v1/devices | List Devices
*DeviceSecretsApi* | [**get_activation_lock_bypass_code**](docs/DeviceSecretsApi.md#get_activation_lock_bypass_code) | **GET** /api/v1/devices/{device_id}/secrets/bypasscode | Get Activation Lock Bypass Code
*DeviceSecretsApi* | [**get_filevault_recovery_key**](docs/DeviceSecretsApi.md#get_filevault_recovery_key) | **GET** /api/v1/devices/{device_id}/secrets/filevaultkey | Get FileVault Recovery Key
*DeviceSecretsApi* | [**get_recovery_lock_password**](docs/DeviceSecretsApi.md#get_recovery_lock_password) | **GET** /api/v1/devices/{device_id}/secrets/recoverypassword | Get Recovery Lock Password
*DeviceSecretsApi* | [**get_unlock_pin**](docs/DeviceSecretsApi.md#get_unlock_pin) | **GET** /api/v1/devices/{device_id}/secrets/unlockpin | Get Unlock Pin
*InHouseAppsApi* | [**create_inhouse_app**](docs/InHouseAppsApi.md#create_inhouse_app) | **POST** /api/v1/library/ipa-apps | Create In-House App
*InHouseAppsApi* | [**delete_inhouse_app**](docs/InHouseAppsApi.md#delete_inhouse_app) | **DELETE** /api/v1/library/ipa-apps/{library_item_id} | Delete In-House App
*InHouseAppsApi* | [**get_inhouse_app**](docs/InHouseAppsApi.md#get_inhouse_app) | **GET** /api/v1/library/ipa-apps/{library_item_id} | Get In-House App
*InHouseAppsApi* | [**list_inhouse_apps**](docs/InHouseAppsApi.md#list_inhouse_apps) | **GET** /api/v1/library/ipa-apps | List In-House Apps
*InHouseAppsApi* | [**update_inhouse_app**](docs/InHouseAppsApi.md#update_inhouse_app) | **PATCH** /api/v1/library/ipa-apps/{library_item_id} | Update In-House App
*InHouseAppsApi* | [**upload_inhouse_app**](docs/InHouseAppsApi.md#upload_inhouse_app) | **POST** /api/v1/library/ipa-apps/upload | Upload In-House App
*InHouseAppsApi* | [**upload_inhouse_app_status**](docs/InHouseAppsApi.md#upload_inhouse_app_status) | **GET** /api/v1/library/ipa-apps/upload/{pending_upload_id}/status | Upload In-House App Status
*LibraryItemsApi* | [**get_library_item_activity**](docs/LibraryItemsApi.md#get_library_item_activity) | **GET** /api/v1/library/library-items/{library_item_id}/activity | Get Library Item Activity
*LibraryItemsApi* | [**get_library_item_statuses**](docs/LibraryItemsApi.md#get_library_item_statuses) | **GET** /api/v1/library/library-items/{library_item_id}/status | Get Library Item Statuses
*LostModeApi* | [**disable_lost_mode**](docs/LostModeApi.md#disable_lost_mode) | **POST** /api/v1/devices/{device_id}/action/disablelostmode | Disable Lost Mode
*LostModeApi* | [**enable_lost_mode**](docs/LostModeApi.md#enable_lost_mode) | **POST** /api/v1/devices/{device_id}/action/enablelostmode | Enable Lost Mode
*LostModeApi* | [**play_lost_mode_sound**](docs/LostModeApi.md#play_lost_mode_sound) | **POST** /api/v1/devices/{device_id}/action/playlostmodesound | Play Lost Mode Sound
*LostModeApi* | [**update_location**](docs/LostModeApi.md#update_location) | **POST** /api/v1/devices/{device_id}/action/updatelocation | Update Location
*NotesApi* | [**create_device_note**](docs/NotesApi.md#create_device_note) | **POST** /api/v1/devices/{device_id}/notes | Create Device Note
*NotesApi* | [**delete_device_note**](docs/NotesApi.md#delete_device_note) | **DELETE** /api/v1/devices/{device_id}/notes/{note_id} | Delete Device Note
*NotesApi* | [**get_device_notes**](docs/NotesApi.md#get_device_notes) | **GET** /api/v1/devices/{device_id}/notes | Get Device Notes
*NotesApi* | [**retrieve_device_note**](docs/NotesApi.md#retrieve_device_note) | **GET** /api/v1/devices/{device_id}/notes/{note_id} | Retrieve Device Note
*NotesApi* | [**update_device_note**](docs/NotesApi.md#update_device_note) | **PATCH** /api/v1/devices/{device_id}/notes/{note_id} | Update Device Note
*PrismApi* | [**activation_lock**](docs/PrismApi.md#activation_lock) | **GET** /api/v1/prism/activation_lock | Activation lock
*PrismApi* | [**application_firewall**](docs/PrismApi.md#application_firewall) | **GET** /api/v1/prism/application_firewall | Application firewall
*PrismApi* | [**applications**](docs/PrismApi.md#applications) | **GET** /api/v1/prism/apps | Applications
*PrismApi* | [**certificates**](docs/PrismApi.md#certificates) | **GET** /api/v1/prism/certificates | Certificates
*PrismApi* | [**count**](docs/PrismApi.md#count) | **GET** /api/v1/prism/count | Count
*PrismApi* | [**desktop_and_screensaver**](docs/PrismApi.md#desktop_and_screensaver) | **GET** /api/v1/prism/desktop_and_screensaver | Desktop and Screensaver
*PrismApi* | [**device_information**](docs/PrismApi.md#device_information) | **GET** /api/v1/prism/device_information | Device information
*PrismApi* | [**filevault**](docs/PrismApi.md#filevault) | **GET** /api/v1/prism/filevault | FileVault
*PrismApi* | [**gatekeeper_and_xprotect**](docs/PrismApi.md#gatekeeper_and_xprotect) | **GET** /api/v1/prism/gatekeeper_and_xprotect | Gatekeeper and XProtect
*PrismApi* | [**get_category_export**](docs/PrismApi.md#get_category_export) | **GET** /api/v1/prism/export/{export_id} | Get category export
*PrismApi* | [**installed_profiles**](docs/PrismApi.md#installed_profiles) | **GET** /api/v1/prism/installed_profiles | Installed profiles
*PrismApi* | [**kernel_extensions**](docs/PrismApi.md#kernel_extensions) | **GET** /api/v1/prism/kernel_extensions | Kernel Extensions
*PrismApi* | [**launch_agents_and_daemons**](docs/PrismApi.md#launch_agents_and_daemons) | **GET** /api/v1/prism/launch_agents_and_daemons | Launch Agents and Daemons
*PrismApi* | [**local_users**](docs/PrismApi.md#local_users) | **GET** /api/v1/prism/local_users | Local users
*PrismApi* | [**request_category_export**](docs/PrismApi.md#request_category_export) | **POST** /api/v1/prism/export | Request category export
*PrismApi* | [**startup_settings**](docs/PrismApi.md#startup_settings) | **GET** /api/v1/prism/startup_settings | Startup settings
*PrismApi* | [**system_extensions**](docs/PrismApi.md#system_extensions) | **GET** /api/v1/prism/system_extensions | System Extensions
*PrismApi* | [**transparency_database**](docs/PrismApi.md#transparency_database) | **GET** /api/v1/prism/transparency_database | Transparency database
*SelfServiceApi* | [**list_self_service_categories**](docs/SelfServiceApi.md#list_self_service_categories) | **GET** /api/v1/self-service/categories | List Self Service Categories
*SettingsApi* | [**licensing**](docs/SettingsApi.md#licensing) | **GET** /api/v1/settings/licensing | Licensing
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /api/v1/tags | Create Tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /api/v1/tags/{tag_id} | Delete Tag
*TagsApi* | [**get_tags**](docs/TagsApi.md#get_tags) | **GET** /api/v1/tags | Get Tags
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PATCH** /api/v1/tags/{tag_id} | Update Tag
*ThreatsApi* | [**get_threat_details**](docs/ThreatsApi.md#get_threat_details) | **GET** /api/v1/threat-details | Get Threat Details
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /api/v1/users/{user_id} | Get User
*UsersApi* | [**list_users**](docs/UsersApi.md#list_users) | **GET** /api/v1/users | List Users


## Documentation For Models



<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearer"></a>
### bearer

- **Type**: Bearer authentication (API Token)


## Author

mitchelsblake@gmail.com


