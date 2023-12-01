# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.0.30
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr


class DetailedCountry(BaseModel):
    """
    DetailedCountry
    """

    name: Optional[StrictStr] = Field(default=None, description="Country name")
    settings_name: Optional[StrictStr] = Field(
        default=None, description="Country settings name"
    )
    iso: Optional[StrictStr] = Field(default=None, description="Country iso code")
    fiscal_iso: Optional[StrictStr] = Field(
        default=None, description="Country fiscal iso code"
    )
    uic: Optional[StrictStr] = Field(default=None, description="Country uic")
    __properties = ["name", "settings_name", "iso", "fiscal_iso", "uic"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DetailedCountry:
        """Create an instance of DetailedCountry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DetailedCountry:
        """Create an instance of DetailedCountry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DetailedCountry.parse_obj(obj)

        _obj = DetailedCountry.parse_obj(
            {
                "name": obj.get("name") if obj.get("name") is not None else None,
                "settings_name": obj.get("settings_name")
                if obj.get("settings_name") is not None
                else None,
                "iso": obj.get("iso") if obj.get("iso") is not None else None,
                "fiscal_iso": obj.get("fiscal_iso")
                if obj.get("fiscal_iso") is not None
                else None,
                "uic": obj.get("uic") if obj.get("uic") is not None else None,
            }
        )
        return _obj
