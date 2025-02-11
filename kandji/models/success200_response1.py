# coding: utf-8

"""
    Kandji API

    <html><head></head><body><h1 id=&quot;welcome-to-the-kandji-api-documentation&quot;>Welcome to the Kandji API Documentation</h1> <p>You can find your API URL in Settings &gt; Access. The API URL will follow the below formats.</p> <ul> <li><p>US - <code>https://SubDomain.api.kandji.io</code></p> </li> <li><p>EU - <code>https://SubDomain.api.eu.kandji.io</code></p> </li> </ul> <p>For information on how to obtain an API token, please refer to the following support article.</p> <p><a href=&quot;https://support.kandji.io/api&quot;>https://support.kandji.io/api</a></p> <h4 id=&quot;rate-limit&quot;>Rate Limit</h4> <p>The Kandji API currently has an API rate limit of 10,000 requests per hour per customer.</p> <h4 id=&quot;request-methods&quot;>Request Methods</h4> <p>HTTP request methods supported by the Kandji API.</p> <div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table> <thead> <tr> <th>Method</th> <th>Definition</th> </tr> </thead> <tbody> <tr> <td>GET</td> <td>The <code>GET</code> method requests a representation of the specified resource.</td> </tr> <tr> <td>POST</td> <td>The <code>POST</code> method submits an entity to the specified resource.</td> </tr> <tr> <td>PATCH</td> <td>The <code>PATCH</code> method applies partial modifications to a resource.</td> </tr> <tr> <td>DELETE</td> <td>The <code>DELETE</code> method deletes the specified resource.</td> </tr> </tbody> </table> </div><h4 id=&quot;response-codes&quot;>Response codes</h4> <p>Not all response codes apply to every endpoint.</p> <div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table> <thead> <tr> <th>Code</th> <th>Response</th> </tr> </thead> <tbody> <tr> <td>200</td> <td>OK</td> </tr> <tr> <td>201</td> <td>Created</td> </tr> <tr> <td>204</td> <td>No content</td> </tr> <tr> <td></td> <td>Typical response when sending the DELETE method.</td> </tr> <tr> <td>400</td> <td>Bad Request</td> </tr> <tr> <td></td> <td>&quot;Command already running&quot; - The command may already be running in a <em>Pending</em> state waiting on the device.</td> </tr> <tr> <td></td> <td>&quot;Command is not allowed for current device&quot; - The command may not be compatible with the target device.</td> </tr> <tr> <td></td> <td>&quot;JSON parse error - Expecting ',' delimiter: line 3 column 2 (char 65)&quot;</td> </tr> <tr> <td>401</td> <td>Unauthorized</td> </tr> <tr> <td></td> <td>This error can occur if the token is incorrect, was revoked, or the token has expired.</td> </tr> <tr> <td>403</td> <td>Forbidden</td> </tr> <tr> <td></td> <td>The request was understood but cannot be authorized.</td> </tr> <tr> <td>404</td> <td>Not found</td> </tr> <tr> <td></td> <td>Unable to locate the resource in the Kandji tenant.</td> </tr> <tr> <td>415</td> <td>Unsupported Media Type</td> </tr> <tr> <td></td> <td>The request contains a media type which the server or resource does not support.</td> </tr> <tr> <td>500</td> <td>Internal server error</td> </tr> <tr> <td>503</td> <td>Service unavailable</td> </tr> <tr> <td></td> <td>This error can occur if a file upload is still being processed via the custom apps API.</td> </tr> </tbody> </table> </div><h4 id=&quot;data-structure&quot;>Data structure</h4> <p>The API returns all structured responses in JSON schema format.</p> <h4 id=&quot;examples&quot;>Examples</h4> <p>Code examples using the API can be found in the Kandji support <a href=&quot;https://github.com/kandji-inc/support/tree/main/api-tools&quot;>GitHub</a>.</p> </body></html>

    The version of the OpenAPI document: 1.0.0
    Contact: mitchelsblake@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kandji.models.success200_response1_dep_account import Success200Response1DepAccount
from kandji.models.success200_response1_mdm_device import Success200Response1MdmDevice
from typing import Optional, Set
from typing_extensions import Self

class Success200Response1(BaseModel):
    """
    Success200Response1
    """ # noqa: E501
    blueprint_id: Optional[StrictStr] = None
    mdm_device: Optional[Success200Response1MdmDevice] = None
    user_id: Optional[StrictStr] = None
    dep_account: Optional[Success200Response1DepAccount] = None
    asset_tag: Optional[StrictStr] = None
    color: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    device_assigned_by: Optional[StrictStr] = None
    device_assigned_date: Optional[StrictStr] = None
    device_family: Optional[StrictStr] = None
    model: Optional[StrictStr] = None
    os: Optional[StrictStr] = None
    profile_assign_time: Optional[StrictStr] = None
    profile_push_time: Optional[StrictStr] = None
    profile_status: Optional[StrictStr] = None
    serial_number: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    last_assignment_status: Optional[StrictStr] = None
    failed_assignment_attempts: Optional[StrictInt] = None
    assignment_status_received_at: Optional[StrictStr] = None
    blueprint: Optional[StrictStr] = None
    user: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["blueprint_id", "mdm_device", "user_id", "dep_account", "asset_tag", "color", "description", "device_assigned_by", "device_assigned_date", "device_family", "model", "os", "profile_assign_time", "profile_push_time", "profile_status", "serial_number", "id", "last_assignment_status", "failed_assignment_attempts", "assignment_status_received_at", "blueprint", "user"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Success200Response1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of mdm_device
        if self.mdm_device:
            _dict['mdm_device'] = self.mdm_device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dep_account
        if self.dep_account:
            _dict['dep_account'] = self.dep_account.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Success200Response1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "blueprint_id": obj.get("blueprint_id"),
            "mdm_device": Success200Response1MdmDevice.from_dict(obj["mdm_device"]) if obj.get("mdm_device") is not None else None,
            "user_id": obj.get("user_id"),
            "dep_account": Success200Response1DepAccount.from_dict(obj["dep_account"]) if obj.get("dep_account") is not None else None,
            "asset_tag": obj.get("asset_tag"),
            "color": obj.get("color"),
            "description": obj.get("description"),
            "device_assigned_by": obj.get("device_assigned_by"),
            "device_assigned_date": obj.get("device_assigned_date"),
            "device_family": obj.get("device_family"),
            "model": obj.get("model"),
            "os": obj.get("os"),
            "profile_assign_time": obj.get("profile_assign_time"),
            "profile_push_time": obj.get("profile_push_time"),
            "profile_status": obj.get("profile_status"),
            "serial_number": obj.get("serial_number"),
            "id": obj.get("id"),
            "last_assignment_status": obj.get("last_assignment_status"),
            "failed_assignment_attempts": obj.get("failed_assignment_attempts"),
            "assignment_status_received_at": obj.get("assignment_status_received_at"),
            "blueprint": obj.get("blueprint"),
            "user": obj.get("user")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


