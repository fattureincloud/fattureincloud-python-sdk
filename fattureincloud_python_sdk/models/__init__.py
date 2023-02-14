# coding: utf-8

# flake8: noqa
"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.26
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from fattureincloud_python_sdk.models.archive_document import ArchiveDocument
from fattureincloud_python_sdk.models.attachment_data import AttachmentData
from fattureincloud_python_sdk.models.cashbook_entry import CashbookEntry
from fattureincloud_python_sdk.models.cashbook_entry_document import (
    CashbookEntryDocument,
)
from fattureincloud_python_sdk.models.cashbook_entry_kind import CashbookEntryKind
from fattureincloud_python_sdk.models.cashbook_entry_type import CashbookEntryType
from fattureincloud_python_sdk.models.city import City
from fattureincloud_python_sdk.models.client import Client
from fattureincloud_python_sdk.models.client_type import ClientType
from fattureincloud_python_sdk.models.company import Company
from fattureincloud_python_sdk.models.company_info import CompanyInfo
from fattureincloud_python_sdk.models.company_info_access_info import (
    CompanyInfoAccessInfo,
)
from fattureincloud_python_sdk.models.company_info_plan_info import CompanyInfoPlanInfo
from fattureincloud_python_sdk.models.company_info_plan_info_functions import (
    CompanyInfoPlanInfoFunctions,
)
from fattureincloud_python_sdk.models.company_info_plan_info_functions_status import (
    CompanyInfoPlanInfoFunctionsStatus,
)
from fattureincloud_python_sdk.models.company_info_plan_info_limits import (
    CompanyInfoPlanInfoLimits,
)
from fattureincloud_python_sdk.models.company_type import CompanyType
from fattureincloud_python_sdk.models.controlled_company import ControlledCompany
from fattureincloud_python_sdk.models.create_archive_document_request import (
    CreateArchiveDocumentRequest,
)
from fattureincloud_python_sdk.models.create_archive_document_response import (
    CreateArchiveDocumentResponse,
)
from fattureincloud_python_sdk.models.create_cashbook_entry_request import (
    CreateCashbookEntryRequest,
)
from fattureincloud_python_sdk.models.create_cashbook_entry_response import (
    CreateCashbookEntryResponse,
)
from fattureincloud_python_sdk.models.create_client_request import CreateClientRequest
from fattureincloud_python_sdk.models.create_client_response import CreateClientResponse
from fattureincloud_python_sdk.models.create_f24_request import CreateF24Request
from fattureincloud_python_sdk.models.create_f24_response import CreateF24Response
from fattureincloud_python_sdk.models.create_issued_document_request import (
    CreateIssuedDocumentRequest,
)
from fattureincloud_python_sdk.models.create_issued_document_response import (
    CreateIssuedDocumentResponse,
)
from fattureincloud_python_sdk.models.create_payment_account_request import (
    CreatePaymentAccountRequest,
)
from fattureincloud_python_sdk.models.create_payment_account_response import (
    CreatePaymentAccountResponse,
)
from fattureincloud_python_sdk.models.create_payment_method_request import (
    CreatePaymentMethodRequest,
)
from fattureincloud_python_sdk.models.create_payment_method_response import (
    CreatePaymentMethodResponse,
)
from fattureincloud_python_sdk.models.create_product_request import CreateProductRequest
from fattureincloud_python_sdk.models.create_product_response import (
    CreateProductResponse,
)
from fattureincloud_python_sdk.models.create_receipt_request import CreateReceiptRequest
from fattureincloud_python_sdk.models.create_receipt_response import (
    CreateReceiptResponse,
)
from fattureincloud_python_sdk.models.create_received_document_request import (
    CreateReceivedDocumentRequest,
)
from fattureincloud_python_sdk.models.create_received_document_response import (
    CreateReceivedDocumentResponse,
)
from fattureincloud_python_sdk.models.create_supplier_request import (
    CreateSupplierRequest,
)
from fattureincloud_python_sdk.models.create_supplier_response import (
    CreateSupplierResponse,
)
from fattureincloud_python_sdk.models.create_vat_type_request import (
    CreateVatTypeRequest,
)
from fattureincloud_python_sdk.models.create_vat_type_response import (
    CreateVatTypeResponse,
)
from fattureincloud_python_sdk.models.currency import Currency
from fattureincloud_python_sdk.models.detailed_country import DetailedCountry
from fattureincloud_python_sdk.models.document_template import DocumentTemplate
from fattureincloud_python_sdk.models.e_invoice_rejection_reason import (
    EInvoiceRejectionReason,
)
from fattureincloud_python_sdk.models.email import Email
from fattureincloud_python_sdk.models.email_attachment import EmailAttachment
from fattureincloud_python_sdk.models.email_data import EmailData
from fattureincloud_python_sdk.models.email_data_default_sender_email import (
    EmailDataDefaultSenderEmail,
)
from fattureincloud_python_sdk.models.email_recipient_status import EmailRecipientStatus
from fattureincloud_python_sdk.models.email_schedule import EmailSchedule
from fattureincloud_python_sdk.models.email_schedule_include import EmailScheduleInclude
from fattureincloud_python_sdk.models.email_status import EmailStatus
from fattureincloud_python_sdk.models.entity import Entity
from fattureincloud_python_sdk.models.entity_type import EntityType
from fattureincloud_python_sdk.models.f24 import F24
from fattureincloud_python_sdk.models.f24_status import F24Status
from fattureincloud_python_sdk.models.function_status import FunctionStatus
from fattureincloud_python_sdk.models.get_archive_document_response import (
    GetArchiveDocumentResponse,
)
from fattureincloud_python_sdk.models.get_cashbook_entry_response import (
    GetCashbookEntryResponse,
)
from fattureincloud_python_sdk.models.get_client_response import GetClientResponse
from fattureincloud_python_sdk.models.get_company_info_response import (
    GetCompanyInfoResponse,
)
from fattureincloud_python_sdk.models.get_e_invoice_rejection_reason_response import (
    GetEInvoiceRejectionReasonResponse,
)
from fattureincloud_python_sdk.models.get_email_data_response import (
    GetEmailDataResponse,
)
from fattureincloud_python_sdk.models.get_existing_issued_document_totals_request import (
    GetExistingIssuedDocumentTotalsRequest,
)
from fattureincloud_python_sdk.models.get_existing_issued_document_totals_response import (
    GetExistingIssuedDocumentTotalsResponse,
)
from fattureincloud_python_sdk.models.get_existing_received_document_totals_request import (
    GetExistingReceivedDocumentTotalsRequest,
)
from fattureincloud_python_sdk.models.get_existing_received_document_totals_response import (
    GetExistingReceivedDocumentTotalsResponse,
)
from fattureincloud_python_sdk.models.get_f24_response import GetF24Response
from fattureincloud_python_sdk.models.get_issued_document_pre_create_info_response import (
    GetIssuedDocumentPreCreateInfoResponse,
)
from fattureincloud_python_sdk.models.get_issued_document_response import (
    GetIssuedDocumentResponse,
)
from fattureincloud_python_sdk.models.get_new_issued_document_totals_request import (
    GetNewIssuedDocumentTotalsRequest,
)
from fattureincloud_python_sdk.models.get_new_issued_document_totals_response import (
    GetNewIssuedDocumentTotalsResponse,
)
from fattureincloud_python_sdk.models.get_new_received_document_totals_request import (
    GetNewReceivedDocumentTotalsRequest,
)
from fattureincloud_python_sdk.models.get_new_received_document_totals_response import (
    GetNewReceivedDocumentTotalsResponse,
)
from fattureincloud_python_sdk.models.get_payment_account_response import (
    GetPaymentAccountResponse,
)
from fattureincloud_python_sdk.models.get_payment_method_response import (
    GetPaymentMethodResponse,
)
from fattureincloud_python_sdk.models.get_product_response import GetProductResponse
from fattureincloud_python_sdk.models.get_receipt_pre_create_info_response import (
    GetReceiptPreCreateInfoResponse,
)
from fattureincloud_python_sdk.models.get_receipt_response import GetReceiptResponse
from fattureincloud_python_sdk.models.get_receipts_monthly_totals_response import (
    GetReceiptsMonthlyTotalsResponse,
)
from fattureincloud_python_sdk.models.get_received_document_pre_create_info_response import (
    GetReceivedDocumentPreCreateInfoResponse,
)
from fattureincloud_python_sdk.models.get_received_document_response import (
    GetReceivedDocumentResponse,
)
from fattureincloud_python_sdk.models.get_supplier_response import GetSupplierResponse
from fattureincloud_python_sdk.models.get_user_info_response import GetUserInfoResponse
from fattureincloud_python_sdk.models.get_user_info_response_email_confirmation_state import (
    GetUserInfoResponseEmailConfirmationState,
)
from fattureincloud_python_sdk.models.get_user_info_response_info import (
    GetUserInfoResponseInfo,
)
from fattureincloud_python_sdk.models.get_vat_type_response import GetVatTypeResponse
from fattureincloud_python_sdk.models.issued_document import IssuedDocument
from fattureincloud_python_sdk.models.issued_document_ei_data import (
    IssuedDocumentEiData,
)
from fattureincloud_python_sdk.models.issued_document_extra_data import (
    IssuedDocumentExtraData,
)
from fattureincloud_python_sdk.models.issued_document_items_list_item import (
    IssuedDocumentItemsListItem,
)
from fattureincloud_python_sdk.models.issued_document_options import (
    IssuedDocumentOptions,
)
from fattureincloud_python_sdk.models.issued_document_payments_list_item import (
    IssuedDocumentPaymentsListItem,
)
from fattureincloud_python_sdk.models.issued_document_payments_list_item_payment_terms import (
    IssuedDocumentPaymentsListItemPaymentTerms,
)
from fattureincloud_python_sdk.models.issued_document_pre_create_info import (
    IssuedDocumentPreCreateInfo,
)
from fattureincloud_python_sdk.models.issued_document_pre_create_info_default_values import (
    IssuedDocumentPreCreateInfoDefaultValues,
)
from fattureincloud_python_sdk.models.issued_document_pre_create_info_extra_data_default_values import (
    IssuedDocumentPreCreateInfoExtraDataDefaultValues,
)
from fattureincloud_python_sdk.models.issued_document_pre_create_info_items_default_values import (
    IssuedDocumentPreCreateInfoItemsDefaultValues,
)
from fattureincloud_python_sdk.models.issued_document_status import IssuedDocumentStatus
from fattureincloud_python_sdk.models.issued_document_totals import IssuedDocumentTotals
from fattureincloud_python_sdk.models.issued_document_type import IssuedDocumentType
from fattureincloud_python_sdk.models.join_issued_documents_response import (
    JoinIssuedDocumentsResponse,
)
from fattureincloud_python_sdk.models.language import Language
from fattureincloud_python_sdk.models.list_archive_categories_response import (
    ListArchiveCategoriesResponse,
)
from fattureincloud_python_sdk.models.list_archive_documents_response import (
    ListArchiveDocumentsResponse,
)
from fattureincloud_python_sdk.models.list_archive_documents_response_page import (
    ListArchiveDocumentsResponsePage,
)
from fattureincloud_python_sdk.models.list_cashbook_entries_response import (
    ListCashbookEntriesResponse,
)
from fattureincloud_python_sdk.models.list_cities_response import ListCitiesResponse
from fattureincloud_python_sdk.models.list_clients_response import ListClientsResponse
from fattureincloud_python_sdk.models.list_clients_response_page import (
    ListClientsResponsePage,
)
from fattureincloud_python_sdk.models.list_cost_centers_response import (
    ListCostCentersResponse,
)
from fattureincloud_python_sdk.models.list_countries_response import (
    ListCountriesResponse,
)
from fattureincloud_python_sdk.models.list_currencies_response import (
    ListCurrenciesResponse,
)
from fattureincloud_python_sdk.models.list_delivery_notes_default_causals_response import (
    ListDeliveryNotesDefaultCausalsResponse,
)
from fattureincloud_python_sdk.models.list_detailed_countries_response import (
    ListDetailedCountriesResponse,
)
from fattureincloud_python_sdk.models.list_emails_response import ListEmailsResponse
from fattureincloud_python_sdk.models.list_emails_response_page import (
    ListEmailsResponsePage,
)
from fattureincloud_python_sdk.models.list_f24_response import ListF24Response
from fattureincloud_python_sdk.models.list_f24_response_aggregated_data import (
    ListF24ResponseAggregatedData,
)
from fattureincloud_python_sdk.models.list_f24_response_aggregation import (
    ListF24ResponseAggregation,
)
from fattureincloud_python_sdk.models.list_f24_response_page import ListF24ResponsePage
from fattureincloud_python_sdk.models.list_issued_documents_response import (
    ListIssuedDocumentsResponse,
)
from fattureincloud_python_sdk.models.list_issued_documents_response_page import (
    ListIssuedDocumentsResponsePage,
)
from fattureincloud_python_sdk.models.list_languages_response import (
    ListLanguagesResponse,
)
from fattureincloud_python_sdk.models.list_payment_accounts_response import (
    ListPaymentAccountsResponse,
)
from fattureincloud_python_sdk.models.list_payment_methods_response import (
    ListPaymentMethodsResponse,
)
from fattureincloud_python_sdk.models.list_product_categories_response import (
    ListProductCategoriesResponse,
)
from fattureincloud_python_sdk.models.list_products_response import ListProductsResponse
from fattureincloud_python_sdk.models.list_products_response_page import (
    ListProductsResponsePage,
)
from fattureincloud_python_sdk.models.list_receipts_response import ListReceiptsResponse
from fattureincloud_python_sdk.models.list_receipts_response_page import (
    ListReceiptsResponsePage,
)
from fattureincloud_python_sdk.models.list_received_document_categories_response import (
    ListReceivedDocumentCategoriesResponse,
)
from fattureincloud_python_sdk.models.list_received_documents_response import (
    ListReceivedDocumentsResponse,
)
from fattureincloud_python_sdk.models.list_received_documents_response_page import (
    ListReceivedDocumentsResponsePage,
)
from fattureincloud_python_sdk.models.list_revenue_centers_response import (
    ListRevenueCentersResponse,
)
from fattureincloud_python_sdk.models.list_suppliers_response import (
    ListSuppliersResponse,
)
from fattureincloud_python_sdk.models.list_suppliers_response_page import (
    ListSuppliersResponsePage,
)
from fattureincloud_python_sdk.models.list_templates_response import (
    ListTemplatesResponse,
)
from fattureincloud_python_sdk.models.list_units_of_measure_response import (
    ListUnitsOfMeasureResponse,
)
from fattureincloud_python_sdk.models.list_user_companies_response import (
    ListUserCompaniesResponse,
)
from fattureincloud_python_sdk.models.list_user_companies_response_data import (
    ListUserCompaniesResponseData,
)
from fattureincloud_python_sdk.models.list_vat_types_response import (
    ListVatTypesResponse,
)
from fattureincloud_python_sdk.models.modify_archive_document_request import (
    ModifyArchiveDocumentRequest,
)
from fattureincloud_python_sdk.models.modify_archive_document_response import (
    ModifyArchiveDocumentResponse,
)
from fattureincloud_python_sdk.models.modify_cashbook_entry_request import (
    ModifyCashbookEntryRequest,
)
from fattureincloud_python_sdk.models.modify_cashbook_entry_response import (
    ModifyCashbookEntryResponse,
)
from fattureincloud_python_sdk.models.modify_client_request import ModifyClientRequest
from fattureincloud_python_sdk.models.modify_client_response import ModifyClientResponse
from fattureincloud_python_sdk.models.modify_f24_request import ModifyF24Request
from fattureincloud_python_sdk.models.modify_f24_response import ModifyF24Response
from fattureincloud_python_sdk.models.modify_issued_document_request import (
    ModifyIssuedDocumentRequest,
)
from fattureincloud_python_sdk.models.modify_issued_document_response import (
    ModifyIssuedDocumentResponse,
)
from fattureincloud_python_sdk.models.modify_payment_account_request import (
    ModifyPaymentAccountRequest,
)
from fattureincloud_python_sdk.models.modify_payment_account_response import (
    ModifyPaymentAccountResponse,
)
from fattureincloud_python_sdk.models.modify_payment_method_request import (
    ModifyPaymentMethodRequest,
)
from fattureincloud_python_sdk.models.modify_payment_method_response import (
    ModifyPaymentMethodResponse,
)
from fattureincloud_python_sdk.models.modify_product_request import ModifyProductRequest
from fattureincloud_python_sdk.models.modify_product_response import (
    ModifyProductResponse,
)
from fattureincloud_python_sdk.models.modify_receipt_request import ModifyReceiptRequest
from fattureincloud_python_sdk.models.modify_receipt_response import (
    ModifyReceiptResponse,
)
from fattureincloud_python_sdk.models.modify_received_document_request import (
    ModifyReceivedDocumentRequest,
)
from fattureincloud_python_sdk.models.modify_received_document_response import (
    ModifyReceivedDocumentResponse,
)
from fattureincloud_python_sdk.models.modify_supplier_request import (
    ModifySupplierRequest,
)
from fattureincloud_python_sdk.models.modify_supplier_response import (
    ModifySupplierResponse,
)
from fattureincloud_python_sdk.models.modify_vat_type_request import (
    ModifyVatTypeRequest,
)
from fattureincloud_python_sdk.models.modify_vat_type_response import (
    ModifyVatTypeResponse,
)
from fattureincloud_python_sdk.models.monthly_total import MonthlyTotal
from fattureincloud_python_sdk.models.original_document_type import OriginalDocumentType
from fattureincloud_python_sdk.models.pagination import Pagination
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.models.payment_method import PaymentMethod
from fattureincloud_python_sdk.models.payment_method_details import PaymentMethodDetails
from fattureincloud_python_sdk.models.payment_method_type import PaymentMethodType
from fattureincloud_python_sdk.models.payment_terms_type import PaymentTermsType
from fattureincloud_python_sdk.models.permission_level import PermissionLevel
from fattureincloud_python_sdk.models.permissions import Permissions
from fattureincloud_python_sdk.models.permissions_fic_issued_documents_detailed import (
    PermissionsFicIssuedDocumentsDetailed,
)
from fattureincloud_python_sdk.models.product import Product
from fattureincloud_python_sdk.models.receipt import Receipt
from fattureincloud_python_sdk.models.receipt_items_list_item import (
    ReceiptItemsListItem,
)
from fattureincloud_python_sdk.models.receipt_pre_create_info import (
    ReceiptPreCreateInfo,
)
from fattureincloud_python_sdk.models.receipt_type import ReceiptType
from fattureincloud_python_sdk.models.received_document import ReceivedDocument
from fattureincloud_python_sdk.models.received_document_entity import (
    ReceivedDocumentEntity,
)
from fattureincloud_python_sdk.models.received_document_info import ReceivedDocumentInfo
from fattureincloud_python_sdk.models.received_document_info_default_values import (
    ReceivedDocumentInfoDefaultValues,
)
from fattureincloud_python_sdk.models.received_document_info_items_default_values import (
    ReceivedDocumentInfoItemsDefaultValues,
)
from fattureincloud_python_sdk.models.received_document_items_list_item import (
    ReceivedDocumentItemsListItem,
)
from fattureincloud_python_sdk.models.received_document_payments_list_item import (
    ReceivedDocumentPaymentsListItem,
)
from fattureincloud_python_sdk.models.received_document_payments_list_item_payment_terms import (
    ReceivedDocumentPaymentsListItemPaymentTerms,
)
from fattureincloud_python_sdk.models.received_document_totals import (
    ReceivedDocumentTotals,
)
from fattureincloud_python_sdk.models.received_document_type import ReceivedDocumentType
from fattureincloud_python_sdk.models.schedule_email_request import ScheduleEmailRequest
from fattureincloud_python_sdk.models.send_e_invoice_request import SendEInvoiceRequest
from fattureincloud_python_sdk.models.send_e_invoice_request_data import (
    SendEInvoiceRequestData,
)
from fattureincloud_python_sdk.models.send_e_invoice_request_options import (
    SendEInvoiceRequestOptions,
)
from fattureincloud_python_sdk.models.send_e_invoice_response import (
    SendEInvoiceResponse,
)
from fattureincloud_python_sdk.models.send_e_invoice_response_data import (
    SendEInvoiceResponseData,
)
from fattureincloud_python_sdk.models.sender_email import SenderEmail
from fattureincloud_python_sdk.models.show_totals_mode import ShowTotalsMode
from fattureincloud_python_sdk.models.supplier import Supplier
from fattureincloud_python_sdk.models.supplier_type import SupplierType
from fattureincloud_python_sdk.models.transform_issued_document_response import (
    TransformIssuedDocumentResponse,
)
from fattureincloud_python_sdk.models.upload_archive_attachment_response import (
    UploadArchiveAttachmentResponse,
)
from fattureincloud_python_sdk.models.upload_f24_attachment_response import (
    UploadF24AttachmentResponse,
)
from fattureincloud_python_sdk.models.upload_issued_document_attachment_response import (
    UploadIssuedDocumentAttachmentResponse,
)
from fattureincloud_python_sdk.models.upload_received_document_attachment_response import (
    UploadReceivedDocumentAttachmentResponse,
)
from fattureincloud_python_sdk.models.user import User
from fattureincloud_python_sdk.models.user_company_role import UserCompanyRole
from fattureincloud_python_sdk.models.vat_item import VatItem
from fattureincloud_python_sdk.models.vat_kind import VatKind
from fattureincloud_python_sdk.models.vat_type import VatType
from fattureincloud_python_sdk.models.verify_e_invoice_xml_error_response import (
    VerifyEInvoiceXmlErrorResponse,
)
from fattureincloud_python_sdk.models.verify_e_invoice_xml_error_response_error import (
    VerifyEInvoiceXmlErrorResponseError,
)
from fattureincloud_python_sdk.models.verify_e_invoice_xml_error_response_error_validation_result import (
    VerifyEInvoiceXmlErrorResponseErrorValidationResult,
)
from fattureincloud_python_sdk.models.verify_e_invoice_xml_error_response_extra import (
    VerifyEInvoiceXmlErrorResponseExtra,
)
from fattureincloud_python_sdk.models.verify_e_invoice_xml_response import (
    VerifyEInvoiceXmlResponse,
)
from fattureincloud_python_sdk.models.verify_e_invoice_xml_response_data import (
    VerifyEInvoiceXmlResponseData,
)
