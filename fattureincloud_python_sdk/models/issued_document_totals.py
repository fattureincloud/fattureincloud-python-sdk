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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self


class IssuedDocumentTotals(BaseModel):
    """
    IssuedDocumentTotals
    """  # noqa: E501

    amount_net: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document total net amount"
    )
    amount_rivalsa: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document rivalsa amount"
    )
    amount_net_with_rivalsa: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document net amount with rivalsa"
    )
    amount_cassa: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document cassa amount"
    )
    taxable_amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document taxable amount"
    )
    not_taxable_amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document not taxable amount"
    )
    amount_vat: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document total vat amount"
    )
    amount_gross: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document total gross amount"
    )
    taxable_amount_withholding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document Taxable withholding tax amount"
    )
    amount_withholding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document withholding tax amount"
    )
    taxable_amount_other_withholding_tax: Optional[Union[StrictFloat, StrictInt]] = (
        Field(
            default=None,
            description="Issued document other withholding tax taxable amount",
        )
    )
    amount_other_withholding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document other withholding tax amount"
    )
    stamp_duty: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document stamp duty value [0 if not present]."
    )
    amount_due: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document total amount due"
    )
    is_enasarco_maximal_exceeded: Optional[StrictBool] = Field(
        default=None, description="Is enasarco maximal excedeed"
    )
    payments_sum: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document payments sum"
    )
    vat_list: Optional[Dict[str, Dict[str, Any]]] = None
    __properties: ClassVar[List[str]] = [
        "amount_net",
        "amount_rivalsa",
        "amount_net_with_rivalsa",
        "amount_cassa",
        "taxable_amount",
        "not_taxable_amount",
        "amount_vat",
        "amount_gross",
        "taxable_amount_withholding_tax",
        "amount_withholding_tax",
        "taxable_amount_other_withholding_tax",
        "amount_other_withholding_tax",
        "stamp_duty",
        "amount_due",
        "is_enasarco_maximal_exceeded",
        "payments_sum",
        "vat_list",
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
        """Create an instance of IssuedDocumentTotals from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in vat_list (dict)
        _field_dict = {}
        if self.vat_list:
            for _key_vat_list in self.vat_list:
                if self.vat_list[_key_vat_list]:
                    _field_dict[_key_vat_list] = self.vat_list[_key_vat_list].to_dict()
            _dict["vat_list"] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssuedDocumentTotals from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "amount_net": obj.get("amount_net"),
                "amount_rivalsa": obj.get("amount_rivalsa"),
                "amount_net_with_rivalsa": obj.get("amount_net_with_rivalsa"),
                "amount_cassa": obj.get("amount_cassa"),
                "taxable_amount": obj.get("taxable_amount"),
                "not_taxable_amount": obj.get("not_taxable_amount"),
                "amount_vat": obj.get("amount_vat"),
                "amount_gross": obj.get("amount_gross"),
                "taxable_amount_withholding_tax": obj.get(
                    "taxable_amount_withholding_tax"
                ),
                "amount_withholding_tax": obj.get("amount_withholding_tax"),
                "taxable_amount_other_withholding_tax": obj.get(
                    "taxable_amount_other_withholding_tax"
                ),
                "amount_other_withholding_tax": obj.get("amount_other_withholding_tax"),
                "stamp_duty": obj.get("stamp_duty"),
                "amount_due": obj.get("amount_due"),
                "is_enasarco_maximal_exceeded": obj.get("is_enasarco_maximal_exceeded"),
                "payments_sum": obj.get("payments_sum"),
                "vat_list": (
                    dict(
                        (_k, VatItem.from_dict(_v))
                        for _k, _v in obj["vat_list"].items()
                    )
                    if obj.get("vat_list") is not None
                    else None
                ),
            }
        )
        return _obj
