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
from typing import Any, Dict, List, Optional
from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
    conlist,
    validator,
)
from fattureincloud_python_sdk.models.currency import Currency
from fattureincloud_python_sdk.models.document_template import DocumentTemplate
from fattureincloud_python_sdk.models.entity import Entity
from fattureincloud_python_sdk.models.issued_document_ei_data import (
    IssuedDocumentEiData,
)
from fattureincloud_python_sdk.models.issued_document_extra_data import (
    IssuedDocumentExtraData,
)
from fattureincloud_python_sdk.models.issued_document_items_list_item import (
    IssuedDocumentItemsListItem,
)
from fattureincloud_python_sdk.models.issued_document_payments_list_item import (
    IssuedDocumentPaymentsListItem,
)
from fattureincloud_python_sdk.models.issued_document_type import IssuedDocumentType
from fattureincloud_python_sdk.models.language import Language
from fattureincloud_python_sdk.models.payment_method import PaymentMethod
from fattureincloud_python_sdk.models.show_totals_mode import ShowTotalsMode


class IssuedDocument(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(
        None, description="Unique identifier of the document."
    )
    entity: Optional[Entity] = None
    type: Optional[IssuedDocumentType] = None
    number: Optional[StrictInt] = Field(
        None,
        description="Number of the document [If not specified, next number is used]",
    )
    numeration: Optional[StrictStr] = Field(
        None,
        description="Numeration of the document [Not available if type=delivery_note]",
    )
    var_date: Optional[date] = Field(
        None,
        alias="date",
        description="Date of the document [If not specified, today date is used]",
    )
    year: Optional[StrictInt] = Field(None, description="Invoice year.")
    currency: Optional[Currency] = None
    language: Optional[Language] = None
    subject: Optional[StrictStr] = Field(None, description="Issued document subject.")
    visible_subject: Optional[StrictStr] = Field(
        None, description="Issued document visible subject."
    )
    rc_center: Optional[StrictStr] = Field(
        None, description="Revenue center [or cost center if type=supplier_order]."
    )
    notes: Optional[StrictStr] = Field(None, description="Issued document extra notes.")
    rivalsa: Optional[StrictFloat] = Field(
        None, description='"Rivalsa INPS" percentual value'
    )
    cassa: Optional[StrictFloat] = Field(
        None, description='"Cassa previdenziale" percentual value'
    )
    amount_cassa: Optional[StrictFloat] = Field(
        None, description="[Read Only] Cassa amount."
    )
    cassa_taxable: Optional[StrictFloat] = Field(
        None, description="Cassa taxable percentage"
    )
    amount_cassa_taxable: Optional[StrictFloat] = Field(
        None,
        description="[Can be set only if cassa_taxable is NULL] Cassa2 taxable amount",
    )
    cassa2: Optional[StrictFloat] = Field(
        None, description='"Cassa previdenziale 2" percentual value'
    )
    amount_cassa2: Optional[StrictFloat] = Field(
        None, description="[Read Only] Cassa amount."
    )
    cassa2_taxable: Optional[StrictFloat] = Field(
        None, description="Cassa2 taxable percentage"
    )
    amount_cassa2_taxable: Optional[StrictFloat] = Field(
        None,
        description="[Can be set only if cassa2_taxable is NULL] Cassa2 taxable amount",
    )
    global_cassa_taxable: Optional[StrictFloat] = Field(
        None, description="Global cassa taxable percentage"
    )
    amount_global_cassa_taxable: Optional[StrictFloat] = Field(
        None,
        description="[Can be set only if global_cassa_taxable is NULL] Global cassa taxable amount",
    )
    withholding_tax: Optional[StrictFloat] = Field(
        None, description="Withholding tax (ritenuta d'acconto) percentual value"
    )
    withholding_tax_taxable: Optional[StrictFloat] = Field(
        None, description="Withholding tax taxable (imponibile) percentual value"
    )
    other_withholding_tax: Optional[StrictFloat] = Field(
        None, description="Other withholding tax (altra ritenuta) percentual value"
    )
    stamp_duty: Optional[StrictFloat] = Field(
        None, description="Stamp duty value [0 if not present]"
    )
    payment_method: Optional[PaymentMethod] = None
    use_split_payment: Optional[StrictBool] = Field(
        None, description="Use split payment"
    )
    use_gross_prices: Optional[StrictBool] = Field(None, description="Use gross prices")
    e_invoice: Optional[StrictBool] = Field(
        None, description="Indicates if this is an e-invoice."
    )
    ei_data: Optional[IssuedDocumentEiData] = None
    ei_cassa_type: Optional[StrictStr] = Field(None, description="E-invoice cassa type")
    ei_cassa2_type: Optional[StrictStr] = Field(
        None, description="E-invoice cassa2 type"
    )
    ei_withholding_tax_causal: Optional[StrictStr] = Field(
        None, description="E-invoice withholding tax causal"
    )
    ei_other_withholding_tax_type: Optional[StrictStr] = Field(
        None, description="E-invoice other withholding tax type"
    )
    ei_other_withholding_tax_causal: Optional[StrictStr] = Field(
        None, description="E-invoice other withholding tax causal"
    )
    items_list: Optional[conlist(IssuedDocumentItemsListItem)] = None
    payments_list: Optional[conlist(IssuedDocumentPaymentsListItem)] = None
    template: Optional[DocumentTemplate] = None
    delivery_note_template: Optional[DocumentTemplate] = None
    acc_inv_template: Optional[DocumentTemplate] = None
    h_margins: Optional[StrictInt] = Field(None, description="Horizontal margins.")
    v_margins: Optional[StrictInt] = Field(None, description="Vertical margins.")
    show_payments: Optional[StrictBool] = Field(
        None, description="Shows the expiration dates of the payments on the document."
    )
    show_payment_method: Optional[StrictBool] = Field(
        None, description="Show the payment method details on the document."
    )
    show_totals: Optional[ShowTotalsMode] = None
    show_paypal_button: Optional[StrictBool] = Field(
        None, description="Show paypal button"
    )
    show_notification_button: Optional[StrictBool] = Field(
        None, description="Show notification button"
    )
    show_tspay_button: Optional[StrictBool] = Field(
        None, description="Show ts pay button."
    )
    delivery_note: Optional[StrictBool] = None
    accompanying_invoice: Optional[StrictBool] = Field(
        None, description="Attach an accompanying invoice."
    )
    dn_number: Optional[StrictInt] = Field(
        None, description="Number (for the attached delivery note)."
    )
    dn_date: Optional[date] = Field(
        None, description="Date (for the attached delivery note)."
    )
    dn_ai_packages_number: Optional[StrictStr] = Field(
        None, description="Number of packages (for the attached delivery note)."
    )
    dn_ai_weight: Optional[StrictStr] = Field(
        None, description="Weight (for the attached delivery note)."
    )
    dn_ai_causal: Optional[StrictStr] = Field(
        None, description="Causal (for the attached delivery note)."
    )
    dn_ai_destination: Optional[StrictStr] = Field(
        None, description="Destination (for the attached delivery note)."
    )
    dn_ai_transporter: Optional[StrictStr] = Field(
        None, description="Transporter (for the attached delivery note)."
    )
    dn_ai_notes: Optional[StrictStr] = Field(
        None, description="Notes (for the attached delivery note)."
    )
    is_marked: Optional[StrictBool] = Field(
        None, description="This is true if the document is marked."
    )
    amount_net: Optional[StrictFloat] = Field(
        None, description="[Read Only] Total net amount (competenze)."
    )
    amount_vat: Optional[StrictFloat] = Field(
        None, description="[Read Only] Total vat amount (IVA)."
    )
    amount_gross: Optional[StrictFloat] = Field(
        None, description="[Read Only] Total gross amount (totale documento)."
    )
    amount_due_discount: Optional[StrictFloat] = Field(
        None, description="Amount due discount"
    )
    amount_rivalsa: Optional[StrictFloat] = Field(
        None, description="[Read Only] Rivalsa amount."
    )
    amount_rivalsa_taxable: Optional[StrictFloat] = Field(
        None, description="Taxable rivalsa amount"
    )
    amount_withholding_tax: Optional[StrictFloat] = Field(
        None, description="[Read Only] Withholding tax amount (ritenuta d'acconto)."
    )
    amount_withholding_tax_taxable: Optional[StrictFloat] = Field(
        None, description="Taxable withholding tax amount"
    )
    amount_other_withholding_tax: Optional[StrictFloat] = Field(
        None, description="[Read Only] Other withholding tax amount (altra ritenuta)."
    )
    amount_other_withholding_tax_taxable: Optional[StrictFloat] = Field(
        None, description="Taxable other withholding tax amount"
    )
    amount_enasarco_taxable: Optional[StrictFloat] = Field(
        None, description="Taxable enasarco amount"
    )
    extra_data: Optional[IssuedDocumentExtraData] = None
    seen_date: Optional[date] = Field(
        None, description="Date when the client/supplier has seen the document."
    )
    next_due_date: Optional[date] = Field(
        None, description="Date of the next not paid payment."
    )
    url: Optional[StrictStr] = Field(
        None,
        description="[Temporary] [Read Only]   Public url of the document PDF file.",
    )
    dn_url: Optional[StrictStr] = Field(
        None,
        description="[Temporary] [Read Only]   Public url of the attached delivery note PDF file.",
    )
    ai_url: Optional[StrictStr] = Field(
        None,
        description="[Temporary] [Read Only]   Public url of the accompanying invoice PDF file.",
    )
    attachment_url: Optional[StrictStr] = Field(
        None,
        description="[Temporary] [Read Only] Public url of the attached file. Authomatically set if a valid attachment token is passed via POST /issued_documents or PUT /issued_documents/{documentId}.",
    )
    attachment_token: Optional[StrictStr] = Field(
        None,
        description="[Write Only] Attachment token returned by POST /issued_documents/attachment. Used to attach the file already uploaded.",
    )
    ei_raw: Optional[Dict[str, Any]] = Field(
        None, description="Advanced raw attributes for e-invoices."
    )
    ei_status: Optional[StrictStr] = Field(
        None,
        description="[Read only] Status of the e-invoice.   * `attempt` - We are trying to send the invoice, please wait up to 2 hours   * `missing` - The invoice is missing   * `not_sent` - The invoice has yet to be sent   * `sent` - The invoice was sent   * `pending` - The checks for the digital signature and sending are in progress   * `processing` - The SDI is delivering the invoice to the customer   * `error` - An error occurred while handling the invoice, please try to resend it or contact support   * `discarded` - The invoice has been rejected by the SDI, so it must be corrected and re-sent   * `not_delivered` - The SDI was unable to deliver the invoice   * `accepted` - The customer accepted the invoice   * `rejected` - The customer rejected the invoice, so it must be corrected   * `no_response` - A response has not yet been received whithin the deadline, contact the customer to ascertain the status of the invoice   * `manual_accepted` - The customer accepted the invoice   * `manual_rejected` - The customer rejected the invoice ",
    )
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties = [
        "id",
        "entity",
        "type",
        "number",
        "numeration",
        "date",
        "year",
        "currency",
        "language",
        "subject",
        "visible_subject",
        "rc_center",
        "notes",
        "rivalsa",
        "cassa",
        "amount_cassa",
        "cassa_taxable",
        "amount_cassa_taxable",
        "cassa2",
        "amount_cassa2",
        "cassa2_taxable",
        "amount_cassa2_taxable",
        "global_cassa_taxable",
        "amount_global_cassa_taxable",
        "withholding_tax",
        "withholding_tax_taxable",
        "other_withholding_tax",
        "stamp_duty",
        "payment_method",
        "use_split_payment",
        "use_gross_prices",
        "e_invoice",
        "ei_data",
        "ei_cassa_type",
        "ei_cassa2_type",
        "ei_withholding_tax_causal",
        "ei_other_withholding_tax_type",
        "ei_other_withholding_tax_causal",
        "items_list",
        "payments_list",
        "template",
        "delivery_note_template",
        "acc_inv_template",
        "h_margins",
        "v_margins",
        "show_payments",
        "show_payment_method",
        "show_totals",
        "show_paypal_button",
        "show_notification_button",
        "show_tspay_button",
        "delivery_note",
        "accompanying_invoice",
        "dn_number",
        "dn_date",
        "dn_ai_packages_number",
        "dn_ai_weight",
        "dn_ai_causal",
        "dn_ai_destination",
        "dn_ai_transporter",
        "dn_ai_notes",
        "is_marked",
        "amount_net",
        "amount_vat",
        "amount_gross",
        "amount_due_discount",
        "amount_rivalsa",
        "amount_rivalsa_taxable",
        "amount_withholding_tax",
        "amount_withholding_tax_taxable",
        "amount_other_withholding_tax",
        "amount_other_withholding_tax_taxable",
        "amount_enasarco_taxable",
        "extra_data",
        "seen_date",
        "next_due_date",
        "url",
        "dn_url",
        "ai_url",
        "attachment_url",
        "attachment_token",
        "ei_raw",
        "ei_status",
        "created_at",
        "updated_at",
    ]

    @validator("ei_status")
    def ei_status_validate_enum(cls, v):
        if v is None:
            return v

        if v not in (
            "attempt",
            "missing",
            "not_sent",
            "sent",
            "pending",
            "processing",
            "error",
            "discarded",
            "not_delivered",
            "accepted",
            "rejected",
            "no_response",
            "manual_accepted",
            "manual_rejected",
        ):
            raise ValueError(
                "must validate the enum values ('attempt', 'missing', 'not_sent', 'sent', 'pending', 'processing', 'error', 'discarded', 'not_delivered', 'accepted', 'rejected', 'no_response', 'manual_accepted', 'manual_rejected')"
            )
        return v

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
    def from_json(cls, json_str: str) -> IssuedDocument:
        """Create an instance of IssuedDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "amount_cassa",
                "amount_cassa2",
                "amount_net",
                "amount_vat",
                "amount_gross",
                "amount_rivalsa",
                "amount_withholding_tax",
                "amount_other_withholding_tax",
                "attachment_url",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of entity
        if self.entity:
            _dict["entity"] = self.entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict["currency"] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of language
        if self.language:
            _dict["language"] = self.language.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict["payment_method"] = self.payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ei_data
        if self.ei_data:
            _dict["ei_data"] = self.ei_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items_list (list)
        _items = []
        if self.items_list:
            for _item in self.items_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["items_list"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payments_list (list)
        _items = []
        if self.payments_list:
            for _item in self.payments_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["payments_list"] = _items
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict["template"] = self.template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delivery_note_template
        if self.delivery_note_template:
            _dict["delivery_note_template"] = self.delivery_note_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of acc_inv_template
        if self.acc_inv_template:
            _dict["acc_inv_template"] = self.acc_inv_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extra_data
        if self.extra_data:
            _dict["extra_data"] = self.extra_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IssuedDocument:
        """Create an instance of IssuedDocument from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IssuedDocument.parse_obj(obj)

        _obj = IssuedDocument.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "entity": Entity.from_dict(obj.get("entity"))
                if obj.get("entity") is not None
                else None,
                "type": obj.get("type"),
                "number": obj.get("number") if obj.get("number") is not None else None,
                "numeration": obj.get("numeration")
                if obj.get("numeration") is not None
                else None,
                "var_date": obj.get("date") if obj.get("date") is not None else None,
                "year": obj.get("year") if obj.get("year") is not None else None,
                "currency": Currency.from_dict(obj.get("currency"))
                if obj.get("currency") is not None
                else None,
                "language": Language.from_dict(obj.get("language"))
                if obj.get("language") is not None
                else None,
                "subject": obj.get("subject")
                if obj.get("subject") is not None
                else None,
                "visible_subject": obj.get("visible_subject")
                if obj.get("visible_subject") is not None
                else None,
                "rc_center": obj.get("rc_center")
                if obj.get("rc_center") is not None
                else None,
                "notes": obj.get("notes") if obj.get("notes") is not None else None,
                "rivalsa": float(obj.get("rivalsa"))
                if obj.get("rivalsa") is not None
                else None,
                "cassa": float(obj.get("cassa"))
                if obj.get("cassa") is not None
                else None,
                "amount_cassa": float(obj.get("amount_cassa"))
                if obj.get("amount_cassa") is not None
                else None,
                "cassa_taxable": float(obj.get("cassa_taxable"))
                if obj.get("cassa_taxable") is not None
                else None,
                "amount_cassa_taxable": float(obj.get("amount_cassa_taxable"))
                if obj.get("amount_cassa_taxable") is not None
                else None,
                "cassa2": float(obj.get("cassa2"))
                if obj.get("cassa2") is not None
                else None,
                "amount_cassa2": float(obj.get("amount_cassa2"))
                if obj.get("amount_cassa2") is not None
                else None,
                "cassa2_taxable": float(obj.get("cassa2_taxable"))
                if obj.get("cassa2_taxable") is not None
                else None,
                "amount_cassa2_taxable": float(obj.get("amount_cassa2_taxable"))
                if obj.get("amount_cassa2_taxable") is not None
                else None,
                "global_cassa_taxable": float(obj.get("global_cassa_taxable"))
                if obj.get("global_cassa_taxable") is not None
                else None,
                "amount_global_cassa_taxable": float(
                    obj.get("amount_global_cassa_taxable")
                )
                if obj.get("amount_global_cassa_taxable") is not None
                else None,
                "withholding_tax": float(obj.get("withholding_tax"))
                if obj.get("withholding_tax") is not None
                else None,
                "withholding_tax_taxable": float(obj.get("withholding_tax_taxable"))
                if obj.get("withholding_tax_taxable") is not None
                else None,
                "other_withholding_tax": float(obj.get("other_withholding_tax"))
                if obj.get("other_withholding_tax") is not None
                else None,
                "stamp_duty": float(obj.get("stamp_duty"))
                if obj.get("stamp_duty") is not None
                else None,
                "payment_method": PaymentMethod.from_dict(obj.get("payment_method"))
                if obj.get("payment_method") is not None
                else None,
                "use_split_payment": obj.get("use_split_payment")
                if obj.get("use_split_payment") is not None
                else None,
                "use_gross_prices": obj.get("use_gross_prices")
                if obj.get("use_gross_prices") is not None
                else None,
                "e_invoice": obj.get("e_invoice")
                if obj.get("e_invoice") is not None
                else None,
                "ei_data": IssuedDocumentEiData.from_dict(obj.get("ei_data"))
                if obj.get("ei_data") is not None
                else None,
                "ei_cassa_type": obj.get("ei_cassa_type")
                if obj.get("ei_cassa_type") is not None
                else None,
                "ei_cassa2_type": obj.get("ei_cassa2_type")
                if obj.get("ei_cassa2_type") is not None
                else None,
                "ei_withholding_tax_causal": obj.get("ei_withholding_tax_causal")
                if obj.get("ei_withholding_tax_causal") is not None
                else None,
                "ei_other_withholding_tax_type": obj.get(
                    "ei_other_withholding_tax_type"
                )
                if obj.get("ei_other_withholding_tax_type") is not None
                else None,
                "ei_other_withholding_tax_causal": obj.get(
                    "ei_other_withholding_tax_causal"
                )
                if obj.get("ei_other_withholding_tax_causal") is not None
                else None,
                "items_list": [
                    IssuedDocumentItemsListItem.from_dict(_item)
                    for _item in obj.get("items_list")
                ]
                if obj.get("items_list") is not None
                else None,
                "payments_list": [
                    IssuedDocumentPaymentsListItem.from_dict(_item)
                    for _item in obj.get("payments_list")
                ]
                if obj.get("payments_list") is not None
                else None,
                "template": DocumentTemplate.from_dict(obj.get("template"))
                if obj.get("template") is not None
                else None,
                "delivery_note_template": DocumentTemplate.from_dict(
                    obj.get("delivery_note_template")
                )
                if obj.get("delivery_note_template") is not None
                else None,
                "acc_inv_template": DocumentTemplate.from_dict(
                    obj.get("acc_inv_template")
                )
                if obj.get("acc_inv_template") is not None
                else None,
                "h_margins": obj.get("h_margins")
                if obj.get("h_margins") is not None
                else None,
                "v_margins": obj.get("v_margins")
                if obj.get("v_margins") is not None
                else None,
                "show_payments": obj.get("show_payments")
                if obj.get("show_payments") is not None
                else None,
                "show_payment_method": obj.get("show_payment_method")
                if obj.get("show_payment_method") is not None
                else None,
                "show_totals": obj.get("show_totals"),
                "show_paypal_button": obj.get("show_paypal_button")
                if obj.get("show_paypal_button") is not None
                else None,
                "show_notification_button": obj.get("show_notification_button")
                if obj.get("show_notification_button") is not None
                else None,
                "show_tspay_button": obj.get("show_tspay_button")
                if obj.get("show_tspay_button") is not None
                else None,
                "delivery_note": obj.get("delivery_note")
                if obj.get("delivery_note") is not None
                else None,
                "accompanying_invoice": obj.get("accompanying_invoice")
                if obj.get("accompanying_invoice") is not None
                else None,
                "dn_number": obj.get("dn_number")
                if obj.get("dn_number") is not None
                else None,
                "dn_date": obj.get("dn_date")
                if obj.get("dn_date") is not None
                else None,
                "dn_ai_packages_number": obj.get("dn_ai_packages_number")
                if obj.get("dn_ai_packages_number") is not None
                else None,
                "dn_ai_weight": obj.get("dn_ai_weight")
                if obj.get("dn_ai_weight") is not None
                else None,
                "dn_ai_causal": obj.get("dn_ai_causal")
                if obj.get("dn_ai_causal") is not None
                else None,
                "dn_ai_destination": obj.get("dn_ai_destination")
                if obj.get("dn_ai_destination") is not None
                else None,
                "dn_ai_transporter": obj.get("dn_ai_transporter")
                if obj.get("dn_ai_transporter") is not None
                else None,
                "dn_ai_notes": obj.get("dn_ai_notes")
                if obj.get("dn_ai_notes") is not None
                else None,
                "is_marked": obj.get("is_marked")
                if obj.get("is_marked") is not None
                else None,
                "amount_net": float(obj.get("amount_net"))
                if obj.get("amount_net") is not None
                else None,
                "amount_vat": float(obj.get("amount_vat"))
                if obj.get("amount_vat") is not None
                else None,
                "amount_gross": float(obj.get("amount_gross"))
                if obj.get("amount_gross") is not None
                else None,
                "amount_due_discount": float(obj.get("amount_due_discount"))
                if obj.get("amount_due_discount") is not None
                else None,
                "amount_rivalsa": float(obj.get("amount_rivalsa"))
                if obj.get("amount_rivalsa") is not None
                else None,
                "amount_rivalsa_taxable": float(obj.get("amount_rivalsa_taxable"))
                if obj.get("amount_rivalsa_taxable") is not None
                else None,
                "amount_withholding_tax": float(obj.get("amount_withholding_tax"))
                if obj.get("amount_withholding_tax") is not None
                else None,
                "amount_withholding_tax_taxable": float(
                    obj.get("amount_withholding_tax_taxable")
                )
                if obj.get("amount_withholding_tax_taxable") is not None
                else None,
                "amount_other_withholding_tax": float(
                    obj.get("amount_other_withholding_tax")
                )
                if obj.get("amount_other_withholding_tax") is not None
                else None,
                "amount_other_withholding_tax_taxable": float(
                    obj.get("amount_other_withholding_tax_taxable")
                )
                if obj.get("amount_other_withholding_tax_taxable") is not None
                else None,
                "amount_enasarco_taxable": float(obj.get("amount_enasarco_taxable"))
                if obj.get("amount_enasarco_taxable") is not None
                else None,
                "extra_data": IssuedDocumentExtraData.from_dict(obj.get("extra_data"))
                if obj.get("extra_data") is not None
                else None,
                "seen_date": obj.get("seen_date")
                if obj.get("seen_date") is not None
                else None,
                "next_due_date": obj.get("next_due_date")
                if obj.get("next_due_date") is not None
                else None,
                "url": obj.get("url") if obj.get("url") is not None else None,
                "dn_url": obj.get("dn_url") if obj.get("dn_url") is not None else None,
                "ai_url": obj.get("ai_url") if obj.get("ai_url") is not None else None,
                "attachment_url": obj.get("attachment_url")
                if obj.get("attachment_url") is not None
                else None,
                "attachment_token": obj.get("attachment_token")
                if obj.get("attachment_token") is not None
                else None,
                "ei_raw": obj.get("ei_raw") if obj.get("ei_raw") is not None else None,
                "ei_status": obj.get("ei_status")
                if obj.get("ei_status") is not None
                else None,
                "created_at": obj.get("created_at")
                if obj.get("created_at") is not None
                else None,
                "updated_at": obj.get("updated_at")
                if obj.get("updated_at") is not None
                else None,
            }
        )
        return _obj
