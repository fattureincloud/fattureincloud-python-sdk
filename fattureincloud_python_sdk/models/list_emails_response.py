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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.email import Email
from typing import Optional, Set
from typing_extensions import Self


class ListEmailsResponse(BaseModel):
    """
    ListEmailsResponse
    """  # noqa: E501

    current_page: Optional[StrictInt] = Field(
        default=None, description="Current page number."
    )
    first_page_url: Optional[StrictStr] = Field(
        default=None, description="First page url."
    )
    var_from: Optional[StrictInt] = Field(
        default=None, description="First result of the page.", alias="from"
    )
    last_page: Optional[StrictInt] = Field(
        default=None, description="Last page number."
    )
    last_page_url: Optional[StrictStr] = Field(
        default=None, description="Last page url."
    )
    next_page_url: Optional[StrictStr] = Field(
        default=None, description="Next page url"
    )
    path: Optional[StrictStr] = Field(default=None, description="Request path.")
    per_page: Optional[StrictInt] = Field(
        default=None, description="Number of result per page."
    )
    prev_page_url: Optional[StrictStr] = Field(
        default=None, description="Previous page url."
    )
    to: Optional[StrictInt] = Field(
        default=None, description="Last result of the page."
    )
    total: Optional[StrictInt] = Field(
        default=None, description="Total number of results"
    )
    data: Optional[List[Email]] = None
    __properties: ClassVar[List[str]] = [
        "current_page",
        "first_page_url",
        "from",
        "last_page",
        "last_page_url",
        "next_page_url",
        "path",
        "per_page",
        "prev_page_url",
        "to",
        "total",
        "data",
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
        """Create an instance of ListEmailsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict["data"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListEmailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "current_page": obj.get("current_page"),
                "first_page_url": obj.get("first_page_url"),
                "from": obj.get("from"),
                "last_page": obj.get("last_page"),
                "last_page_url": obj.get("last_page_url"),
                "next_page_url": obj.get("next_page_url"),
                "path": obj.get("path"),
                "per_page": obj.get("per_page"),
                "prev_page_url": obj.get("prev_page_url"),
                "to": obj.get("to"),
                "total": obj.get("total"),
                "data": (
                    [Email.from_dict(_item) for _item in obj["data"]]
                    if obj.get("data") is not None
                    else None
                ),
            }
        )
        return _obj
