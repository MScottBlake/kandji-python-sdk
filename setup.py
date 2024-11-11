# coding: utf-8

"""
    Kandji API

    Welcome to the Kandji API Documentation =======================================    You can find your API URL in Settings \\> Access. The API URL will follow the below formats.   * US \\- `https://SubDomain.api.kandji.io` * EU \\- `https://SubDomain.api.eu.kandji.io`    For information on how to obtain an API token, please refer to the following support article.   <https://support.kandji.io/api>   #### Rate Limit    The Kandji API currently has an API rate limit of 10,000 requests per hour per customer.   #### Request Methods   HTTP request methods supported by the Kandji API.     | Method | Definition | | --- | --- | | GET | The `GET` method requests a representation of the specified resource. | | POST | The `POST` method submits an entity to the specified resource. | | PATCH | The `PATCH` method applies partial modifications to a resource. | | DELETE | The `DELETE` method deletes the specified resource. |   #### Response codes   Not all response codes apply to every endpoint.     | Code | Response | | --- | --- | | 200 | OK | | 201 | Created | | 204 | No content | |  | Typical response when sending the DELETE method. | | 400 | Bad Request | |  | 'Command already running' \\- The command may already be running in a *Pending* state waiting on the device. | |  | 'Command is not allowed for current device' \\- The command may not be compatible with the target device. | |  | 'JSON parse error \\- Expecting ',' delimiter: line 3 column 2 (char 65\\)' | | 401 | Unauthorized | |  | This error can occur if the token is incorrect, was revoked, or the token has expired. |  | 403 | Forbidden | |  | The request was understood but cannot be authorized. | | 404 | Not found | |  | Unable to locate the resource in the Kandji tenant. | | 415 | Unsupported Media Type | |  | The request contains a media type which the server or resource does not support. | | 500 | Internal server error |  | 503 | Service unavailable | |  | This error can occur if a file upload is still being processed via the custom apps API. |   #### Data structure   The API returns all structured responses in JSON schema format.   #### Examples    Code examples using the API can be found in the Kandji support [GitHub](https://github.com/kandji-inc/support/tree/main/api-tools).

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "kandji-python-sdk"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Kandji API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Kandji API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Welcome to the Kandji API Documentation &#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;    You can find your API URL in Settings \\&gt; Access. The API URL will follow the below formats.   * US \\- &#x60;https://SubDomain.api.kandji.io&#x60; * EU \\- &#x60;https://SubDomain.api.eu.kandji.io&#x60;    For information on how to obtain an API token, please refer to the following support article.   &lt;https://support.kandji.io/api&gt;   #### Rate Limit    The Kandji API currently has an API rate limit of 10,000 requests per hour per customer.   #### Request Methods   HTTP request methods supported by the Kandji API.     | Method | Definition | | --- | --- | | GET | The &#x60;GET&#x60; method requests a representation of the specified resource. | | POST | The &#x60;POST&#x60; method submits an entity to the specified resource. | | PATCH | The &#x60;PATCH&#x60; method applies partial modifications to a resource. | | DELETE | The &#x60;DELETE&#x60; method deletes the specified resource. |   #### Response codes   Not all response codes apply to every endpoint.     | Code | Response | | --- | --- | | 200 | OK | | 201 | Created | | 204 | No content | |  | Typical response when sending the DELETE method. | | 400 | Bad Request | |  | &#39;Command already running&#39; \\- The command may already be running in a *Pending* state waiting on the device. | |  | &#39;Command is not allowed for current device&#39; \\- The command may not be compatible with the target device. | |  | &#39;JSON parse error \\- Expecting &#39;,&#39; delimiter: line 3 column 2 (char 65\\)&#39; | | 401 | Unauthorized | |  | This error can occur if the token is incorrect, was revoked, or the token has expired. |  | 403 | Forbidden | |  | The request was understood but cannot be authorized. | | 404 | Not found | |  | Unable to locate the resource in the Kandji tenant. | | 415 | Unsupported Media Type | |  | The request contains a media type which the server or resource does not support. | | 500 | Internal server error |  | 503 | Service unavailable | |  | This error can occur if a file upload is still being processed via the custom apps API. |   #### Data structure   The API returns all structured responses in JSON schema format.   #### Examples    Code examples using the API can be found in the Kandji support [GitHub](https://github.com/kandji-inc/support/tree/main/api-tools).
    """,  # noqa: E501
    package_data={"kandji_python_sdk": ["py.typed"]},
)