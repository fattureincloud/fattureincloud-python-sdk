# fattureincloud_python_sdk.ReceivedDocumentsApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_received_document**](ReceivedDocumentsApi.md#create_received_document) | **POST** /c/{company_id}/received_documents | Create Received Document
[**delete_received_document**](ReceivedDocumentsApi.md#delete_received_document) | **DELETE** /c/{company_id}/received_documents/{document_id} | Delete Received Document
[**delete_received_document_attachment**](ReceivedDocumentsApi.md#delete_received_document_attachment) | **DELETE** /c/{company_id}/received_documents/{document_id}/attachment | Delete Received Document Attachment
[**get_existing_received_document_totals**](ReceivedDocumentsApi.md#get_existing_received_document_totals) | **POST** /c/{company_id}/received_documents/{document_id}/totals | Get Existing Received Document Totals
[**get_new_received_document_totals**](ReceivedDocumentsApi.md#get_new_received_document_totals) | **POST** /c/{company_id}/received_documents/totals | Get New Received Document Totals
[**get_received_document**](ReceivedDocumentsApi.md#get_received_document) | **GET** /c/{company_id}/received_documents/{document_id} | Get Received Document
[**get_received_document_pre_create_info**](ReceivedDocumentsApi.md#get_received_document_pre_create_info) | **GET** /c/{company_id}/received_documents/info | Get Received Document Pre-Create Info
[**list_received_documents**](ReceivedDocumentsApi.md#list_received_documents) | **GET** /c/{company_id}/received_documents | List Received Documents
[**modify_received_document**](ReceivedDocumentsApi.md#modify_received_document) | **PUT** /c/{company_id}/received_documents/{document_id} | Modify Received Document
[**upload_received_document_attachment**](ReceivedDocumentsApi.md#upload_received_document_attachment) | **POST** /c/{company_id}/received_documents/attachment | Upload Received Document Attachment


# **create_received_document**
> CreateReceivedDocumentResponse create_received_document(company_id)

Create Received Document

Creates a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from fattureincloud_python_sdk.model.create_received_document_request import CreateReceivedDocumentRequest
from fattureincloud_python_sdk.model.create_received_document_response import CreateReceivedDocumentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_received_document_request = CreateReceivedDocumentRequest(
        pending_id=1,
        data=ReceivedDocument(
            id=1,
            type=ReceivedDocumentType("expense"),
            entity=ReceivedDocumentEntity(
                id=1,
                name="name_example",
            ),
            date=dateutil_parser('1970-01-01').date(),
            category="category_example",
            description="description_example",
            amount_net=3.14,
            amount_vat=3.14,
            amount_withholding_tax=3.14,
            amount_other_withholding_tax=3.14,
            amortization=3.14,
            rc_center="rc_center_example",
            invoice_number="invoice_number_example",
            is_marked=True,
            is_detailed=True,
            e_invoice=True,
            currency=Currency(
                id="EUR",
                symbol="€",
                exchange_rate="1",
                html_symbol="EUR",
            ),
            tax_deductibility=3.14,
            vat_deductibility=3.14,
            items_list=[
                ReceivedDocumentItemsListItem(
                    id=1,
                    product_id=1,
                    code="code_example",
                    name="name_example",
                    measure="measure_example",
                    net_price=3.14,
                    category="category_example",
                    qty=3.14,
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
                    stock=3.14,
                ),
            ],
            payments_list=[
                ReceivedDocumentPaymentsListItem(
                    id=1,
                    amount=3.14,
                    due_date=dateutil_parser('1970-01-01').date(),
                    paid_date=dateutil_parser('1970-01-01').date(),
                    payment_terms=ReceivedDocumentPaymentsListItemPaymentTerms(
                        days=1,
                        type="type_example",
                    ),
                    status="status_example",
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                ),
            ],
            attachment_token="attachment_token_example",
        ),
    ) # CreateReceivedDocumentRequest | Document to create (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Received Document
        api_response = api_instance.create_received_document(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->create_received_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Received Document
        api_response = api_instance.create_received_document(company_id, create_received_document_request=create_received_document_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->create_received_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **create_received_document_request** | [**CreateReceivedDocumentRequest**](CreateReceivedDocumentRequest.md)| Document to create | [optional]

### Return type

[**CreateReceivedDocumentResponse**](CreateReceivedDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_received_document**
> delete_received_document(company_id, document_id)

Delete Received Document

Deletes the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Delete Received Document
        api_instance.delete_received_document(company_id, document_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->delete_received_document: %s\n" % e)
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
**200** | Document removed. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_received_document_attachment**
> delete_received_document_attachment(company_id, document_id)

Delete Received Document Attachment

Removes the attachment of the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Delete Received Document Attachment
        api_instance.delete_received_document_attachment(company_id, document_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->delete_received_document_attachment: %s\n" % e)
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
**200** | File removed |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_existing_received_document_totals**
> GetExistingReceivedDocumentTotalsResponse get_existing_received_document_totals(company_id, document_id)

Get Existing Received Document Totals

Returns the totals for the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from fattureincloud_python_sdk.model.get_existing_received_document_totals_request import GetExistingReceivedDocumentTotalsRequest
from fattureincloud_python_sdk.model.get_existing_received_document_totals_response import GetExistingReceivedDocumentTotalsResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    get_existing_received_document_totals_request = GetExistingReceivedDocumentTotalsRequest(
        data=ReceivedDocument(
            id=1,
            type=ReceivedDocumentType("expense"),
            entity=ReceivedDocumentEntity(
                id=1,
                name="name_example",
            ),
            date=dateutil_parser('1970-01-01').date(),
            category="category_example",
            description="description_example",
            amount_net=3.14,
            amount_vat=3.14,
            amount_withholding_tax=3.14,
            amount_other_withholding_tax=3.14,
            amortization=3.14,
            rc_center="rc_center_example",
            invoice_number="invoice_number_example",
            is_marked=True,
            is_detailed=True,
            e_invoice=True,
            currency=Currency(
                id="EUR",
                symbol="€",
                exchange_rate="1",
                html_symbol="EUR",
            ),
            tax_deductibility=3.14,
            vat_deductibility=3.14,
            items_list=[
                ReceivedDocumentItemsListItem(
                    id=1,
                    product_id=1,
                    code="code_example",
                    name="name_example",
                    measure="measure_example",
                    net_price=3.14,
                    category="category_example",
                    qty=3.14,
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
                    stock=3.14,
                ),
            ],
            payments_list=[
                ReceivedDocumentPaymentsListItem(
                    id=1,
                    amount=3.14,
                    due_date=dateutil_parser('1970-01-01').date(),
                    paid_date=dateutil_parser('1970-01-01').date(),
                    payment_terms=ReceivedDocumentPaymentsListItemPaymentTerms(
                        days=1,
                        type="type_example",
                    ),
                    status="status_example",
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                ),
            ],
            attachment_token="attachment_token_example",
        ),
    ) # GetExistingReceivedDocumentTotalsRequest | Received document. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Existing Received Document Totals
        api_response = api_instance.get_existing_received_document_totals(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->get_existing_received_document_totals: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Existing Received Document Totals
        api_response = api_instance.get_existing_received_document_totals(company_id, document_id, get_existing_received_document_totals_request=get_existing_received_document_totals_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->get_existing_received_document_totals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **get_existing_received_document_totals_request** | [**GetExistingReceivedDocumentTotalsRequest**](GetExistingReceivedDocumentTotalsRequest.md)| Received document. | [optional]

### Return type

[**GetExistingReceivedDocumentTotalsResponse**](GetExistingReceivedDocumentTotalsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document Totals. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_received_document_totals**
> GetNewReceivedDocumentTotalsResponse get_new_received_document_totals(company_id)

Get New Received Document Totals

Returns the totals for a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from fattureincloud_python_sdk.model.get_new_received_document_totals_request import GetNewReceivedDocumentTotalsRequest
from fattureincloud_python_sdk.model.get_new_received_document_totals_response import GetNewReceivedDocumentTotalsResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    get_new_received_document_totals_request = GetNewReceivedDocumentTotalsRequest(
        data=ReceivedDocument(
            id=1,
            type=ReceivedDocumentType("expense"),
            entity=ReceivedDocumentEntity(
                id=1,
                name="name_example",
            ),
            date=dateutil_parser('1970-01-01').date(),
            category="category_example",
            description="description_example",
            amount_net=3.14,
            amount_vat=3.14,
            amount_withholding_tax=3.14,
            amount_other_withholding_tax=3.14,
            amortization=3.14,
            rc_center="rc_center_example",
            invoice_number="invoice_number_example",
            is_marked=True,
            is_detailed=True,
            e_invoice=True,
            currency=Currency(
                id="EUR",
                symbol="€",
                exchange_rate="1",
                html_symbol="EUR",
            ),
            tax_deductibility=3.14,
            vat_deductibility=3.14,
            items_list=[
                ReceivedDocumentItemsListItem(
                    id=1,
                    product_id=1,
                    code="code_example",
                    name="name_example",
                    measure="measure_example",
                    net_price=3.14,
                    category="category_example",
                    qty=3.14,
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
                    stock=3.14,
                ),
            ],
            payments_list=[
                ReceivedDocumentPaymentsListItem(
                    id=1,
                    amount=3.14,
                    due_date=dateutil_parser('1970-01-01').date(),
                    paid_date=dateutil_parser('1970-01-01').date(),
                    payment_terms=ReceivedDocumentPaymentsListItemPaymentTerms(
                        days=1,
                        type="type_example",
                    ),
                    status="status_example",
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                ),
            ],
            attachment_token="attachment_token_example",
        ),
    ) # GetNewReceivedDocumentTotalsRequest | Received document. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get New Received Document Totals
        api_response = api_instance.get_new_received_document_totals(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->get_new_received_document_totals: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get New Received Document Totals
        api_response = api_instance.get_new_received_document_totals(company_id, get_new_received_document_totals_request=get_new_received_document_totals_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->get_new_received_document_totals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **get_new_received_document_totals_request** | [**GetNewReceivedDocumentTotalsRequest**](GetNewReceivedDocumentTotalsRequest.md)| Received document. | [optional]

### Return type

[**GetNewReceivedDocumentTotalsResponse**](GetNewReceivedDocumentTotalsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document Totals. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_received_document**
> GetReceivedDocumentResponse get_received_document(company_id, document_id)

Get Received Document

Gets the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from fattureincloud_python_sdk.model.get_received_document_response import GetReceivedDocumentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Received Document
        api_response = api_instance.get_received_document(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->get_received_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Received Document
        api_response = api_instance.get_received_document(company_id, document_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->get_received_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]

### Return type

[**GetReceivedDocumentResponse**](GetReceivedDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document details. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_received_document_pre_create_info**
> GetReceivedDocumentPreCreateInfoResponse get_received_document_pre_create_info(company_id, type)

Get Received Document Pre-Create Info

Retrieves the information useful while creating a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from fattureincloud_python_sdk.model.get_received_document_pre_create_info_response import GetReceivedDocumentPreCreateInfoResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = "expense" # str | The type of the received document.

    # example passing only required values which don't have defaults set
    try:
        # Get Received Document Pre-Create Info
        api_response = api_instance.get_received_document_pre_create_info(company_id, type)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->get_received_document_pre_create_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **type** | **str**| The type of the received document. |

### Return type

[**GetReceivedDocumentPreCreateInfoResponse**](GetReceivedDocumentPreCreateInfoResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pre-create info |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_received_documents**
> ListReceivedDocumentsResponse list_received_documents(company_id, type)

List Received Documents

Lists the received documents.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from fattureincloud_python_sdk.model.list_received_documents_response import ListReceivedDocumentsResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = "expense" # str | The type of the received document.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)
    sort = "sort_example" # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) if omitted the server will use the default value of 1
    per_page = 5 # int | The size of the page. (optional) if omitted the server will use the default value of 5
    q = "q_example" # str | Query for filtering the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Received Documents
        api_response = api_instance.list_received_documents(company_id, type)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->list_received_documents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Received Documents
        api_response = api_instance.list_received_documents(company_id, type, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->list_received_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **type** | **str**| The type of the received document. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]
 **sort** | **str**| List of comma-separated fields for result sorting (minus for desc sorting). | [optional]
 **page** | **int**| The page to retrieve. | [optional] if omitted the server will use the default value of 1
 **per_page** | **int**| The size of the page. | [optional] if omitted the server will use the default value of 5
 **q** | **str**| Query for filtering the results. | [optional]

### Return type

[**ListReceivedDocumentsResponse**](ListReceivedDocumentsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_received_document**
> ModifyReceivedDocumentResponse modify_received_document(company_id, document_id)

Modify Received Document

Modifies the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from fattureincloud_python_sdk.model.modify_received_document_request import ModifyReceivedDocumentRequest
from fattureincloud_python_sdk.model.modify_received_document_response import ModifyReceivedDocumentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    modify_received_document_request = ModifyReceivedDocumentRequest(
        data=ReceivedDocument(
            id=1,
            type=ReceivedDocumentType("expense"),
            entity=ReceivedDocumentEntity(
                id=1,
                name="name_example",
            ),
            date=dateutil_parser('1970-01-01').date(),
            category="category_example",
            description="description_example",
            amount_net=3.14,
            amount_vat=3.14,
            amount_withholding_tax=3.14,
            amount_other_withholding_tax=3.14,
            amortization=3.14,
            rc_center="rc_center_example",
            invoice_number="invoice_number_example",
            is_marked=True,
            is_detailed=True,
            e_invoice=True,
            currency=Currency(
                id="EUR",
                symbol="€",
                exchange_rate="1",
                html_symbol="EUR",
            ),
            tax_deductibility=3.14,
            vat_deductibility=3.14,
            items_list=[
                ReceivedDocumentItemsListItem(
                    id=1,
                    product_id=1,
                    code="code_example",
                    name="name_example",
                    measure="measure_example",
                    net_price=3.14,
                    category="category_example",
                    qty=3.14,
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
                    stock=3.14,
                ),
            ],
            payments_list=[
                ReceivedDocumentPaymentsListItem(
                    id=1,
                    amount=3.14,
                    due_date=dateutil_parser('1970-01-01').date(),
                    paid_date=dateutil_parser('1970-01-01').date(),
                    payment_terms=ReceivedDocumentPaymentsListItemPaymentTerms(
                        days=1,
                        type="type_example",
                    ),
                    status="status_example",
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                ),
            ],
            attachment_token="attachment_token_example",
        ),
    ) # ModifyReceivedDocumentRequest | Modified document. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Received Document
        api_response = api_instance.modify_received_document(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->modify_received_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Received Document
        api_response = api_instance.modify_received_document(company_id, document_id, modify_received_document_request=modify_received_document_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->modify_received_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **modify_received_document_request** | [**ModifyReceivedDocumentRequest**](ModifyReceivedDocumentRequest.md)| Modified document. | [optional]

### Return type

[**ModifyReceivedDocumentResponse**](ModifyReceivedDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modified document. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_received_document_attachment**
> UploadReceivedDocumentAttachmentResponse upload_received_document_attachment(company_id)

Upload Received Document Attachment

Uploads an attachment destined to a received document. The actual association between the document and the attachment must be implemented separately, using the returned token.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import received_documents_api
from fattureincloud_python_sdk.model.upload_received_document_attachment_response import UploadReceivedDocumentAttachmentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = received_documents_api.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    filename = "attachment.pdf" # str, none_type | Name of the file. (optional)
    attachment = open('/path/to/file', 'rb') # file_type, none_type | Valid format: .png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload Received Document Attachment
        api_response = api_instance.upload_received_document_attachment(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->upload_received_document_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload Received Document Attachment
        api_response = api_instance.upload_received_document_attachment(company_id, filename=filename, attachment=attachment)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceivedDocumentsApi->upload_received_document_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **filename** | **str, none_type**| Name of the file. | [optional]
 **attachment** | **file_type, none_type**| Valid format: .png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx | [optional]

### Return type

[**UploadReceivedDocumentAttachmentResponse**](UploadReceivedDocumentAttachmentResponse.md)

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

