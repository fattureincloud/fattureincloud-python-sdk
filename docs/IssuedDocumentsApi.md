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
[**join_issued_documents**](IssuedDocumentsApi.md#join_issued_documents) | **GET** /c/{company_id}/issued_documents/join | Join issued documents
[**list_issued_documents**](IssuedDocumentsApi.md#list_issued_documents) | **GET** /c/{company_id}/issued_documents | List Issued Documents
[**modify_issued_document**](IssuedDocumentsApi.md#modify_issued_document) | **PUT** /c/{company_id}/issued_documents/{document_id} | Modify Issued Document
[**schedule_email**](IssuedDocumentsApi.md#schedule_email) | **POST** /c/{company_id}/issued_documents/{document_id}/email | Schedule Email
[**transform_issued_document**](IssuedDocumentsApi.md#transform_issued_document) | **GET** /c/{company_id}/issued_documents/transform | Transform issued document
[**upload_issued_document_attachment**](IssuedDocumentsApi.md#upload_issued_document_attachment) | **POST** /c/{company_id}/issued_documents/attachment | Upload Issued Document Attachment


# **create_issued_document**
> CreateIssuedDocumentResponse create_issued_document(company_id, create_issued_document_request=create_issued_document_request)

Create Issued Document

Creates a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_issued_document_request import CreateIssuedDocumentRequest
from fattureincloud_python_sdk.models.create_issued_document_response import CreateIssuedDocumentResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_issued_document_request = {"data":{"type":"receipt","numeration":"rec123","subject":"","visible_subject":"","amount_net":68.18,"amount_vat":6.82,"amount_due_discount":0,"entity":{"id":54321,"name":"Mary Red S.r.L.","vat_number":"IT05432181211","tax_code":"IT05432181211","address_street":"Via Italia, 66","address_postal_code":"20900","address_city":"Milano","address_province":"MI","address_extra":"","country":"Italia","certified_email":"mary@pec.red.com","ei_code":"ABCXCR1"},"date":"2021-08-20","number":1,"next_due_date":"2021-12-31","attachment_token":"ypbqqe4u8w8bdabcd5fd5b1a","items_list":[{"product_id":333,"code":"SG3","name":"Soggiorno","measure":"","net_price":68.18182,"category":"","id":277875565,"gross_price":75,"apply_withholding_taxes":true,"discount":0,"discount_highlight":false,"in_dn":false,"qty":1,"vat":{"id":3,"value":10,"description":""},"stock":true,"description":"","not_taxable":false}],"payments_list":[{"amount":75,"due_date":"2020-08-23","id":444,"payment_terms":{"days":0,"type":"standard"},"status":"not_paid"}],"payment_method":{"id":4}}} # CreateIssuedDocumentRequest | The Issued Document (optional)

    try:
        # Create Issued Document
        api_response = api_instance.create_issued_document(company_id, create_issued_document_request=create_issued_document_request)
        print("The response of IssuedDocumentsApi->create_issued_document:\n")
        pprint(api_response)
    except Exception as e:
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Delete Issued Document
        api_instance.delete_issued_document(company_id, document_id)
    except Exception as e:
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Delete Issued Document Attachment
        api_instance.delete_issued_document_attachment(company_id, document_id)
    except Exception as e:
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
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_email_data_response import GetEmailDataResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Get Email Data
        api_response = api_instance.get_email_data(company_id, document_id)
        print("The response of IssuedDocumentsApi->get_email_data:\n")
        pprint(api_response)
    except Exception as e:
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
> GetExistingIssuedDocumentTotalsResponse get_existing_issued_document_totals(company_id, document_id, get_existing_issued_document_totals_request=get_existing_issued_document_totals_request)

Get Existing Issued Document Totals

Returns the totals for a specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_existing_issued_document_totals_request import GetExistingIssuedDocumentTotalsRequest
from fattureincloud_python_sdk.models.get_existing_issued_document_totals_response import GetExistingIssuedDocumentTotalsResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    get_existing_issued_document_totals_request = {"data":{"rivalsa":20}} # GetExistingIssuedDocumentTotalsRequest |  (optional)

    try:
        # Get Existing Issued Document Totals
        api_response = api_instance.get_existing_issued_document_totals(company_id, document_id, get_existing_issued_document_totals_request=get_existing_issued_document_totals_request)
        print("The response of IssuedDocumentsApi->get_existing_issued_document_totals:\n")
        pprint(api_response)
    except Exception as e:
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
> GetIssuedDocumentResponse get_issued_document(company_id, document_id, fields=fields, fieldset=fieldset)

Get Issued Document

Gets the specified document. 

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_issued_document_response import GetIssuedDocumentResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get Issued Document
        api_response = api_instance.get_issued_document(company_id, document_id, fields=fields, fieldset=fieldset)
        print("The response of IssuedDocumentsApi->get_issued_document:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_issued_document_pre_create_info_response import GetIssuedDocumentPreCreateInfoResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = 'type_example' # str | The type of the issued document.

    try:
        # Get Issued Document Pre-create info
        api_response = api_instance.get_issued_document_pre_create_info(company_id, type)
        print("The response of IssuedDocumentsApi->get_issued_document_pre_create_info:\n")
        pprint(api_response)
    except Exception as e:
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
> GetNewIssuedDocumentTotalsResponse get_new_issued_document_totals(company_id, get_new_issued_document_totals_request=get_new_issued_document_totals_request)

Get New Issued Document Totals

Returns the totals for a new document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_new_issued_document_totals_request import GetNewIssuedDocumentTotalsRequest
from fattureincloud_python_sdk.models.get_new_issued_document_totals_response import GetNewIssuedDocumentTotalsResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    get_new_issued_document_totals_request = {"data":{"id":12345,"type":"receipt","year":2021,"numeration":"rec123","subject":"","visible_subject":"","rc_center":"","stamp_duty":0,"use_gross_prices":false,"delivery_note":false,"accompanying_invoice":false,"amount_net":68.18,"amount_vat":6.82,"amount_due_discount":0,"amount_rivalsa":0,"amount_cassa":0,"amount_withholding_tax":0,"amount_other_withholding_tax":0,"h_margins":15,"v_margins":16,"show_payment_method":false,"show_payments":true,"show_totals":"all","show_paypal_button":true,"show_notification_button":false,"is_marked":false,"created_at":"2021-08-13 09:30:20","updated_at":"2021-08-23 05:34:20","entity":{"id":54321,"name":"Mary Red S.r.L.","vat_number":"IT05432181211","tax_code":"IT05432181211","address_street":"Via Italia, 66","address_postal_code":"20900","address_city":"Milano","address_province":"MI","address_extra":"","country":"Italia","certified_email":"mary@pec.red.com","ei_code":"ABCXCR1"},"date":"2021-08-20","number":1,"currency":{"id":"EUR","exchange_rate":"1.00000","symbol":"€"},"language":{"code":"it","name":"Italiano"},"notes":"","rivalsa":0,"cassa":0,"withholding_tax":0,"withholding_tax_taxable":100,"other_withholding_tax":0,"payment_method":{"id":4,"name":"Credit card"},"use_split_payment":false,"items_list":[{"product_id":5432,"code":"SG3","name":"Soggiorno","measure":"","net_price":68.18182,"category":"","id":277876033,"apply_withholding_taxes":true,"discount":0,"discount_highlight":false,"in_dn":false,"qty":1,"vat":{"id":3,"value":10,"description":""},"stock":false,"description":"","not_taxable":false}],"payments_list":[{"amount":75,"due_date":"2020-08-23","id":69078013,"payment_terms":{"days":0,"type":"standard"},"status":"not_paid"}],"attachment_url":"kdijrnf893hnwkfk45f50f.pdf","next_due_date":"2020-08-23","template":{"id":2821,"name":"Light Smoke"},"url":"y12h45rn9yf2mse0p43t7ec90vr.pdf"}} # GetNewIssuedDocumentTotalsRequest |  (optional)

    try:
        # Get New Issued Document Totals
        api_response = api_instance.get_new_issued_document_totals(company_id, get_new_issued_document_totals_request=get_new_issued_document_totals_request)
        print("The response of IssuedDocumentsApi->get_new_issued_document_totals:\n")
        pprint(api_response)
    except Exception as e:
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

# **join_issued_documents**
> JoinIssuedDocumentsResponse join_issued_documents(company_id, ids, group=group, e_invoice=e_invoice)

Join issued documents

Joins issued documents.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.join_issued_documents_response import JoinIssuedDocumentsResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    ids = '1,2,3,4' # str | Ids of the documents.
    group = 56 # int | Group items. (optional)
    e_invoice = 56 # int | New document e_invoice. (optional)

    try:
        # Join issued documents
        api_response = api_instance.join_issued_documents(company_id, ids, group=group, e_invoice=e_invoice)
        print("The response of IssuedDocumentsApi->join_issued_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuedDocumentsApi->join_issued_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **ids** | **str**| Ids of the documents. | 
 **group** | **int**| Group items. | [optional] 
 **e_invoice** | **int**| New document e_invoice. | [optional] 

### Return type

[**JoinIssuedDocumentsResponse**](JoinIssuedDocumentsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_issued_documents**
> ListIssuedDocumentsResponse list_issued_documents(company_id, type, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q, inclusive=inclusive)

List Issued Documents

Lists the issued documents.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_issued_documents_response import ListIssuedDocumentsResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    type = 'type_example' # str | The type of the issued document.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)
    sort = 'sort_example' # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) (default to 1)
    per_page = 5 # int | The size of the page. (optional) (default to 5)
    q = 'q_example' # str | Query for filtering the results. (optional)
    inclusive = 56 # int | (Only for type = delivery_notes) Include invoices delivery notes. (optional)

    try:
        # List Issued Documents
        api_response = api_instance.list_issued_documents(company_id, type, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q, inclusive=inclusive)
        print("The response of IssuedDocumentsApi->list_issued_documents:\n")
        pprint(api_response)
    except Exception as e:
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
 **page** | **int**| The page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| The size of the page. | [optional] [default to 5]
 **q** | **str**| Query for filtering the results. | [optional] 
 **inclusive** | **int**| (Only for type &#x3D; delivery_notes) Include invoices delivery notes. | [optional] 

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
> ModifyIssuedDocumentResponse modify_issued_document(company_id, document_id, modify_issued_document_request=modify_issued_document_request)

Modify Issued Document

Modifies the specified document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_issued_document_request import ModifyIssuedDocumentRequest
from fattureincloud_python_sdk.models.modify_issued_document_response import ModifyIssuedDocumentResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    modify_issued_document_request = {"data":{"type":"receipt","numeration":"rec123","subject":"","visible_subject":"","amount_net":68.18,"amount_vat":6.82,"amount_due_discount":0,"entity":{"id":54321,"name":"Mary Red S.r.L.","vat_number":"IT05432181211","tax_code":"IT05432181211","address_street":"Via Italia, 66","address_postal_code":"20900","address_city":"Milano","address_province":"MI","address_extra":"","country":"Italia","certified_email":"mary@pec.red.com","ei_code":"ABCXCR1"},"date":"2021-08-20","number":1,"next_due_date":"2021-12-31","attachment_token":"ypbqqe4u8w8bdabcd5fd5b1a","items_list":[{"product_id":333,"code":"SG3","name":"Soggiorno","measure":"","net_price":68.18182,"category":"","id":277875565,"gross_price":75,"apply_withholding_taxes":true,"discount":0,"discount_highlight":false,"in_dn":false,"qty":1,"vat":{"id":3,"value":10,"description":""},"stock":true,"description":"","not_taxable":false}],"payments_list":[{"amount":75,"due_date":"2020-08-23","id":444,"payment_terms":{"days":0,"type":"standard"},"status":"not_paid"}]}} # ModifyIssuedDocumentRequest | The modified document (optional)

    try:
        # Modify Issued Document
        api_response = api_instance.modify_issued_document(company_id, document_id, modify_issued_document_request=modify_issued_document_request)
        print("The response of IssuedDocumentsApi->modify_issued_document:\n")
        pprint(api_response)
    except Exception as e:
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
> schedule_email(company_id, document_id, schedule_email_request=schedule_email_request)

Schedule Email

Schedules the sending of a document by email.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.schedule_email_request import ScheduleEmailRequest
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    schedule_email_request = {"data":{"sender_email":"mariorossi@fattureincloud.it","recipient_email":"mary.red@example.com","subject":"Nostra pro forma nr. 1","body":"Gentile Mario Rossi,<br>per vedere la nostra pro forma di  o per scaricarne una copia in versione PDF prema sul bottone sottostante.<br><br>{{allegati}}<br><br>Cordiali saluti,<br><b>Mario Rossi</b>","include":{"document":false,"delivery_note":false,"attachment":false,"accompanying_invoice":false},"attach_pdf":true,"send_copy":false}} # ScheduleEmailRequest | Email Schedule (optional)

    try:
        # Schedule Email
        api_instance.schedule_email(company_id, document_id, schedule_email_request=schedule_email_request)
    except Exception as e:
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

# **transform_issued_document**
> TransformIssuedDocumentResponse transform_issued_document(company_id, original_document_id, new_type, e_invoice=e_invoice, transform_keep_copy=transform_keep_copy)

Transform issued document

Transforms the document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.transform_issued_document_response import TransformIssuedDocumentResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    original_document_id = 56 # int | Original document id.
    new_type = 'new_type_example' # str | New document type.
    e_invoice = 56 # int | New document e_invoice. (optional)
    transform_keep_copy = 56 # int | Keep the old document. (optional)

    try:
        # Transform issued document
        api_response = api_instance.transform_issued_document(company_id, original_document_id, new_type, e_invoice=e_invoice, transform_keep_copy=transform_keep_copy)
        print("The response of IssuedDocumentsApi->transform_issued_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuedDocumentsApi->transform_issued_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **original_document_id** | **int**| Original document id. | 
 **new_type** | **str**| New document type. | 
 **e_invoice** | **int**| New document e_invoice. | [optional] 
 **transform_keep_copy** | **int**| Keep the old document. | [optional] 

### Return type

[**TransformIssuedDocumentResponse**](TransformIssuedDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_issued_document_attachment**
> UploadIssuedDocumentAttachmentResponse upload_issued_document_attachment(company_id, filename=filename, attachment=attachment)

Upload Issued Document Attachment

Uploads an attachment destined to an issued document. The actual association between the document and the attachment must be implemented separately, using the returned token.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.upload_issued_document_attachment_response import UploadIssuedDocumentAttachmentResponse
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
    api_instance = fattureincloud_python_sdk.IssuedDocumentsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    filename = 'filename_example' # str | Attachment file name (optional)
    attachment = None # bytearray | Attachment file [.png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx] (optional)

    try:
        # Upload Issued Document Attachment
        api_response = api_instance.upload_issued_document_attachment(company_id, filename=filename, attachment=attachment)
        print("The response of IssuedDocumentsApi->upload_issued_document_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuedDocumentsApi->upload_issued_document_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **filename** | **str**| Attachment file name | [optional] 
 **attachment** | **bytearray**| Attachment file [.png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx] | [optional] 

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

