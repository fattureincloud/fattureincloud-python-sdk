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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class IssuedDocumentOptions(BaseModel):
    """
    IssuedDocumentOptions
    """  # noqa: E501

    fix_payments: Optional[StrictBool] = Field(
        default=None,
        description="Fixes your last payment amount to match your document total",
    )
    create_from: Optional[List[StrictStr]] = Field(
        default=None, description="Original documents ids [only for join/transform]"
    )
    transform: Optional[StrictBool] = Field(
        default=None, description="Tranform a document [only for transform]"
    )
    keep_copy: Optional[StrictBool] = Field(
        default=None, description="Keep original document [only for transform]"
    )
    join_type: Optional[StrictStr] = Field(
        default=None, description="Join type [only for join]"
    )
    __properties: ClassVar[List[str]] = [
        "fix_payments",
        "create_from",
        "transform",
        "keep_copy",
        "join_type",
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
        """Create an instance of IssuedDocumentOptions from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssuedDocumentOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "fix_payments": obj.get("fix_payments"),
                "create_from": obj.get("create_from"),
                "transform": obj.get("transform"),
                "keep_copy": obj.get("keep_copy"),
                "join_type": obj.get("join_type"),
            }
        )
        return _obj
