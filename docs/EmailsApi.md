# fattureincloud_python_sdk.EmailsApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_emails**](EmailsApi.md#list_emails) | **GET** /c/{company_id}/emails | List Emails


# **list_emails**
> ListEmailsResponse list_emails(company_id)

List Emails

List Emails.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_emails_response import ListEmailsResponse
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
    api_instance = fattureincloud_python_sdk.EmailsApi(api_client)
    company_id = 12345 # int | The ID of the company.

    try:
        # List Emails
        api_response = api_instance.list_emails(company_id)
        print("The response of EmailsApi->list_emails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->list_emails: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 

### Return type

[**ListEmailsResponse**](ListEmailsResponse.md)

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

