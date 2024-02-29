# fattureincloud_python_sdk.TaxesApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_f24**](TaxesApi.md#create_f24) | **POST** /c/{company_id}/taxes | Create F24
[**delete_f24**](TaxesApi.md#delete_f24) | **DELETE** /c/{company_id}/taxes/{document_id} | Delete F24
[**delete_f24_attachment**](TaxesApi.md#delete_f24_attachment) | **DELETE** /c/{company_id}/taxes/{document_id}/attachment | Delete F24 Attachment
[**get_f24**](TaxesApi.md#get_f24) | **GET** /c/{company_id}/taxes/{document_id} | Get F24
[**list_f24**](TaxesApi.md#list_f24) | **GET** /c/{company_id}/taxes | List F24
[**modify_f24**](TaxesApi.md#modify_f24) | **PUT** /c/{company_id}/taxes/{document_id} | Modify F24
[**upload_f24_attachment**](TaxesApi.md#upload_f24_attachment) | **POST** /c/{company_id}/taxes/attachment | Upload F24 Attachment


# **create_f24**
> CreateF24Response create_f24(company_id, create_f24_request=create_f24_request)

Create F24

Creates a new F24.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_f24_request import CreateF24Request
from fattureincloud_python_sdk.models.create_f24_response import CreateF24Response
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
    api_instance = fattureincloud_python_sdk.TaxesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_f24_request = {"data":{"amount":840.36,"description":"PAGAMENTO IVA 2021","due_date":"2021-12-31","status":"paid","payment_account":{"id":111},"attachment_token":"b19c01da9b1688fb73d0d9e8ad"}} # CreateF24Request | The F24 to create (optional)

    try:
        # Create F24
        api_response = api_instance.create_f24(company_id, create_f24_request=create_f24_request)
        print("The response of TaxesApi->create_f24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesApi->create_f24: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **create_f24_request** | [**CreateF24Request**](CreateF24Request.md)| The F24 to create | [optional] 

### Return type

[**CreateF24Response**](CreateF24Response.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created F24 |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_f24**
> delete_f24(company_id, document_id)

Delete F24

Removes the specified F24.

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
    api_instance = fattureincloud_python_sdk.TaxesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Delete F24
        api_instance.delete_f24(company_id, document_id)
    except Exception as e:
        print("Exception when calling TaxesApi->delete_f24: %s\n" % e)
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

# **delete_f24_attachment**
> delete_f24_attachment(company_id, document_id)

Delete F24 Attachment

Removes the attachment of the specified F24.

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
    api_instance = fattureincloud_python_sdk.TaxesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Delete F24 Attachment
        api_instance.delete_f24_attachment(company_id, document_id)
    except Exception as e:
        print("Exception when calling TaxesApi->delete_f24_attachment: %s\n" % e)
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
**200** | File Removed. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_f24**
> GetF24Response get_f24(company_id, document_id, fields=fields, fieldset=fieldset)

Get F24

Gets the specified F24.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_f24_response import GetF24Response
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
    api_instance = fattureincloud_python_sdk.TaxesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get F24
        api_response = api_instance.get_f24(company_id, document_id, fields=fields, fieldset=fieldset)
        print("The response of TaxesApi->get_f24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesApi->get_f24: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **document_id** | **int**| The ID of the document. | 
 **fields** | **str**| List of comma-separated fields. | [optional] 
 **fieldset** | **str**| Name of the fieldset. | [optional] 

### Return type

[**GetF24Response**](GetF24Response.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The F24 |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_f24**
> ListF24Response list_f24(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)

List F24

Lists the F24s.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_f24_response import ListF24Response
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
    api_instance = fattureincloud_python_sdk.TaxesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)
    sort = 'sort_example' # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) (default to 1)
    per_page = 5 # int | The size of the page. (optional) (default to 5)
    q = 'q_example' # str | Query for filtering the results. (optional)

    try:
        # List F24
        api_response = api_instance.list_f24(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)
        print("The response of TaxesApi->list_f24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesApi->list_f24: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **fields** | **str**| List of comma-separated fields. | [optional] 
 **fieldset** | **str**| Name of the fieldset. | [optional] 
 **sort** | **str**| List of comma-separated fields for result sorting (minus for desc sorting). | [optional] 
 **page** | **int**| The page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| The size of the page. | [optional] [default to 5]
 **q** | **str**| Query for filtering the results. | [optional] 

### Return type

[**ListF24Response**](ListF24Response.md)

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

# **modify_f24**
> ModifyF24Response modify_f24(company_id, document_id, modify_f24_request=modify_f24_request)

Modify F24

Modifies the specified F24.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_f24_request import ModifyF24Request
from fattureincloud_python_sdk.models.modify_f24_response import ModifyF24Response
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
    api_instance = fattureincloud_python_sdk.TaxesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    modify_f24_request = {"data":{"amount":840.36,"description":"PAGAMENTO IVA 2021","due_date":"2021-12-31","status":"paid","payment_account":{"id":111}}} # ModifyF24Request | The F24 (optional)

    try:
        # Modify F24
        api_response = api_instance.modify_f24(company_id, document_id, modify_f24_request=modify_f24_request)
        print("The response of TaxesApi->modify_f24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesApi->modify_f24: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **document_id** | **int**| The ID of the document. | 
 **modify_f24_request** | [**ModifyF24Request**](ModifyF24Request.md)| The F24 | [optional] 

### Return type

[**ModifyF24Response**](ModifyF24Response.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The modified F24 |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_f24_attachment**
> UploadF24AttachmentResponse upload_f24_attachment(company_id, filename=filename, attachment=attachment)

Upload F24 Attachment

Uploads an attachment destined to a F24. The actual association between the document and the attachment must be implemented separately, using the returned token.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.upload_f24_attachment_response import UploadF24AttachmentResponse
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
    api_instance = fattureincloud_python_sdk.TaxesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    filename = 'filename_example' # str | Attachment file name (optional)
    attachment = None # bytearray | Attachment file [.png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx] (optional)

    try:
        # Upload F24 Attachment
        api_response = api_instance.upload_f24_attachment(company_id, filename=filename, attachment=attachment)
        print("The response of TaxesApi->upload_f24_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxesApi->upload_f24_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **filename** | **str**| Attachment file name | [optional] 
 **attachment** | **bytearray**| Attachment file [.png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx] | [optional] 

### Return type

[**UploadF24AttachmentResponse**](UploadF24AttachmentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment Token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

