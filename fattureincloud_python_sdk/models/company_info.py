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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.company_info_access_info import (
    CompanyInfoAccessInfo,
)
from fattureincloud_python_sdk.models.company_info_plan_info import CompanyInfoPlanInfo
from fattureincloud_python_sdk.models.company_type import CompanyType
from fattureincloud_python_sdk.models.fatture_in_cloud_plan_type import (
    FattureInCloudPlanType,
)
from typing import Optional, Set
from typing_extensions import Self


class CompanyInfo(BaseModel):
    """
    CompanyInfo
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Company id")
    name: Optional[StrictStr] = Field(default=None, description="Company name")
    email: Optional[StrictStr] = Field(default=None, description="Company email")
    type: Optional[CompanyType] = None
    access_info: Optional[CompanyInfoAccessInfo] = None
    fic_license_expire: Optional[date] = None
    fic_plan_name: Optional[FattureInCloudPlanType] = None
    plan_info: Optional[CompanyInfoPlanInfo] = None
    accountant_id: Optional[StrictInt] = Field(
        default=None, description="Company accountant id"
    )
    is_accountant: Optional[StrictBool] = Field(
        default=None, description="Is the logged account an accountant."
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "email",
        "type",
        "access_info",
        "fic_license_expire",
        "fic_plan_name",
        "plan_info",
        "accountant_id",
        "is_accountant",
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
        """Create an instance of CompanyInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_info
        if self.access_info:
            _dict["access_info"] = self.access_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan_info
        if self.plan_info:
            _dict["plan_info"] = self.plan_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CompanyInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "email": obj.get("email"),
                "type": obj.get("type"),
                "access_info": (
                    CompanyInfoAccessInfo.from_dict(obj["access_info"])
                    if obj.get("access_info") is not None
                    else None
                ),
                "fic_license_expire": obj.get("fic_license_expire"),
                "fic_plan_name": obj.get("fic_plan_name"),
                "plan_info": (
                    CompanyInfoPlanInfo.from_dict(obj["plan_info"])
                    if obj.get("plan_info") is not None
                    else None
                ),
                "accountant_id": obj.get("accountant_id"),
                "is_accountant": obj.get("is_accountant"),
            }
        )
        return _obj
