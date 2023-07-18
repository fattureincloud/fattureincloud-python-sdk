# fattureincloud_python_sdk.ClientsApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ClientsApi.md#create_client) | **POST** /c/{company_id}/entities/clients | Create Client
[**delete_client**](ClientsApi.md#delete_client) | **DELETE** /c/{company_id}/entities/clients/{client_id} | Delete Client
[**get_client**](ClientsApi.md#get_client) | **GET** /c/{company_id}/entities/clients/{client_id} | Get Client
[**list_clients**](ClientsApi.md#list_clients) | **GET** /c/{company_id}/entities/clients | List Clients
[**modify_client**](ClientsApi.md#modify_client) | **PUT** /c/{company_id}/entities/clients/{client_id} | Modify Client


# **create_client**
> CreateClientResponse create_client(company_id, create_client_request=create_client_request)

Create Client

Creates a new client.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_client_request import CreateClientRequest
from fattureincloud_python_sdk.models.create_client_response import CreateClientResponse
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
    api_instance = fattureincloud_python_sdk.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_client_request = {"data":{"code":"AE86","name":"Avv. Maria Rossi","type":"person","first_name":"Maria","last_name":"Rossi","contact_person":"","vat_number":"IT12345640962","tax_code":"BLTGNI5ABCDA794E","address_street":"Via Roma, 1","address_postal_code":"20900","address_city":"Milano","address_province":"MI","address_extra":"","country":"Italia","email":"maria.rossi@example.com","certified_email":"maria.rossi@pec.example.com","phone":"1234567890","fax":"","notes":"","default_payment_terms":1,"default_payment_terms_type":"standard","bank_name":"Indesa","bank_iban":"IT40P123456781000000123456","bank_swift_code":"AK86PCT","shipping_address":"Corso Magellano 4","e_invoice":true,"ei_code":"111111","default_vat":{"id":54321,"value":45,"description":"","is_disabled":false}}} # CreateClientRequest | The client to create (optional)

    try:
        # Create Client
        api_response = api_instance.create_client(company_id, create_client_request=create_client_request)
        print("The response of ClientsApi->create_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->create_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **create_client_request** | [**CreateClientRequest**](CreateClientRequest.md)| The client to create | [optional] 

### Return type

[**CreateClientResponse**](CreateClientResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> delete_client(company_id, client_id)

Delete Client

Deletes the specified client.

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
    api_instance = fattureincloud_python_sdk.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    client_id = 56 # int | The ID of the client.

    try:
        # Delete Client
        api_instance.delete_client(company_id, client_id)
    except Exception as e:
        print("Exception when calling ClientsApi->delete_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **client_id** | **int**| The ID of the client. | 

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
**200** | Entity Removed |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> GetClientResponse get_client(company_id, client_id, fields=fields, fieldset=fieldset)

Get Client

Gets the specified client.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_client_response import GetClientResponse
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
    api_instance = fattureincloud_python_sdk.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    client_id = 56 # int | The ID of the client.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get Client
        api_response = api_instance.get_client(company_id, client_id, fields=fields, fieldset=fieldset)
        print("The response of ClientsApi->get_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->get_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **client_id** | **int**| The ID of the client. | 
 **fields** | **str**| List of comma-separated fields. | [optional] 
 **fieldset** | **str**| Name of the fieldset. | [optional] 

### Return type

[**GetClientResponse**](GetClientResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client Details. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients**
> ListClientsResponse list_clients(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)

List Clients

Lists the clients.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_clients_response import ListClientsResponse
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
    api_instance = fattureincloud_python_sdk.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)
    sort = 'sort_example' # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) (default to 1)
    per_page = 5 # int | The size of the page. (optional) (default to 5)
    q = 'q_example' # str | Query for filtering the results. (optional)

    try:
        # List Clients
        api_response = api_instance.list_clients(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)
        print("The response of ClientsApi->list_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->list_clients: %s\n" % e)
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

[**ListClientsResponse**](ListClientsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_client**
> ModifyClientResponse modify_client(company_id, client_id, modify_client_request=modify_client_request)

Modify Client

Modifies the specified client.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_client_request import ModifyClientRequest
from fattureincloud_python_sdk.models.modify_client_response import ModifyClientResponse
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
    api_instance = fattureincloud_python_sdk.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    client_id = 56 # int | The ID of the client.
    modify_client_request = {"data":{"code":"AE86","name":"Avv. Maria Rossi","type":"person","first_name":"Maria","last_name":"Rossi","contact_person":"","vat_number":"IT12345640962","tax_code":"BLTGNI5ABCDA794E","address_street":"Via Roma, 1","address_postal_code":"20900","address_city":"Milano","address_province":"MI","address_extra":"","country":"Italia","email":"maria.rossi@example.com","certified_email":"maria.rossi@pec.example.com","phone":"1234567890","fax":"","notes":"","default_payment_terms":1,"default_payment_terms_type":"standard","bank_name":"Indesa","bank_iban":"IT40P123456781000000123456","bank_swift_code":"AK86PCT","shipping_address":"Corso Magellano 4","e_invoice":true,"ei_code":"111111","default_vat":{"id":54321,"value":45,"description":"","is_disabled":false}}} # ModifyClientRequest | The modified Client. First level parameters are managed in delta mode. (optional)

    try:
        # Modify Client
        api_response = api_instance.modify_client(company_id, client_id, modify_client_request=modify_client_request)
        print("The response of ClientsApi->modify_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->modify_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **client_id** | **int**| The ID of the client. | 
 **modify_client_request** | [**ModifyClientRequest**](ModifyClientRequest.md)| The modified Client. First level parameters are managed in delta mode. | [optional] 

### Return type

[**ModifyClientResponse**](ModifyClientResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client modified. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

