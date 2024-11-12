# coding: utf-8

"""
    Kandji API

    <html><head></head><body><h1 id=&quot;welcome-to-the-kandji-api-documentation&quot;>Welcome to the Kandji API Documentation</h1> <p>You can find your API URL in Settings &gt; Access. The API URL will follow the below formats.</p> <ul> <li><p>US - <code>https://SubDomain.api.kandji.io</code></p> </li> <li><p>EU - <code>https://SubDomain.api.eu.kandji.io</code></p>  </li> </ul> <p>For information on how to obtain an API token, please refer to the following support article.</p> <p><a href=&quot;https://support.kandji.io/api&quot;>https://support.kandji.io/api</a></p>  <h4 id=&quot;rate-limit&quot;>Rate Limit</h4> <p>The Kandji API currently has an API rate limit of 10,000 requests per hour per customer.</p> <h4 id=&quot;request-methods&quot;>Request Methods</h4> <p>HTTP request methods supported by the Kandji API.</p> <div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table> <thead> <tr> <th>Method</th> <th>Definition</th>  </tr> </thead> <tbody> <tr> <td>GET</td> <td>The <code>GET</code> method requests a representation of the specified resource.</td> </tr> <tr> <td>POST</td>  <td>The <code>POST</code> method submits an entity to the specified resource.</td>  </tr> <tr> <td>PATCH</td> <td>The <code>PATCH</code> method applies partial modifications to a resource.</td> </tr> <tr> <td>DELETE</td> <td>The <code>DELETE</code> method deletes the specified resource.</td> </tr> </tbody> </table> </div><h4 id=&quot;response-codes&quot;>Response codes</h4> <p>Not all response codes apply to every endpoint.</p> <div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table>  <thead> <tr> <th>Code</th> <th>Response</th> </tr> </thead> <tbody> <tr>  <td>200</td> <td>OK</td> </tr> <tr> <td>201</td> <td>Created</td> </tr>  <tr> <td>204</td> <td>No content</td> </tr> <tr> <td></td> <td>Typical response when sending the DELETE method.</td> </tr> <tr> <td>400</td> <td>Bad Request</td>  </tr> <tr> <td></td> <td>&quot;Command already running&quot; - The command may already be running in a <em>Pending</em> state waiting on the device.</td>  </tr> <tr> <td></td> <td>&quot;Command is not allowed for current device&quot; - The command may not be compatible with the target device.</td> </tr> <tr>  <td></td> <td>&quot;JSON parse error - Expecting ',' delimiter: line 3 column 2 (char 65)&quot;</td> </tr> <tr> <td>401</td> <td>Unauthorized</td> </tr>  <tr> <td></td> <td>This error can occur if the token is incorrect, was revoked, or the token has expired.</td> </tr> <tr> <td>403</td> <td>Forbidden</td>  </tr> <tr> <td></td> <td>The request was understood but cannot be authorized.</td>  </tr> <tr> <td>404</td> <td>Not found</td> </tr> <tr> <td></td> <td>Unable to locate the resource in the Kandji tenant.</td> </tr> <tr> <td>415</td>  <td>Unsupported Media Type</td> </tr> <tr> <td></td> <td>The request contains a media type which the server or resource does not support.</td> </tr> <tr>  <td>500</td> <td>Internal server error</td> </tr> <tr> <td>503</td> <td>Service unavailable</td> </tr> <tr> <td></td> <td>This error can occur if a file upload is still being processed via the custom apps API.</td> </tr> </tbody> </table>  </div><h4 id=&quot;data-structure&quot;>Data structure</h4> <p>The API returns all structured responses in JSON schema format.</p> <h4 id=&quot;examples&quot;>Examples</h4>  <p>Code examples using the API can be found in the Kandji support <a href=&quot;https://github.com/kandji-inc/support/tree/main/api-tools&quot;>GitHub</a>.</p> </body></html>

    The version of the OpenAPI document: 1.0.0
    Contact: mitchelsblake@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kandji_python_sdk.api.blueprints_api import BlueprintsApi


class TestBlueprintsApi(unittest.TestCase):
    """BlueprintsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BlueprintsApi()

    def tearDown(self) -> None:
        pass

    def test_assign_library_item(self) -> None:
        """Test case for assign_library_item

        Assign Library Item
        """
        pass

    def test_create_blueprint(self) -> None:
        """Test case for create_blueprint

        Create Blueprint
        """
        pass

    def test_delete_blueprint(self) -> None:
        """Test case for delete_blueprint

        Delete Blueprint
        """
        pass

    def test_get_blueprint(self) -> None:
        """Test case for get_blueprint

        Get Blueprint
        """
        pass

    def test_get_blueprint_templates(self) -> None:
        """Test case for get_blueprint_templates

        Get Blueprint Templates
        """
        pass

    def test_get_manual_enrollment_profile(self) -> None:
        """Test case for get_manual_enrollment_profile

        Get Manual Enrollment Profile
        """
        pass

    def test_list_blueprints(self) -> None:
        """Test case for list_blueprints

        List Blueprints
        """
        pass

    def test_list_library_items(self) -> None:
        """Test case for list_library_items

        List Library Items
        """
        pass

    def test_remove_library_item(self) -> None:
        """Test case for remove_library_item

        Remove Library Item
        """
        pass

    def test_update_blueprint(self) -> None:
        """Test case for update_blueprint

        Update Blueprint
        """
        pass


if __name__ == '__main__':
    unittest.main()
