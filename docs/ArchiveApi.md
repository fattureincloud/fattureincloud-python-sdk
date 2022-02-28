# fattureincloud_python_sdk.ArchiveApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_archive_document**](ArchiveApi.md#create_archive_document) | **POST** /c/{company_id}/archive | Create Archive Document
[**delete_archive_document**](ArchiveApi.md#delete_archive_document) | **DELETE** /c/{company_id}/archive/{document_id} | Delete Archive Document
[**get_archive_document**](ArchiveApi.md#get_archive_document) | **GET** /c/{company_id}/archive/{document_id} | Get Archive Document
[**list_archive_documents**](ArchiveApi.md#list_archive_documents) | **GET** /c/{company_id}/archive | List Archive Documents
[**modify_archive_document**](ArchiveApi.md#modify_archive_document) | **PUT** /c/{company_id}/archive/{document_id} | Modify Archive Document
[**upload_archive_document_attachment**](ArchiveApi.md#upload_archive_document_attachment) | **POST** /c/{company_id}/archive/attachment | Upload Archive Document Attachment


# **create_archive_document**
> CreateArchiveDocumentResponse create_archive_document(company_id)

Create Archive Document

Creates a new archive document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import archive_api
from fattureincloud_python_sdk.model.create_archive_document_response import CreateArchiveDocumentResponse
from fattureincloud_python_sdk.model.create_archive_document_request import CreateArchiveDocumentRequest
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

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

    # example passing only required values which don't have defaults set
    try:
        # Create Archive Document
        api_response = api_instance.create_archive_document(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->create_archive_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Archive Document
        api_response = api_instance.create_archive_document(company_id, create_archive_document_request=create_archive_document_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->create_archive_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **create_archive_document_request** | [**CreateArchiveDocumentRequest**](CreateArchiveDocumentRequest.md)| The Archive Document. | [optional]

### Return type

[**CreateArchiveDocumentResponse**](CreateArchiveDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Archive Document. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_archive_document**
> delete_archive_document(company_id, document_id)

Delete Archive Document

Deletes the specified archive document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import archive_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = archive_api.ArchiveApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Delete Archive Document
        api_instance.delete_archive_document(company_id, document_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->delete_archive_document: %s\n" % e)
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

# **get_archive_document**
> GetArchiveDocumentResponse get_archive_document(company_id, document_id)

Get Archive Document

Gets the specified archive document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import archive_api
from fattureincloud_python_sdk.model.get_archive_document_response import GetArchiveDocumentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = archive_api.ArchiveApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Archive Document
        api_response = api_instance.get_archive_document(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->get_archive_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Archive Document
        api_response = api_instance.get_archive_document(company_id, document_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->get_archive_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]

### Return type

[**GetArchiveDocumentResponse**](GetArchiveDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Archive Document Details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_archive_documents**
> ListArchiveDocumentsResponse list_archive_documents(company_id)

List Archive Documents

Lists the archive documents.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import archive_api
from fattureincloud_python_sdk.model.list_archive_documents_response import ListArchiveDocumentsResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = archive_api.ArchiveApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)
    sort = "sort_example" # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) if omitted the server will use the default value of 1
    per_page = 5 # int | The size of the page. (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # List Archive Documents
        api_response = api_instance.list_archive_documents(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->list_archive_documents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Archive Documents
        api_response = api_instance.list_archive_documents(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->list_archive_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]
 **sort** | **str**| List of comma-separated fields for result sorting (minus for desc sorting). | [optional]
 **page** | **int**| The page to retrieve. | [optional] if omitted the server will use the default value of 1
 **per_page** | **int**| The size of the page. | [optional] if omitted the server will use the default value of 5

### Return type

[**ListArchiveDocumentsResponse**](ListArchiveDocumentsResponse.md)

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

# **modify_archive_document**
> ModifyArchiveDocumentResponse modify_archive_document(company_id, document_id)

Modify Archive Document

Modifies the specified archive document.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import archive_api
from fattureincloud_python_sdk.model.modify_archive_document_response import ModifyArchiveDocumentResponse
from fattureincloud_python_sdk.model.modify_archive_document_request import ModifyArchiveDocumentRequest
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = archive_api.ArchiveApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    modify_archive_document_request = ModifyArchiveDocumentRequest(
        data=ArchiveDocument(
            id=1,
            date=dateutil_parser('1970-01-01').date(),
            description="description_example",
            category="category_example",
            attachment_token="attachment_token_example",
        ),
    ) # ModifyArchiveDocumentRequest | Modified Archive Document (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Archive Document
        api_response = api_instance.modify_archive_document(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->modify_archive_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Archive Document
        api_response = api_instance.modify_archive_document(company_id, document_id, modify_archive_document_request=modify_archive_document_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->modify_archive_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **modify_archive_document_request** | [**ModifyArchiveDocumentRequest**](ModifyArchiveDocumentRequest.md)| Modified Archive Document | [optional]

### Return type

[**ModifyArchiveDocumentResponse**](ModifyArchiveDocumentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The modified Archived Document |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_archive_document_attachment**
> UploadArchiveAttachmentResponse upload_archive_document_attachment(company_id)

Upload Archive Document Attachment

Uploads an attachment destined to an archive document. The actual association between the document and the attachment must be implemented separately, using the returned token.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import archive_api
from fattureincloud_python_sdk.model.upload_archive_attachment_response import UploadArchiveAttachmentResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = archive_api.ArchiveApi(api_client)
    company_id = 12345 # int | The ID of the company.
    filename = "attachment.pdf" # str, none_type | Name of the file. (optional)
    attachment = open('/path/to/file', 'rb') # file_type, none_type | Valid format: .png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload Archive Document Attachment
        api_response = api_instance.upload_archive_document_attachment(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->upload_archive_document_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload Archive Document Attachment
        api_response = api_instance.upload_archive_document_attachment(company_id, filename=filename, attachment=attachment)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ArchiveApi->upload_archive_document_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **filename** | **str, none_type**| Name of the file. | [optional]
 **attachment** | **file_type, none_type**| Valid format: .png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx | [optional]

### Return type

[**UploadArchiveAttachmentResponse**](UploadArchiveAttachmentResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

