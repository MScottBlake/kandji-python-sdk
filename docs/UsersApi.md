# kandji.UsersApi

All URIs are relative to *https://&lt;sub_domain&gt;.api.kandji.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /api/v1/users/{user_id} | Delete User
[**get_user**](UsersApi.md#get_user) | **GET** /api/v1/users/{user_id} | Get User
[**list_users**](UsersApi.md#list_users) | **GET** /api/v1/users | List Users


# **delete_user**
> delete_user(user_id)

Delete User

<p>This endpoint makes a request to delete a specified user directory integration user by id (uuid).</p>
<h3 id=&quot;user-still-assigned-to-device&quot;>User still assigned to device</h3>
<p>You will see the following response (400 bad request), if a user is still assigned to one or more devices. The user will need to be unassigned from the device either manually through the UI in the web app or programatically using the Update device API endpoint.</p>
<pre class=&quot;click-to-expand-wrapper is-snippet-wrapper&quot;><code class=&quot;language-json&quot;>{
    &quot;detail&quot;: &quot;User still assigned to one or more devices.&quot;
}

</code></pre>

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
    api_instance = kandji.UsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Delete User
        api_instance.delete_user(user_id)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * Content-Type -  <br>  |
**400** | Bad Request |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UsersGetUser200Response get_user(user_id)

Get User

This endpoint makes a request to retrieve a specified user directory integration user by id.

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.users_get_user200_response import UsersGetUser200Response
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
    api_instance = kandji.UsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User
        api_response = api_instance.get_user(user_id)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UsersGetUser200Response**](UsersGetUser200Response.md)

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

# **list_users**
> AuditLogListAuditEvents200Response list_users(email=email, id=id, integration_id=integration_id, archived=archived, cursor=cursor)

List Users

<p>This endpoint makes a request to retrieve a list of users from user directory integrations.</p>
<p>A maximum of 300 records are returned per request, and pagination can be performed leveraging the URLs provided in the <code>next</code> and <code>previous</code> keys in the response. If there are no more results available, the respective key will be <code>null</code>.</p>

### Example

* Bearer (API Token) Authentication (bearer):

```python
import kandji
from kandji.models.audit_log_list_audit_events200_response import AuditLogListAuditEvents200Response
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
    api_instance = kandji.UsersApi(api_client)
    email = 'test_user_01@accuhive.io' # str | Returns users with email addresses containing the provided string. (optional)
    id = '69c009ca-1f78-4bdf-bb93-08d6d39041db' # str | Search for a user matching the provided UUID value. (optional)
    integration_id = 'f7461096-4ef9-43aa-88e9-ca1967ba0b38' # str | Search for a integration matching the provided UUID value. (optional)
    archived = 'false' # str | Return only users that are either archived (true) or not archived (false). Archived users are users that appear in the Users module under the Archived tab. (optional)
    cursor = '' # str | Cursor for the next or previous page of results. Can also store the URL in the next and previous fields in the response. (optional)

    try:
        # List Users
        api_response = api_instance.list_users(email=email, id=id, integration_id=integration_id, archived=archived, cursor=cursor)
        print("The response of UsersApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Returns users with email addresses containing the provided string. | [optional] 
 **id** | **str**| Search for a user matching the provided UUID value. | [optional] 
 **integration_id** | **str**| Search for a integration matching the provided UUID value. | [optional] 
 **archived** | **str**| Return only users that are either archived (true) or not archived (false). Archived users are users that appear in the Users module under the Archived tab. | [optional] 
 **cursor** | **str**| Cursor for the next or previous page of results. Can also store the URL in the next and previous fields in the response. | [optional] 

### Return type

[**AuditLogListAuditEvents200Response**](AuditLogListAuditEvents200Response.md)

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

