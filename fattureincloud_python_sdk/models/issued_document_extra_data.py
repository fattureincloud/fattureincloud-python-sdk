# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.28
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr


class IssuedDocumentExtraData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    show_sofort_button: Optional[StrictBool] = None
    multifatture_sent: Optional[StrictInt] = None
    ts_communication: Optional[StrictBool] = None
    ts_flag_tipo_spesa: Optional[StrictFloat] = Field(
        None,
        description="1 => TK (Ticket di pronto soccorso); 2 => SR (Visita in intramoenia)",
    )
    ts_pagamento_tracciato: Optional[StrictBool] = None
    ts_tipo_spesa: Optional[StrictStr] = Field(
        None,
        description="Can be [ 'TK', 'FC', 'FV', 'SV', 'SP', 'AD', 'AS', 'SR', 'CT', 'PI', 'IC', 'AA' ]. Refer to the technical specifications to learn more.",
    )
    ts_opposizione: Optional[StrictBool] = None
    ts_status: Optional[StrictInt] = None
    ts_file_id: Optional[StrictStr] = None
    ts_sent_date: Optional[date] = None
    ts_full_amount: Optional[StrictBool] = None
    imported_by: Optional[StrictStr] = None
    ts_single_sending: Optional[StrictBool] = None
    __properties = [
        "show_sofort_button",
        "multifatture_sent",
        "ts_communication",
        "ts_flag_tipo_spesa",
        "ts_pagamento_tracciato",
        "ts_tipo_spesa",
        "ts_opposizione",
        "ts_status",
        "ts_file_id",
        "ts_sent_date",
        "ts_full_amount",
        "imported_by",
        "ts_single_sending",
    ]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> IssuedDocumentExtraData:
        """Create an instance of IssuedDocumentExtraData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IssuedDocumentExtraData:
        """Create an instance of IssuedDocumentExtraData from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IssuedDocumentExtraData.parse_obj(obj)

        _obj = IssuedDocumentExtraData.parse_obj(
            {
                "show_sofort_button": obj.get("show_sofort_button")
                if obj.get("show_sofort_button") is not None
                else None,
                "multifatture_sent": obj.get("multifatture_sent")
                if obj.get("multifatture_sent") is not None
                else None,
                "ts_communication": obj.get("ts_communication")
                if obj.get("ts_communication") is not None
                else None,
                "ts_flag_tipo_spesa": float(obj.get("ts_flag_tipo_spesa"))
                if obj.get("ts_flag_tipo_spesa") is not None
                else None,
                "ts_pagamento_tracciato": obj.get("ts_pagamento_tracciato")
                if obj.get("ts_pagamento_tracciato") is not None
                else None,
                "ts_tipo_spesa": obj.get("ts_tipo_spesa")
                if obj.get("ts_tipo_spesa") is not None
                else None,
                "ts_opposizione": obj.get("ts_opposizione")
                if obj.get("ts_opposizione") is not None
                else None,
                "ts_status": obj.get("ts_status")
                if obj.get("ts_status") is not None
                else None,
                "ts_file_id": obj.get("ts_file_id")
                if obj.get("ts_file_id") is not None
                else None,
                "ts_sent_date": obj.get("ts_sent_date")
                if obj.get("ts_sent_date") is not None
                else None,
                "ts_full_amount": obj.get("ts_full_amount")
                if obj.get("ts_full_amount") is not None
                else None,
                "imported_by": obj.get("imported_by")
                if obj.get("imported_by") is not None
                else None,
                "ts_single_sending": obj.get("ts_single_sending")
                if obj.get("ts_single_sending") is not None
                else None,
            }
        )
        return _obj
