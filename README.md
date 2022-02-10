# FattureInCloud Python SDK

Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy. 

The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.10
- Package version: 2.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.fattureincloud.it](https://www.fattureincloud.it)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install fattureincloud-python-sdk
```
(you may need to run `pip` with root permission: `sudo pip install fattureincloud-python-sdk`)

Then import the package:
```python
import fattureincloud_python_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import fattureincloud_python_sdk
from pprint import pprint
from fattureincloud_python_sdk.api import archive_api
from fattureincloud_python_sdk.model.create_archive_document_request import CreateArchiveDocumentRequest
from fattureincloud_python_sdk.model.create_archive_document_response import CreateArchiveDocumentResponse
from fattureincloud_python_sdk.model.get_archive_document_response import GetArchiveDocumentResponse
from fattureincloud_python_sdk.model.list_archive_documents_response import ListArchiveDocumentsResponse
from fattureincloud_python_sdk.model.modify_archive_document_request import ModifyArchiveDocumentRequest
from fattureincloud_python_sdk.model.modify_archive_document_response import ModifyArchiveDocumentResponse
from fattureincloud_python_sdk.model.upload_archive_attachment_response import UploadArchiveAttachmentResponse
# Defining the host is optional and defaults to https://api-v2.fattureincloud.it
# See configuration.py for a list of all supported configuration parameters.
configuration = fattureincloud_python_sdk.Configuration(
    host = "https://api-v2.fattureincloud.it"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    host = "https://api-v2.fattureincloud.it"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = archive_api.ArchiveApi(api_client)
    company_id = 12345 # int | The ID of the company.
create_archive_document_request = CreateArchiveDocumentRequest(
        data=ArchiveDocument(
            id=1,
            date=dateutil_parser('1970-01-01').date(),
            description="description_example",
            category="category_example",
            attachment_token="attachment_token_example",
        ),
    ) # CreateArchiveDocumentRequest | The Archive Document. (optional)

    try:
        # Create Archive Document
        api_response = api_instance.create_archive_document(company_id, create_archive_document_request=create_archive_document_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->create_archive_document: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api-v2.fattureincloud.it*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArchiveApi* | [**create_archive_document**](docs/ArchiveApi.md#create_archive_document) | **POST** /c/{company_id}/archive | Create Archive Document
*ArchiveApi* | [**delete_archive_document**](docs/ArchiveApi.md#delete_archive_document) | **DELETE** /c/{company_id}/archive/{document_id} | Delete Archive Document
*ArchiveApi* | [**get_archive_document**](docs/ArchiveApi.md#get_archive_document) | **GET** /c/{company_id}/archive/{document_id} | Get Archive Document
*ArchiveApi* | [**list_archive_documents**](docs/ArchiveApi.md#list_archive_documents) | **GET** /c/{company_id}/archive | List Archive Documents
*ArchiveApi* | [**modify_archive_document**](docs/ArchiveApi.md#modify_archive_document) | **PUT** /c/{company_id}/archive/{document_id} | Modify Archive Document
*ArchiveApi* | [**upload_archive_document_attachment**](docs/ArchiveApi.md#upload_archive_document_attachment) | **POST** /c/{company_id}/archive/attachment | Upload Archive Document Attachment
*CashbookApi* | [**create_cashbook_entry**](docs/CashbookApi.md#create_cashbook_entry) | **POST** /c/{company_id}/cashbook | Create Cashbook Entry
*CashbookApi* | [**delete_cashbook_entry**](docs/CashbookApi.md#delete_cashbook_entry) | **DELETE** /c/{company_id}/cashbook/{document_id} | Delete Cashbook Entry
*CashbookApi* | [**get_cashbook_entry**](docs/CashbookApi.md#get_cashbook_entry) | **GET** /c/{company_id}/cashbook/{document_id} | Get Cashbook Entry
*CashbookApi* | [**list_cashbook_entries**](docs/CashbookApi.md#list_cashbook_entries) | **GET** /c/{company_id}/cashbook | List Cashbook Entries
*CashbookApi* | [**modify_cashbook_entry**](docs/CashbookApi.md#modify_cashbook_entry) | **PUT** /c/{company_id}/cashbook/{document_id} | Modify Cashbook Entry
*ClientsApi* | [**create_client**](docs/ClientsApi.md#create_client) | **POST** /c/{company_id}/entities/clients | Create Client
*ClientsApi* | [**delete_client**](docs/ClientsApi.md#delete_client) | **DELETE** /c/{company_id}/entities/clients/{client_id} | Delete Client
*ClientsApi* | [**get_client**](docs/ClientsApi.md#get_client) | **GET** /c/{company_id}/entities/clients/{client_id} | Get Client
*ClientsApi* | [**list_clients**](docs/ClientsApi.md#list_clients) | **GET** /c/{company_id}/entities/clients | List Clients
*ClientsApi* | [**modify_client**](docs/ClientsApi.md#modify_client) | **PUT** /c/{company_id}/entities/clients/{client_id} | Modify Client
*CompaniesApi* | [**get_company_info**](docs/CompaniesApi.md#get_company_info) | **GET** /c/{company_id}/company/info | Get Company Info
*InfoApi* | [**list_archive_categories**](docs/InfoApi.md#list_archive_categories) | **GET** /c/{company_id}/info/archive_categories | List Archive Categories
*InfoApi* | [**list_cities**](docs/InfoApi.md#list_cities) | **GET** /info/cities | List Cities
*InfoApi* | [**list_cost_centers**](docs/InfoApi.md#list_cost_centers) | **GET** /c/{company_id}/info/cost_centers | List Cost Centers
*InfoApi* | [**list_countries**](docs/InfoApi.md#list_countries) | **GET** /info/countries | List Countries
*InfoApi* | [**list_currencies**](docs/InfoApi.md#list_currencies) | **GET** /info/currencies | List Currencies
*InfoApi* | [**list_delivery_notes_default_causals**](docs/InfoApi.md#list_delivery_notes_default_causals) | **GET** /info/dn_causals | List Delivery Notes Default Causals
*InfoApi* | [**list_languages**](docs/InfoApi.md#list_languages) | **GET** /info/languages | List Languages
*InfoApi* | [**list_payment_accounts**](docs/InfoApi.md#list_payment_accounts) | **GET** /c/{company_id}/info/payment_accounts | List Payment Accounts
*InfoApi* | [**list_payment_methods**](docs/InfoApi.md#list_payment_methods) | **GET** /c/{company_id}/info/payment_methods | List Payment Methods
*InfoApi* | [**list_product_categories**](docs/InfoApi.md#list_product_categories) | **GET** /c/{company_id}/info/product_categories | List Product Categories
*InfoApi* | [**list_received_document_categories**](docs/InfoApi.md#list_received_document_categories) | **GET** /c/{company_id}/info/received_document_categories | List Received Document Categories
*InfoApi* | [**list_revenue_centers**](docs/InfoApi.md#list_revenue_centers) | **GET** /c/{company_id}/info/revenue_centers | List Revenue Centers
*InfoApi* | [**list_templates**](docs/InfoApi.md#list_templates) | **GET** /info/templates | List Templates
*InfoApi* | [**list_units_of_measure**](docs/InfoApi.md#list_units_of_measure) | **GET** /info/measures | List Units of Measure
*InfoApi* | [**list_vat_types**](docs/InfoApi.md#list_vat_types) | **GET** /c/{company_id}/info/vat_types | List Vat Types
*IssuedDocumentsApi* | [**create_issued_document**](docs/IssuedDocumentsApi.md#create_issued_document) | **POST** /c/{company_id}/issued_documents | Create Issued Document
*IssuedDocumentsApi* | [**delete_issued_document**](docs/IssuedDocumentsApi.md#delete_issued_document) | **DELETE** /c/{company_id}/issued_documents/{document_id} | Delete Issued Document
*IssuedDocumentsApi* | [**delete_issued_document_attachment**](docs/IssuedDocumentsApi.md#delete_issued_document_attachment) | **DELETE** /c/{company_id}/issued_documents/{document_id}/attachment | Delete Issued Document Attachment
*IssuedDocumentsApi* | [**get_email_data**](docs/IssuedDocumentsApi.md#get_email_data) | **GET** /c/{company_id}/issued_documents/{document_id}/email | Get Email Data
*IssuedDocumentsApi* | [**get_existing_issued_document_totals**](docs/IssuedDocumentsApi.md#get_existing_issued_document_totals) | **POST** /c/{company_id}/issued_documents/{document_id}/totals | Get Existing Issued Document Totals
*IssuedDocumentsApi* | [**get_issued_document**](docs/IssuedDocumentsApi.md#get_issued_document) | **GET** /c/{company_id}/issued_documents/{document_id} | Get Issued Document
*IssuedDocumentsApi* | [**get_issued_document_pre_create_info**](docs/IssuedDocumentsApi.md#get_issued_document_pre_create_info) | **GET** /c/{company_id}/issued_documents/info | Get Issued Document Pre-create info
*IssuedDocumentsApi* | [**get_new_issued_document_totals**](docs/IssuedDocumentsApi.md#get_new_issued_document_totals) | **POST** /c/{company_id}/issued_documents/totals | Get New Issued Document Totals
*IssuedDocumentsApi* | [**list_issued_documents**](docs/IssuedDocumentsApi.md#list_issued_documents) | **GET** /c/{company_id}/issued_documents | List Issued Documents
*IssuedDocumentsApi* | [**modify_issued_document**](docs/IssuedDocumentsApi.md#modify_issued_document) | **PUT** /c/{company_id}/issued_documents/{document_id} | Modify Issued Document
*IssuedDocumentsApi* | [**schedule_email**](docs/IssuedDocumentsApi.md#schedule_email) | **POST** /c/{company_id}/issued_documents/{document_id}/email | Schedule Email
*IssuedDocumentsApi* | [**upload_issued_document_attachment**](docs/IssuedDocumentsApi.md#upload_issued_document_attachment) | **POST** /c/{company_id}/issued_documents/attachment | Upload Issued Document Attachment
*IssuedEInvoicesApi* | [**get_e_invoice_rejection_reason**](docs/IssuedEInvoicesApi.md#get_e_invoice_rejection_reason) | **GET** /c/{company_id}/issued_documents/{document_id}/e_invoice/error_reason | Get EInvoice rejection reason
*IssuedEInvoicesApi* | [**get_e_invoice_xml**](docs/IssuedEInvoicesApi.md#get_e_invoice_xml) | **GET** /c/{company_id}/issued_documents/{document_id}/e_invoice/xml | Get e-invoice XML
*IssuedEInvoicesApi* | [**send_e_invoice**](docs/IssuedEInvoicesApi.md#send_e_invoice) | **POST** /c/{company_id}/issued_documents/{document_id}/e_invoice/send | Send the e-invoice
*IssuedEInvoicesApi* | [**verify_e_invoice_xml**](docs/IssuedEInvoicesApi.md#verify_e_invoice_xml) | **GET** /c/{company_id}/issued_documents/{document_id}/e_invoice/xml_verify | Verify e-invoice xml
*ProductsApi* | [**create_product**](docs/ProductsApi.md#create_product) | **POST** /c/{company_id}/products | Create Product
*ProductsApi* | [**delete_product**](docs/ProductsApi.md#delete_product) | **DELETE** /c/{company_id}/products/{product_id} | Delete Product
*ProductsApi* | [**get_product**](docs/ProductsApi.md#get_product) | **GET** /c/{company_id}/products/{product_id} | Get Product
*ProductsApi* | [**list_products**](docs/ProductsApi.md#list_products) | **GET** /c/{company_id}/products | List Products
*ProductsApi* | [**modify_product**](docs/ProductsApi.md#modify_product) | **PUT** /c/{company_id}/products/{product_id} | Modify Product
*ReceiptsApi* | [**create_receipt**](docs/ReceiptsApi.md#create_receipt) | **POST** /c/{company_id}/receipts | Create Receipt
*ReceiptsApi* | [**delete_receipt**](docs/ReceiptsApi.md#delete_receipt) | **DELETE** /c/{company_id}/receipts/{document_id} | Delete Receipt
*ReceiptsApi* | [**get_receipt**](docs/ReceiptsApi.md#get_receipt) | **GET** /c/{company_id}/receipts/{document_id} | Get Receipt
*ReceiptsApi* | [**get_receipt_pre_create_info**](docs/ReceiptsApi.md#get_receipt_pre_create_info) | **GET** /c/{company_id}/receipts/info | Get Receipt Pre-Create Info
*ReceiptsApi* | [**get_receipts_monthly_totals**](docs/ReceiptsApi.md#get_receipts_monthly_totals) | **GET** /c/{company_id}/receipts/monthly_totals | Get Receipts Monthly Totals
*ReceiptsApi* | [**list_receipts**](docs/ReceiptsApi.md#list_receipts) | **GET** /c/{company_id}/receipts | List Receipts
*ReceiptsApi* | [**modify_receipt**](docs/ReceiptsApi.md#modify_receipt) | **PUT** /c/{company_id}/receipts/{document_id} | Modify Receipt
*ReceivedDocumentsApi* | [**create_received_document**](docs/ReceivedDocumentsApi.md#create_received_document) | **POST** /c/{company_id}/received_documents | Create Received Document
*ReceivedDocumentsApi* | [**delete_received_document**](docs/ReceivedDocumentsApi.md#delete_received_document) | **DELETE** /c/{company_id}/received_documents/{document_id} | Delete Received Document
*ReceivedDocumentsApi* | [**delete_received_document_attachment**](docs/ReceivedDocumentsApi.md#delete_received_document_attachment) | **DELETE** /c/{company_id}/received_documents/{document_id}/attachment | Delete Received Document Attachment
*ReceivedDocumentsApi* | [**get_existing_received_document_totals**](docs/ReceivedDocumentsApi.md#get_existing_received_document_totals) | **POST** /c/{company_id}/received_documents/{document_id}/totals | Get Existing Received Document Totals
*ReceivedDocumentsApi* | [**get_new_received_document_totals**](docs/ReceivedDocumentsApi.md#get_new_received_document_totals) | **POST** /c/{company_id}/received_documents/totals | Get New Received Document Totals
*ReceivedDocumentsApi* | [**get_received_document**](docs/ReceivedDocumentsApi.md#get_received_document) | **GET** /c/{company_id}/received_documents/{document_id} | Get Received Document
*ReceivedDocumentsApi* | [**get_received_document_pre_create_info**](docs/ReceivedDocumentsApi.md#get_received_document_pre_create_info) | **GET** /c/{company_id}/received_documents/info | Get Received Document Pre-Create Info
*ReceivedDocumentsApi* | [**list_received_documents**](docs/ReceivedDocumentsApi.md#list_received_documents) | **GET** /c/{company_id}/received_documents | List Received Documents
*ReceivedDocumentsApi* | [**modify_received_document**](docs/ReceivedDocumentsApi.md#modify_received_document) | **PUT** /c/{company_id}/received_documents/{document_id} | Modify Received Document
*ReceivedDocumentsApi* | [**upload_received_document_attachment**](docs/ReceivedDocumentsApi.md#upload_received_document_attachment) | **POST** /c/{company_id}/received_documents/attachment | Upload Received Document Attachment
*SettingsApi* | [**create_payment_account**](docs/SettingsApi.md#create_payment_account) | **POST** /c/{company_id}/settings/payment_accounts | Create Payment Account
*SettingsApi* | [**create_payment_method**](docs/SettingsApi.md#create_payment_method) | **POST** /c/{company_id}/settings/payment_methods | Create Payment Method
*SettingsApi* | [**create_vat_type**](docs/SettingsApi.md#create_vat_type) | **POST** /c/{company_id}/settings/vat_types | Create Vat Type
*SettingsApi* | [**delete_payment_account**](docs/SettingsApi.md#delete_payment_account) | **DELETE** /c/{company_id}/settings/payment_accounts/{payment_account_id} | Delete Payment Account
*SettingsApi* | [**delete_payment_method**](docs/SettingsApi.md#delete_payment_method) | **DELETE** /c/{company_id}/settings/payment_methods/{payment_method_id} | Delete Payment Method
*SettingsApi* | [**delete_vat_type**](docs/SettingsApi.md#delete_vat_type) | **DELETE** /c/{company_id}/settings/vat_types/{vat_type_id} | Delete Vat Type
*SettingsApi* | [**get_payment_account**](docs/SettingsApi.md#get_payment_account) | **GET** /c/{company_id}/settings/payment_accounts/{payment_account_id} | Get Payment Account
*SettingsApi* | [**get_payment_method**](docs/SettingsApi.md#get_payment_method) | **GET** /c/{company_id}/settings/payment_methods/{payment_method_id} | Get Payment Method
*SettingsApi* | [**get_vat_type**](docs/SettingsApi.md#get_vat_type) | **GET** /c/{company_id}/settings/vat_types/{vat_type_id} | Get Vat Type
*SettingsApi* | [**modify_payment_account**](docs/SettingsApi.md#modify_payment_account) | **PUT** /c/{company_id}/settings/payment_accounts/{payment_account_id} | Modify Payment Account
*SettingsApi* | [**modify_payment_method**](docs/SettingsApi.md#modify_payment_method) | **PUT** /c/{company_id}/settings/payment_methods/{payment_method_id} | Modify Payment Method
*SettingsApi* | [**modify_vat_type**](docs/SettingsApi.md#modify_vat_type) | **PUT** /c/{company_id}/settings/vat_types/{vat_type_id} | Modify Vat Type
*SuppliersApi* | [**create_supplier**](docs/SuppliersApi.md#create_supplier) | **POST** /c/{company_id}/entities/suppliers | Create Supplier
*SuppliersApi* | [**delete_supplier**](docs/SuppliersApi.md#delete_supplier) | **DELETE** /c/{company_id}/entities/suppliers/{supplier_id} | Delete Supplier
*SuppliersApi* | [**get_supplier**](docs/SuppliersApi.md#get_supplier) | **GET** /c/{company_id}/entities/suppliers/{supplier_id} | Get Supplier
*SuppliersApi* | [**list_suppliers**](docs/SuppliersApi.md#list_suppliers) | **GET** /c/{company_id}/entities/suppliers | List Suppliers
*SuppliersApi* | [**modify_supplier**](docs/SuppliersApi.md#modify_supplier) | **PUT** /c/{company_id}/entities/suppliers/{supplier_id} | Modify Supplier
*TaxesApi* | [**create_f24**](docs/TaxesApi.md#create_f24) | **POST** /c/{company_id}/taxes | Create F24
*TaxesApi* | [**delete_f24**](docs/TaxesApi.md#delete_f24) | **DELETE** /c/{company_id}/taxes/{document_id} | Delete F24
*TaxesApi* | [**delete_f24_attachment**](docs/TaxesApi.md#delete_f24_attachment) | **DELETE** /c/{company_id}/taxes/{document_id}/attachment | Delete F24 Attachment
*TaxesApi* | [**get_f24**](docs/TaxesApi.md#get_f24) | **GET** /c/{company_id}/taxes/{document_id} | Get F24
*TaxesApi* | [**list_f24**](docs/TaxesApi.md#list_f24) | **GET** /c/{company_id}/taxes | List F24
*TaxesApi* | [**modify_f24**](docs/TaxesApi.md#modify_f24) | **PUT** /c/{company_id}/taxes/{document_id} | Modify F24
*TaxesApi* | [**upload_f24_attachment**](docs/TaxesApi.md#upload_f24_attachment) | **POST** /c/{company_id}/taxes/attachment | Upload F24 Attachment
*UserApi* | [**get_user_info**](docs/UserApi.md#get_user_info) | **GET** /user/info | Get User Info
*UserApi* | [**list_user_companies**](docs/UserApi.md#list_user_companies) | **GET** /user/companies | List User Companies


## Documentation For Models

 - [ArchiveDocument](docs/ArchiveDocument.md)
 - [AttachmentData](docs/AttachmentData.md)
 - [CashbookEntry](docs/CashbookEntry.md)
 - [CashbookEntryDocument](docs/CashbookEntryDocument.md)
 - [CashbookEntryKind](docs/CashbookEntryKind.md)
 - [CashbookEntryType](docs/CashbookEntryType.md)
 - [City](docs/City.md)
 - [Client](docs/Client.md)
 - [ClientType](docs/ClientType.md)
 - [Company](docs/Company.md)
 - [CompanyInfo](docs/CompanyInfo.md)
 - [CompanyInfoAccessInfo](docs/CompanyInfoAccessInfo.md)
 - [CompanyInfoPlanInfo](docs/CompanyInfoPlanInfo.md)
 - [CompanyInfoPlanInfoFunctions](docs/CompanyInfoPlanInfoFunctions.md)
 - [CompanyInfoPlanInfoFunctionsStatus](docs/CompanyInfoPlanInfoFunctionsStatus.md)
 - [CompanyInfoPlanInfoLimits](docs/CompanyInfoPlanInfoLimits.md)
 - [CompanyType](docs/CompanyType.md)
 - [ControlledCompany](docs/ControlledCompany.md)
 - [CreateArchiveDocumentRequest](docs/CreateArchiveDocumentRequest.md)
 - [CreateArchiveDocumentResponse](docs/CreateArchiveDocumentResponse.md)
 - [CreateCashbookEntryRequest](docs/CreateCashbookEntryRequest.md)
 - [CreateCashbookEntryResponse](docs/CreateCashbookEntryResponse.md)
 - [CreateClientRequest](docs/CreateClientRequest.md)
 - [CreateClientResponse](docs/CreateClientResponse.md)
 - [CreateF24Request](docs/CreateF24Request.md)
 - [CreateF24Response](docs/CreateF24Response.md)
 - [CreateIssuedDocumentRequest](docs/CreateIssuedDocumentRequest.md)
 - [CreateIssuedDocumentResponse](docs/CreateIssuedDocumentResponse.md)
 - [CreatePaymentAccountRequest](docs/CreatePaymentAccountRequest.md)
 - [CreatePaymentAccountResponse](docs/CreatePaymentAccountResponse.md)
 - [CreatePaymentMethodRequest](docs/CreatePaymentMethodRequest.md)
 - [CreatePaymentMethodResponse](docs/CreatePaymentMethodResponse.md)
 - [CreateProductRequest](docs/CreateProductRequest.md)
 - [CreateProductResponse](docs/CreateProductResponse.md)
 - [CreateReceiptRequest](docs/CreateReceiptRequest.md)
 - [CreateReceiptResponse](docs/CreateReceiptResponse.md)
 - [CreateReceivedDocumentRequest](docs/CreateReceivedDocumentRequest.md)
 - [CreateReceivedDocumentResponse](docs/CreateReceivedDocumentResponse.md)
 - [CreateSupplierRequest](docs/CreateSupplierRequest.md)
 - [CreateSupplierResponse](docs/CreateSupplierResponse.md)
 - [CreateVatTypeRequest](docs/CreateVatTypeRequest.md)
 - [CreateVatTypeResponse](docs/CreateVatTypeResponse.md)
 - [Currency](docs/Currency.md)
 - [DefaultPaymentTermsType](docs/DefaultPaymentTermsType.md)
 - [DocumentTemplate](docs/DocumentTemplate.md)
 - [EinvoiceRejectionReason](docs/EinvoiceRejectionReason.md)
 - [EmailData](docs/EmailData.md)
 - [EmailDataDefaultSenderEmail](docs/EmailDataDefaultSenderEmail.md)
 - [EmailSchedule](docs/EmailSchedule.md)
 - [EmailScheduleInclude](docs/EmailScheduleInclude.md)
 - [Entity](docs/Entity.md)
 - [EntityType](docs/EntityType.md)
 - [F24](docs/F24.md)
 - [F24Status](docs/F24Status.md)
 - [FunctionStatus](docs/FunctionStatus.md)
 - [GetArchiveDocumentResponse](docs/GetArchiveDocumentResponse.md)
 - [GetCashbookEntryResponse](docs/GetCashbookEntryResponse.md)
 - [GetClientResponse](docs/GetClientResponse.md)
 - [GetCompanyInfoResponse](docs/GetCompanyInfoResponse.md)
 - [GetEInvoiceRejectionReasonResponse](docs/GetEInvoiceRejectionReasonResponse.md)
 - [GetEmailDataResponse](docs/GetEmailDataResponse.md)
 - [GetExistingIssuedDocumentTotalsRequest](docs/GetExistingIssuedDocumentTotalsRequest.md)
 - [GetExistingIssuedDocumentTotalsResponse](docs/GetExistingIssuedDocumentTotalsResponse.md)
 - [GetExistingReceivedDocumentTotalsRequest](docs/GetExistingReceivedDocumentTotalsRequest.md)
 - [GetExistingReceivedDocumentTotalsResponse](docs/GetExistingReceivedDocumentTotalsResponse.md)
 - [GetF24Response](docs/GetF24Response.md)
 - [GetIssuedDocumentPreCreateInfoResponse](docs/GetIssuedDocumentPreCreateInfoResponse.md)
 - [GetIssuedDocumentResponse](docs/GetIssuedDocumentResponse.md)
 - [GetNewIssuedDocumentTotalsRequest](docs/GetNewIssuedDocumentTotalsRequest.md)
 - [GetNewIssuedDocumentTotalsResponse](docs/GetNewIssuedDocumentTotalsResponse.md)
 - [GetNewReceivedDocumentTotalsRequest](docs/GetNewReceivedDocumentTotalsRequest.md)
 - [GetNewReceivedDocumentTotalsResponse](docs/GetNewReceivedDocumentTotalsResponse.md)
 - [GetPaymentAccountResponse](docs/GetPaymentAccountResponse.md)
 - [GetPaymentMethodResponse](docs/GetPaymentMethodResponse.md)
 - [GetProductResponse](docs/GetProductResponse.md)
 - [GetReceiptPreCreateInfoResponse](docs/GetReceiptPreCreateInfoResponse.md)
 - [GetReceiptResponse](docs/GetReceiptResponse.md)
 - [GetReceiptsMonthlyTotalsResponse](docs/GetReceiptsMonthlyTotalsResponse.md)
 - [GetReceivedDocumentPreCreateInfoResponse](docs/GetReceivedDocumentPreCreateInfoResponse.md)
 - [GetReceivedDocumentResponse](docs/GetReceivedDocumentResponse.md)
 - [GetSupplierResponse](docs/GetSupplierResponse.md)
 - [GetUserInfoResponse](docs/GetUserInfoResponse.md)
 - [GetUserInfoResponseEmailConfirmationState](docs/GetUserInfoResponseEmailConfirmationState.md)
 - [GetUserInfoResponseInfo](docs/GetUserInfoResponseInfo.md)
 - [GetVatTypeResponse](docs/GetVatTypeResponse.md)
 - [IssuedDocument](docs/IssuedDocument.md)
 - [IssuedDocumentEiData](docs/IssuedDocumentEiData.md)
 - [IssuedDocumentExtraData](docs/IssuedDocumentExtraData.md)
 - [IssuedDocumentItemsListItem](docs/IssuedDocumentItemsListItem.md)
 - [IssuedDocumentPaymentsListItem](docs/IssuedDocumentPaymentsListItem.md)
 - [IssuedDocumentPreCreateInfo](docs/IssuedDocumentPreCreateInfo.md)
 - [IssuedDocumentPreCreateInfoDefaultValues](docs/IssuedDocumentPreCreateInfoDefaultValues.md)
 - [IssuedDocumentPreCreateInfoExtraDataDefaultValues](docs/IssuedDocumentPreCreateInfoExtraDataDefaultValues.md)
 - [IssuedDocumentPreCreateInfoItemsDefaultValues](docs/IssuedDocumentPreCreateInfoItemsDefaultValues.md)
 - [IssuedDocumentStatus](docs/IssuedDocumentStatus.md)
 - [IssuedDocumentTotals](docs/IssuedDocumentTotals.md)
 - [IssuedDocumentTotalsVatList](docs/IssuedDocumentTotalsVatList.md)
 - [IssuedDocumentTotalsVatListVatItem](docs/IssuedDocumentTotalsVatListVatItem.md)
 - [IssuedDocumentType](docs/IssuedDocumentType.md)
 - [Language](docs/Language.md)
 - [ListArchiveCategoriesResponse](docs/ListArchiveCategoriesResponse.md)
 - [ListArchiveDocumentsResponse](docs/ListArchiveDocumentsResponse.md)
 - [ListArchiveDocumentsResponsePage](docs/ListArchiveDocumentsResponsePage.md)
 - [ListCashbookEntriesResponse](docs/ListCashbookEntriesResponse.md)
 - [ListCitiesResponse](docs/ListCitiesResponse.md)
 - [ListClientsResponse](docs/ListClientsResponse.md)
 - [ListClientsResponsePage](docs/ListClientsResponsePage.md)
 - [ListCostCentersResponse](docs/ListCostCentersResponse.md)
 - [ListCountriesResponse](docs/ListCountriesResponse.md)
 - [ListCurrenciesResponse](docs/ListCurrenciesResponse.md)
 - [ListDeliveryNotesDefaultCausalsResponse](docs/ListDeliveryNotesDefaultCausalsResponse.md)
 - [ListF24Response](docs/ListF24Response.md)
 - [ListF24ResponseAggregatedData](docs/ListF24ResponseAggregatedData.md)
 - [ListF24ResponseAggregation](docs/ListF24ResponseAggregation.md)
 - [ListF24ResponsePage](docs/ListF24ResponsePage.md)
 - [ListIssuedDocumentsResponse](docs/ListIssuedDocumentsResponse.md)
 - [ListIssuedDocumentsResponsePage](docs/ListIssuedDocumentsResponsePage.md)
 - [ListLanguagesResponse](docs/ListLanguagesResponse.md)
 - [ListPaymentAccountsResponse](docs/ListPaymentAccountsResponse.md)
 - [ListPaymentMethodsResponse](docs/ListPaymentMethodsResponse.md)
 - [ListProductCategoriesResponse](docs/ListProductCategoriesResponse.md)
 - [ListProductsResponse](docs/ListProductsResponse.md)
 - [ListProductsResponsePage](docs/ListProductsResponsePage.md)
 - [ListReceiptsResponse](docs/ListReceiptsResponse.md)
 - [ListReceiptsResponsePage](docs/ListReceiptsResponsePage.md)
 - [ListReceivedDocumentCategoriesResponse](docs/ListReceivedDocumentCategoriesResponse.md)
 - [ListReceivedDocumentsResponse](docs/ListReceivedDocumentsResponse.md)
 - [ListReceivedDocumentsResponsePage](docs/ListReceivedDocumentsResponsePage.md)
 - [ListRevenueCentersResponse](docs/ListRevenueCentersResponse.md)
 - [ListSuppliersResponse](docs/ListSuppliersResponse.md)
 - [ListSuppliersResponsePage](docs/ListSuppliersResponsePage.md)
 - [ListTemplatesResponse](docs/ListTemplatesResponse.md)
 - [ListUnitsOfMeasureResponse](docs/ListUnitsOfMeasureResponse.md)
 - [ListUserCompaniesResponse](docs/ListUserCompaniesResponse.md)
 - [ListUserCompaniesResponseData](docs/ListUserCompaniesResponseData.md)
 - [ListVatTypesResponse](docs/ListVatTypesResponse.md)
 - [ModifyArchiveDocumentRequest](docs/ModifyArchiveDocumentRequest.md)
 - [ModifyArchiveDocumentResponse](docs/ModifyArchiveDocumentResponse.md)
 - [ModifyCashbookEntryRequest](docs/ModifyCashbookEntryRequest.md)
 - [ModifyCashbookEntryResponse](docs/ModifyCashbookEntryResponse.md)
 - [ModifyClientRequest](docs/ModifyClientRequest.md)
 - [ModifyClientResponse](docs/ModifyClientResponse.md)
 - [ModifyF24Request](docs/ModifyF24Request.md)
 - [ModifyF24Response](docs/ModifyF24Response.md)
 - [ModifyIssuedDocumentRequest](docs/ModifyIssuedDocumentRequest.md)
 - [ModifyIssuedDocumentResponse](docs/ModifyIssuedDocumentResponse.md)
 - [ModifyPaymentAccountRequest](docs/ModifyPaymentAccountRequest.md)
 - [ModifyPaymentAccountResponse](docs/ModifyPaymentAccountResponse.md)
 - [ModifyPaymentMethodRequest](docs/ModifyPaymentMethodRequest.md)
 - [ModifyPaymentMethodResponse](docs/ModifyPaymentMethodResponse.md)
 - [ModifyProductRequest](docs/ModifyProductRequest.md)
 - [ModifyProductResponse](docs/ModifyProductResponse.md)
 - [ModifyReceiptRequest](docs/ModifyReceiptRequest.md)
 - [ModifyReceiptResponse](docs/ModifyReceiptResponse.md)
 - [ModifyReceivedDocumentRequest](docs/ModifyReceivedDocumentRequest.md)
 - [ModifyReceivedDocumentResponse](docs/ModifyReceivedDocumentResponse.md)
 - [ModifySupplierRequest](docs/ModifySupplierRequest.md)
 - [ModifySupplierResponse](docs/ModifySupplierResponse.md)
 - [ModifyVatTypeRequest](docs/ModifyVatTypeRequest.md)
 - [ModifyVatTypeResponse](docs/ModifyVatTypeResponse.md)
 - [MonthlyTotal](docs/MonthlyTotal.md)
 - [OriginalDocumentType](docs/OriginalDocumentType.md)
 - [Pagination](docs/Pagination.md)
 - [PaymentAccount](docs/PaymentAccount.md)
 - [PaymentAccountType](docs/PaymentAccountType.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentMethodDetails](docs/PaymentMethodDetails.md)
 - [PaymentMethodType](docs/PaymentMethodType.md)
 - [PermissionLevel](docs/PermissionLevel.md)
 - [Permissions](docs/Permissions.md)
 - [PermissionsFicIssuedDocumentsDetailed](docs/PermissionsFicIssuedDocumentsDetailed.md)
 - [Product](docs/Product.md)
 - [Receipt](docs/Receipt.md)
 - [ReceiptItemsListItem](docs/ReceiptItemsListItem.md)
 - [ReceiptPreCreateInfo](docs/ReceiptPreCreateInfo.md)
 - [ReceiptType](docs/ReceiptType.md)
 - [ReceivedDocument](docs/ReceivedDocument.md)
 - [ReceivedDocumentEntity](docs/ReceivedDocumentEntity.md)
 - [ReceivedDocumentInfo](docs/ReceivedDocumentInfo.md)
 - [ReceivedDocumentInfoDefaultValues](docs/ReceivedDocumentInfoDefaultValues.md)
 - [ReceivedDocumentInfoItemsDefaultValues](docs/ReceivedDocumentInfoItemsDefaultValues.md)
 - [ReceivedDocumentItemsListItem](docs/ReceivedDocumentItemsListItem.md)
 - [ReceivedDocumentPaymentsListItem](docs/ReceivedDocumentPaymentsListItem.md)
 - [ReceivedDocumentPaymentsListItemPaymentTerms](docs/ReceivedDocumentPaymentsListItemPaymentTerms.md)
 - [ReceivedDocumentTotals](docs/ReceivedDocumentTotals.md)
 - [ReceivedDocumentType](docs/ReceivedDocumentType.md)
 - [ScheduleEmailRequest](docs/ScheduleEmailRequest.md)
 - [SendEInvoiceRequest](docs/SendEInvoiceRequest.md)
 - [SendEInvoiceRequestData](docs/SendEInvoiceRequestData.md)
 - [SendEInvoiceResponse](docs/SendEInvoiceResponse.md)
 - [SendEInvoiceResponseData](docs/SendEInvoiceResponseData.md)
 - [SenderEmail](docs/SenderEmail.md)
 - [ShowTotalsMode](docs/ShowTotalsMode.md)
 - [Supplier](docs/Supplier.md)
 - [SupplierType](docs/SupplierType.md)
 - [UploadArchiveAttachmentResponse](docs/UploadArchiveAttachmentResponse.md)
 - [UploadF24AttachmentResponse](docs/UploadF24AttachmentResponse.md)
 - [UploadIssuedDocumentAttachmentResponse](docs/UploadIssuedDocumentAttachmentResponse.md)
 - [UploadReceivedDocumentAttachmentResponse](docs/UploadReceivedDocumentAttachmentResponse.md)
 - [User](docs/User.md)
 - [UserCompanyRole](docs/UserCompanyRole.md)
 - [VatKind](docs/VatKind.md)
 - [VatType](docs/VatType.md)
 - [VerifyEInvoiceXmlErrorResponse](docs/VerifyEInvoiceXmlErrorResponse.md)
 - [VerifyEInvoiceXmlErrorResponseError](docs/VerifyEInvoiceXmlErrorResponseError.md)
 - [VerifyEInvoiceXmlErrorResponseExtra](docs/VerifyEInvoiceXmlErrorResponseExtra.md)
 - [VerifyEInvoiceXmlResponse](docs/VerifyEInvoiceXmlResponse.md)
 - [VerifyEInvoiceXmlResponseData](docs/VerifyEInvoiceXmlResponseData.md)


## Documentation For Authorization


## OAuth2AuthenticationCodeFlow

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://api-v2.fattureincloud.it/oauth/authorize
- **Scopes**: 
 - **entity.clients:r**: 
 - **entity.clients:a**: 
 - **entity.suppliers:r**: 
 - **entity.suppliers:a**: 
 - **products:r**: 
 - **products:a**: 
 - **issued_documents.invoice:r**: 
 - **issued_documents.credit_note:r**: 
 - **issued_documents.receipt:r**: 
 - **issued_documents.order:r**: 
 - **issued_documents.quote:r**: 
 - **issued_documents.proforma:r**: 
 - **issued_documents.delivery_note:r**: 
 - **issued_documents.invoice:a**: 
 - **issued_documents.credit_note:a**: 
 - **issued_documents.receipt:a**: 
 - **issued_documents.order:a**: 
 - **issued_documents.quote:a**: 
 - **issued_documents.proforma:a**: 
 - **issued_documents.delivery_note:a**: 
 - **received_documents:r**: 
 - **received_documents:a**: 
 - **stock:r**: 
 - **stock:a**: 
 - **receipts:r**: 
 - **receipts:a**: 
 - **taxes:r**: 
 - **taxes:a**: 
 - **archive:r**: 
 - **archive:a**: 
 - **cashbook:r**: 
 - **cashbook:a**: 
 - **settings:r**: 
 - **settings:a**: 
 - **situation:r**: 


## Author

info@fattureincloud.it


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in fattureincloud_python_sdk.apis and fattureincloud_python_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from fattureincloud_python_sdk.api.default_api import DefaultApi`
- `from fattureincloud_python_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import fattureincloud_python_sdk
from fattureincloud_python_sdk.apis import *
from fattureincloud_python_sdk.models import *
```

