# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.0.31
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from fattureincloud_python_sdk.models.document_template import DocumentTemplate
from fattureincloud_python_sdk.models.payment_method import PaymentMethod

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class IssuedDocumentPreCreateInfoDefaultValues(BaseModel):
    """
    Issued document default values
    """  # noqa: E501

    default_template: Optional[DocumentTemplate] = None
    dn_template: Optional[DocumentTemplate] = None
    ai_template: Optional[DocumentTemplate] = None
    notes: Optional[StrictStr] = Field(default=None, description="Default notes.")
    rivalsa: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Default rivalsa percentage."
    )
    cassa: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Default cassa percentage."
    )
    withholding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Default withholding tax percentage."
    )
    withholding_tax_taxable: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Default withholding tax taxable percentage."
    )
    other_withholding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Default other withholding tax percentage."
    )
    use_gross_prices: Optional[StrictBool] = Field(
        default=None, description="Use gross price by default."
    )
    payment_method: Optional[PaymentMethod] = None
    __properties: ClassVar[List[str]] = [
        "default_template",
        "dn_template",
        "ai_template",
        "notes",
        "rivalsa",
        "cassa",
        "withholding_tax",
        "withholding_tax_taxable",
        "other_withholding_tax",
        "use_gross_prices",
        "payment_method",
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
        """Create an instance of IssuedDocumentPreCreateInfoDefaultValues from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default_template
        if self.default_template:
            _dict["default_template"] = self.default_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dn_template
        if self.dn_template:
            _dict["dn_template"] = self.dn_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ai_template
        if self.ai_template:
            _dict["ai_template"] = self.ai_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict["payment_method"] = self.payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IssuedDocumentPreCreateInfoDefaultValues from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "default_template": DocumentTemplate.from_dict(
                    obj.get("default_template")
                )
                if obj.get("default_template") is not None
                else None,
                "dn_template": DocumentTemplate.from_dict(obj.get("dn_template"))
                if obj.get("dn_template") is not None
                else None,
                "ai_template": DocumentTemplate.from_dict(obj.get("ai_template"))
                if obj.get("ai_template") is not None
                else None,
                "notes": obj.get("notes"),
                "rivalsa": obj.get("rivalsa"),
                "cassa": obj.get("cassa"),
                "withholding_tax": obj.get("withholding_tax"),
                "withholding_tax_taxable": obj.get("withholding_tax_taxable"),
                "other_withholding_tax": obj.get("other_withholding_tax"),
                "use_gross_prices": obj.get("use_gross_prices"),
                "payment_method": PaymentMethod.from_dict(obj.get("payment_method"))
                if obj.get("payment_method") is not None
                else None,
            }
        )
        return _obj
