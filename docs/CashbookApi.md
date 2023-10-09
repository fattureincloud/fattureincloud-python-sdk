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
> CreateCashbookEntryResponse create_cashbook_entry(company_id, create_cashbook_entry_request=create_cashbook_entry_request)

Create Cashbook Entry

Creates a new cashbook entry.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_cashbook_entry_request import CreateCashbookEntryRequest
from fattureincloud_python_sdk.models.create_cashbook_entry_response import CreateCashbookEntryResponse
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
    api_instance = fattureincloud_python_sdk.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_cashbook_entry_request = {"data":{"date":"2021-08-24","amount_in":122,"payment_account_in":{"id":333},"description":"Fattura n. 201/2021","entity_name":"Rossi S.r.l.","kind":"issued_document","document":{"id":54321},"type":"in"}} # CreateCashbookEntryRequest | Cashbook entry.  (optional)

    try:
        # Create Cashbook Entry
        api_response = api_instance.create_cashbook_entry(company_id, create_cashbook_entry_request=create_cashbook_entry_request)
        print("The response of CashbookApi->create_cashbook_entry:\n")
        pprint(api_response)
    except Exception as e:
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
import os
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
    api_instance = fattureincloud_python_sdk.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 'document_id_example' # str | The ID of the document.

    try:
        # Delete Cashbook Entry
        api_instance.delete_cashbook_entry(company_id, document_id)
    except Exception as e:
        print("Exception when calling CashbookApi->delete_cashbook_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **document_id** | **str**| The ID of the document. | 

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
> GetCashbookEntryResponse get_cashbook_entry(company_id, document_id, fields=fields, fieldset=fieldset)

Get Cashbook Entry

Gets the specified cashbook entry.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_cashbook_entry_response import GetCashbookEntryResponse
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
    api_instance = fattureincloud_python_sdk.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 'document_id_example' # str | The ID of the document.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get Cashbook Entry
        api_response = api_instance.get_cashbook_entry(company_id, document_id, fields=fields, fieldset=fieldset)
        print("The response of CashbookApi->get_cashbook_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashbookApi->get_cashbook_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **document_id** | **str**| The ID of the document. | 
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
> ListCashbookEntriesResponse list_cashbook_entries(company_id, date_from, date_to, year=year, type=type, payment_account_id=payment_account_id)

List Cashbook Entries

Lists the cashbook entries.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_cashbook_entries_response import ListCashbookEntriesResponse
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
    api_instance = fattureincloud_python_sdk.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    date_from = 'date_from_example' # str | Start date.
    date_to = 'date_to_example' # str | End date.
    year = 56 # int | Filter cashbook by year. (optional)
    type = 'type_example' # str | Filter cashbook by type. (optional)
    payment_account_id = 56 # int | Filter by payment account. (optional)

    try:
        # List Cashbook Entries
        api_response = api_instance.list_cashbook_entries(company_id, date_from, date_to, year=year, type=type, payment_account_id=payment_account_id)
        print("The response of CashbookApi->list_cashbook_entries:\n")
        pprint(api_response)
    except Exception as e:
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
> ModifyCashbookEntryResponse modify_cashbook_entry(company_id, document_id, modify_cashbook_entry_request=modify_cashbook_entry_request)

Modify Cashbook Entry

Modifies the specified cashbook entry.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_cashbook_entry_request import ModifyCashbookEntryRequest
from fattureincloud_python_sdk.models.modify_cashbook_entry_response import ModifyCashbookEntryResponse
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
    api_instance = fattureincloud_python_sdk.CashbookApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 'document_id_example' # str | The ID of the document.
    modify_cashbook_entry_request = {"data":{"date":"2021-08-24","amount_in":122,"payment_account_in":{"id":333},"description":"Fattura n. 201/2021","entity_name":"Rossi S.r.l."}} # ModifyCashbookEntryRequest | Cashbook Entry (optional)

    try:
        # Modify Cashbook Entry
        api_response = api_instance.modify_cashbook_entry(company_id, document_id, modify_cashbook_entry_request=modify_cashbook_entry_request)
        print("The response of CashbookApi->modify_cashbook_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashbookApi->modify_cashbook_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **document_id** | **str**| The ID of the document. | 
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

