# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.1.3
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.email_schedule_include import EmailScheduleInclude
from typing import Optional, Set
from typing_extensions import Self


class EmailSchedule(BaseModel):
    """
    EmailSchedule
    """  # noqa: E501

    sender_id: Optional[StrictInt] = Field(
        default=None,
        description="Email sender id [required if **sender_email** is not specified]",
    )
    sender_email: Optional[StrictStr] = Field(
        default=None,
        description="Email sender address [required if **sender_id** is not specified]",
    )
    recipient_email: Optional[StrictStr] = Field(
        default=None, description="Email recipient emails [comma separated]"
    )
    subject: Optional[StrictStr] = Field(default=None, description="Email subject")
    body: Optional[StrictStr] = Field(
        default=None, description="Email body [HTML Escaped] [max size 50KiB]"
    )
    include: Optional[EmailScheduleInclude] = None
    attach_pdf: Optional[StrictBool] = Field(
        default=None, description="Attach the pdf of the document"
    )
    send_copy: Optional[StrictBool] = Field(
        default=None,
        description="Send a copy of the email to the **cc_email** specified by **Get email data**",
    )
    __properties: ClassVar[List[str]] = [
        "sender_id",
        "sender_email",
        "recipient_email",
        "subject",
        "body",
        "include",
        "attach_pdf",
        "send_copy",
    ]

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
        """Create an instance of EmailSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of include
        if self.include:
            _dict["include"] = self.include.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmailSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "sender_id": obj.get("sender_id"),
                "sender_email": obj.get("sender_email"),
                "recipient_email": obj.get("recipient_email"),
                "subject": obj.get("subject"),
                "body": obj.get("body"),
                "include": (
                    EmailScheduleInclude.from_dict(obj["include"])
                    if obj.get("include") is not None
                    else None
                ),
                "attach_pdf": obj.get("attach_pdf"),
                "send_copy": obj.get("send_copy"),
            }
        )
        return _obj
