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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.company_type import CompanyType
from fattureincloud_python_sdk.models.controlled_company import ControlledCompany
from fattureincloud_python_sdk.models.fatture_in_cloud_plan_type import (
    FattureInCloudPlanType,
)
from typing import Optional, Set
from typing_extensions import Self


class Company(BaseModel):
    """
    Company
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Company id")
    name: Optional[StrictStr] = Field(default=None, description="Company name")
    type: Optional[CompanyType] = None
    access_token: Optional[StrictStr] = Field(
        default=None,
        description="Company authentication token for this company. [Only if type=company]",
    )
    controlled_companies: Optional[List[ControlledCompany]] = Field(
        default=None,
        description="Company list of controlled companies [Only if type=accountant]",
    )
    fic_license_expire: Optional[date] = None
    fic_plan: Optional[FattureInCloudPlanType] = None
    connection_id: Optional[StrictInt] = Field(
        default=None, description="Company connection id"
    )
    tax_code: Optional[StrictStr] = Field(default=None, description="Company tax code")
    vat_number: Optional[StrictStr] = Field(
        default=None, description="Company vat number"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "type",
        "access_token",
        "controlled_companies",
        "fic_license_expire",
        "fic_plan",
        "connection_id",
        "tax_code",
        "vat_number",
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
        """Create an instance of Company from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in controlled_companies (list)
        _items = []
        if self.controlled_companies:
            for _item_controlled_companies in self.controlled_companies:
                if _item_controlled_companies:
                    _items.append(_item_controlled_companies.to_dict())
            _dict["controlled_companies"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Company from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "type": obj.get("type"),
                "access_token": obj.get("access_token"),
                "controlled_companies": (
                    [
                        ControlledCompany.from_dict(_item)
                        for _item in obj["controlled_companies"]
                    ]
                    if obj.get("controlled_companies") is not None
                    else None
                ),
                "fic_license_expire": obj.get("fic_license_expire"),
                "fic_plan": obj.get("fic_plan"),
                "connection_id": obj.get("connection_id"),
                "tax_code": obj.get("tax_code"),
                "vat_number": obj.get("vat_number"),
            }
        )
        return _obj
