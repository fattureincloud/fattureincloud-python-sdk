# fattureincloud_python_sdk.IssuedEInvoicesApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_e_invoice_rejection_reason**](IssuedEInvoicesApi.md#get_e_invoice_rejection_reason) | **GET** /c/{company_id}/issued_documents/{document_id}/e_invoice/error_reason | Get e-invoice rejection reason
[**get_e_invoice_xml**](IssuedEInvoicesApi.md#get_e_invoice_xml) | **GET** /c/{company_id}/issued_documents/{document_id}/e_invoice/xml | Get e-invoice XML
[**send_e_invoice**](IssuedEInvoicesApi.md#send_e_invoice) | **POST** /c/{company_id}/issued_documents/{document_id}/e_invoice/send | Send the e-invoice
[**verify_e_invoice_xml**](IssuedEInvoicesApi.md#verify_e_invoice_xml) | **GET** /c/{company_id}/issued_documents/{document_id}/e_invoice/xml_verify | Verify e-invoice XML


# **get_e_invoice_rejection_reason**
> GetEInvoiceRejectionReasonResponse get_e_invoice_rejection_reason(company_id, document_id)

Get e-invoice rejection reason

Get e-invoice rejection reason

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_e_invoices_api
from fattureincloud_python_sdk.model.get_e_invoice_rejection_reason_response import GetEInvoiceRejectionReasonResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_e_invoices_api.IssuedEInvoicesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Get e-invoice rejection reason
        api_response = api_instance.get_e_invoice_rejection_reason(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedEInvoicesApi->get_e_invoice_rejection_reason: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |

### Return type

[**GetEInvoiceRejectionReasonResponse**](GetEInvoiceRejectionReasonResponse.md)

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

# **get_e_invoice_xml**
> str get_e_invoice_xml(company_id, document_id)

Get e-invoice XML

Downloads the e-invoice in XML format.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_e_invoices_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_e_invoices_api.IssuedEInvoicesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    include_attachment = True # bool | Include the attachment to the XML e-invoice. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get e-invoice XML
        api_response = api_instance.get_e_invoice_xml(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedEInvoicesApi->get_e_invoice_xml: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get e-invoice XML
        api_response = api_instance.get_e_invoice_xml(company_id, document_id, include_attachment=include_attachment)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedEInvoicesApi->get_e_invoice_xml: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **include_attachment** | **bool**| Include the attachment to the XML e-invoice. | [optional]

### Return type

**str**

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_e_invoice**
> SendEInvoiceResponse send_e_invoice(company_id, document_id)

Send the e-invoice

Sends the e-invoice to SDI.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_e_invoices_api
from fattureincloud_python_sdk.model.send_e_invoice_response import SendEInvoiceResponse
from fattureincloud_python_sdk.model.send_e_invoice_request import SendEInvoiceRequest
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_e_invoices_api.IssuedEInvoicesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.
    send_e_invoice_request = SendEInvoiceRequest(
        data=SendEInvoiceRequestData(
            cassa_type="cassa_type_example",
            withholding_tax_causal="withholding_tax_causal_example",
        ),
    ) # SendEInvoiceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send the e-invoice
        api_response = api_instance.send_e_invoice(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedEInvoicesApi->send_e_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send the e-invoice
        api_response = api_instance.send_e_invoice(company_id, document_id, send_e_invoice_request=send_e_invoice_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedEInvoicesApi->send_e_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |
 **send_e_invoice_request** | [**SendEInvoiceRequest**](SendEInvoiceRequest.md)|  | [optional]

### Return type

[**SendEInvoiceResponse**](SendEInvoiceResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_e_invoice_xml**
> VerifyEInvoiceXmlResponse verify_e_invoice_xml(company_id, document_id)

Verify e-invoice XML

Verifies the e-invoice XML format. Checks if all of the mandatory fields are filled and compliant to the right format.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import issued_e_invoices_api
from fattureincloud_python_sdk.model.verify_e_invoice_xml_response import VerifyEInvoiceXmlResponse
from fattureincloud_python_sdk.model.verify_e_invoice_xml_error_response import VerifyEInvoiceXmlErrorResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issued_e_invoices_api.IssuedEInvoicesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 1 # int | The ID of the document.

    # example passing only required values which don't have defaults set
    try:
        # Verify e-invoice XML
        api_response = api_instance.verify_e_invoice_xml(company_id, document_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling IssuedEInvoicesApi->verify_e_invoice_xml: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **document_id** | **int**| The ID of the document. |

### Return type

[**VerifyEInvoiceXmlResponse**](VerifyEInvoiceXmlResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

