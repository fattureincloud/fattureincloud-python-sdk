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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from fattureincloud_python_sdk.models.issued_document_payments_list_item_payment_terms import (
    IssuedDocumentPaymentsListItemPaymentTerms,
)
from fattureincloud_python_sdk.models.issued_document_status import IssuedDocumentStatus
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from typing import Optional, Set
from typing_extensions import Self


class IssuedDocumentPaymentsListItem(BaseModel):
    """
    IssuedDocumentPaymentsListItem
    """  # noqa: E501

    id: Optional[StrictInt] = Field(
        default=None, description="Issued document payment item id"
    )
    due_date: Optional[date] = Field(
        default=None, description="Issued document payment due date"
    )
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document payment amount"
    )
    status: Optional[IssuedDocumentStatus] = IssuedDocumentStatus.NOT_PAID
    payment_account: Optional[PaymentAccount] = None
    paid_date: Optional[date] = Field(
        default=None,
        description="Issued document payment date [Only if status is paid]",
    )
    ei_raw: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Issued document payment advanced raw attributes for e-invoices",
    )
    payment_terms: Optional[IssuedDocumentPaymentsListItemPaymentTerms] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "due_date",
        "amount",
        "status",
        "payment_account",
        "paid_date",
        "ei_raw",
        "payment_terms",
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
        """Create an instance of IssuedDocumentPaymentsListItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payment_account
        if self.payment_account:
            _dict["payment_account"] = self.payment_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_terms
        if self.payment_terms:
            _dict["payment_terms"] = self.payment_terms.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssuedDocumentPaymentsListItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "due_date": obj.get("due_date"),
                "amount": obj.get("amount"),
                "status": (
                    obj.get("status")
                    if obj.get("status") is not None
                    else IssuedDocumentStatus.NOT_PAID
                ),
                "payment_account": (
                    PaymentAccount.from_dict(obj["payment_account"])
                    if obj.get("payment_account") is not None
                    else None
                ),
                "paid_date": obj.get("paid_date"),
                "ei_raw": obj.get("ei_raw"),
                "payment_terms": (
                    IssuedDocumentPaymentsListItemPaymentTerms.from_dict(
                        obj["payment_terms"]
                    )
                    if obj.get("payment_terms") is not None
                    else None
                ),
            }
        )
        return _obj
