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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from kandji.models.inline_object10_activation_lock import InlineObject10ActivationLock
from kandji.models.inline_object10_apple_business_manager import InlineObject10AppleBusinessManager
from kandji.models.inline_object10_automated_device_enrollment import InlineObject10AutomatedDeviceEnrollment
from kandji.models.inline_object10_cellular import InlineObject10Cellular
from kandji.models.inline_object10_filevault import InlineObject10Filevault
from kandji.models.inline_object10_general import InlineObject10General
from kandji.models.inline_object10_hardware_overview import InlineObject10HardwareOverview
from kandji.models.inline_object10_kandji_agent import InlineObject10KandjiAgent
from kandji.models.inline_object10_lost_mode import InlineObject10LostMode
from kandji.models.inline_object10_mdm import InlineObject10Mdm
from kandji.models.inline_object10_recovery_information import InlineObject10RecoveryInformation
from kandji.models.inline_object10_security_information import InlineObject10SecurityInformation
from kandji.models.inline_object10_users import InlineObject10Users
from typing import Optional, Set
from typing_extensions import Self

class InlineObject10(BaseModel):
    """
    InlineObject10
    """ # noqa: E501
    general: Optional[InlineObject10General] = None
    mdm: Optional[InlineObject10Mdm] = None
    activation_lock: Optional[InlineObject10ActivationLock] = None
    filevault: Optional[InlineObject10Filevault] = None
    lost_mode: Optional[InlineObject10LostMode] = None
    automated_device_enrollment: Optional[InlineObject10AutomatedDeviceEnrollment] = None
    kandji_agent: Optional[InlineObject10KandjiAgent] = None
    hardware_overview: Optional[InlineObject10HardwareOverview] = None
    volumes: Optional[Any] = None
    network: Optional[Dict[str, Any]] = None
    recovery_information: Optional[InlineObject10RecoveryInformation] = None
    users: Optional[InlineObject10Users] = None
    installed_profiles: Optional[Any] = None
    apple_business_manager: Optional[InlineObject10AppleBusinessManager] = None
    security_information: Optional[InlineObject10SecurityInformation] = None
    cellular: Optional[InlineObject10Cellular] = None
    tags: Optional[Any] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["general", "mdm", "activation_lock", "filevault", "lost_mode", "automated_device_enrollment", "kandji_agent", "hardware_overview", "volumes", "network", "recovery_information", "users", "installed_profiles", "apple_business_manager", "security_information", "cellular", "tags"]

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
        """Create an instance of InlineObject10 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of general
        if self.general:
            _dict['general'] = self.general.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mdm
        if self.mdm:
            _dict['mdm'] = self.mdm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of activation_lock
        if self.activation_lock:
            _dict['activation_lock'] = self.activation_lock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filevault
        if self.filevault:
            _dict['filevault'] = self.filevault.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lost_mode
        if self.lost_mode:
            _dict['lost_mode'] = self.lost_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of automated_device_enrollment
        if self.automated_device_enrollment:
            _dict['automated_device_enrollment'] = self.automated_device_enrollment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kandji_agent
        if self.kandji_agent:
            _dict['kandji_agent'] = self.kandji_agent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hardware_overview
        if self.hardware_overview:
            _dict['hardware_overview'] = self.hardware_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recovery_information
        if self.recovery_information:
            _dict['recovery_information'] = self.recovery_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of users
        if self.users:
            _dict['users'] = self.users.to_dict()
        # override the default output from pydantic by calling `to_dict()` of apple_business_manager
        if self.apple_business_manager:
            _dict['apple_business_manager'] = self.apple_business_manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security_information
        if self.security_information:
            _dict['security_information'] = self.security_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cellular
        if self.cellular:
            _dict['cellular'] = self.cellular.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if volumes (nullable) is None
        # and model_fields_set contains the field
        if self.volumes is None and "volumes" in self.model_fields_set:
            _dict['volumes'] = None

        # set to None if installed_profiles (nullable) is None
        # and model_fields_set contains the field
        if self.installed_profiles is None and "installed_profiles" in self.model_fields_set:
            _dict['installed_profiles'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InlineObject10 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "general": InlineObject10General.from_dict(obj["general"]) if obj.get("general") is not None else None,
            "mdm": InlineObject10Mdm.from_dict(obj["mdm"]) if obj.get("mdm") is not None else None,
            "activation_lock": InlineObject10ActivationLock.from_dict(obj["activation_lock"]) if obj.get("activation_lock") is not None else None,
            "filevault": InlineObject10Filevault.from_dict(obj["filevault"]) if obj.get("filevault") is not None else None,
            "lost_mode": InlineObject10LostMode.from_dict(obj["lost_mode"]) if obj.get("lost_mode") is not None else None,
            "automated_device_enrollment": InlineObject10AutomatedDeviceEnrollment.from_dict(obj["automated_device_enrollment"]) if obj.get("automated_device_enrollment") is not None else None,
            "kandji_agent": InlineObject10KandjiAgent.from_dict(obj["kandji_agent"]) if obj.get("kandji_agent") is not None else None,
            "hardware_overview": InlineObject10HardwareOverview.from_dict(obj["hardware_overview"]) if obj.get("hardware_overview") is not None else None,
            "volumes": obj.get("volumes"),
            "network": obj.get("network"),
            "recovery_information": InlineObject10RecoveryInformation.from_dict(obj["recovery_information"]) if obj.get("recovery_information") is not None else None,
            "users": InlineObject10Users.from_dict(obj["users"]) if obj.get("users") is not None else None,
            "installed_profiles": obj.get("installed_profiles"),
            "apple_business_manager": InlineObject10AppleBusinessManager.from_dict(obj["apple_business_manager"]) if obj.get("apple_business_manager") is not None else None,
            "security_information": InlineObject10SecurityInformation.from_dict(obj["security_information"]) if obj.get("security_information") is not None else None,
            "cellular": InlineObject10Cellular.from_dict(obj["cellular"]) if obj.get("cellular") is not None else None,
            "tags": obj.get("tags")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


