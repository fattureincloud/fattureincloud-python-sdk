# fattureincloud_python_sdk.IssuedDocumentsApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_issued_document**](IssuedDocumentsApi.md#create_issued_document) | **POST** /c/{company_id}/issued_documents | Create Issued Document
[**delete_issued_document**](IssuedDocumentsApi.md#delete_issued_document) | **DELETE** /c/{company_id}/issued_documents/{document_id} | Delete Issued Document
[**delete_issued_document_attachment**](IssuedDocumentsApi.md#delete_issued_document_attachment) | **DELETE** /c/{company_id}/issued_documents/{document_id}/attachment | Delete Issued Document Attachment
[**get_email_data**](IssuedDocumentsApi.md#get_email_data) | **GET** /c/{company_id}/issued_documents/{document_id}/email | Get Email Data
[**get_existing_issued_document_totals**](IssuedDocumentsApi.md#get_existing_issued_document_totals) | **POST** /c/{company_id}/issued_documents/{document_id}/totals | Get Existing Issued Document Totals
[**get_issued_document**](IssuedDocumentsApi.md#get_issued_document) | **GET** /c/{company_id}/issued_documents/{document_id} | Get Issued Document
[**get_issued_document_pre_create_info**](IssuedDocumentsApi.md#get_issued_document_pre_create_info) | **GET** /c/{company_id}/issued_documents/info | Get Issued Document Pre-create info
[**get_new_issued_document_totals**](IssuedDocumentsApi.md#get_new_issued_document_totals) | **POST** /c/{company_id}/issued_documents/totals | Get New Issued Document Totals
[**list_issued_documents**](IssuedDocumentsApi.md#list_issued_documents) | **GET** /c/{company_id}/issued_documents | List Issued Documents
[**modify_issued_document**](IssuedDocumentsApi.md#modify_issued_document) | **PUT** /c/{company_id}/issued_documents/{document_id} | Modify Issued Document
[**schedule_email**](IssuedDocumentsApi.md#schedule_email) | **POST** /c/{company_id}/issued_documents/{document_id}/email | Schedule Email
[**upload_issued_document_attachment**](IssuedDocumentsApi.md#upload_issued_document_attachment) | **POST** /c/{company_id}/issued_documents/attachment | Upload Issued Document Attachment


# **create_issued_document**
> CreateIssuedDocumentResponse create_issued_document(company_id)

Create Issued Document

Creates a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.create_issued_document_request import CreateIssuedDocumentRequest
from fattureincloud_python_sdk.model.create_issued_document_response import CreateIssuedDocumentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_issued_document_request = CreateIssuedDocumentRequest(
        data=IssuedDocument(
            id=1,
            entity=Entity(
                id=1,
                code="123",
                name="Rossi S.r.l.",
                type=EntityType("company"),
                first_name="first_name_example",
                last_name="last_name_example",
                contact_person="contact_person_example",
                vat_number="IT01234567890",
                tax_code="RSSMRA44A12E890Q",
                address_street="Via dei tigli, 12",
                address_postal_code="24010",
                address_city="Bergamo",
                address_province="BG",
                address_extra="address_extra_example",
                country="Italia",
                email="mario.rossi@example.it",
                certified_email="mario.rossi@pec.example.it",
                phone="phone_example",
                fax="fax_example",
                notes="notes_example",
                default_vat=VatType(
                    id=1,
                    value=22,
                    description="Non imponibile art. 123",
                    notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                    e_invoice=True,
                    ei_type="2",
                    ei_description="ei_description_example",
                    is_disabled=True,
                ),
                default_payment_terms=30,
                default_payment_terms_type=DefaultPaymentTermsType("standard"),
                default_payment_method=PaymentMethod(
                    id=1,
                    name="name_example",
                    type=PaymentMethodType("standard"),
                    is_default=True,
                    default_payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    details=[
                        PaymentMethodDetails(
                            title="title_example",
                            description="description_example",
                        ),
                    ],
                    bank_iban="bank_iban_example",
                    bank_name="bank_name_example",
                    bank_beneficiary="bank_beneficiary_example",
                    ei_payment_method="ei_payment_method_example",
                ),
                bank_name="bank_name_example",
                bank_iban="bank_iban_example",
                bank_swift_code="bank_swift_code_example",
                shipping_address="shipping_address_example",
                e_invoice=True,
                ei_code="ei_code_example",
                has_intent_declaration=True,
                intent_declaration_protocol_number=dateutil_parser('1970-01-01').date(),
                intent_declaration_protocol_date="intent_declaration_protocol_date_example",
                created_at="created_at_example",
                updated_at="updated_at_example",
            ),
            type=IssuedDocumentType("invoice"),
            number=1,
            numeration="/A",
            date=dateutil_parser('1970-01-01').date(),
            year=1,
            currency=Currency(
                id="EUR",
                symbol="€",
                exchange_rate="1",
                html_symbol="EUR",
            ),
            language=Language(
                code="code_example",
                name="name_example",
            ),
            subject="subject_example",
            visible_subject="visible_subject_example",
            rc_center="rc_center_example",
            notes="notes_example",
            rivalsa=3.14,
            cassa=3.14,
            cassa_taxable=3.14,
            amount_cassa_taxable=3.14,
            cassa2=3.14,
            cassa2_taxable=3.14,
            amount_cassa2_taxable=3.14,
            global_cassa_taxable=3.14,
            amount_global_cassa_taxable=3.14,
            withholding_tax=3.14,
            withholding_tax_taxable=3.14,
            other_withholding_tax=3.14,
            stamp_duty=3.14,
            payment_method=PaymentMethod(
                id=1,
                name="name_example",
                type=PaymentMethodType("standard"),
                is_default=True,
                default_payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                details=[
                    PaymentMethodDetails(
                        title="title_example",
                        description="description_example",
                    ),
                ],
                bank_iban="bank_iban_example",
                bank_name="bank_name_example",
                bank_beneficiary="bank_beneficiary_example",
                ei_payment_method="ei_payment_method_example",
            ),
            use_split_payment=True,
            use_gross_prices=True,
            e_invoice=True,
            ei_data=IssuedDocumentEiData(
                vat_kind=VatKind("vat_kind_example"),
                original_document_type=OriginalDocumentType("ordine"),
                od_number="od_number_example",
                od_date=dateutil_parser('1970-01-01').date(),
                cig="cig_example",
                cup="cup_example",
                payment_method="payment_method_example",
                bank_name="bank_name_example",
                bank_iban="bank_iban_example",
                bank_beneficiary="bank_beneficiary_example",
                invoice_number="invoice_number_example",
                invoice_date=dateutil_parser('1970-01-01').date(),
            ),
            ei_cassa_type="ei_cassa_type_example",
            ei_cassa2_type="ei_cassa2_type_example",
            ei_withholding_tax_causal="ei_withholding_tax_causal_example",
            ei_other_withholding_tax_type="ei_other_withholding_tax_type_example",
            ei_other_withholding_tax_causal="ei_other_withholding_tax_causal_example",
            items_list=[
                IssuedDocumentItemsListItem(
                    id=1,
                    product_id=1234,
                    code="239874892374982",
                    name="Water bottle",
                    category="category_example",
                    description="description_example",
                    qty=3.14,
                    measure="measure_example",
                    net_price=1.23,
                    gross_price=1.45,
                    vat=VatType(
                        id=1,
                        value=22,
                        description="Non imponibile art. 123",
                        notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                        e_invoice=True,
                        ei_type="2",
                        ei_description="ei_description_example",
                        is_disabled=True,
                    ),
                    not_taxable=True,
                    apply_withholding_taxes=True,
                    discount=3.14,
                    discount_highlight=True,
                    in_ddt=True,
                    stock=True,
                    ei_raw={},
                ),
            ],
            payments_list=[
                IssuedDocumentPaymentsListItem(
                    id=1,
                    due_date=dateutil_parser('Tue Apr 03 00:00:00 UTC 2018').date(),
                    amount=1.45,
                    status=IssuedDocumentStatus("not_paid"),
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    paid_date=dateutil_parser('Tue Apr 03 00:00:00 UTC 2018').date(),
                    ei_raw={},
                    payment_terms=IssuedDocumentPaymentsListItemPaymentTerms(
                        days=1,
                        type="standard",
                    ),
                ),
            ],
            template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            delivery_note_template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            acc_inv_template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            h_margins=1,
            v_margins=1,
            show_payments=True,
            show_payment_method=True,
            show_totals=ShowTotalsMode("all"),
            show_paypal_button=True,
            show_notification_button=True,
            show_tspay_button=True,
            delivery_note=True,
            accompanying_invoice=True,
            dn_number=1,
            dn_date=dateutil_parser('1970-01-01').date(),
            dn_ai_packages_number="dn_ai_packages_number_example",
            dn_ai_weight="dn_ai_weight_example",
            dn_ai_causal="dn_ai_causal_example",
            dn_ai_destination="dn_ai_destination_example",
            dn_ai_transporter="dn_ai_transporter_example",
            dn_ai_notes="dn_ai_notes_example",
            is_marked=True,
            amount_due_discount=3.14,
            amount_rivalsa_taxable=3.14,
            amount_withholding_tax_taxable=3.14,
            amount_other_withholding_tax_taxable=3.14,
            amount_enasarco_taxable=3.14,
            extra_data=IssuedDocumentExtraData(
                show_sofort_button=True,
                multifatture_sent=1,
                ts_communication=True,
                ts_flag_tipo_spesa=3.14,
                ts_pagamento_tracciato=True,
                ts_tipo_spesa="ts_tipo_spesa_example",
                ts_opposizione=True,
                ts_status=1,
                ts_file_id="ts_file_id_example",
                ts_sent_date=dateutil_parser('1970-01-01').date(),
                ts_full_amount=True,
                imported_by="imported_by_example",
                ts_single_sending=True,
            ),
            seen_date=dateutil_parser('1970-01-01').date(),
            next_due_date=dateutil_parser('1970-01-01').date(),
            url="url_example",
            attachment_token="attachment_token_example",
            ei_raw={},
            ei_status="attempt",
        ),
        options=IssuedDocumentOptions(
            fix_payments=True,
        ),
    ) # CreateIssuedDocumentRequest | The Issued Document (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Issued Document
        api_response = api_instance.create_issued_document(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->create_issued_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Issued Document
        api_response = api_instance.create_issued_document(company_id, create_issued_document_request=create_issued_document_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->create_issued_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **create_issued_document_request** | [**CreateIssuedDocumentRequest**](CreateIssuedDocumentRequest.md)| The Issued Document | [optional]

### Return type

[**CreateIssuedDocumentResponse**](CreateIssuedDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document created. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issued_document**
> delete_issued_document(company_id, document_id)

Delete Issued Document

Deletes the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Delete Issued Document
        api_instance.delete_issued_document(company_id, document_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->delete_issued_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |

### Return type

void (empty response body)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document removed |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issued_document_attachment**
> delete_issued_document_attachment(company_id, document_id)

Delete Issued Document Attachment

Removes the attachment of the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Delete Issued Document Attachment
        api_instance.delete_issued_document_attachment(company_id, document_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->delete_issued_document_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |

### Return type

void (empty response body)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File removed. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_data**
> GetEmailDataResponse get_email_data(company_id, document_id)

Get Email Data

Gets the pre-compiled email details.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.get_email_data_response import GetEmailDataResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Get Email Data
        api_response = api_instance.get_email_data(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->get_email_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |

### Return type

[**GetEmailDataResponse**](GetEmailDataResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailData |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_existing_issued_document_totals**
> GetExistingIssuedDocumentTotalsResponse get_existing_issued_document_totals(company_id, document_id)

Get Existing Issued Document Totals

Returns the totals for a specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.get_existing_issued_document_totals_request import GetExistingIssuedDocumentTotalsRequest
from fattureincloud_python_sdk.model.get_existing_issued_document_totals_response import GetExistingIssuedDocumentTotalsResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    get_existing_issued_document_totals_request = GetExistingIssuedDocumentTotalsRequest(
        data=IssuedDocument(
            id=1,
            entity=Entity(
                id=1,
                code="123",
                name="Rossi S.r.l.",
                type=EntityType("company"),
                first_name="first_name_example",
                last_name="last_name_example",
                contact_person="contact_person_example",
                vat_number="IT01234567890",
                tax_code="RSSMRA44A12E890Q",
                address_street="Via dei tigli, 12",
                address_postal_code="24010",
                address_city="Bergamo",
                address_province="BG",
                address_extra="address_extra_example",
                country="Italia",
                email="mario.rossi@example.it",
                certified_email="mario.rossi@pec.example.it",
                phone="phone_example",
                fax="fax_example",
                notes="notes_example",
                default_vat=VatType(
                    id=1,
                    value=22,
                    description="Non imponibile art. 123",
                    notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                    e_invoice=True,
                    ei_type="2",
                    ei_description="ei_description_example",
                    is_disabled=True,
                ),
                default_payment_terms=30,
                default_payment_terms_type=DefaultPaymentTermsType("standard"),
                default_payment_method=PaymentMethod(
                    id=1,
                    name="name_example",
                    type=PaymentMethodType("standard"),
                    is_default=True,
                    default_payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    details=[
                        PaymentMethodDetails(
                            title="title_example",
                            description="description_example",
                        ),
                    ],
                    bank_iban="bank_iban_example",
                    bank_name="bank_name_example",
                    bank_beneficiary="bank_beneficiary_example",
                    ei_payment_method="ei_payment_method_example",
                ),
                bank_name="bank_name_example",
                bank_iban="bank_iban_example",
                bank_swift_code="bank_swift_code_example",
                shipping_address="shipping_address_example",
                e_invoice=True,
                ei_code="ei_code_example",
                has_intent_declaration=True,
                intent_declaration_protocol_number=dateutil_parser('1970-01-01').date(),
                intent_declaration_protocol_date="intent_declaration_protocol_date_example",
                created_at="created_at_example",
                updated_at="updated_at_example",
            ),
            type=IssuedDocumentType("invoice"),
            number=1,
            numeration="/A",
            date=dateutil_parser('1970-01-01').date(),
            year=1,
            currency=Currency(
                id="EUR",
                symbol="€",
                exchange_rate="1",
                html_symbol="EUR",
            ),
            language=Language(
                code="code_example",
                name="name_example",
            ),
            subject="subject_example",
            visible_subject="visible_subject_example",
            rc_center="rc_center_example",
            notes="notes_example",
            rivalsa=3.14,
            cassa=3.14,
            cassa_taxable=3.14,
            amount_cassa_taxable=3.14,
            cassa2=3.14,
            cassa2_taxable=3.14,
            amount_cassa2_taxable=3.14,
            global_cassa_taxable=3.14,
            amount_global_cassa_taxable=3.14,
            withholding_tax=3.14,
            withholding_tax_taxable=3.14,
            other_withholding_tax=3.14,
            stamp_duty=3.14,
            payment_method=PaymentMethod(
                id=1,
                name="name_example",
                type=PaymentMethodType("standard"),
                is_default=True,
                default_payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                details=[
                    PaymentMethodDetails(
                        title="title_example",
                        description="description_example",
                    ),
                ],
                bank_iban="bank_iban_example",
                bank_name="bank_name_example",
                bank_beneficiary="bank_beneficiary_example",
                ei_payment_method="ei_payment_method_example",
            ),
            use_split_payment=True,
            use_gross_prices=True,
            e_invoice=True,
            ei_data=IssuedDocumentEiData(
                vat_kind=VatKind("vat_kind_example"),
                original_document_type=OriginalDocumentType("ordine"),
                od_number="od_number_example",
                od_date=dateutil_parser('1970-01-01').date(),
                cig="cig_example",
                cup="cup_example",
                payment_method="payment_method_example",
                bank_name="bank_name_example",
                bank_iban="bank_iban_example",
                bank_beneficiary="bank_beneficiary_example",
                invoice_number="invoice_number_example",
                invoice_date=dateutil_parser('1970-01-01').date(),
            ),
            ei_cassa_type="ei_cassa_type_example",
            ei_cassa2_type="ei_cassa2_type_example",
            ei_withholding_tax_causal="ei_withholding_tax_causal_example",
            ei_other_withholding_tax_type="ei_other_withholding_tax_type_example",
            ei_other_withholding_tax_causal="ei_other_withholding_tax_causal_example",
            items_list=[
                IssuedDocumentItemsListItem(
                    id=1,
                    product_id=1234,
                    code="239874892374982",
                    name="Water bottle",
                    category="category_example",
                    description="description_example",
                    qty=3.14,
                    measure="measure_example",
                    net_price=1.23,
                    gross_price=1.45,
                    vat=VatType(
                        id=1,
                        value=22,
                        description="Non imponibile art. 123",
                        notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                        e_invoice=True,
                        ei_type="2",
                        ei_description="ei_description_example",
                        is_disabled=True,
                    ),
                    not_taxable=True,
                    apply_withholding_taxes=True,
                    discount=3.14,
                    discount_highlight=True,
                    in_ddt=True,
                    stock=True,
                    ei_raw={},
                ),
            ],
            payments_list=[
                IssuedDocumentPaymentsListItem(
                    id=1,
                    due_date=dateutil_parser('Tue Apr 03 00:00:00 UTC 2018').date(),
                    amount=1.45,
                    status=IssuedDocumentStatus("not_paid"),
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    paid_date=dateutil_parser('Tue Apr 03 00:00:00 UTC 2018').date(),
                    ei_raw={},
                    payment_terms=IssuedDocumentPaymentsListItemPaymentTerms(
                        days=1,
                        type="standard",
                    ),
                ),
            ],
            template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            delivery_note_template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            acc_inv_template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            h_margins=1,
            v_margins=1,
            show_payments=True,
            show_payment_method=True,
            show_totals=ShowTotalsMode("all"),
            show_paypal_button=True,
            show_notification_button=True,
            show_tspay_button=True,
            delivery_note=True,
            accompanying_invoice=True,
            dn_number=1,
            dn_date=dateutil_parser('1970-01-01').date(),
            dn_ai_packages_number="dn_ai_packages_number_example",
            dn_ai_weight="dn_ai_weight_example",
            dn_ai_causal="dn_ai_causal_example",
            dn_ai_destination="dn_ai_destination_example",
            dn_ai_transporter="dn_ai_transporter_example",
            dn_ai_notes="dn_ai_notes_example",
            is_marked=True,
            amount_due_discount=3.14,
            amount_rivalsa_taxable=3.14,
            amount_withholding_tax_taxable=3.14,
            amount_other_withholding_tax_taxable=3.14,
            amount_enasarco_taxable=3.14,
            extra_data=IssuedDocumentExtraData(
                show_sofort_button=True,
                multifatture_sent=1,
                ts_communication=True,
                ts_flag_tipo_spesa=3.14,
                ts_pagamento_tracciato=True,
                ts_tipo_spesa="ts_tipo_spesa_example",
                ts_opposizione=True,
                ts_status=1,
                ts_file_id="ts_file_id_example",
                ts_sent_date=dateutil_parser('1970-01-01').date(),
                ts_full_amount=True,
                imported_by="imported_by_example",
                ts_single_sending=True,
            ),
            seen_date=dateutil_parser('1970-01-01').date(),
            next_due_date=dateutil_parser('1970-01-01').date(),
            url="url_example",
            attachment_token="attachment_token_example",
            ei_raw={},
            ei_status="attempt",
        ),
    ) # GetExistingIssuedDocumentTotalsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Existing Issued Document Totals
        api_response = api_instance.get_existing_issued_document_totals(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->get_existing_issued_document_totals: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Existing Issued Document Totals
        api_response = api_instance.get_existing_issued_document_totals(company_id, document_id, get_existing_issued_document_totals_request=get_existing_issued_document_totals_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->get_existing_issued_document_totals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **get_existing_issued_document_totals_request** | [**GetExistingIssuedDocumentTotalsRequest**](GetExistingIssuedDocumentTotalsRequest.md)|  | [optional]

### Return type

[**GetExistingIssuedDocumentTotalsResponse**](GetExistingIssuedDocumentTotalsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Totals. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issued_document**
> GetIssuedDocumentResponse get_issued_document(company_id, document_id)

Get Issued Document

Gets the specified document. 

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.get_issued_document_response import GetIssuedDocumentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Issued Document
        api_response = api_instance.get_issued_document(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->get_issued_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Issued Document
        api_response = api_instance.get_issued_document(company_id, document_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->get_issued_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]

### Return type

[**GetIssuedDocumentResponse**](GetIssuedDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document Details. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issued_document_pre_create_info**
> GetIssuedDocumentPreCreateInfoResponse get_issued_document_pre_create_info(company_id, type)

Get Issued Document Pre-create info

Retrieves the information useful while creating a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.get_issued_document_pre_create_info_response import GetIssuedDocumentPreCreateInfoResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = "invoice" # str | The type of the issued document.

    # example passing only required values which don't have defaults set
    try:
        # Get Issued Document Pre-create info
        api_response = api_instance.get_issued_document_pre_create_info(company_id, type)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->get_issued_document_pre_create_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **type** | **str**| The type of the issued document. |

### Return type

[**GetIssuedDocumentPreCreateInfoResponse**](GetIssuedDocumentPreCreateInfoResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pre-create info. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_issued_document_totals**
> GetNewIssuedDocumentTotalsResponse get_new_issued_document_totals(company_id)

Get New Issued Document Totals

Returns the totals for a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.get_new_issued_document_totals_response import GetNewIssuedDocumentTotalsResponse
from fattureincloud_python_sdk.model.get_new_issued_document_totals_request import GetNewIssuedDocumentTotalsRequest
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    get_new_issued_document_totals_request = GetNewIssuedDocumentTotalsRequest(
        data=IssuedDocument(
            id=1,
            entity=Entity(
                id=1,
                code="123",
                name="Rossi S.r.l.",
                type=EntityType("company"),
                first_name="first_name_example",
                last_name="last_name_example",
                contact_person="contact_person_example",
                vat_number="IT01234567890",
                tax_code="RSSMRA44A12E890Q",
                address_street="Via dei tigli, 12",
                address_postal_code="24010",
                address_city="Bergamo",
                address_province="BG",
                address_extra="address_extra_example",
                country="Italia",
                email="mario.rossi@example.it",
                certified_email="mario.rossi@pec.example.it",
                phone="phone_example",
                fax="fax_example",
                notes="notes_example",
                default_vat=VatType(
                    id=1,
                    value=22,
                    description="Non imponibile art. 123",
                    notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                    e_invoice=True,
                    ei_type="2",
                    ei_description="ei_description_example",
                    is_disabled=True,
                ),
                default_payment_terms=30,
                default_payment_terms_type=DefaultPaymentTermsType("standard"),
                default_payment_method=PaymentMethod(
                    id=1,
                    name="name_example",
                    type=PaymentMethodType("standard"),
                    is_default=True,
                    default_payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    details=[
                        PaymentMethodDetails(
                            title="title_example",
                            description="description_example",
                        ),
                    ],
                    bank_iban="bank_iban_example",
                    bank_name="bank_name_example",
                    bank_beneficiary="bank_beneficiary_example",
                    ei_payment_method="ei_payment_method_example",
                ),
                bank_name="bank_name_example",
                bank_iban="bank_iban_example",
                bank_swift_code="bank_swift_code_example",
                shipping_address="shipping_address_example",
                e_invoice=True,
                ei_code="ei_code_example",
                has_intent_declaration=True,
                intent_declaration_protocol_number=dateutil_parser('1970-01-01').date(),
                intent_declaration_protocol_date="intent_declaration_protocol_date_example",
                created_at="created_at_example",
                updated_at="updated_at_example",
            ),
            type=IssuedDocumentType("invoice"),
            number=1,
            numeration="/A",
            date=dateutil_parser('1970-01-01').date(),
            year=1,
            currency=Currency(
                id="EUR",
                symbol="€",
                exchange_rate="1",
                html_symbol="EUR",
            ),
            language=Language(
                code="code_example",
                name="name_example",
            ),
            subject="subject_example",
            visible_subject="visible_subject_example",
            rc_center="rc_center_example",
            notes="notes_example",
            rivalsa=3.14,
            cassa=3.14,
            cassa_taxable=3.14,
            amount_cassa_taxable=3.14,
            cassa2=3.14,
            cassa2_taxable=3.14,
            amount_cassa2_taxable=3.14,
            global_cassa_taxable=3.14,
            amount_global_cassa_taxable=3.14,
            withholding_tax=3.14,
            withholding_tax_taxable=3.14,
            other_withholding_tax=3.14,
            stamp_duty=3.14,
            payment_method=PaymentMethod(
                id=1,
                name="name_example",
                type=PaymentMethodType("standard"),
                is_default=True,
                default_payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                details=[
                    PaymentMethodDetails(
                        title="title_example",
                        description="description_example",
                    ),
                ],
                bank_iban="bank_iban_example",
                bank_name="bank_name_example",
                bank_beneficiary="bank_beneficiary_example",
                ei_payment_method="ei_payment_method_example",
            ),
            use_split_payment=True,
            use_gross_prices=True,
            e_invoice=True,
            ei_data=IssuedDocumentEiData(
                vat_kind=VatKind("vat_kind_example"),
                original_document_type=OriginalDocumentType("ordine"),
                od_number="od_number_example",
                od_date=dateutil_parser('1970-01-01').date(),
                cig="cig_example",
                cup="cup_example",
                payment_method="payment_method_example",
                bank_name="bank_name_example",
                bank_iban="bank_iban_example",
                bank_beneficiary="bank_beneficiary_example",
                invoice_number="invoice_number_example",
                invoice_date=dateutil_parser('1970-01-01').date(),
            ),
            ei_cassa_type="ei_cassa_type_example",
            ei_cassa2_type="ei_cassa2_type_example",
            ei_withholding_tax_causal="ei_withholding_tax_causal_example",
            ei_other_withholding_tax_type="ei_other_withholding_tax_type_example",
            ei_other_withholding_tax_causal="ei_other_withholding_tax_causal_example",
            items_list=[
                IssuedDocumentItemsListItem(
                    id=1,
                    product_id=1234,
                    code="239874892374982",
                    name="Water bottle",
                    category="category_example",
                    description="description_example",
                    qty=3.14,
                    measure="measure_example",
                    net_price=1.23,
                    gross_price=1.45,
                    vat=VatType(
                        id=1,
                        value=22,
                        description="Non imponibile art. 123",
                        notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                        e_invoice=True,
                        ei_type="2",
                        ei_description="ei_description_example",
                        is_disabled=True,
                    ),
                    not_taxable=True,
                    apply_withholding_taxes=True,
                    discount=3.14,
                    discount_highlight=True,
                    in_ddt=True,
                    stock=True,
                    ei_raw={},
                ),
            ],
            payments_list=[
                IssuedDocumentPaymentsListItem(
                    id=1,
                    due_date=dateutil_parser('Tue Apr 03 00:00:00 UTC 2018').date(),
                    amount=1.45,
                    status=IssuedDocumentStatus("not_paid"),
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    paid_date=dateutil_parser('Tue Apr 03 00:00:00 UTC 2018').date(),
                    ei_raw={},
                    payment_terms=IssuedDocumentPaymentsListItemPaymentTerms(
                        days=1,
                        type="standard",
                    ),
                ),
            ],
            template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            delivery_note_template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            acc_inv_template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            h_margins=1,
            v_margins=1,
            show_payments=True,
            show_payment_method=True,
            show_totals=ShowTotalsMode("all"),
            show_paypal_button=True,
            show_notification_button=True,
            show_tspay_button=True,
            delivery_note=True,
            accompanying_invoice=True,
            dn_number=1,
            dn_date=dateutil_parser('1970-01-01').date(),
            dn_ai_packages_number="dn_ai_packages_number_example",
            dn_ai_weight="dn_ai_weight_example",
            dn_ai_causal="dn_ai_causal_example",
            dn_ai_destination="dn_ai_destination_example",
            dn_ai_transporter="dn_ai_transporter_example",
            dn_ai_notes="dn_ai_notes_example",
            is_marked=True,
            amount_due_discount=3.14,
            amount_rivalsa_taxable=3.14,
            amount_withholding_tax_taxable=3.14,
            amount_other_withholding_tax_taxable=3.14,
            amount_enasarco_taxable=3.14,
            extra_data=IssuedDocumentExtraData(
                show_sofort_button=True,
                multifatture_sent=1,
                ts_communication=True,
                ts_flag_tipo_spesa=3.14,
                ts_pagamento_tracciato=True,
                ts_tipo_spesa="ts_tipo_spesa_example",
                ts_opposizione=True,
                ts_status=1,
                ts_file_id="ts_file_id_example",
                ts_sent_date=dateutil_parser('1970-01-01').date(),
                ts_full_amount=True,
                imported_by="imported_by_example",
                ts_single_sending=True,
            ),
            seen_date=dateutil_parser('1970-01-01').date(),
            next_due_date=dateutil_parser('1970-01-01').date(),
            url="url_example",
            attachment_token="attachment_token_example",
            ei_raw={},
            ei_status="attempt",
        ),
    ) # GetNewIssuedDocumentTotalsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get New Issued Document Totals
        api_response = api_instance.get_new_issued_document_totals(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->get_new_issued_document_totals: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get New Issued Document Totals
        api_response = api_instance.get_new_issued_document_totals(company_id, get_new_issued_document_totals_request=get_new_issued_document_totals_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->get_new_issued_document_totals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **get_new_issued_document_totals_request** | [**GetNewIssuedDocumentTotalsRequest**](GetNewIssuedDocumentTotalsRequest.md)|  | [optional]

### Return type

[**GetNewIssuedDocumentTotalsResponse**](GetNewIssuedDocumentTotalsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Totals. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_issued_documents**
> ListIssuedDocumentsResponse list_issued_documents(company_id, type)

List Issued Documents

Lists the issued documents.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.list_issued_documents_response import ListIssuedDocumentsResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = "invoice" # str | The type of the issued document.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)
    sort = "sort_example" # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) if omitted the server will use the default value of 1
    per_page = 5 # int | The size of the page. (optional) if omitted the server will use the default value of 5
    q = "q_example" # str | Query for filtering the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Issued Documents
        api_response = api_instance.list_issued_documents(company_id, type)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->list_issued_documents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Issued Documents
        api_response = api_instance.list_issued_documents(company_id, type, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->list_issued_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **type** | **str**| The type of the issued document. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]
 **sort** | **str**| List of comma-separated fields for result sorting (minus for desc sorting). | [optional]
 **page** | **int**| The page to retrieve. | [optional] if omitted the server will use the default value of 1
 **per_page** | **int**| The size of the page. | [optional] if omitted the server will use the default value of 5
 **q** | **str**| Query for filtering the results. | [optional]

### Return type

[**ListIssuedDocumentsResponse**](ListIssuedDocumentsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results list. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_issued_document**
> ModifyIssuedDocumentResponse modify_issued_document(company_id, document_id)

Modify Issued Document

Modifies the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.modify_issued_document_request import ModifyIssuedDocumentRequest
from fattureincloud_python_sdk.model.modify_issued_document_response import ModifyIssuedDocumentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    modify_issued_document_request = ModifyIssuedDocumentRequest(
        data=IssuedDocument(
            id=1,
            entity=Entity(
                id=1,
                code="123",
                name="Rossi S.r.l.",
                type=EntityType("company"),
                first_name="first_name_example",
                last_name="last_name_example",
                contact_person="contact_person_example",
                vat_number="IT01234567890",
                tax_code="RSSMRA44A12E890Q",
                address_street="Via dei tigli, 12",
                address_postal_code="24010",
                address_city="Bergamo",
                address_province="BG",
                address_extra="address_extra_example",
                country="Italia",
                email="mario.rossi@example.it",
                certified_email="mario.rossi@pec.example.it",
                phone="phone_example",
                fax="fax_example",
                notes="notes_example",
                default_vat=VatType(
                    id=1,
                    value=22,
                    description="Non imponibile art. 123",
                    notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                    e_invoice=True,
                    ei_type="2",
                    ei_description="ei_description_example",
                    is_disabled=True,
                ),
                default_payment_terms=30,
                default_payment_terms_type=DefaultPaymentTermsType("standard"),
                default_payment_method=PaymentMethod(
                    id=1,
                    name="name_example",
                    type=PaymentMethodType("standard"),
                    is_default=True,
                    default_payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    details=[
                        PaymentMethodDetails(
                            title="title_example",
                            description="description_example",
                        ),
                    ],
                    bank_iban="bank_iban_example",
                    bank_name="bank_name_example",
                    bank_beneficiary="bank_beneficiary_example",
                    ei_payment_method="ei_payment_method_example",
                ),
                bank_name="bank_name_example",
                bank_iban="bank_iban_example",
                bank_swift_code="bank_swift_code_example",
                shipping_address="shipping_address_example",
                e_invoice=True,
                ei_code="ei_code_example",
                has_intent_declaration=True,
                intent_declaration_protocol_number=dateutil_parser('1970-01-01').date(),
                intent_declaration_protocol_date="intent_declaration_protocol_date_example",
                created_at="created_at_example",
                updated_at="updated_at_example",
            ),
            type=IssuedDocumentType("invoice"),
            number=1,
            numeration="/A",
            date=dateutil_parser('1970-01-01').date(),
            year=1,
            currency=Currency(
                id="EUR",
                symbol="€",
                exchange_rate="1",
                html_symbol="EUR",
            ),
            language=Language(
                code="code_example",
                name="name_example",
            ),
            subject="subject_example",
            visible_subject="visible_subject_example",
            rc_center="rc_center_example",
            notes="notes_example",
            rivalsa=3.14,
            cassa=3.14,
            cassa_taxable=3.14,
            amount_cassa_taxable=3.14,
            cassa2=3.14,
            cassa2_taxable=3.14,
            amount_cassa2_taxable=3.14,
            global_cassa_taxable=3.14,
            amount_global_cassa_taxable=3.14,
            withholding_tax=3.14,
            withholding_tax_taxable=3.14,
            other_withholding_tax=3.14,
            stamp_duty=3.14,
            payment_method=PaymentMethod(
                id=1,
                name="name_example",
                type=PaymentMethodType("standard"),
                is_default=True,
                default_payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                details=[
                    PaymentMethodDetails(
                        title="title_example",
                        description="description_example",
                    ),
                ],
                bank_iban="bank_iban_example",
                bank_name="bank_name_example",
                bank_beneficiary="bank_beneficiary_example",
                ei_payment_method="ei_payment_method_example",
            ),
            use_split_payment=True,
            use_gross_prices=True,
            e_invoice=True,
            ei_data=IssuedDocumentEiData(
                vat_kind=VatKind("vat_kind_example"),
                original_document_type=OriginalDocumentType("ordine"),
                od_number="od_number_example",
                od_date=dateutil_parser('1970-01-01').date(),
                cig="cig_example",
                cup="cup_example",
                payment_method="payment_method_example",
                bank_name="bank_name_example",
                bank_iban="bank_iban_example",
                bank_beneficiary="bank_beneficiary_example",
                invoice_number="invoice_number_example",
                invoice_date=dateutil_parser('1970-01-01').date(),
            ),
            ei_cassa_type="ei_cassa_type_example",
            ei_cassa2_type="ei_cassa2_type_example",
            ei_withholding_tax_causal="ei_withholding_tax_causal_example",
            ei_other_withholding_tax_type="ei_other_withholding_tax_type_example",
            ei_other_withholding_tax_causal="ei_other_withholding_tax_causal_example",
            items_list=[
                IssuedDocumentItemsListItem(
                    id=1,
                    product_id=1234,
                    code="239874892374982",
                    name="Water bottle",
                    category="category_example",
                    description="description_example",
                    qty=3.14,
                    measure="measure_example",
                    net_price=1.23,
                    gross_price=1.45,
                    vat=VatType(
                        id=1,
                        value=22,
                        description="Non imponibile art. 123",
                        notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                        e_invoice=True,
                        ei_type="2",
                        ei_description="ei_description_example",
                        is_disabled=True,
                    ),
                    not_taxable=True,
                    apply_withholding_taxes=True,
                    discount=3.14,
                    discount_highlight=True,
                    in_ddt=True,
                    stock=True,
                    ei_raw={},
                ),
            ],
            payments_list=[
                IssuedDocumentPaymentsListItem(
                    id=1,
                    due_date=dateutil_parser('Tue Apr 03 00:00:00 UTC 2018').date(),
                    amount=1.45,
                    status=IssuedDocumentStatus("not_paid"),
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    paid_date=dateutil_parser('Tue Apr 03 00:00:00 UTC 2018').date(),
                    ei_raw={},
                    payment_terms=IssuedDocumentPaymentsListItemPaymentTerms(
                        days=1,
                        type="standard",
                    ),
                ),
            ],
            template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            delivery_note_template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            acc_inv_template=DocumentTemplate(
                id=123,
                name="Light Smoke",
                type="type_example",
            ),
            h_margins=1,
            v_margins=1,
            show_payments=True,
            show_payment_method=True,
            show_totals=ShowTotalsMode("all"),
            show_paypal_button=True,
            show_notification_button=True,
            show_tspay_button=True,
            delivery_note=True,
            accompanying_invoice=True,
            dn_number=1,
            dn_date=dateutil_parser('1970-01-01').date(),
            dn_ai_packages_number="dn_ai_packages_number_example",
            dn_ai_weight="dn_ai_weight_example",
            dn_ai_causal="dn_ai_causal_example",
            dn_ai_destination="dn_ai_destination_example",
            dn_ai_transporter="dn_ai_transporter_example",
            dn_ai_notes="dn_ai_notes_example",
            is_marked=True,
            amount_due_discount=3.14,
            amount_rivalsa_taxable=3.14,
            amount_withholding_tax_taxable=3.14,
            amount_other_withholding_tax_taxable=3.14,
            amount_enasarco_taxable=3.14,
            extra_data=IssuedDocumentExtraData(
                show_sofort_button=True,
                multifatture_sent=1,
                ts_communication=True,
                ts_flag_tipo_spesa=3.14,
                ts_pagamento_tracciato=True,
                ts_tipo_spesa="ts_tipo_spesa_example",
                ts_opposizione=True,
                ts_status=1,
                ts_file_id="ts_file_id_example",
                ts_sent_date=dateutil_parser('1970-01-01').date(),
                ts_full_amount=True,
                imported_by="imported_by_example",
                ts_single_sending=True,
            ),
            seen_date=dateutil_parser('1970-01-01').date(),
            next_due_date=dateutil_parser('1970-01-01').date(),
            url="url_example",
            attachment_token="attachment_token_example",
            ei_raw={},
            ei_status="attempt",
        ),
        options=IssuedDocumentOptions(
            fix_payments=True,
        ),
    ) # ModifyIssuedDocumentRequest | The modified document (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Issued Document
        api_response = api_instance.modify_issued_document(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->modify_issued_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Issued Document
        api_response = api_instance.modify_issued_document(company_id, document_id, modify_issued_document_request=modify_issued_document_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->modify_issued_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **modify_issued_document_request** | [**ModifyIssuedDocumentRequest**](ModifyIssuedDocumentRequest.md)| The modified document | [optional]

### Return type

[**ModifyIssuedDocumentResponse**](ModifyIssuedDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document edited |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_email**
> schedule_email(company_id, document_id)

Schedule Email

Schedules the sending of a document by email.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.schedule_email_request import ScheduleEmailRequest
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    schedule_email_request = ScheduleEmailRequest(
        data=EmailSchedule(
            sender_id=1,
            sender_email="sender_email_example",
            recipient_email="recipient_email_example",
            subject="subject_example",
            body="body_example",
            include=EmailScheduleInclude(
                document=True,
                delivery_note=True,
                attachment=True,
                accompanying_invoice=True,
            ),
            attach_pdf=True,
            send_copy=True,
        ),
    ) # ScheduleEmailRequest | Email Schedule (optional)

    # example passing only required values which don't have defaults set
    try:
        # Schedule Email
        api_instance.schedule_email(company_id, document_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->schedule_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedule Email
        api_instance.schedule_email(company_id, document_id, schedule_email_request=schedule_email_request)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->schedule_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **schedule_email_request** | [**ScheduleEmailRequest**](ScheduleEmailRequest.md)| Email Schedule | [optional]

### Return type

void (empty response body)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_issued_document_attachment**
> UploadIssuedDocumentAttachmentResponse upload_issued_document_attachment(company_id)

Upload Issued Document Attachment

Uploads an attachment destined to an issued document. The actual association between the document and the attachment must be implemented separately, using the returned token.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_documents_api
from fattureincloud_python_sdk.model.upload_issued_document_attachment_response import UploadIssuedDocumentAttachmentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_documents_api.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    filename = "attachment.pdf" # str, none_type | Name of the file. (optional)
    attachment = open('/path/to/file', 'rb') # file_type, none_type | Valid format: .png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload Issued Document Attachment
        api_response = api_instance.upload_issued_document_attachment(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->upload_issued_document_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload Issued Document Attachment
        api_response = api_instance.upload_issued_document_attachment(company_id, filename=filename, attachment=attachment)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedDocumentsApi->upload_issued_document_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **filename** | **str, none_type**| Name of the file. | [optional]
 **attachment** | **file_type, none_type**| Valid format: .png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx | [optional]

### Return type

[**UploadIssuedDocumentAttachmentResponse**](UploadIssuedDocumentAttachmentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment Token. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

