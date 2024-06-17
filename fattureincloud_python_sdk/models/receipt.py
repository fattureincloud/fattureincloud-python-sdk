# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.1.0
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.receipt_items_list_item import (
    ReceiptItemsListItem,
)
from fattureincloud_python_sdk.models.receipt_type import ReceiptType
from typing import Optional, Set
from typing_extensions import Self


class Receipt(BaseModel):
    """
    Receipt
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Receipt id")
    var_date: Optional[date] = Field(
        default=None, description="Receipt date", alias="date"
    )
    number: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Receipt number"
    )
    numeration: Optional[StrictStr] = Field(
        default=None, description="Receipt numeration"
    )
    amount_net: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Receipt total net amount"
    )
    amount_vat: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Receipt total vat amount"
    )
    amount_gross: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Receipt total gross amount"
    )
    use_gross_prices: Optional[StrictBool] = Field(
        default=None, description="Receipt uses gross prices"
    )
    type: Optional[ReceiptType] = None
    description: Optional[StrictStr] = Field(
        default=None, description="Receipt description"
    )
    rc_center: Optional[StrictStr] = Field(
        default=None, description="Receipt revenue center"
    )
    created_at: Optional[StrictStr] = Field(
        default=None, description="Receipt creation date"
    )
    updated_at: Optional[StrictStr] = Field(
        default=None, description="Receipt last update date"
    )
    payment_account: Optional[PaymentAccount] = None
    items_list: Optional[List[ReceiptItemsListItem]] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "date",
        "number",
        "numeration",
        "amount_net",
        "amount_vat",
        "amount_gross",
        "use_gross_prices",
        "type",
        "description",
        "rc_center",
        "created_at",
        "updated_at",
        "payment_account",
        "items_list",
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
        """Create an instance of Receipt from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items_list (list)
        _items = []
        if self.items_list:
            for _item in self.items_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["items_list"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Receipt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "date": obj.get("date"),
                "number": obj.get("number"),
                "numeration": obj.get("numeration"),
                "amount_net": obj.get("amount_net"),
                "amount_vat": obj.get("amount_vat"),
                "amount_gross": obj.get("amount_gross"),
                "use_gross_prices": obj.get("use_gross_prices"),
                "type": obj.get("type"),
                "description": obj.get("description"),
                "rc_center": obj.get("rc_center"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "payment_account": (
                    PaymentAccount.from_dict(obj["payment_account"])
                    if obj.get("payment_account") is not None
                    else None
                ),
                "items_list": (
                    [
                        ReceiptItemsListItem.from_dict(_item)
                        for _item in obj["items_list"]
                    ]
                    if obj.get("items_list") is not None
                    else None
                ),
            }
        )
        return _obj
