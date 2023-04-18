# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.27
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from fattureincloud_python_sdk.models.company_info_access_info import (
    CompanyInfoAccessInfo,
)
from fattureincloud_python_sdk.models.company_info_plan_info import CompanyInfoPlanInfo
from fattureincloud_python_sdk.models.company_type import CompanyType


class CompanyInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(None, description="Company unique identifier.")
    name: Optional[StrictStr] = Field(None, description="Company name.")
    email: Optional[StrictStr] = Field(None, description="Company email.")
    type: Optional[CompanyType] = None
    access_info: Optional[CompanyInfoAccessInfo] = None
    plan_info: Optional[CompanyInfoPlanInfo] = None
    accountant_id: Optional[StrictInt] = Field(
        None, description="Accountant unique identifier."
    )
    is_accountant: Optional[StrictBool] = Field(
        None, description="Determine if the logged account is an accountant."
    )
    __properties = [
        "id",
        "name",
        "email",
        "type",
        "access_info",
        "plan_info",
        "accountant_id",
        "is_accountant",
    ]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CompanyInfo:
        """Create an instance of CompanyInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of access_info
        if self.access_info:
            _dict["access_info"] = self.access_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan_info
        if self.plan_info:
            _dict["plan_info"] = self.plan_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompanyInfo:
        """Create an instance of CompanyInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CompanyInfo.parse_obj(obj)

        _obj = CompanyInfo.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "name": obj.get("name") if obj.get("name") is not None else None,
                "email": obj.get("email") if obj.get("email") is not None else None,
                "type": obj.get("type"),
                "access_info": CompanyInfoAccessInfo.from_dict(obj.get("access_info"))
                if obj.get("access_info") is not None
                else None,
                "plan_info": CompanyInfoPlanInfo.from_dict(obj.get("plan_info"))
                if obj.get("plan_info") is not None
                else None,
                "accountant_id": obj.get("accountant_id")
                if obj.get("accountant_id") is not None
                else None,
                "is_accountant": obj.get("is_accountant")
                if obj.get("is_accountant") is not None
                else None,
            }
        )
        return _obj
