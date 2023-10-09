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
> CreateReceivedDocumentResponse create_received_document(company_id, create_received_document_request=create_received_document_request)

Create Received Document

Creates a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_received_document_request import CreateReceivedDocumentRequest
from fattureincloud_python_sdk.models.create_received_document_response import CreateReceivedDocumentResponse
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_received_document_request = {"data":{"type":"expense","description":"Soggiorno di lavoro","amortization":1,"rc_center":"","invoice_number":"","is_marked":false,"is_detailed":false,"e_invoice":false,"entity":{"id":111,"name":"Hotel Rubino Palace"},"date":"2021-08-15","next_due_date":"2021-08-15","currency":{"id":"EUR","exchange_rate":"1.00000","symbol":"€"},"amount_net":592,"amount_vat":0,"amount_gross":592,"amount_withholding_tax":0,"amount_other_withholding_tax":0,"tax_deductibility":50,"vat_deductibility":100,"payments_list":[{"amount":592,"due_date":"2021-08-15","paid_date":"2021-08-15","id":777,"payment_terms":{"days":0,"type":"standard"},"status":"paid","payment_account":{"id":222,"name":"Contanti","virtual":false}}],"attachment_token":"bnopjao8gvydtgnewgiovs74yrfqwefEF"}} # CreateReceivedDocumentRequest | Document to create (optional)

    try:
        # Create Received Document
        api_response = api_instance.create_received_document(company_id, create_received_document_request=create_received_document_request)
        print("The response of ReceivedDocumentsApi->create_received_document:\n")
        pprint(api_response)
    except Exception as e:
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Delete Received Document
        api_instance.delete_received_document(company_id, document_id)
    except Exception as e:
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Delete Received Document Attachment
        api_instance.delete_received_document_attachment(company_id, document_id)
    except Exception as e:
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
> GetExistingReceivedDocumentTotalsResponse get_existing_received_document_totals(company_id, document_id, get_existing_received_document_totals_request=get_existing_received_document_totals_request)

Get Existing Received Document Totals

Returns the totals for the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_existing_received_document_totals_request import GetExistingReceivedDocumentTotalsRequest
from fattureincloud_python_sdk.models.get_existing_received_document_totals_response import GetExistingReceivedDocumentTotalsResponse
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    get_existing_received_document_totals_request = {"data":{"amount_vat":20}} # GetExistingReceivedDocumentTotalsRequest | Received document. (optional)

    try:
        # Get Existing Received Document Totals
        api_response = api_instance.get_existing_received_document_totals(company_id, document_id, get_existing_received_document_totals_request=get_existing_received_document_totals_request)
        print("The response of ReceivedDocumentsApi->get_existing_received_document_totals:\n")
        pprint(api_response)
    except Exception as e:
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
> GetNewReceivedDocumentTotalsResponse get_new_received_document_totals(company_id, get_new_received_document_totals_request=get_new_received_document_totals_request)

Get New Received Document Totals

Returns the totals for a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_new_received_document_totals_request import GetNewReceivedDocumentTotalsRequest
from fattureincloud_python_sdk.models.get_new_received_document_totals_response import GetNewReceivedDocumentTotalsResponse
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    get_new_received_document_totals_request = {"data":{"type":"expense","description":"Soggiorno di lavoro","amortization":1,"rc_center":"","invoice_number":"","is_marked":false,"is_detailed":false,"e_invoice":false,"created_at":"2021-08-15 14:02:02","updated_at":"2021-08-15 14:02:02","entity":{"id":111,"name":"Hotel Rubino Palace"},"date":"2021-08-15","next_due_date":"2021-08-15","currency":{"id":"EUR","exchange_rate":"1.00000","symbol":"€"},"amount_net":592,"amount_vat":10,"amount_withholding_tax":0,"amount_other_withholding_tax":0,"tax_deductibility":50,"vat_deductibility":100,"payments_list":[{"amount":592,"due_date":"2021-08-15","paid_date":"2021-08-15","id":777,"payment_terms":{"days":0,"type":"standard"},"status":"paid"}]}} # GetNewReceivedDocumentTotalsRequest | Received document. (optional)

    try:
        # Get New Received Document Totals
        api_response = api_instance.get_new_received_document_totals(company_id, get_new_received_document_totals_request=get_new_received_document_totals_request)
        print("The response of ReceivedDocumentsApi->get_new_received_document_totals:\n")
        pprint(api_response)
    except Exception as e:
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
> GetReceivedDocumentResponse get_received_document(company_id, document_id, fields=fields, fieldset=fieldset)

