from enum import Enum


class Scope(Enum):

    # Read permission to the Clients registry
    ENTITY_CLIENTS_READ = "entity.clients:r"

    # Write permission to the Clients registry
    ENTITY_CLIENTS_ALL = "entity.clients:a"

    # Read permission to the Suppliers registry
    ENTITY_SUPPLIERS_READ = "entity.suppliers:r"

    # Write permission to the Suppliers registry
    ENTITY_SUPPLIERS_ALL = "entity.suppliers:a"

    # Read permission to the Products
    PRODUCTS_READ = "products:r"

    # Write permission to the Products
    PRODUCTS_ALL = "products:a"

    # Read permission to the issued Invoices
    ISSUED_DOCUMENTS_INVOICES_READ = "issued_documents.invoices:r"

    # Read permission to the issued Credit Notes
    ISSUED_DOCUMENTS_CREDIT_NOTES_READ = "issued_documents.credit_notes:r"

    # Read permission to the issued Receipts
    ISSUED_DOCUMENTS_RECEIPTS_READ = "issued_documents.receipts:r"

    # Read permission to the issued Orders
    ISSUED_DOCUMENTS_ORDERS_READ = "issued_documents.orders:r"

    # Read permission to the issued Quotes
    ISSUED_DOCUMENTS_QUOTES_READ = "issued_documents.quotes:r"

    # Read permission to the issued Proformas
    ISSUED_DOCUMENTS_PROFORMAS_READ = "issued_documents.proformas:r"

    # Read permission to the issued Delivery Notes
    ISSUED_DOCUMENTS_DELIVERY_NOTES_READ = "issued_documents.delivery_notes:r"

    # Read permission to the issued Work Reports
    ISSUED_DOCUMENTS_WORK_REPORTS_READ = "issued_documents.work_reports:r"

    # Read permission to the issued Supplier Orders
    ISSUED_DOCUMENTS_SUPPLIER_ORDERS_READ = "issued_documents.supplier_orders:r"

    # Read permission to the issued Self Invoices
    ISSUED_DOCUMENTS_SELF_INVOICES_READ = "issued_documents.self_invoices:r"

    # Write permission to the issued Invoices
    ISSUED_DOCUMENTS_INVOICES_ALL = "issued_documents.invoices:a"

    # Write permission to the issued Credit Notes
    ISSUED_DOCUMENTS_CREDIT_NOTES_ALL = "issued_documents.credit_notes:a"

    # Write permission to the issued issued Receipts
    ISSUED_DOCUMENTS_RECEIPTS_ALL = "issued_documents.receipts:a"

    # Write permission to the issued Orders
    ISSUED_DOCUMENTS_ORDERS_ALL = "issued_documents.orders:a"

    # Write permission to the issued Quotes
    ISSUED_DOCUMENTS_QUOTES_ALL = "issued_documents.quotes:a"

    # Write permission to the issued Proformas
    ISSUED_DOCUMENTS_PROFORMAS_ALL = "issued_documents.proformas:a"

    # Write permission to the issued Delivery Notes
    ISSUED_DOCUMENTS_DELIVERY_NOTES_ALL = "issued_documents.delivery_notes:a"

    # Write permission to the issued Work Reports
    ISSUED_DOCUMENTS_WORK_REPORTS_ALL = "issued_documents.work_reports:a"

    # Write permission to the issued Supplier Orders
    ISSUED_DOCUMENTS_SUPPLIER_ORDERS_ALL = "issued_documents.supplier_orders:a"

    # Write permission to the issued Self Invoices
    ISSUED_DOCUMENTS_SELF_INVOICES_ALL = "issued_documents.self_invoices:a"

    # Read permission to the Received Documents
    RECEIVED_DOCUMENTS_READ = "received_documents:r"

    # Write permission to the Received Documents
    RECEIVED_DOCUMENTS_ALL = "received_documents:a"

    # Read permission to the Stock movements
    STOCK_READ = "stock:r"

    # Write permission to the Stock movements
    STOCK_ALL = "stock:a"

    # Read permission to the Receipts
    RECEIPTS_READ = "receipts:r"

    # Write permission to the Receipts
    RECEIPTS_ALL = "receipts:a"

    # Read permission to the Taxes
    TAXES_READ = "taxes:r"

    # Write permission to the Taxes
    TAXES_ALL = "taxes:a"

    # Read permission to the Archive Documents
    ARCHIVE_READ = "archive:r"

    # Read permission to the Archive Documents
    ARCHIVE_ALL = "archive:a"

    # Read permission to the Cashbook
    CASHBOOK_READ = "cashbook:r"

    # Write permission to the Cashbook
    CASHBOOK_ALL = "cashbook:a"

    # Read permission to the Settings
    SETTINGS_READ = "settings:r"

    # Write permission to the Settings
    SETTINGS_ALL = "settings:a"

    # Read permission to the company Situation
    SITUATION_READ = "situation:r"
