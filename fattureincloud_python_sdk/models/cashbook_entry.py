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

from datetime import date
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from fattureincloud_python_sdk.models.cashbook_entry_document import (
    CashbookEntryDocument,
)
from fattureincloud_python_sdk.models.cashbook_entry_kind import CashbookEntryKind
from fattureincloud_python_sdk.models.cashbook_entry_type import CashbookEntryType
from fattureincloud_python_sdk.models.payment_account import PaymentAccount


class CashbookEntry(BaseModel):
    """
    CashbookEntry
    """

    id: Optional[StrictStr] = Field(default=None, description="Cashbook id")
    var_date: Optional[date] = Field(
        default=None, description="Cashbook date", alias="date"
    )
    description: Optional[StrictStr] = Field(
        default=None, description="Cashbook description"
    )
    kind: Optional[CashbookEntryKind] = None
    type: Optional[CashbookEntryType] = None
    entity_name: Optional[StrictStr] = Field(
        default=None, description="Cashbook entity name"
    )
    document: Optional[CashbookEntryDocument] = None
    amount_in: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="[Only for cashbook entry in] Cashbook total amount in",
    )
    payment_account_in: Optional[PaymentAccount] = None
    amount_out: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="[Only for cashbook entry out] Cashbook total amount out",
    )
    payment_account_out: Optional[PaymentAccount] = None
    __properties = [
        "id",
        "date",
        "description",
        "kind",
        "type",
        "entity_name",
        "document",
        "amount_in",
        "payment_account_in",
        "amount_out",
        "payment_account_out",
    ]

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
    def from_json(cls, json_str: str) -> CashbookEntry:
        """Create an instance of CashbookEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of document
        if self.document:
            _dict["document"] = self.document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_account_in
        if self.payment_account_in:
            _dict["payment_account_in"] = self.payment_account_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_account_out
        if self.payment_account_out:
            _dict["payment_account_out"] = self.payment_account_out.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CashbookEntry:
        """Create an instance of CashbookEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CashbookEntry.parse_obj(obj)

        _obj = CashbookEntry.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "var_date": obj.get("date") if obj.get("date") is not None else None,
                "description": obj.get("description")
                if obj.get("description") is not None
                else None,
                "kind": obj.get("kind"),
                "type": obj.get("type"),
                "entity_name": obj.get("entity_name")
                if obj.get("entity_name") is not None
                else None,
                "document": CashbookEntryDocument.from_dict(obj.get("document"))
                if obj.get("document") is not None
                else None,
                "amount_in": float(obj.get("amount_in"))
                if obj.get("amount_in") is not None
                else None,
                "payment_account_in": PaymentAccount.from_dict(
                    obj.get("payment_account_in")
                )
                if obj.get("payment_account_in") is not None
                else None,
                "amount_out": float(obj.get("amount_out"))
                if obj.get("amount_out") is not None
                else None,
                "payment_account_out": PaymentAccount.from_dict(
                    obj.get("payment_account_out")
                )
                if obj.get("payment_account_out") is not None
                else None,
            }
        )
        return _obj
