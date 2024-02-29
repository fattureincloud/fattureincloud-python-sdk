# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.0.32
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.event_type import EventType
from fattureincloud_python_sdk.models.webhooks_subscription_config import (
    WebhooksSubscriptionConfig,
)
from typing import Optional, Set
from typing_extensions import Self


class WebhooksSubscription(BaseModel):
    """
    WebhooksSubscription
    """  # noqa: E501

    id: Optional[StrictStr] = Field(
        default=None, description="Webhooks subscription id"
    )
    sink: Optional[StrictStr] = Field(
        default=None, description="Webhooks callback uri."
    )
    verified: Optional[StrictBool] = Field(
        default=None,
        description="[Read Only] True if the webhooks subscription has been verified.",
    )
    types: Optional[List[EventType]] = Field(
        default=None, description="Webhooks events types."
    )
    config: Optional[WebhooksSubscriptionConfig] = None
    __properties: ClassVar[List[str]] = ["id", "sink", "verified", "types", "config"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WebhooksSubscription from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict["config"] = self.config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhooksSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "sink": obj.get("sink"),
                "verified": obj.get("verified"),
                "types": obj.get("types"),
                "config": (
                    WebhooksSubscriptionConfig.from_dict(obj["config"])
                    if obj.get("config") is not None
                    else None
                ),
            }
        )
        return _obj
