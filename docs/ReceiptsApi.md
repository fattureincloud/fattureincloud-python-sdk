# fattureincloud_python_sdk.ReceiptsApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_receipt**](ReceiptsApi.md#create_receipt) | **POST** /c/{company_id}/receipts | Create Receipt
[**delete_receipt**](ReceiptsApi.md#delete_receipt) | **DELETE** /c/{company_id}/receipts/{document_id} | Delete Receipt
[**get_receipt**](ReceiptsApi.md#get_receipt) | **GET** /c/{company_id}/receipts/{document_id} | Get Receipt
[**get_receipt_pre_create_info**](ReceiptsApi.md#get_receipt_pre_create_info) | **GET** /c/{company_id}/receipts/info | Get Receipt Pre-Create Info
[**get_receipts_monthly_totals**](ReceiptsApi.md#get_receipts_monthly_totals) | **GET** /c/{company_id}/receipts/monthly_totals | Get Receipts Monthly Totals
[**list_receipts**](ReceiptsApi.md#list_receipts) | **GET** /c/{company_id}/receipts | List Receipts
[**modify_receipt**](ReceiptsApi.md#modify_receipt) | **PUT** /c/{company_id}/receipts/{document_id} | Modify Receipt


# **create_receipt**
> CreateReceiptResponse create_receipt(company_id)

Create Receipt

Creates a new receipt.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import receipts_api
from fattureincloud_python_sdk.model.create_receipt_request import CreateReceiptRequest
from fattureincloud_python_sdk.model.create_receipt_response import CreateReceiptResponse
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
    api_instance = receipts_api.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_receipt_request = CreateReceiptRequest(
        data=Receipt(
            id=1,
            date=dateutil_parser('1970-01-01').date(),
            number=3.14,
            numeration="numeration_example",
            amount_net=3.14,
            amount_vat=3.14,
            amount_gross=3.14,
            use_gross_prices=False,
            type=ReceiptType("till_receipt"),
            description="description_example",
            rc_center="rc_center_example",
            created_at="created_at_example",
            updated_at="updated_at_example",
            payment_account=PaymentAccount(
                id=1,
                name="Conto Banca Intesa",
                type=PaymentAccountType("standard"),
                iban="iban_example",
                sia="sia_example",
                cuc="cuc_example",
                virtual=True,
            ),
            items_list=[
                ReceiptItemsListItem(
                    id=1,
                    amount_net=3.14,
                    amount_gross=3.14,
                    category="category_example",
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
                ),
            ],
        ),
        autocomplete_number=True,
    ) # CreateReceiptRequest | The Receipt to create. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Receipt
        api_response = api_instance.create_receipt(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->create_receipt: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Receipt
        api_response = api_instance.create_receipt(company_id, create_receipt_request=create_receipt_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->create_receipt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **create_receipt_request** | [**CreateReceiptRequest**](CreateReceiptRequest.md)| The Receipt to create. | [optional]

### Return type

[**CreateReceiptResponse**](CreateReceiptResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created Receipt. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_receipt**
> delete_receipt(company_id, document_id)

Delete Receipt

Deletes the specified receipt.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import receipts_api
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
    api_instance = receipts_api.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Delete Receipt
        api_instance.delete_receipt(company_id, document_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->delete_receipt: %s\n" % e)
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

# **get_receipt**
> GetReceiptResponse get_receipt(company_id, document_id)

Get Receipt

Gets the specified receipt.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import receipts_api
from fattureincloud_python_sdk.model.get_receipt_response import GetReceiptResponse
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
    api_instance = receipts_api.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Receipt
        api_response = api_instance.get_receipt(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->get_receipt: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Receipt
        api_response = api_instance.get_receipt(company_id, document_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->get_receipt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]

### Return type

[**GetReceiptResponse**](GetReceiptResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Receipt Details. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_pre_create_info**
> GetReceiptPreCreateInfoResponse get_receipt_pre_create_info(company_id)

Get Receipt Pre-Create Info

Retrieves the information useful while creating a new receipt.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import receipts_api
from fattureincloud_python_sdk.model.get_receipt_pre_create_info_response import GetReceiptPreCreateInfoResponse
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
    api_instance = receipts_api.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.

    # example passing only required values which don't have defaults set
    try:
        # Get Receipt Pre-Create Info
        api_response = api_instance.get_receipt_pre_create_info(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->get_receipt_pre_create_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |

### Return type

[**GetReceiptPreCreateInfoResponse**](GetReceiptPreCreateInfoResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pre-create info. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts_monthly_totals**
> GetReceiptsMonthlyTotalsResponse get_receipts_monthly_totals(company_id, type, year)

Get Receipts Monthly Totals

Returns the monthly totals by year and receipt type.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import receipts_api
from fattureincloud_python_sdk.model.get_receipts_monthly_totals_response import GetReceiptsMonthlyTotalsResponse
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
    api_instance = receipts_api.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = "sales_receipt" # str | Receipt Type
    year = "year_example" # str | Year for which you want monthly totals

    # example passing only required values which don't have defaults set
    try:
        # Get Receipts Monthly Totals
        api_response = api_instance.get_receipts_monthly_totals(company_id, type, year)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->get_receipts_monthly_totals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **type** | **str**| Receipt Type |
 **year** | **str**| Year for which you want monthly totals |

### Return type

[**GetReceiptsMonthlyTotalsResponse**](GetReceiptsMonthlyTotalsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monthly Totals. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_receipts**
> ListReceiptsResponse list_receipts(company_id)

List Receipts

Lists the receipts.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import receipts_api
from fattureincloud_python_sdk.model.list_receipts_response import ListReceiptsResponse
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
    api_instance = receipts_api.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)
    page = 1 # int | The page to retrieve. (optional) if omitted the server will use the default value of 1
    per_page = 5 # int | The size of the page. (optional) if omitted the server will use the default value of 5
    sort = "sort_example" # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Receipts
        api_response = api_instance.list_receipts(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->list_receipts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Receipts
        api_response = api_instance.list_receipts(company_id, fields=fields, fieldset=fieldset, page=page, per_page=per_page, sort=sort)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->list_receipts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]
 **page** | **int**| The page to retrieve. | [optional] if omitted the server will use the default value of 1
 **per_page** | **int**| The size of the page. | [optional] if omitted the server will use the default value of 5
 **sort** | **str**| List of comma-separated fields for result sorting (minus for desc sorting). | [optional]

### Return type

[**ListReceiptsResponse**](ListReceiptsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Receipts list. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_receipt**
> ModifyReceiptResponse modify_receipt(company_id, document_id)

Modify Receipt

Modifies the specified receipt.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import receipts_api
from fattureincloud_python_sdk.model.modify_receipt_request import ModifyReceiptRequest
from fattureincloud_python_sdk.model.modify_receipt_response import ModifyReceiptResponse
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
    api_instance = receipts_api.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    modify_receipt_request = ModifyReceiptRequest(
        data=Receipt(
            id=1,
            date=dateutil_parser('1970-01-01').date(),
            number=3.14,
            numeration="numeration_example",
            amount_net=3.14,
            amount_vat=3.14,
            amount_gross=3.14,
            use_gross_prices=False,
            type=ReceiptType("till_receipt"),
            description="description_example",
            rc_center="rc_center_example",
            created_at="created_at_example",
            updated_at="updated_at_example",
            payment_account=PaymentAccount(
                id=1,
                name="Conto Banca Intesa",
                type=PaymentAccountType("standard"),
                iban="iban_example",
                sia="sia_example",
                cuc="cuc_example",
                virtual=True,
            ),
            items_list=[
                ReceiptItemsListItem(
                    id=1,
                    amount_net=3.14,
                    amount_gross=3.14,
                    category="category_example",
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
                ),
            ],
        ),
    ) # ModifyReceiptRequest | Modified receipt. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Receipt
        api_response = api_instance.modify_receipt(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->modify_receipt: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Receipt
        api_response = api_instance.modify_receipt(company_id, document_id, modify_receipt_request=modify_receipt_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ReceiptsApi->modify_receipt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **modify_receipt_request** | [**ModifyReceiptRequest**](ModifyReceiptRequest.md)| Modified receipt. | [optional]

### Return type

[**ModifyReceiptResponse**](ModifyReceiptResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modified receipt. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

