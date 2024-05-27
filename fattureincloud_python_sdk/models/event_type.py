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


class EventType(str, Enum):
    """
    Webhooks event type
    """

    """
    allowed enum values
    """
    ISSUED_DOCUMENTS_INVOICES_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.invoices.create"
    )
    ISSUED_DOCUMENTS_INVOICES_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.invoices.update"
    )
    ISSUED_DOCUMENTS_INVOICES_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.invoices.delete"
    )
    ISSUED_DOCUMENTS_QUOTES_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.quotes.create"
    )
    ISSUED_DOCUMENTS_QUOTES_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.quotes.update"
    )
    ISSUED_DOCUMENTS_QUOTES_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.quotes.delete"
    )
    ISSUED_DOCUMENTS_PROFORMAS_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.proformas.create"
    )
    ISSUED_DOCUMENTS_PROFORMAS_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.proformas.update"
    )
    ISSUED_DOCUMENTS_PROFORMAS_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.proformas.delete"
    )
    ISSUED_DOCUMENTS_RECEIPTS_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.receipts.create"
    )
    ISSUED_DOCUMENTS_RECEIPTS_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.receipts.update"
    )
    ISSUED_DOCUMENTS_RECEIPTS_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.receipts.delete"
    )
    ISSUED_DOCUMENTS_DELIVERY_NOTES_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.delivery_notes.create"
    )
    ISSUED_DOCUMENTS_DELIVERY_NOTES_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.delivery_notes.update"
    )
    ISSUED_DOCUMENTS_DELIVERY_NOTES_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.delivery_notes.delete"
    )
    ISSUED_DOCUMENTS_CREDIT_NOTES_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.credit_notes.create"
    )
    ISSUED_DOCUMENTS_CREDIT_NOTES_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.credit_notes.update"
    )
    ISSUED_DOCUMENTS_CREDIT_NOTES_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.credit_notes.delete"
    )
    ISSUED_DOCUMENTS_ORDERS_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.orders.create"
    )
    ISSUED_DOCUMENTS_ORDERS_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.orders.update"
    )
    ISSUED_DOCUMENTS_ORDERS_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.orders.delete"
    )
    ISSUED_DOCUMENTS_WORK_REPORTS_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.work_reports.create"
    )
    ISSUED_DOCUMENTS_WORK_REPORTS_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.work_reports.update"
    )
    ISSUED_DOCUMENTS_WORK_REPORTS_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.work_reports.delete"
    )
    ISSUED_DOCUMENTS_SUPPLIER_ORDERS_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.supplier_orders.create"
    )
    ISSUED_DOCUMENTS_SUPPLIER_ORDERS_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.supplier_orders.update"
    )
    ISSUED_DOCUMENTS_SUPPLIER_ORDERS_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.supplier_orders.delete"
    )
    ISSUED_DOCUMENTS_SELF_INVOICES_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.self_invoices.create"
    )
    ISSUED_DOCUMENTS_SELF_INVOICES_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.self_invoices.update"
    )
    ISSUED_DOCUMENTS_SELF_INVOICES_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.self_invoices.delete"
    )
    ISSUED_DOCUMENTS_ALL_CREATE = (
        "it.fattureincloud.webhooks.issued_documents.all.create"
    )
    ISSUED_DOCUMENTS_ALL_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.all.update"
    )
    ISSUED_DOCUMENTS_ALL_DELETE = (
        "it.fattureincloud.webhooks.issued_documents.all.delete"
    )
    RECEIVED_DOCUMENTS_CREATE = (
        "it.fattureincloud.webhooks.received_documents.create"
    )
    RECEIVED_DOCUMENTS_UPDATE = (
        "it.fattureincloud.webhooks.received_documents.update"
    )
    RECEIVED_DOCUMENTS_DELETE = (
        "it.fattureincloud.webhooks.received_documents.delete"
    )
    RECEIPTS_CREATE = (
        "it.fattureincloud.webhooks.receipts.create"
    )
    RECEIPTS_UPDATE = (
        "it.fattureincloud.webhooks.receipts.update"
    )
    RECEIPTS_DELETE = (
        "it.fattureincloud.webhooks.receipts.delete"
    )
    TAXES_CREATE = (
        "it.fattureincloud.webhooks.taxes.create"
    )
    TAXES_UPDATE = (
        "it.fattureincloud.webhooks.taxes.update"
    )
    TAXES_DELETE = (
        "it.fattureincloud.webhooks.taxes.delete"
    )
    ARCHIVE_DOCUMENTS_CREATE = (
        "it.fattureincloud.webhooks.archive_documents.create"
    )
    ARCHIVE_DOCUMENTS_UPDATE = (
        "it.fattureincloud.webhooks.archive_documents.update"
    )
    ARCHIVE_DOCUMENTS_DELETE = (
        "it.fattureincloud.webhooks.archive_documents.delete"
    )
    CASHBOOK_CREATE = (
        "it.fattureincloud.webhooks.cashbook.create"
    )
    CASHBOOK_UPDATE = (
        "it.fattureincloud.webhooks.cashbook.update"
    )
    CASHBOOK_DELETE = (
        "it.fattureincloud.webhooks.cashbook.delete"
    )
    PRODUCTS_CREATE = (
        "it.fattureincloud.webhooks.products.create"
    )
    PRODUCTS_UPDATE = (
        "it.fattureincloud.webhooks.products.update"
    )
    PRODUCTS_DELETE = (
        "it.fattureincloud.webhooks.products.delete"
    )
    PRODUCTS_STOCK_UPDATE = (
        "it.fattureincloud.webhooks.products.stock_update"
    )
    ENTITIES_CLIENTS_CREATE = (
        "it.fattureincloud.webhooks.entities.clients.create"
    )
    ENTITIES_CLIENTS_UPDATE = (
        "it.fattureincloud.webhooks.entities.clients.update"
    )
    ENTITIES_CLIENTS_DELETE = (
        "it.fattureincloud.webhooks.entities.clients.delete"
    )
    ENTITIES_SUPPLIERS_CREATE = (
        "it.fattureincloud.webhooks.entities.suppliers.create"
    )
    ENTITIES_SUPPLIERS_UPDATE = (
        "it.fattureincloud.webhooks.entities.suppliers.update"
    )
    ENTITIES_SUPPLIERS_DELETE = (
        "it.fattureincloud.webhooks.entities.suppliers.delete"
    )
    ENTITIES_ALL_CREATE = (
        "it.fattureincloud.webhooks.entities.all.create"
    )
    ENTITIES_ALL_UPDATE = (
        "it.fattureincloud.webhooks.entities.all.update"
    )
    ENTITIES_ALL_DELETE = (
        "it.fattureincloud.webhooks.entities.all.delete"
    )
    ISSUED_DOCUMENTS_E_INVOICES_STATUS_UPDATE = (
        "it.fattureincloud.webhooks.issued_documents.e_invoices.status_update"
    )
    RECEIVED_DOCUMENTS_E_INVOICES_RECEIVE = (
        "it.fattureincloud.webhooks.received_documents.e_invoices.receive"
    )

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EventType from a JSON string"""
        return cls(json.loads(json_str))
