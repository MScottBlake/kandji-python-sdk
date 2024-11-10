# kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi

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
> object create_ade_integration(blueprint_id, email, file, phone)

Create ADE integration

This request will create a new ADE integration.   The default `blueprint_id`, `phone` number, `email` address, and MDM server token `file` downloaded from ABM are required and must be sent in the request.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
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

**object**

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

**WARNING!** ============   This is a HIGHLY destructive action.    Deleting an ADE token will unassign the associated device records from Kandji. For currently enrolled devices that were assigned to Kandji via the delete ADE integration will not be impacted until they are wiped and reprovisioned. This action is essentially the same as removing an ADE token from MDM and then adding it back.   If applicable, be sure to reassign the device records in ABM.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
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

This request returns the public key used to create an MDM server connection in Apple Business Manager.   The encoded information needs to be saved to a file with the `.pem` format and then uploaded to ABM.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)

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
> object get_ade_device(device_id)

Get ADE device

Get information about a specific Automated Device Enrollment device.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
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

This request returns a specific ADE integration based on the `ade_token_id` passed.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
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
> object list_ade_devices(blueprint_id=blueprint_id, user_id=user_id, dep_account=dep_account, device_family=device_family, model=model, os=os, profile_status=profile_status, serial_number=serial_number, page=page)

List ADE devices

Get a list of Automated Device Enrollment devices.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    blueprint_id = 'fce0cc58-caa5-40d2-a0d7-a0b257127ec5' # str | Return results 'containing' the specified blueprint id (optional)
    user_id = '8136' # str | 'exact' match on kandji user ID number (optional)
    dep_account = '' # str | The ADE token UUID (optional)
    device_family = '' # str | Mac, iPhone, iPad, AppleTV, iPod (optional)
    model = 'MacBook Air' # str | Return model results 'containing' the specified model string. \\\\\\- 'iPad (8th Generation)', 'MacBook Air' (optional)
    os = '' # str | OSX, iOS, tvOS (optional)
    profile_status = '' # str | The automated device enrollment profile assignment status \\\\\\- assigned, empty, pushed, removed (optional)
    serial_number = '' # str | Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned. (optional)
    page = '1' # str | Use the \\`page\\` parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the \\`next\\` and \\`previous\\` key attributes in the response can be used to request the next page of results or return to the previous page. (optional)

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
 **blueprint_id** | **str**| Return results &#39;containing&#39; the specified blueprint id | [optional] 
 **user_id** | **str**| &#39;exact&#39; match on kandji user ID number | [optional] 
 **dep_account** | **str**| The ADE token UUID | [optional] 
 **device_family** | **str**| Mac, iPhone, iPad, AppleTV, iPod | [optional] 
 **model** | **str**| Return model results &#39;containing&#39; the specified model string. \\\\\\- &#39;iPad (8th Generation)&#39;, &#39;MacBook Air&#39; | [optional] 
 **os** | **str**| OSX, iOS, tvOS | [optional] 
 **profile_status** | **str**| The automated device enrollment profile assignment status \\\\\\- assigned, empty, pushed, removed | [optional] 
 **serial_number** | **str**| Search for a specific device by Serial Number. If partial serial number is provided in the query, all device containing the partial string will be returned. | [optional] 
 **page** | **str**| Use the \\&#x60;page\\&#x60; parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the \\&#x60;next\\&#x60; and \\&#x60;previous\\&#x60; key attributes in the response can be used to request the next page of results or return to the previous page. | [optional] 

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

This request returns a list of configured ADE integrations.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)

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
> object list_devices_associated_to_ade_token(ade_token_id, page=page)

List devices associated to ADE token

This request returns a list of devices associated with a specified `ade_token_id` as well as their enrollment status.   When the `mdm_device` key value is `null`, this can be taken as an indication that the device is awaiting enrollment into Kandji.   When data is present within the mdm\\ _device dictionary, you can reference the `device_id` as the ID of the enrolled device record.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 
    page = '1' # str | Use the \\`page\\` parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the \\`next\\` and \\`previous\\` key attributes in the response can be used to request the next page of results or return to the previous page. (optional)

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
 **page** | **str**| Use the \\&#x60;page\\&#x60; parameter to page through results or to request a specific page. By default, if a page is not specified, page 1 is returned. Note: 300 device records are returned per page of results. Alternatively, the \\&#x60;next\\&#x60; and \\&#x60;previous\\&#x60; key attributes in the response can be used to request the next page of results or return to the previous page. | [optional] 

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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Xss-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_ade_integration**
> renew_ade_integration(ade_token_id, blueprint_id, email, file, phone)

Renew ADE integration

This request will renew an existing ADE integration.   The default `blueprint_id`, `phone` number, `email` address, and MDM server token `file` from the associated MDM server in ABM are required and must be sent in the request.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
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
> object update_ade_device(device_id, body=body)

Update ADE device

Update a specific Automated Device Enrollment device's blueprint assignment, user assignment, and asset tag.   ### Request Parameters    `device_id` (path parameter): The unique identifier of the device.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    device_id = 'device_id_example' # str | 
    body = 'body_example' # str |  (optional)

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

This request will update the default blueprint, phone number, and email address in an existing ADE integration.   The default `blueprint_id`, `phone` number, and `email` address must be sent in the request.

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
    api_instance = kandji_python_sdk.AutomatedDeviceEnrollmentIntegrationsApi(api_client)
    ade_token_id = 'ade_token_id_example' # str | 
    body = 'body_example' # str |  (optional)

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

