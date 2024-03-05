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
> CreateReceiptResponse create_receipt(company_id, create_receipt_request=create_receipt_request)

Create Receipt

Creates a new receipt.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_receipt_request import CreateReceiptRequest
from fattureincloud_python_sdk.models.create_receipt_response import CreateReceiptResponse
from fattureincloud_python_sdk.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_receipt_request = {"data":{"date":"2021-08-19","number":6,"numeration":"REC006","amount_net":8.2,"amount_vat":1.8,"type":"sales_receipt","description":"cassa 1","rc_center":"","payment_account":{"id":555,"name":"contanti"},"items_list":[{"id":888,"amount_net":8.2,"amount_vat":1.8,"category":"altro","vat":{"id":0,"value":22,"description":"iva"}}]}} # CreateReceiptRequest | The Receipt to create. (optional)

    try:
        # Create Receipt
        api_response = api_instance.create_receipt(company_id, create_receipt_request=create_receipt_request)
        print("The response of ReceiptsApi->create_receipt:\n")
        pprint(api_response)
    except Exception as e:
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
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Delete Receipt
        api_instance.delete_receipt(company_id, document_id)
    except Exception as e:
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
> GetReceiptResponse get_receipt(company_id, document_id, fields=fields, fieldset=fieldset)

Get Receipt

Gets the specified receipt.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_receipt_response import GetReceiptResponse
from fattureincloud_python_sdk.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get Receipt
        api_response = api_instance.get_receipt(company_id, document_id, fields=fields, fieldset=fieldset)
        print("The response of ReceiptsApi->get_receipt:\n")
        pprint(api_response)
    except Exception as e:
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
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_receipt_pre_create_info_response import GetReceiptPreCreateInfoResponse
from fattureincloud_python_sdk.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.

    try:
        # Get Receipt Pre-Create Info
        api_response = api_instance.get_receipt_pre_create_info(company_id)
        print("The response of ReceiptsApi->get_receipt_pre_create_info:\n")
        pprint(api_response)
    except Exception as e:
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
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_receipts_monthly_totals_response import GetReceiptsMonthlyTotalsResponse
from fattureincloud_python_sdk.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = 'type_example' # str | Receipt Type
    year = 'year_example' # str | Year for which you want monthly totals

    try:
        # Get Receipts Monthly Totals
        api_response = api_instance.get_receipts_monthly_totals(company_id, type, year)
        print("The response of ReceiptsApi->get_receipts_monthly_totals:\n")
        pprint(api_response)
    except Exception as e:
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
> ListReceiptsResponse list_receipts(company_id, fields=fields, fieldset=fieldset, page=page, per_page=per_page, sort=sort, q=q)

List Receipts

Lists the receipts.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_receipts_response import ListReceiptsResponse
from fattureincloud_python_sdk.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)
    page = 1 # int | The page to retrieve. (optional) (default to 1)
    per_page = 5 # int | The size of the page. (optional) (default to 5)
    sort = 'sort_example' # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    q = 'q_example' # str | Query for filtering the results. (optional)

    try:
        # List Receipts
        api_response = api_instance.list_receipts(company_id, fields=fields, fieldset=fieldset, page=page, per_page=per_page, sort=sort, q=q)
        print("The response of ReceiptsApi->list_receipts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiptsApi->list_receipts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **fields** | **str**| List of comma-separated fields. | [optional] 
 **fieldset** | **str**| Name of the fieldset. | [optional] 
 **page** | **int**| The page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| The size of the page. | [optional] [default to 5]
 **sort** | **str**| List of comma-separated fields for result sorting (minus for desc sorting). | [optional] 
 **q** | **str**| Query for filtering the results. | [optional] 

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
> ModifyReceiptResponse modify_receipt(company_id, document_id, modify_receipt_request=modify_receipt_request)

Modify Receipt

Modifies the specified receipt.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_receipt_request import ModifyReceiptRequest
from fattureincloud_python_sdk.models.modify_receipt_response import ModifyReceiptResponse
from fattureincloud_python_sdk.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.ReceiptsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    modify_receipt_request = {"data":{"date":"2021-08-19","number":6,"numeration":"REC006","amount_net":8.2,"amount_vat":1.8,"type":"sales_receipt","description":"cassa 1","rc_center":"","payment_account":{"id":555,"name":"contanti"},"items_list":[{"id":888,"amount_net":8.2,"amount_vat":1.8,"category":"altro","vat":{"id":0,"value":22,"description":"iva"}}]}} # ModifyReceiptRequest | Modified receipt. (optional)

    try:
        # Modify Receipt
        api_response = api_instance.modify_receipt(company_id, document_id, modify_receipt_request=modify_receipt_request)
        print("The response of ReceiptsApi->modify_receipt:\n")
        pprint(api_response)
    except Exception as e:
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

