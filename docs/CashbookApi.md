# fattureincloud_python_sdk.CashbookApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cashbook_entry**](CashbookApi.md#create_cashbook_entry) | **POST** /c/{company_id}/cashbook | Create Cashbook Entry
[**delete_cashbook_entry**](CashbookApi.md#delete_cashbook_entry) | **DELETE** /c/{company_id}/cashbook/{document_id} | Delete Cashbook Entry
[**get_cashbook_entry**](CashbookApi.md#get_cashbook_entry) | **GET** /c/{company_id}/cashbook/{document_id} | Get Cashbook Entry
[**list_cashbook_entries**](CashbookApi.md#list_cashbook_entries) | **GET** /c/{company_id}/cashbook | List Cashbook Entries
[**modify_cashbook_entry**](CashbookApi.md#modify_cashbook_entry) | **PUT** /c/{company_id}/cashbook/{document_id} | Modify Cashbook Entry


# **create_cashbook_entry**
> CreateCashbookEntryResponse create_cashbook_entry(company_id)

Create Cashbook Entry

Creates a new cashbook entry.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import cashbook_api
from fattureincloud_python_sdk.model.create_cashbook_entry_response import CreateCashbookEntryResponse
from fattureincloud_python_sdk.model.create_cashbook_entry_request import CreateCashbookEntryRequest
from pprint import pprint
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
    api_instance = cashbook_api.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_cashbook_entry_request = CreateCashbookEntryRequest(
        data=CashbookEntry(
            id="id_example",
            date=dateutil_parser('1970-01-01').date(),
            description="description_example",
            kind=CashbookEntryKind("cashbook"),
            type=CashbookEntryType("in"),
            entity_name="entity_name_example",
            document=CashbookEntryDocument(
                id=1,
                type="type_example",
                path="path_example",
            ),
            amount_in=3.14,
            payment_account_in=PaymentAccount(
                id=1,
                name="Conto Banca Intesa",
                type=PaymentAccountType("standard"),
                iban="iban_example",
                sia="sia_example",
                cuc="cuc_example",
                virtual=True,
            ),
            amount_out=3.14,
            payment_account_out=PaymentAccount(
                id=1,
                name="Conto Banca Intesa",
                type=PaymentAccountType("standard"),
                iban="iban_example",
                sia="sia_example",
                cuc="cuc_example",
                virtual=True,
            ),
        ),
    ) # CreateCashbookEntryRequest | Cashbook entry.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Cashbook Entry
        api_response = api_instance.create_cashbook_entry(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling CashbookApi->create_cashbook_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Cashbook Entry
        api_response = api_instance.create_cashbook_entry(company_id, create_cashbook_entry_request=create_cashbook_entry_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling CashbookApi->create_cashbook_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **create_cashbook_entry_request** | [**CreateCashbookEntryRequest**](CreateCashbookEntryRequest.md)| Cashbook entry.  | [optional]

### Return type

[**CreateCashbookEntryResponse**](CreateCashbookEntryResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created Cashbook Entry. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cashbook_entry**
> delete_cashbook_entry(company_id, document_id)

Delete Cashbook Entry

Deletes the specified cashbook entry.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import cashbook_api
from pprint import pprint
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
    api_instance = cashbook_api.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Delete Cashbook Entry
        api_instance.delete_cashbook_entry(company_id, document_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling CashbookApi->delete_cashbook_entry: %s\n" % e)
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

# **get_cashbook_entry**
> GetCashbookEntryResponse get_cashbook_entry(company_id, document_id)

Get Cashbook Entry

Gets the specified cashbook entry.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import cashbook_api
from fattureincloud_python_sdk.model.get_cashbook_entry_response import GetCashbookEntryResponse
from pprint import pprint
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
    api_instance = cashbook_api.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Cashbook Entry
        api_response = api_instance.get_cashbook_entry(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling CashbookApi->get_cashbook_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Cashbook Entry
        api_response = api_instance.get_cashbook_entry(company_id, document_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling CashbookApi->get_cashbook_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]

### Return type

[**GetCashbookEntryResponse**](GetCashbookEntryResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cashbook Entry. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cashbook_entries**
> ListCashbookEntriesResponse list_cashbook_entries(company_id, date_from, date_to)

List Cashbook Entries

Lists the cashbook entries.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import cashbook_api
from fattureincloud_python_sdk.model.list_cashbook_entries_response import ListCashbookEntriesResponse
from pprint import pprint
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
    api_instance = cashbook_api.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    date_from = "date_from_example" # str | Start date.
    date_to = "date_to_example" # str | End date.
    year = 1 # int | Filter cashbook by year. (optional)
    type = "all" # str | Filter cashbook by type. (optional)
    payment_account_id = 1 # int | Filter by payment account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Cashbook Entries
        api_response = api_instance.list_cashbook_entries(company_id, date_from, date_to)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling CashbookApi->list_cashbook_entries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Cashbook Entries
        api_response = api_instance.list_cashbook_entries(company_id, date_from, date_to, year=year, type=type, payment_account_id=payment_account_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling CashbookApi->list_cashbook_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **date_from** | **str**| Start date. |
 **date_to** | **str**| End date. |
 **year** | **int**| Filter cashbook by year. | [optional]
 **type** | **str**| Filter cashbook by type. | [optional]
 **payment_account_id** | **int**| Filter by payment account. | [optional]

### Return type

[**ListCashbookEntriesResponse**](ListCashbookEntriesResponse.md)

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

# **modify_cashbook_entry**
> ModifyCashbookEntryResponse modify_cashbook_entry(company_id, document_id)

Modify Cashbook Entry

Modifies the specified cashbook entry.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import cashbook_api
from fattureincloud_python_sdk.model.modify_cashbook_entry_response import ModifyCashbookEntryResponse
from fattureincloud_python_sdk.model.modify_cashbook_entry_request import ModifyCashbookEntryRequest
from pprint import pprint
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
    api_instance = cashbook_api.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    modify_cashbook_entry_request = ModifyCashbookEntryRequest(
        data=CashbookEntry(
            id="id_example",
            date=dateutil_parser('1970-01-01').date(),
            description="description_example",
            kind=CashbookEntryKind("cashbook"),
            type=CashbookEntryType("in"),
            entity_name="entity_name_example",
            document=CashbookEntryDocument(
                id=1,
                type="type_example",
                path="path_example",
            ),
            amount_in=3.14,
            payment_account_in=PaymentAccount(
                id=1,
                name="Conto Banca Intesa",
                type=PaymentAccountType("standard"),
                iban="iban_example",
                sia="sia_example",
                cuc="cuc_example",
                virtual=True,
            ),
            amount_out=3.14,
            payment_account_out=PaymentAccount(
                id=1,
                name="Conto Banca Intesa",
                type=PaymentAccountType("standard"),
                iban="iban_example",
                sia="sia_example",
                cuc="cuc_example",
                virtual=True,
            ),
        ),
    ) # ModifyCashbookEntryRequest | Cashbook Entry (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Cashbook Entry
        api_response = api_instance.modify_cashbook_entry(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling CashbookApi->modify_cashbook_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Cashbook Entry
        api_response = api_instance.modify_cashbook_entry(company_id, document_id, modify_cashbook_entry_request=modify_cashbook_entry_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling CashbookApi->modify_cashbook_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **modify_cashbook_entry_request** | [**ModifyCashbookEntryRequest**](ModifyCashbookEntryRequest.md)| Cashbook Entry | [optional]

### Return type

[**ModifyCashbookEntryResponse**](ModifyCashbookEntryResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The modified Cashbook Entry |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

