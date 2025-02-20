# coding: utf-8

# flake8: noqa

"""
    Kandji API

    <html><head></head><body><h1 id=&quot;welcome-to-the-kandji-api-documentation&quot;>Welcome to the Kandji API Documentation</h1> <p>You can find your API URL in Settings &gt; Access. The API URL will follow the below formats.</p> <ul> <li><p>US - <code>https://SubDomain.api.kandji.io</code></p> </li> <li><p>EU - <code>https://SubDomain.api.eu.kandji.io</code></p> </li> </ul> <p>For information on how to obtain an API token, please refer to the following support article.</p> <p><a href=&quot;https://support.kandji.io/api&quot;>https://support.kandji.io/api</a></p> <h4 id=&quot;rate-limit&quot;>Rate Limit</h4> <p>The Kandji API currently has an API rate limit of 10,000 requests per hour per customer.</p> <h4 id=&quot;request-methods&quot;>Request Methods</h4> <p>HTTP request methods supported by the Kandji API.</p> <div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table> <thead> <tr> <th>Method</th> <th>Definition</th> </tr> </thead> <tbody> <tr> <td>GET</td> <td>The <code>GET</code> method requests a representation of the specified resource.</td> </tr> <tr> <td>POST</td> <td>The <code>POST</code> method submits an entity to the specified resource.</td> </tr> <tr> <td>PATCH</td> <td>The <code>PATCH</code> method applies partial modifications to a resource.</td> </tr> <tr> <td>DELETE</td> <td>The <code>DELETE</code> method deletes the specified resource.</td> </tr> </tbody> </table> </div><h4 id=&quot;response-codes&quot;>Response codes</h4> <p>Not all response codes apply to every endpoint.</p> <div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table> <thead> <tr> <th>Code</th> <th>Response</th> </tr> </thead> <tbody> <tr> <td>200</td> <td>OK</td> </tr> <tr> <td>201</td> <td>Created</td> </tr> <tr> <td>204</td> <td>No content</td> </tr> <tr> <td></td> <td>Typical response when sending the DELETE method.</td> </tr> <tr> <td>400</td> <td>Bad Request</td> </tr> <tr> <td></td> <td>&quot;Command already running&quot; - The command may already be running in a <em>Pending</em> state waiting on the device.</td> </tr> <tr> <td></td> <td>&quot;Command is not allowed for current device&quot; - The command may not be compatible with the target device.</td> </tr> <tr> <td></td> <td>&quot;JSON parse error - Expecting ',' delimiter: line 3 column 2 (char 65)&quot;</td> </tr> <tr> <td>401</td> <td>Unauthorized</td> </tr> <tr> <td></td> <td>This error can occur if the token is incorrect, was revoked, or the token has expired.</td> </tr> <tr> <td>403</td> <td>Forbidden</td> </tr> <tr> <td></td> <td>The request was understood but cannot be authorized.</td> </tr> <tr> <td>404</td> <td>Not found</td> </tr> <tr> <td></td> <td>Unable to locate the resource in the Kandji tenant.</td> </tr> <tr> <td>415</td> <td>Unsupported Media Type</td> </tr> <tr> <td></td> <td>The request contains a media type which the server or resource does not support.</td> </tr> <tr> <td>500</td> <td>Internal server error</td> </tr> <tr> <td>503</td> <td>Service unavailable</td> </tr> <tr> <td></td> <td>This error can occur if a file upload is still being processed via the custom apps API.</td> </tr> </tbody> </table> </div><h4 id=&quot;data-structure&quot;>Data structure</h4> <p>The API returns all structured responses in JSON schema format.</p> <h4 id=&quot;examples&quot;>Examples</h4> <p>Code examples using the API can be found in the Kandji support <a href=&quot;https://github.com/kandji-inc/support/tree/main/api-tools&quot;>GitHub</a>.</p> </body></html>

    The version of the OpenAPI document: 1.0.0
    Contact: mitchelsblake@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from kandji.api.automated_device_enrollment_integrations_api import AutomatedDeviceEnrollmentIntegrationsApi
from kandji.api.blueprints_api import BlueprintsApi
from kandji.api.device_actions_api import DeviceActionsApi
from kandji.api.device_information_api import DeviceInformationApi
from kandji.api.device_secrets_api import DeviceSecretsApi
from kandji.api.library_items_api import LibraryItemsApi
from kandji.api.prism_api import PrismApi
from kandji.api.settings_api import SettingsApi
from kandji.api.tags_api import TagsApi
from kandji.api.threats_api import ThreatsApi
from kandji.api.users_api import UsersApi
from kandji.api.vulnerabilities_api import VulnerabilitiesApi

# import ApiClient
from kandji.api_response import ApiResponse
from kandji.api_client import ApiClient
from kandji.configuration import Configuration
from kandji.exceptions import OpenApiException
from kandji.exceptions import ApiTypeError
from kandji.exceptions import ApiValueError
from kandji.exceptions import ApiKeyError
from kandji.exceptions import ApiAttributeError
from kandji.exceptions import ApiException

# import models into sdk package
from kandji.models.automated_device_enrollment_integrations_create_ade_integration200_response import AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response
from kandji.models.automated_device_enrollment_integrations_create_ade_integration200_response_blueprint import AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200ResponseBlueprint
from kandji.models.automated_device_enrollment_integrations_create_ade_integration200_response_defaults import AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200ResponseDefaults
from kandji.models.automated_device_enrollment_integrations_create_ade_integration200_response_device_counts import AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200ResponseDeviceCounts
from kandji.models.automated_device_enrollment_integrations_get_ade_device200_response import AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response
from kandji.models.automated_device_enrollment_integrations_get_ade_device200_response_dep_account import AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseDepAccount
from kandji.models.automated_device_enrollment_integrations_get_ade_device200_response_mdm_device import AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200ResponseMdmDevice
from kandji.models.automated_device_enrollment_integrations_list_ade_devices200_response import AutomatedDeviceEnrollmentIntegrationsListAdeDevices200Response
from kandji.models.automated_device_enrollment_integrations_list_ade_devices400_response import AutomatedDeviceEnrollmentIntegrationsListAdeDevices400Response
from kandji.models.automated_device_enrollment_integrations_list_devices_associated_to_ade_token200_response import AutomatedDeviceEnrollmentIntegrationsListDevicesAssociatedToAdeToken200Response
from kandji.models.blueprints_create_blueprint201_response import BlueprintsCreateBlueprint201Response
from kandji.models.blueprints_create_blueprint201_response_enrollment_code import BlueprintsCreateBlueprint201ResponseEnrollmentCode
from kandji.models.blueprints_get_blueprint200_response import BlueprintsGetBlueprint200Response
from kandji.models.blueprints_update_blueprint200_response import BlueprintsUpdateBlueprint200Response
from kandji.models.device_actions_get_device_commands200_response import DeviceActionsGetDeviceCommands200Response
from kandji.models.device_actions_lock_device200_response import DeviceActionsLockDevice200Response
from kandji.models.device_information_get_device200_response import DeviceInformationGetDevice200Response
from kandji.models.device_information_get_device200_response_user import DeviceInformationGetDevice200ResponseUser
from kandji.models.device_information_get_device_activity200_response import DeviceInformationGetDeviceActivity200Response
from kandji.models.device_information_get_device_apps200_response import DeviceInformationGetDeviceApps200Response
from kandji.models.device_information_get_device_details200_response import DeviceInformationGetDeviceDetails200Response
from kandji.models.device_information_get_device_details200_response_activation_lock import DeviceInformationGetDeviceDetails200ResponseActivationLock
from kandji.models.device_information_get_device_details200_response_apple_business_manager import DeviceInformationGetDeviceDetails200ResponseAppleBusinessManager
from kandji.models.device_information_get_device_details200_response_automated_device_enrollment import DeviceInformationGetDeviceDetails200ResponseAutomatedDeviceEnrollment
from kandji.models.device_information_get_device_details200_response_cellular import DeviceInformationGetDeviceDetails200ResponseCellular
from kandji.models.device_information_get_device_details200_response_filevault import DeviceInformationGetDeviceDetails200ResponseFilevault
from kandji.models.device_information_get_device_details200_response_general import DeviceInformationGetDeviceDetails200ResponseGeneral
from kandji.models.device_information_get_device_details200_response_hardware_overview import DeviceInformationGetDeviceDetails200ResponseHardwareOverview
from kandji.models.device_information_get_device_details200_response_kandji_agent import DeviceInformationGetDeviceDetails200ResponseKandjiAgent
from kandji.models.device_information_get_device_details200_response_lost_mode import DeviceInformationGetDeviceDetails200ResponseLostMode
from kandji.models.device_information_get_device_details200_response_lost_mode_last_location import DeviceInformationGetDeviceDetails200ResponseLostModeLastLocation
from kandji.models.device_information_get_device_details200_response_mdm import DeviceInformationGetDeviceDetails200ResponseMdm
from kandji.models.device_information_get_device_details200_response_recovery_information import DeviceInformationGetDeviceDetails200ResponseRecoveryInformation
from kandji.models.device_information_get_device_details200_response_security_information import DeviceInformationGetDeviceDetails200ResponseSecurityInformation
from kandji.models.device_information_get_device_details200_response_users import DeviceInformationGetDeviceDetails200ResponseUsers
from kandji.models.device_information_get_device_library_items200_response import DeviceInformationGetDeviceLibraryItems200Response
from kandji.models.device_information_get_device_lost_mode_details200_response import DeviceInformationGetDeviceLostModeDetails200Response
from kandji.models.device_information_get_device_parameters200_response import DeviceInformationGetDeviceParameters200Response
from kandji.models.device_information_get_device_status200_response import DeviceInformationGetDeviceStatus200Response
from kandji.models.device_information_update_device200_response import DeviceInformationUpdateDevice200Response
from kandji.models.device_secrets_get_activation_lock_bypass_code200_response import DeviceSecretsGetActivationLockBypassCode200Response
from kandji.models.device_secrets_get_filevault_recovery_key200_response import DeviceSecretsGetFilevaultRecoveryKey200Response
from kandji.models.device_secrets_get_recovery_lock_password200_response import DeviceSecretsGetRecoveryLockPassword200Response
from kandji.models.device_secrets_get_unlock_pin200_response import DeviceSecretsGetUnlockPin200Response
from kandji.models.prism_activation_lock200_response import PrismActivationLock200Response
from kandji.models.prism_applications200_response import PrismApplications200Response
from kandji.models.prism_count200_response import PrismCount200Response
from kandji.models.prism_device_information200_response import PrismDeviceInformation200Response
from kandji.models.prism_get_category_export200_response import PrismGetCategoryExport200Response
from kandji.models.prism_local_users200_response import PrismLocalUsers200Response
from kandji.models.prism_request_category_export200_response import PrismRequestCategoryExport200Response
from kandji.models.prism_request_category_export200_response_args import PrismRequestCategoryExport200ResponseArgs
from kandji.models.prism_request_category_export400_response import PrismRequestCategoryExport400Response
from kandji.models.settings_licensing200_response import SettingsLicensing200Response
from kandji.models.settings_licensing200_response_counts import SettingsLicensing200ResponseCounts
from kandji.models.settings_licensing200_response_limits import SettingsLicensing200ResponseLimits
from kandji.models.settings_licensing200_response_limits_max_devices_per_platform import SettingsLicensing200ResponseLimitsMaxDevicesPerPlatform
from kandji.models.tags_create_tag201_response import TagsCreateTag201Response
from kandji.models.threats_get_threat_details200_response import ThreatsGetThreatDetails200Response
from kandji.models.users_get_user200_response import UsersGetUser200Response
from kandji.models.users_get_user200_response_integration import UsersGetUser200ResponseIntegration
from kandji.models.users_list_users200_response import UsersListUsers200Response
from kandji.models.vulnerabilities_get_vulnerability_description200_response import VulnerabilitiesGetVulnerabilityDescription200Response
from kandji.models.vulnerabilities_list_detections200_response import VulnerabilitiesListDetections200Response
from kandji.models.vulnerabilities_list_vulnerabilities200_response import VulnerabilitiesListVulnerabilities200Response
