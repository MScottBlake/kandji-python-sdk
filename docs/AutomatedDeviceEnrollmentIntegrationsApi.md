# kandji.AutomatedDeviceEnrollmentIntegrationsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ade_integration**](AutomatedDeviceEnrollmentIntegrationsApi.md#create_ade_integration) | **POST** /api/v1/integrations/apple/ade/ | Create ADE integration
[**delete_ade_integration**](AutomatedDeviceEnrollmentIntegrationsApi.md#delete_ade_integration) | **DELETE** /api/v1/integrations/apple/ade/{ade_token_id} | Delete ADE integration
[**download_ade_public_key**](AutomatedDeviceEnrollmentIntegrationsApi.md#download_ade_public_key) | **GET** /api/v1/integrations/apple/ade/public_key/ | Download ADE public key
[**get_ade_device**](AutomatedDeviceEnrollmentIntegrationsApi.md#get_ade_device) | **GET** /api/v1/integrations/apple/ade/devices/{device_id} | Get ADE device
[**get_ade_integration**](AutomatedDeviceEnrollmentIntegrationsApi.md#get_ade_integration) | **GET** /api/v1/integrations/apple/ade/{ade_token_id} | Get ADE integration
[**list_ade_devices**](AutomatedDeviceEnrollmentIntegrationsApi.md#list_ade_devices) | **GET** /api/v1/integrations/apple/ade/devices | List ADE devices
[**list_ade_integrations**](AutomatedDeviceEnrollmentIntegrationsApi.md#list_ade_integrations) | **GET** /api/v1/integrations/apple/ade | List ADE integrations
[**list_devices_associated_to_ade_token**](AutomatedDeviceEnrollmentIntegrationsApi.md#list_devices_associated_to_ade_token) | **GET** /api/v1/integrations/apple/ade/{ade_token_id}/devices | List devices associated to ADE token
[**renew_ade_integration**](AutomatedDeviceEnrollmentIntegrationsApi.md#renew_ade_integration) | **POST** /api/v1/integrations/apple/ade/{ade_token_id}/renew | Renew ADE integration
[**update_ade_device**](AutomatedDeviceEnrollmentIntegrationsApi.md#update_ade_device) | **PATCH** /api/v1/integrations/apple/ade/devices/{device_id} | Update ADE device
[**update_ade_integration**](AutomatedDeviceEnrollmentIntegrationsApi.md#update_ade_integration) | **PATCH** /api/v1/integrations/apple/ade/{ade_token_id} | Update ADE integration


# **create_ade_integration**
> AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response create_ade_integration(blueprint_id, email, file, phone)

Create ADE integration

<p>This request will create a new ADE integration.</p>
<p>The default <code>blueprint_id</code>, <code>phone</code> number, <code>email</code> address, and MDM server token <code>file</code> downloaded from ABM are required and must be sent in the request.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.automated_device_enrollment_integrations_create_ade_integration200_response import AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response
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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    email = 'email_example' # str | 
    file = None # bytearray | This is the MDM server token file(.p7m) download from ABM. Once downloaded from ABM, the file can be uploaded via API.
    phone = 'phone_example' # str | 

    try:
        # Create ADE integration
        api_response = api_instance.create_ade_integration(blueprint_id, email, file, phone)
        print("The response of AutomatedDeviceEnrollmentIntegrationsApi->create_ade_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->create_ade_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 
 **email** | **str**|  | 
 **file** | **bytearray**| This is the MDM server token file(.p7m) download from ABM. Once downloaded from ABM, the file can be uploaded via API. | 
 **phone** | **str**|  | 

### Return type

[**AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response**](AutomatedDeviceEnrollmentIntegrationsCreateAdeIntegration200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ade_integration**
> delete_ade_integration(ade_token_id)

Delete ADE integration

<h1 id=&quot;warning&quot;><strong>WARNING!</strong></h1>
<p>This is a HIGHLY destructive action.</p>
<p>Deleting an ADE token will unassign the associated device records from Kandji. For currently enrolled devices that were assigned to Kandji via the delete ADE integration will not be impacted until they are wiped and reprovisioned. This action is essentially the same as removing an ADE token from MDM and then adding it back.</p>
<p>If applicable, be sure to reassign the device records in ABM.</p>

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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 

    try:
        # Delete ADE integration
        api_instance.delete_ade_integration(ade_token_id)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->delete_ade_integration: %s\n" % e)
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
**204** | No Content |  * Allow -  <br>  * Connection -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Xss-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_ade_public_key**
> str download_ade_public_key()

Download ADE public key

<p>This request returns the public key used to create an MDM server connection in Apple Business Manager.</p>
<p>The encoded information needs to be saved to a file with the <code>.pem</code> format and then uploaded to ABM.</p>

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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)

    try:
        # Download ADE public key
        api_response = api_instance.download_ade_public_key()
        print("The response of AutomatedDeviceEnrollmentIntegrationsApi->download_ade_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->download_ade_public_key: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Xss-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ade_device**
> AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response get_ade_device(device_id)

Get ADE device

Get information about a specific Automated Device Enrollment device.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.automated_device_enrollment_integrations_get_ade_device200_response import AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response
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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get ADE device
        api_response = api_instance.get_ade_device(device_id)
        print("The response of AutomatedDeviceEnrollmentIntegrationsApi->get_ade_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->get_ade_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response**](AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response.md)

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

This request returns a specific ADE integration based on the <code>ade_token_id</code> passed.

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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 

    try:
        # Get ADE integration
        api_instance.get_ade_integration(ade_token_id)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->get_ade_integration: %s\n" % e)
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

# **list_ade_devices**
> BlueprintsListBlueprints200Response list_ade_devices(blueprint_id=blueprint_id, user_id=user_id, dep_account=dep_account, device_family=device_family, model=model, os=os, profile_status=profile_status, serial_number=serial_number, page=page)

List ADE devices

Get a list of Automated Device Enrollment devices.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.blueprints_list_blueprints200_response import BlueprintsListBlueprints200Response
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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    blueprint_id = 'fce0cc58-caa5-40d2-a0d7-a0b257127ec5' # str | Return results &quot;containing&quot; the specified blueprint id (optional)
    user_id = '5344c996-8823-4b37-8d6e-8515fc7c3a0a' # str | &quot;exact&quot; match on kandji user ID value (example: 5344c996-8823-4b37-8d6e-8515fc7c3a0a) (optional)
    dep_account = '' # str | The ADE token UUID (optional)
    device_family = '' # str | iPad, iPhone, iPod, Mac, AppleTV, or Vision (optional)
    model = 'MacBook Air' # str | Return model results &quot;containing&quot; the specified model string. - &quot;iPad (8th Generation)&quot;, &quot;MacBook Air&quot; (optional)
    os = '' # str | iOS, iPadOS, OSX, tvOS, or visionOS (optional)
    profile_status = '' # str | The automated device enrollment profile assignment status - assigned, empty, pushed, removed (optional)
    serial_number = '' # str | Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned. (optional)
    page = '1' # str | Use the <code>page</code> parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the <code>next</code> and <code>previous</code> key attributes in the response can be used to request the next page of results or return to the previous page. (optional)

    try:
        # List ADE devices
        api_response = api_instance.list_ade_devices(blueprint_id=blueprint_id, user_id=user_id, dep_account=dep_account, device_family=device_family, model=model, os=os, profile_status=profile_status, serial_number=serial_number, page=page)
        print("The response of AutomatedDeviceEnrollmentIntegrationsApi->list_ade_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->list_ade_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**| Return results &amp;quot;containing&amp;quot; the specified blueprint id | [optional] 
 **user_id** | **str**| &amp;quot;exact&amp;quot; match on kandji user ID value (example: 5344c996-8823-4b37-8d6e-8515fc7c3a0a) | [optional] 
 **dep_account** | **str**| The ADE token UUID | [optional] 
 **device_family** | **str**| iPad, iPhone, iPod, Mac, AppleTV, or Vision | [optional] 
 **model** | **str**| Return model results &amp;quot;containing&amp;quot; the specified model string. - &amp;quot;iPad (8th Generation)&amp;quot;, &amp;quot;MacBook Air&amp;quot; | [optional] 
 **os** | **str**| iOS, iPadOS, OSX, tvOS, or visionOS | [optional] 
 **profile_status** | **str**| The automated device enrollment profile assignment status - assigned, empty, pushed, removed | [optional] 
 **serial_number** | **str**| Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned. | [optional] 
 **page** | **str**| Use the &lt;code&gt;page&lt;/code&gt; parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the &lt;code&gt;next&lt;/code&gt; and &lt;code&gt;previous&lt;/code&gt; key attributes in the response can be used to request the next page of results or return to the previous page. | [optional] 

### Return type

[**BlueprintsListBlueprints200Response**](BlueprintsListBlueprints200Response.md)

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

This request returns a list of configured ADE integrations.

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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)

    try:
        # List ADE integrations
        api_instance.list_ade_integrations()
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->list_ade_integrations: %s\n" % e)
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

# **list_devices_associated_to_ade_token**
> AutomatedDeviceEnrollmentIntegrationsListDevicesAssociatedToAdeToken200Response list_devices_associated_to_ade_token(ade_token_id, page=page)

List devices associated to ADE token

<p>This request returns a list of devices associated with a specified <code>ade_token_id</code> as well as their enrollment status.</p>
<p>When the <code>mdm_device</code> key value is <code>null</code>, this can be taken as an indication that the device is awaiting enrollment into Kandji.</p>
<p>When data is present within the mdm_device dictionary, you can reference the <code>device_id</code> as the ID of the enrolled device record.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.automated_device_enrollment_integrations_list_devices_associated_to_ade_token200_response import AutomatedDeviceEnrollmentIntegrationsListDevicesAssociatedToAdeToken200Response
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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 
    page = '1' # str | Use the <code>page</code> parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the <code>next</code> and <code>previous</code> key attributes in the response can be used to request the next page of results or return to the previous page. (optional)

    try:
        # List devices associated to ADE token
        api_response = api_instance.list_devices_associated_to_ade_token(ade_token_id, page=page)
        print("The response of AutomatedDeviceEnrollmentIntegrationsApi->list_devices_associated_to_ade_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->list_devices_associated_to_ade_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ade_token_id** | **str**|  | 
 **page** | **str**| Use the &lt;code&gt;page&lt;/code&gt; parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the &lt;code&gt;next&lt;/code&gt; and &lt;code&gt;previous&lt;/code&gt; key attributes in the response can be used to request the next page of results or return to the previous page. | [optional] 

### Return type

[**AutomatedDeviceEnrollmentIntegrationsListDevicesAssociatedToAdeToken200Response**](AutomatedDeviceEnrollmentIntegrationsListDevicesAssociatedToAdeToken200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Xss-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_ade_integration**
> renew_ade_integration(ade_token_id, blueprint_id, email, file, phone)

Renew ADE integration

<p>This request will renew an existing ADE integration.</p>
<p>The default <code>blueprint_id</code>, <code>phone</code> number, <code>email</code> address, and MDM server token <code>file</code> from the associated MDM server in ABM are required and must be sent in the request.</p>

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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 
    blueprint_id = 'blueprint_id_example' # str | 
    email = 'email_example' # str | 
    file = None # bytearray | This is the MDM server token file(.p7m) download from ABM. Once downloaded from ABM, the file can be uploaded via API.
    phone = 'phone_example' # str | 

    try:
        # Renew ADE integration
        api_instance.renew_ade_integration(ade_token_id, blueprint_id, email, file, phone)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->renew_ade_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ade_token_id** | **str**|  | 
 **blueprint_id** | **str**|  | 
 **email** | **str**|  | 
 **file** | **bytearray**| This is the MDM server token file(.p7m) download from ABM. Once downloaded from ABM, the file can be uploaded via API. | 
 **phone** | **str**|  | 

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

# **update_ade_device**
> AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response update_ade_device(device_id, body=body)

Update ADE device

<p>Update a specific Automated Device Enrollment device's blueprint assignment, user assignment, and asset tag.</p>
<h3 id=&quot;request-parameters&quot;>Request Parameters</h3>
<p><code>device_id</code> (path parameter): The unique identifier of the device.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.automated_device_enrollment_integrations_get_ade_device200_response import AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response
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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = {"asset_tag":"123456","blueprint_id":"3013eb7c-d0c1-4689-852a-50776a92036b","user_id":"5344c996-8823-4b37-8d6e-8515fc7c3a0a"} # str |  (optional)

    try:
        # Update ADE device
        api_response = api_instance.update_ade_device(device_id, body=body)
        print("The response of AutomatedDeviceEnrollmentIntegrationsApi->update_ade_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->update_ade_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response**](AutomatedDeviceEnrollmentIntegrationsGetAdeDevice200Response.md)

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

<p>This request will update the default blueprint, phone number, and email address in an existing ADE integration.</p>
<p>The default <code>blueprint_id</code>, <code>phone</code> number, and <code>email</code> address must be sent in the request.</p>

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
    api_instance = kandji.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 
    body = {"blueprint_id":"bf21d9cf-17cf-48b3-890d-7bc27c241bb7","email":"example@accuhive.io","phone":"1234567890"} # str |  (optional)

    try:
        # Update ADE integration
        api_instance.update_ade_integration(ade_token_id, body=body)
    except Exception as e:
        print("Exception when calling AutomatedDeviceEnrollmentIntegrationsApi->update_ade_integration: %s\n" % e)
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

