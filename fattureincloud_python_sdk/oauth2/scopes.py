from enum import Enum


class Scope(Enum):

    ENTITY_CLIENTS_READ = "entity.clients:r"

    ENTITY_CLIENTS_ALL = "entity.clients:a"

    ENTITY_SUPPLIERS_READ = "entity.suppliers:r"

    ENTITY_SUPPLIERS_ALL = "entity.suppliers:a"

    PRODUCTS_READ = "products:r"

    PRODUCTS_ALL = "products:a"

    ISSUED_DOCUMENTS_INVOICE_READ = "issued_documents.invoice:r"

    ISSUED_DOCUMENTS_CREDIT_NOTE_READ = "issued_documents.credit_note:r"

    ISSUED_DOCUMENTS_RECEIPT_READ = "issued_documents.receipt:r"

    ISSUED_DOCUMENTS_ORDER_READ = "issued_documents.order:r"

    ISSUED_DOCUMENTS_QUOTE_READ = "issued_documents.quote:r"

    ISSUED_DOCUMENTS_PROFORMA_READ = "issued_documents.proforma:r"

    ISSUED_DOCUMENTS_DELIVERY_NOTE_READ = "issued_documents.delivery_note:r"

    ISSUED_DOCUMENTS_INVOICE_ALL = "issued_documents.invoice:a"

    ISSUED_DOCUMENTS_CREDIT_NOTE_ALL = "issued_documents.credit_note:a"

    ISSUED_DOCUMENTS_RECEIPT_ALL = "issued_documents.receipt:a"

    ISSUED_DOCUMENTS_ORDER_ALL = "issued_documents.order:a"

    ISSUED_DOCUMENTS_QUOTE_ALL = "issued_documents.quote:a"

    ISSUED_DOCUMENTS_PROFORMA_ALL = "issued_documents.proforma:a"

    ISSUED_DOCUMENTS_DELIVERY_NOTE_ALL = "issued_documents.delivery_note:a"

    RECEIVED_DOCUMENTS_READ = "received_documents:r"

    RECEIVED_DOCUMENTS_ALL = "received_documents:a"

    STOCK_READ = "stock:r"

    STOCK_ALL = "stock:a"

    RECEIPTS_READ = "receipts:r"

    RECEIPTS_ALL = "receipts:a"

    TAXES_READ = "taxes:r"

    TAXES_ALL = "taxes:a"

    ARCHIVE_READ = "archive:r"

    ARCHIVE_ALL = "archive:a"

    CASHBOOK_READ = "cashbook:r"

    CASHBOOK_ALL = "cashbook:a"

    SETTINGS_READ = "settings:r"

    SETTINGS_ALL = "settings:a"

    SITUATION_READ = "situation:r"
