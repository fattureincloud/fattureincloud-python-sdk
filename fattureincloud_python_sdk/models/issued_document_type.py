# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.0.33
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class IssuedDocumentType(str, Enum):
    """
    Issued document type
    """

    """
    allowed enum values
    """
    INVOICE = "invoice"
    QUOTE = "quote"
    PROFORMA = "proforma"
    RECEIPT = "receipt"
    DELIVERY_NOTE = "delivery_note"
    CREDIT_NOTE = "credit_note"
    ORDER = "order"
    WORK_REPORT = "work_report"
    SUPPLIER_ORDER = "supplier_order"
    SELF_OWN_INVOICE = "self_own_invoice"
    SELF_SUPPLIER_INVOICE = "self_supplier_invoice"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IssuedDocumentType from a JSON string"""
        return cls(json.loads(json_str))
