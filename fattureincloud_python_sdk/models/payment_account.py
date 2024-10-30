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
from fattureincloud_python_sdk.models.payment_account_type import PaymentAccountType
from typing import Optional, Set
from typing_extensions import Self


class PaymentAccount(BaseModel):
    """
    PaymentAccount
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Payment account id")
    name: Optional[StrictStr] = Field(default=None, description="Payment account name")
    type: Optional[PaymentAccountType] = PaymentAccountType.STANDARD
    iban: Optional[StrictStr] = Field(default=None, description="Payment account iban")
    sia: Optional[StrictStr] = Field(default=None, description="Payment account sia")
    cuc: Optional[StrictStr] = Field(default=None, description="Payment account cuc")
    virtual: Optional[StrictBool] = Field(
        default=None, description="Payment method is virtual"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "type",
        "iban",
        "sia",
        "cuc",
        "virtual",
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
        """Create an instance of PaymentAccount from a JSON string"""
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
        """Create an instance of PaymentAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "type": (
                    obj.get("type")
                    if obj.get("type") is not None
                    else PaymentAccountType.STANDARD
                ),
                "iban": obj.get("iban"),
                "sia": obj.get("sia"),
                "cuc": obj.get("cuc"),
                "virtual": obj.get("virtual"),
            }
        )
        return _obj
