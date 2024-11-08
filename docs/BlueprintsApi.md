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
**200** | OK |  * Date -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  |

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    name = 'name_example' # str | <p>(required) Set the name of the Blueprint. The name provided must be unique.</p> 
    enrollment_code_is_active = 'enrollment_code_is_active_example' # str | <p>(required) Enable or Disable the Blueprint for manual device enrollment from the enrollment portal</p> 
    enrollment_code_code = 'enrollment_code_code_example' # str | <p>Optionally, set the enrollment code of the Blueprint. This key is not required. If an enrollment code is not supplied in the payload body, it will be randomly generated. The enrollment code will be returned in the response and visible in the Web app.</p> 
    source_type = 'source_type_example' # str | <p>Set the source to create the blueprint from. Possible options: <code>template</code> and <code>blueprint</code>.</p> 
    source_id = 'source_id_example' # str | <p>Set either the source template ID, or the source Blueprint ID to clone an existing template or blueprint.</p> 
    type = 'type_example' # str | <p>Choose the type of blueprint to create. Options: <code>classic</code> or <code>map</code></p> 

    try:
        # Create Blueprint
        api_response = api_instance.create_blueprint(name, enrollment_code_is_active, enrollment_code_code, source_type, source_id, type)
        print("The response of BlueprintsApi->create_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->create_blueprint: %s\n" % e)
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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    limit = '100' # str | <p>Number of results to return per page.</p>  (optional)
    offset = '400' # str | <p>The initial index from which to return the results.</p>  (optional)

    try:
        # Get Blueprint Templates
        api_instance.get_blueprint_templates(limit=limit, offset=offset)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_blueprint_templates: %s\n" % e)
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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    sso = 'true' # str | <p>Use the <code>sso</code> query parameter, set to <code>true</code>, to return a URL instead of the manual enrollment profile. This parameter should only be used for blueprints in which \"Require Authentication\" is configured for Manual Enrollment. The returned URL must be used to authenticate via SSO to receive an enrollment profile. </p>  (optional)

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    id = '97e4e175-1631-43f6-a02b-33fd1c748ab8' # str | <p>Look up a specific Blueprint by its ID</p>  (optional)
    id__in = '11f4eb9a-10ed-4c3d-a7c1-fb87f95743fb,6391086e-85a1-4820-813c-f9c75025fff4' # str | <p>Specify a list of Blueprint IDs to limit the results to.  Multiple values may be separated by commas. There is a double underscore (<code>__</code>) between id and in</p>  (optional)
    name = 'testing_blueprint' # str | <p>Return Blueprint names \"containing\" the specified search string.</p>  (optional)
    limit = '100' # str | <p>Number of results to return per page.</p>  (optional)
    offset = '400' # str | <p>The initial index from which to return the results.</p>  (optional)

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
**200** | OK |  * Connection -  <br>  * Content-Type -  <br>  * Allow -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Ratelimit-Limit -  <br>  * Ratelimit-Remaining -  <br>  * Ratelimit-Reset -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Via -  <br>  * X-Content-Type-Options -  <br>  * X-Frame-Options -  <br>  * X-Kong-Proxy-Latency -  <br>  * X-Kong-Upstream-Latency -  <br>  * X-Ratelimit-Limit-Hour -  <br>  * X-Ratelimit-Limit-Second -  <br>  * X-Ratelimit-Remaining-Hour -  <br>  * X-Ratelimit-Remaining-Second -  <br>  * Accept-Ranges -  <br>  * Access-Control-Allow-Origin -  <br>  * Date -  <br>  * X-Served-By -  <br>  * X-Cache -  <br>  * X-Cache-Hits -  <br>  * X-Timer -  <br>  * Vary -  <br>  * transfer-encoding -  <br>  |

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
**200** | OK |  * Date -  <br>  * Server -  <br>  * Allow -  <br>  * X-Frame-Options -  <br>  * Content-Length -  <br>  * X-Content-Type-Options -  <br>  * Referrer-Policy -  <br>  * Cross-Origin-Opener-Policy -  <br>  * Feature-Policy -  <br>  * Vary -  <br>  * Content-Security-Policy -  <br>  * Content-Type -  <br>  |

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
    api_instance = kandji_python_sdk.BlueprintsApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    name = 'name_example' # str | <p>Update the name of the Blueprint</p> 
    description = 'description_example' # str | <p>Update the description of the Blueprint </p> 
    enrollment_code_code = 'enrollment_code_code_example' # str | <p>Update the enrollment code of the Blueprint </p> 
    enrollment_code_is_active = 'enrollment_code_is_active_example' # str | <p>Disable the Blueprint for manual device enrollment from the enrollment portal.</p> 

    try:
        # Update Blueprint
        api_response = api_instance.update_blueprint(blueprint_id, name, description, enrollment_code_code, enrollment_code_is_active)
        print("The response of BlueprintsApi->update_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->update_blueprint: %s\n" % e)
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