Get Received Document

Gets the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_received_document_response import GetReceivedDocumentResponse
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get Received Document
        api_response = api_instance.get_received_document(company_id, document_id, fields=fields, fieldset=fieldset)
        print("The response of ReceivedDocumentsApi->get_received_document:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_received_document_pre_create_info_response import GetReceivedDocumentPreCreateInfoResponse
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = 'type_example' # str | The type of the received document.

    try:
        # Get Received Document Pre-Create Info
        api_response = api_instance.get_received_document_pre_create_info(company_id, type)
        print("The response of ReceivedDocumentsApi->get_received_document_pre_create_info:\n")
        pprint(api_response)
    except Exception as e:
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
> ListReceivedDocumentsResponse list_received_documents(company_id, type, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)

List Received Documents

Lists the received documents.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_received_documents_response import ListReceivedDocumentsResponse
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = 'type_example' # str | The type of the received document.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)
    sort = 'sort_example' # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) (default to 1)
    per_page = 5 # int | The size of the page. (optional) (default to 5)
    q = 'q_example' # str | Query for filtering the results. (optional)

    try:
        # List Received Documents
        api_response = api_instance.list_received_documents(company_id, type, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)
        print("The response of ReceivedDocumentsApi->list_received_documents:\n")
        pprint(api_response)
    except Exception as e:
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
 **page** | **int**| The page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| The size of the page. | [optional] [default to 5]
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
> ModifyReceivedDocumentResponse modify_received_document(company_id, document_id, modify_received_document_request=modify_received_document_request)

Modify Received Document

Modifies the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_received_document_request import ModifyReceivedDocumentRequest
from fattureincloud_python_sdk.models.modify_received_document_response import ModifyReceivedDocumentResponse
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    modify_received_document_request = {"data":{"type":"expense","description":"Soggiorno di lavoro","amortization":1,"rc_center":"","invoice_number":"","is_marked":false,"is_detailed":false,"e_invoice":false,"entity":{"id":111,"name":"Hotel Rubino Palace"},"date":"2021-08-15","next_due_date":"2021-08-15","currency":{"id":"EUR","exchange_rate":"1.00000","symbol":"€"},"amount_net":592,"amount_vat":0,"amount_gross":592,"amount_withholding_tax":0,"amount_other_withholding_tax":0,"tax_deductibility":50,"vat_deductibility":100,"payments_list":[{"amount":592,"due_date":"2021-08-15","paid_date":"2021-08-15","id":777,"payment_terms":{"days":0,"type":"standard"},"status":"paid","payment_account":{"id":222,"name":"Contanti","virtual":false}}]}} # ModifyReceivedDocumentRequest | Modified document. (optional)

    try:
        # Modify Received Document
        api_response = api_instance.modify_received_document(company_id, document_id, modify_received_document_request=modify_received_document_request)
        print("The response of ReceivedDocumentsApi->modify_received_document:\n")
        pprint(api_response)
    except Exception as e:
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
> UploadReceivedDocumentAttachmentResponse upload_received_document_attachment(company_id, filename=filename, attachment=attachment)

Upload Received Document Attachment

Uploads an attachment destined to a received document. The actual association between the document and the attachment must be implemented separately, using the returned token.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.upload_received_document_attachment_response import UploadReceivedDocumentAttachmentResponse
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
    api_instance = fattureincloud_python_sdk.ReceivedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    filename = 'filename_example' # str | Attachment file name (optional)
    attachment = None # bytearray | Attachment file [.png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx] (optional)

    try:
        # Upload Received Document Attachment
        api_response = api_instance.upload_received_document_attachment(company_id, filename=filename, attachment=attachment)
        print("The response of ReceivedDocumentsApi->upload_received_document_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivedDocumentsApi->upload_received_document_attachment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **filename** | **str**| Attachment file name | [optional] 
 **attachment** | **bytearray**| Attachment file [.png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx] | [optional] 

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

