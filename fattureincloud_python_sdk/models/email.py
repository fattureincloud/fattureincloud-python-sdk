# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.1.0
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.email_attachment import EmailAttachment
from fattureincloud_python_sdk.models.email_recipient_status import EmailRecipientStatus
from fattureincloud_python_sdk.models.email_status import EmailStatus
from typing import Optional, Set
from typing_extensions import Self


class Email(BaseModel):
    """
    Email
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Email id")
    status: Optional[EmailStatus] = None
    sent_date: Optional[datetime] = Field(default=None, description="Email sent date")
    errors_count: Optional[StrictInt] = Field(
        default=None, description="Email errors count"
    )
    error_log: Optional[StrictStr] = Field(default=None, description="Email errors log")
    from_email: Optional[StrictStr] = Field(
        default=None, description="Email sender email"
    )
    from_name: Optional[StrictStr] = Field(
        default=None, description="Email sender name"
    )
    to_email: Optional[StrictStr] = Field(
        default=None, description="Email recipient email"
    )
    to_name: Optional[StrictStr] = Field(
        default=None, description="Email receipient name"
    )
    subject: Optional[StrictStr] = Field(default=None, description="Email subject")
    content: Optional[StrictStr] = Field(default=None, description="Email content")
    copy_to: Optional[StrictStr] = Field(default=None, description="Email cc")
    recipient_status: Optional[EmailRecipientStatus] = None
    recipient_date: Optional[datetime] = Field(
        default=None, description="Email recipient date"
    )
    kind: Optional[StrictStr] = Field(default=None, description="Email kind")
    attachments: Optional[List[EmailAttachment]] = Field(
        default=None, description="Email attachments"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "status",
        "sent_date",
        "errors_count",
        "error_log",
        "from_email",
        "from_name",
        "to_email",
        "to_name",
        "subject",
        "content",
        "copy_to",
        "recipient_status",
        "recipient_date",
        "kind",
        "attachments",
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
        """Create an instance of Email from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict["attachments"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Email from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "status": obj.get("status"),
                "sent_date": obj.get("sent_date"),
                "errors_count": obj.get("errors_count"),
                "error_log": obj.get("error_log"),
                "from_email": obj.get("from_email"),
                "from_name": obj.get("from_name"),
                "to_email": obj.get("to_email"),
                "to_name": obj.get("to_name"),
                "subject": obj.get("subject"),
                "content": obj.get("content"),
                "copy_to": obj.get("copy_to"),
                "recipient_status": obj.get("recipient_status"),
                "recipient_date": obj.get("recipient_date"),
                "kind": obj.get("kind"),
                "attachments": (
                    [EmailAttachment.from_dict(_item) for _item in obj["attachments"]]
                    if obj.get("attachments") is not None
                    else None
                ),
            }
        )
        return _obj
