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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from fattureincloud_python_sdk.models.vat_type import VatType

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ReceiptItemsListItem(BaseModel):
    """
    ReceiptItemsListItem
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Receipt item id")
    amount_net: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Receipt item total net amount"
    )
    amount_gross: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Receipt item total gross amount"
    )
    category: Optional[StrictStr] = Field(
        default=None, description="Receipt item category"
    )
    vat: Optional[VatType] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "amount_net",
        "amount_gross",
        "category",
        "vat",
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReceiptItemsListItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of vat
        if self.vat:
            _dict["vat"] = self.vat.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ReceiptItemsListItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "amount_net": obj.get("amount_net"),
                "amount_gross": obj.get("amount_gross"),
                "category": obj.get("category"),
                "vat": VatType.from_dict(obj.get("vat"))
                if obj.get("vat") is not None
                else None,
            }
        )
        return _obj
