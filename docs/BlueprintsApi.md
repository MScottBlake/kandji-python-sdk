# kandji_python_sdk.BlueprintsApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_library_item**](BlueprintsApi.md#assign_library_item) | **POST** /api/v1/blueprints/{blueprint_id}/assign-library-item | Assign Library Item
[**create_blueprint**](BlueprintsApi.md#create_blueprint) | **POST** /api/v1/blueprints | Create Blueprint
[**delete_blueprint**](BlueprintsApi.md#delete_blueprint) | **DELETE** /api/v1/blueprints/{blueprint_id} | Delete Blueprint
[**get_blueprint**](BlueprintsApi.md#get_blueprint) | **GET** /api/v1/blueprints/{blueprint_id} | Get Blueprint
[**get_blueprint_templates**](BlueprintsApi.md#get_blueprint_templates) | **GET** /api/v1/blueprints/templates/ | Get Blueprint Templates
[**get_manual_enrollment_profile**](BlueprintsApi.md#get_manual_enrollment_profile) | **GET** /api/v1/blueprints/{blueprint_id}/ota-enrollment-profile | Get Manual Enrollment Profile
[**list_blueprints**](BlueprintsApi.md#list_blueprints) | **GET** /api/v1/blueprints | List Blueprints
[**list_library_items**](BlueprintsApi.md#list_library_items) | **GET** /api/v1/blueprints/{blueprint_id}/list-library-items | List Library Items
[**remove_library_item**](BlueprintsApi.md#remove_library_item) | **POST** /api/v1/blueprints/{blueprint_id}/remove-library-item | Remove Library Item
[**update_blueprint**](BlueprintsApi.md#update_blueprint) | **PATCH** /api/v1/blueprints/{blueprint_id} | Update Blueprint


# **assign_library_item**
> object assign_library_item(blueprint_id, body=body)

Assign Library Item

This endpoint allows assigning a library item to a specific blueprint (classic and maps). The response will include a list of library item IDs assigned to the blueprint.   ### Request Parameters   `blueprint_id` (path parameter): The unique identifier of the blueprint.   ### Request Body   * `library_item_id` (string, required) * `assignment_node_id` (string, required for maps)     + Note: To find the assignment\\_node\\_id, view the map in a browser. Then, on your keyboard, press and hold the Option ⌥ key. Each node ID remains fixed for the lifespan of the node on the map.   ### Error responses      | **Code** | **Body** | | --- | --- | | 400 \\- Bad Request | Bad Request | |  | 'Library Item already exists on Blueprint' | |  | 'Library Item already exists in Assignment Node' | |  | 'assignment\\_node\\_id cannot be provided for Classic Blueprint' | |  | 'Must provide assignment\\_node\\ _id for Assignment Map Blueprint' |

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Assign Library Item
        api_response = api_instance.assign_library_item(blueprint_id, body=body)
        print("The response of BlueprintsApi->assign_library_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->assign_library_item: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_blueprint**
> object create_blueprint(enrollment_code_code, enrollment_code_is_active, name, source_id, source_type, type)

Create Blueprint

This request creates a new empty Blueprint or a new Blueprint from a template. The keys `name` and `enrollment_code` `is_active` are required, and the blueprint name key must be unique from the existing blueprint names in the Kandji tenant.   optionally, `type: map` can be used when creating a new Assignment Map blueprint.   Note: If cloning an existing blueprint,\\ `type\\` value and the type of sourced (\\`source.id\\`) blueprint must match and \\`source.type\\` value must be set to \\`blueprint\\`.

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    enrollment_code_code = 'enrollment_code_code_example' # str | Optionally, set the enrollment code of the Blueprint. This key is not required. If an enrollment code is not supplied in the payload body, it will be randomly generated. The enrollment code will be returned in the response and visible in the Web app.
    enrollment_code_is_active = 'enrollment_code_is_active_example' # str | (required) Enable or Disable the Blueprint for manual device enrollment from the enrollment portal
    name = 'name_example' # str | (required) Set the name of the Blueprint. The name provided must be unique.
    source_id = 'source_id_example' # str | Set either the source template ID, or the source Blueprint ID to clone an existing template or blueprint.
    source_type = 'source_type_example' # str | Set the source to create the blueprint from. Possible options: `template` and `blueprint`.
    type = 'type_example' # str | Choose the type of blueprint to create. Options: `classic` or `map`

    try:
        # Create Blueprint
        api_response = api_instance.create_blueprint(enrollment_code_code, enrollment_code_is_active, name, source_id, source_type, type)
        print("The response of BlueprintsApi->create_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->create_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_code_code** | **str**| Optionally, set the enrollment code of the Blueprint. This key is not required. If an enrollment code is not supplied in the payload body, it will be randomly generated. The enrollment code will be returned in the response and visible in the Web app. | 
 **enrollment_code_is_active** | **str**| (required) Enable or Disable the Blueprint for manual device enrollment from the enrollment portal | 
 **name** | **str**| (required) Set the name of the Blueprint. The name provided must be unique. | 
 **source_id** | **str**| Set either the source template ID, or the source Blueprint ID to clone an existing template or blueprint. | 
 **source_type** | **str**| Set the source to create the blueprint from. Possible options: &#x60;template&#x60; and &#x60;blueprint&#x60;. | 
 **type** | **str**| Choose the type of blueprint to create. Options: &#x60;classic&#x60; or &#x60;map&#x60; | 

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

# **delete_blueprint**
> delete_blueprint(blueprint_id)

Delete Blueprint

**WARNING!** ============   This is a HIGHLY destructive action.    Deleting a Blueprint will un\\-manage ALL devices assigned to the Blueprint.    ### Request Parameters   `blueprint_id` (path parameter): The unique identifier of the blueprint.

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 

    try:
        # Delete Blueprint
        api_instance.delete_blueprint(blueprint_id)
    except Exception as e:
        print("Exception when calling BlueprintsApi->delete_blueprint: %s\n" % e)
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

# **get_blueprint**
> get_blueprint(blueprint_id)

Get Blueprint

This request returns information about a specific blueprint based on blueprint ID.   ### Request Parameters   `blueprint_id` (path parameter): The unique identifier of the blueprint.

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 

    try:
        # Get Blueprint
        api_instance.get_blueprint(blueprint_id)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_blueprint: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    limit = '100' # str | Number of results to return per page. (optional)
    offset = '400' # str | The initial index from which to return the results. (optional)

    try:
        # Get Blueprint Templates
        api_instance.get_blueprint_templates(limit=limit, offset=offset)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_blueprint_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Number of results to return per page. | [optional] 
 **offset** | **str**| The initial index from which to return the results. | [optional] 

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

# **get_manual_enrollment_profile**
> str get_manual_enrollment_profile(blueprint_id, sso=sso)

Get Manual Enrollment Profile

This request returns the manual enrollment profile (.mobileconfig file) for a specified Blueprint.   This request will return the enrollment profile even if 'Require Authentication' is configured for the Blueprint in Manual Enrollment.   The enrollment profile will be returned in raw form with response headers:   * `Content-Type` \\= `application/x-apple-aspen-config`  * `Content-Disposition` \\= `attachment;filename=kandji-enroll.mobileconfig`    An optional query parameter `sso=true` can be used to return a URL for SSO authentication instead. If this query parameter is used for a Blueprint that does not require authentication, then the enrollment profile will be returned.   ### Request Parameters   `blueprint_id` (path parameter): The unique identifier of the blueprint.

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    sso = 'true' # str | Use the \\`sso\\` query parameter, set to \\`true\\`, to return a URL instead of the manual enrollment profile. This parameter should only be used for blueprints in which 'Require Authentication' is configured for Manual Enrollment. The returned URL must be used to authenticate via SSO to receive an enrollment profile. (optional)

    try:
        # Get Manual Enrollment Profile
        api_response = api_instance.get_manual_enrollment_profile(blueprint_id, sso=sso)
        print("The response of BlueprintsApi->get_manual_enrollment_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_manual_enrollment_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 
 **sso** | **str**| Use the \\&#x60;sso\\&#x60; query parameter, set to \\&#x60;true\\&#x60;, to return a URL instead of the manual enrollment profile. This parameter should only be used for blueprints in which &#39;Require Authentication&#39; is configured for Manual Enrollment. The returned URL must be used to authenticate via SSO to receive an enrollment profile. | [optional] 

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
**200** | OK |  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Allow -  <br>  * Connection -  <br>  * Content-Disposition -  <br>  * Content-Language -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * Via -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * X-Served-By -  <br>  * X-Timer -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blueprints**
> object list_blueprints(id=id, id__in=id__in, name=name, limit=limit, offset=offset)

List Blueprints

This request returns a list of a blueprint records in the Kandji tenant. Optional query parameters can be specified to filter the results.

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    id = '97e4e175-1631-43f6-a02b-33fd1c748ab8' # str | Look up a specific Blueprint by its ID (optional)
    id__in = '11f4eb9a-10ed-4c3d-a7c1-fb87f95743fb,6391086e-85a1-4820-813c-f9c75025fff4' # str | Specify a list of Blueprint IDs to limit the results to. Multiple values may be separated by commas. There is a double underscore (\\`\\_\\_\\`) between id and in (optional)
    name = 'testing_blueprint' # str | Return Blueprint names 'containing' the specified search string. (optional)
    limit = '100' # str | Number of results to return per page. (optional)
    offset = '400' # str | The initial index from which to return the results. (optional)

    try:
        # List Blueprints
        api_response = api_instance.list_blueprints(id=id, id__in=id__in, name=name, limit=limit, offset=offset)
        print("The response of BlueprintsApi->list_blueprints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->list_blueprints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Look up a specific Blueprint by its ID | [optional] 
 **id__in** | **str**| Specify a list of Blueprint IDs to limit the results to. Multiple values may be separated by commas. There is a double underscore (\\&#x60;\\_\\_\\&#x60;) between id and in | [optional] 
 **name** | **str**| Return Blueprint names &#39;containing&#39; the specified search string. | [optional] 
 **limit** | **str**| Number of results to return per page. | [optional] 
 **offset** | **str**| The initial index from which to return the results. | [optional] 

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

# **list_library_items**
> object list_library_items(blueprint_id)

List Library Items

This API endpoint retrieves a list of library items associated with a specific blueprint. (classic and maps). Requires that the blueprint ID is passed as a path parameter in the URL.   ### Request Parameters    `blueprint_id` (path parameter): The unique identifier of the blueprint.    ### Response fields   * `count` (int): The total count of library items.  * `next` (str): The URL for the next page of results, if available. If not available will value will be `null`. * `previous` (str): The URL for the previous page of results, if available. If not available will value will be `null`. * `results` (object): An array containing objects with the following fields:    + `id` (str): The ID of the library item.  + `name` (str): The name of the library item.

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 

    try:
        # List Library Items
        api_response = api_instance.list_library_items(blueprint_id)
        print("The response of BlueprintsApi->list_library_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->list_library_items: %s\n" % e)
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
**200** | OK |  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Allow -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * Via -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * X-Served-By -  <br>  * X-Timer -  <br>  * transfer-encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_library_item**
> object remove_library_item(blueprint_id, body=body)

Remove Library Item

This endpoint allows removing a library item from a specific blueprint (classic and maps). The response will include a list of library item IDs assigned to the blueprint.   ### Request Parameters   `blueprint_id` (path parameter): The unique identifier of the blueprint.   ### Request Body   * `library_item_id` (string, required) * `assignment_node_id` (string, required for maps)    ### Error responses     | **Code** | **Body** | | --- | --- | | 400 \\- Bad Request | Bad Request | |  | 'assignment\\_node\\_id cannot be provided for Classic Blueprint' | |  | 'Must provide assignment\\_node\\_id for Assignment Map Blueprint' | |  | 'Library Item does not exist on Blueprint' | |  | 'Library Item does not exist in Assignment Node' |

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Remove Library Item
        api_response = api_instance.remove_library_item(blueprint_id, body=body)
        print("The response of BlueprintsApi->remove_library_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->remove_library_item: %s\n" % e)
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
**200** | OK |  * Allow -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_blueprint**
> object update_blueprint(blueprint_id, description, enrollment_code_code, enrollment_code_is_active, name)

Update Blueprint

This requests allows updating of the name, icon, icon color, description, enrollment code, and active status on an existing blueprint.   ### Request Parameters   `blueprint_id` (path parameter): The unique identifier of the blueprint.

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    description = 'description_example' # str | Update the description of the Blueprint
    enrollment_code_code = 'enrollment_code_code_example' # str | Update the enrollment code of the Blueprint
    enrollment_code_is_active = 'enrollment_code_is_active_example' # str | Disable the Blueprint for manual device enrollment from the enrollment portal.
    name = 'name_example' # str | Update the name of the Blueprint

    try:
        # Update Blueprint
        api_response = api_instance.update_blueprint(blueprint_id, description, enrollment_code_code, enrollment_code_is_active, name)
        print("The response of BlueprintsApi->update_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->update_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 
 **description** | **str**| Update the description of the Blueprint | 
 **enrollment_code_code** | **str**| Update the enrollment code of the Blueprint | 
 **enrollment_code_is_active** | **str**| Disable the Blueprint for manual device enrollment from the enrollment portal. | 
 **name** | **str**| Update the name of the Blueprint | 

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
**200** | OK |  * Allow -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  * Date -  <br>  * Feature-Policy -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

