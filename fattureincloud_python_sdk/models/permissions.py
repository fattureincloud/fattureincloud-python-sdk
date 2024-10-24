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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.permission_level import PermissionLevel
from fattureincloud_python_sdk.models.permissions_fic_issued_documents_detailed import (
    PermissionsFicIssuedDocumentsDetailed,
)
from typing import Optional, Set
from typing_extensions import Self


class Permissions(BaseModel):
    """ """  # noqa: E501

    fic_situation: Optional[PermissionLevel] = None
    fic_clients: Optional[PermissionLevel] = None
    fic_suppliers: Optional[PermissionLevel] = None
    fic_products: Optional[PermissionLevel] = None
    fic_issued_documents: Optional[PermissionLevel] = None
    fic_received_documents: Optional[PermissionLevel] = None
    fic_receipts: Optional[PermissionLevel] = None
    fic_calendar: Optional[PermissionLevel] = None
    fic_archive: Optional[PermissionLevel] = None
    fic_taxes: Optional[PermissionLevel] = None
    fic_stock: Optional[PermissionLevel] = None
    fic_cashbook: Optional[PermissionLevel] = None
    fic_settings: Optional[PermissionLevel] = None
    fic_emails: Optional[PermissionLevel] = None
    fic_export: Optional[PermissionLevel] = None
    fic_import_bankstatements: Optional[PermissionLevel] = None
    fic_import_clients_suppliers: Optional[PermissionLevel] = None
    fic_import_issued_documents: Optional[PermissionLevel] = None
    fic_import_products: Optional[PermissionLevel] = None
    fic_recurring: Optional[PermissionLevel] = None
    fic_riba: Optional[PermissionLevel] = None
    dic_employees: Optional[PermissionLevel] = None
    dic_settings: Optional[PermissionLevel] = None
    dic_timesheet: Optional[PermissionLevel] = None
    fic_issued_documents_detailed: Optional[PermissionsFicIssuedDocumentsDetailed] = (
        None
    )
    __properties: ClassVar[List[str]] = [
        "fic_situation",
        "fic_clients",
        "fic_suppliers",
        "fic_products",
        "fic_issued_documents",
        "fic_received_documents",
        "fic_receipts",
        "fic_calendar",
        "fic_archive",
        "fic_taxes",
        "fic_stock",
        "fic_cashbook",
        "fic_settings",
        "fic_emails",
        "fic_export",
        "fic_import_bankstatements",
        "fic_import_clients_suppliers",
        "fic_import_issued_documents",
        "fic_import_products",
        "fic_recurring",
        "fic_riba",
        "dic_employees",
        "dic_settings",
        "dic_timesheet",
        "fic_issued_documents_detailed",
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
        """Create an instance of Permissions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fic_issued_documents_detailed
        if self.fic_issued_documents_detailed:
            _dict["fic_issued_documents_detailed"] = (
                self.fic_issued_documents_detailed.to_dict()
            )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Permissions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "fic_situation": obj.get("fic_situation"),
                "fic_clients": obj.get("fic_clients"),
                "fic_suppliers": obj.get("fic_suppliers"),
                "fic_products": obj.get("fic_products"),
                "fic_issued_documents": obj.get("fic_issued_documents"),
                "fic_received_documents": obj.get("fic_received_documents"),
                "fic_receipts": obj.get("fic_receipts"),
                "fic_calendar": obj.get("fic_calendar"),
                "fic_archive": obj.get("fic_archive"),
                "fic_taxes": obj.get("fic_taxes"),
                "fic_stock": obj.get("fic_stock"),
                "fic_cashbook": obj.get("fic_cashbook"),
                "fic_settings": obj.get("fic_settings"),
                "fic_emails": obj.get("fic_emails"),
                "fic_export": obj.get("fic_export"),
                "fic_import_bankstatements": obj.get("fic_import_bankstatements"),
                "fic_import_clients_suppliers": obj.get("fic_import_clients_suppliers"),
                "fic_import_issued_documents": obj.get("fic_import_issued_documents"),
                "fic_import_products": obj.get("fic_import_products"),
                "fic_recurring": obj.get("fic_recurring"),
                "fic_riba": obj.get("fic_riba"),
                "dic_employees": obj.get("dic_employees"),
                "dic_settings": obj.get("dic_settings"),
                "dic_timesheet": obj.get("dic_timesheet"),
                "fic_issued_documents_detailed": (
                    PermissionsFicIssuedDocumentsDetailed.from_dict(
                        obj["fic_issued_documents_detailed"]
                    )
                    if obj.get("fic_issued_documents_detailed") is not None
                    else None
                ),
            }
        )
        return _obj
