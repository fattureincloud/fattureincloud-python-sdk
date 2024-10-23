# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.1.2
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.currency import Currency
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.received_document_info_default_values import (
    ReceivedDocumentInfoDefaultValues,
)
from fattureincloud_python_sdk.models.received_document_info_items_default_values import (
    ReceivedDocumentInfoItemsDefaultValues,
)
from fattureincloud_python_sdk.models.vat_type import VatType
from typing import Optional, Set
from typing_extensions import Self


class ReceivedDocumentInfo(BaseModel):
    """
    ReceivedDocumentInfo
    """  # noqa: E501

    default_values: Optional[ReceivedDocumentInfoDefaultValues] = None
    items_default_values: Optional[ReceivedDocumentInfoItemsDefaultValues] = None
    countries_list: Optional[List[StrictStr]] = Field(
        default=None, description="Countries list"
    )
    currencies_list: Optional[List[Currency]] = Field(
        default=None, description="Currencies list"
    )
    categories_list: Optional[List[StrictStr]] = Field(
        default=None, description="Categories list"
    )
    payment_accounts_list: Optional[List[Optional[PaymentAccount]]] = Field(
        default=None, description="Payments accounts list"
    )
    vat_types_list: Optional[List[Optional[VatType]]] = Field(
        default=None, description="Vat types list"
    )
    __properties: ClassVar[List[str]] = [
        "default_values",
        "items_default_values",
        "countries_list",
        "currencies_list",
        "categories_list",
        "payment_accounts_list",
        "vat_types_list",
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
        """Create an instance of ReceivedDocumentInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default_values
        if self.default_values:
            _dict["default_values"] = self.default_values.to_dict()
        # override the default output from pydantic by calling `to_dict()` of items_default_values
        if self.items_default_values:
            _dict["items_default_values"] = self.items_default_values.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in currencies_list (list)
        _items = []
        if self.currencies_list:
            for _item_currencies_list in self.currencies_list:
                if _item_currencies_list:
                    _items.append(_item_currencies_list.to_dict())
            _dict["currencies_list"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payment_accounts_list (list)
        _items = []
        if self.payment_accounts_list:
            for _item_payment_accounts_list in self.payment_accounts_list:
                if _item_payment_accounts_list:
                    _items.append(_item_payment_accounts_list.to_dict())
            _dict["payment_accounts_list"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vat_types_list (list)
        _items = []
        if self.vat_types_list:
            for _item_vat_types_list in self.vat_types_list:
                if _item_vat_types_list:
                    _items.append(_item_vat_types_list.to_dict())
            _dict["vat_types_list"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReceivedDocumentInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "default_values": (
                    ReceivedDocumentInfoDefaultValues.from_dict(obj["default_values"])
                    if obj.get("default_values") is not None
                    else None
                ),
                "items_default_values": (
                    ReceivedDocumentInfoItemsDefaultValues.from_dict(
                        obj["items_default_values"]
                    )
                    if obj.get("items_default_values") is not None
                    else None
                ),
                "countries_list": obj.get("countries_list"),
                "currencies_list": (
                    [Currency.from_dict(_item) for _item in obj["currencies_list"]]
                    if obj.get("currencies_list") is not None
                    else None
                ),
                "categories_list": obj.get("categories_list"),
                "payment_accounts_list": (
                    [
                        PaymentAccount.from_dict(_item)
                        for _item in obj["payment_accounts_list"]
                    ]
                    if obj.get("payment_accounts_list") is not None
                    else None
                ),
                "vat_types_list": (
                    [VatType.from_dict(_item) for _item in obj["vat_types_list"]]
                    if obj.get("vat_types_list") is not None
                    else None
                ),
            }
        )
        return _obj
