from enum import Enum


class Scope(Enum):

    ENTITY_CLIENTS_READ = "entity.clients:r"  # Read permission to the Clients registry

    ENTITY_CLIENTS_ALL = "entity.clients:a"  # Write permission to the Clients registry

    ENTITY_SUPPLIERS_READ = (
        "entity.suppliers:r"  # Read permission to the Suppliers registry
    )

    ENTITY_SUPPLIERS_ALL = (
        "entity.suppliers:a"  # Write permission to the Suppliers registry
    )

    PRODUCTS_READ = "products:r"  # Read permission to the Products

    PRODUCTS_ALL = "products:a"  # Write permission to the Products

    ISSUED_DOCUMENTS_INVOICE_READ = (
        "issued_documents.invoice:r"  # Read permission to the issued Invoices
    )

    ISSUED_DOCUMENTS_CREDIT_NOTE_READ = (
        "issued_documents.credit_note:r"  # Read permission to the issued Credit Notes
    )

    ISSUED_DOCUMENTS_RECEIPT_READ = (
        "issued_documents.receipt:r"  # Read permission to the issued Receipts
    )

    ISSUED_DOCUMENTS_ORDER_READ = (
        "issued_documents.order:r"  # Read permission to the issued Orders
    )

    ISSUED_DOCUMENTS_QUOTE_READ = (
        "issued_documents.quote:r"  # Read permission to the issued Quotes
    )

    ISSUED_DOCUMENTS_PROFORMA_READ = (
        "issued_documents.proforma:r"  # Read permission to the issued Proformas
    )

    ISSUED_DOCUMENTS_DELIVERY_NOTE_READ = "issued_documents.delivery_note:r"  # Read permission to the issued Delivery Notes

    ISSUED_DOCUMENTS_INVOICE_ALL = (
        "issued_documents.invoice:a"  # Write permission to the issued Invoices
    )

    ISSUED_DOCUMENTS_CREDIT_NOTE_ALL = (
        "issued_documents.credit_note:a"  # Write permission to the issued Credit Notes
    )

    ISSUED_DOCUMENTS_RECEIPT_ALL = (
        "issued_documents.receipt:a"  # Write permission to the issued issued Receipts
    )

    ISSUED_DOCUMENTS_ORDER_ALL = (
        "issued_documents.order:a"  # Write permission to the issued Orders
    )

    ISSUED_DOCUMENTS_QUOTE_ALL = (
        "issued_documents.quote:a"  # Write permission to the issued Quotes
    )

    ISSUED_DOCUMENTS_PROFORMA_ALL = (
        "issued_documents.proforma:a"  # Write permission to the issued Proformas
    )

    ISSUED_DOCUMENTS_DELIVERY_NOTE_ALL = "issued_documents.delivery_note:a"  # Write permission to the issued Delivery Notes

    RECEIVED_DOCUMENTS_READ = (
        "received_documents:r"  # Read permission to the issued Received Documents
    )

    RECEIVED_DOCUMENTS_ALL = (
        "received_documents:a"  # Write permission to the issued Received Documents
    )

    STOCK_READ = "stock:r"  # Read permission to the Stock movements

    STOCK_ALL = "stock:a"  # Write permission to the Stock movements

    RECEIPTS_READ = "receipts:r"  # Read permission to the Receipts

    RECEIPTS_ALL = "receipts:a"  # Write permission to the Receipts

    TAXES_READ = "taxes:r"  # Read permission to the Taxes

    TAXES_ALL = "taxes:a"  # Write permission to the Taxes

    ARCHIVE_READ = "archive:r"  # Read permission to the Archive Documents

    ARCHIVE_ALL = "archive:a"  # Read permission to the Archive Documents

    CASHBOOK_READ = "cashbook:r"  # Read permission to the Cashbook

    CASHBOOK_ALL = "cashbook:a"  # Write permission to the Cashbook

    SETTINGS_READ = "settings:r"  # Read permission to the Settings

    SETTINGS_ALL = "settings:a"  # Write permission to the Settings

    SITUATION_READ = "situation:r"  # Read permission to the company Situation
