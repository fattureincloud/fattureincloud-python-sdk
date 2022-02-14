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
> CreateClientResponse create_client(company_id)

Create Client

Creates a new client.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import clients_api
from fattureincloud_python_sdk.model.create_client_request import CreateClientRequest
from fattureincloud_python_sdk.model.create_client_response import CreateClientResponse
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
    api_instance = clients_api.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_client_request = CreateClientRequest(
        data=Client(
            id=1,
            code="123",
            name="Rossi S.r.l.",
            type=ClientType("company"),
            first_name="first_name_example",
            last_name="last_name_example",
            contact_person="contact_person_example",
            vat_number="IT01234567890",
            tax_code="RSSMRA44A12E890Q",
            address_street="Via dei tigli, 12",
            address_postal_code="24010",
            address_city="Bergamo",
            address_province="BG",
            address_extra="address_extra_example",
            country="Italia",
            email="mario.rossi@example.it",
            certified_email="mario.rossi@pec.example.it",
            phone="phone_example",
            fax="fax_example",
            notes="notes_example",
            default_vat=VatType(
                id=1,
                value=22,
                description="Non imponibile art. 123",
                notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                e_invoice=True,
                ei_type="2",
                ei_description="ei_description_example",
                is_disabled=True,
            ),
            default_payment_terms=30,
            default_payment_terms_type=DefaultPaymentTermsType("standard"),
            default_payment_method=PaymentMethod(
                id=1,
                name="name_example",
                type=PaymentMethodType("standard"),
                is_default=True,
                default_payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                details=[
                    PaymentMethodDetails(
                        title="title_example",
                        description="description_example",
                    ),
                ],
                bank_iban="bank_iban_example",
                bank_name="bank_name_example",
                bank_beneficiary="bank_beneficiary_example",
                ei_payment_method="ei_payment_method_example",
            ),
            bank_name="bank_name_example",
            bank_iban="bank_iban_example",
            bank_swift_code="bank_swift_code_example",
            shipping_address="shipping_address_example",
            e_invoice=True,
            ei_code="ei_code_example",
            discount_highlight=True,
            default_discount=3.14,
            created_at="created_at_example",
            updated_at="updated_at_example",
        ),
    ) # CreateClientRequest | The client to create (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Client
        api_response = api_instance.create_client(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ClientsApi->create_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Client
        api_response = api_instance.create_client(company_id, create_client_request=create_client_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    client_id = 1 # int | The ID of the client.

    # example passing only required values which don't have defaults set
    try:
        # Delete Client
        api_instance.delete_client(company_id, client_id)
    except fattureincloud_python_sdk.ApiException as e:
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
> GetClientResponse get_client(company_id, client_id)

Get Client

Gets the specified client.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import clients_api
from fattureincloud_python_sdk.model.get_client_response import GetClientResponse
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
    api_instance = clients_api.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    client_id = 1 # int | The ID of the client.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Client
        api_response = api_instance.get_client(company_id, client_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ClientsApi->get_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Client
        api_response = api_instance.get_client(company_id, client_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
> ListClientsResponse list_clients(company_id)

List Clients

Lists the clients.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import clients_api
from fattureincloud_python_sdk.model.list_clients_response import ListClientsResponse
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
    api_instance = clients_api.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)
    sort = "sort_example" # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) if omitted the server will use the default value of 1
    per_page = 5 # int | The size of the page. (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # List Clients
        api_response = api_instance.list_clients(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ClientsApi->list_clients: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Clients
        api_response = api_instance.list_clients(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ClientsApi->list_clients: %s\n" % e)
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
> ModifyClientResponse modify_client(company_id, client_id)

Modify Client

Modifies the specified client.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import clients_api
from fattureincloud_python_sdk.model.modify_client_response import ModifyClientResponse
from fattureincloud_python_sdk.model.modify_client_request import ModifyClientRequest
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
    api_instance = clients_api.ClientsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    client_id = 1 # int | The ID of the client.
    modify_client_request = ModifyClientRequest(
        data=Client(
            id=1,
            code="123",
            name="Rossi S.r.l.",
            type=ClientType("company"),
            first_name="first_name_example",
            last_name="last_name_example",
            contact_person="contact_person_example",
            vat_number="IT01234567890",
            tax_code="RSSMRA44A12E890Q",
            address_street="Via dei tigli, 12",
            address_postal_code="24010",
            address_city="Bergamo",
            address_province="BG",
            address_extra="address_extra_example",
            country="Italia",
            email="mario.rossi@example.it",
            certified_email="mario.rossi@pec.example.it",
            phone="phone_example",
            fax="fax_example",
            notes="notes_example",
            default_vat=VatType(
                id=1,
                value=22,
                description="Non imponibile art. 123",
                notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
                e_invoice=True,
                ei_type="2",
                ei_description="ei_description_example",
                is_disabled=True,
            ),
            default_payment_terms=30,
            default_payment_terms_type=DefaultPaymentTermsType("standard"),
            default_payment_method=PaymentMethod(
                id=1,
                name="name_example",
                type=PaymentMethodType("standard"),
                is_default=True,
                default_payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                details=[
                    PaymentMethodDetails(
                        title="title_example",
                        description="description_example",
                    ),
                ],
                bank_iban="bank_iban_example",
                bank_name="bank_name_example",
                bank_beneficiary="bank_beneficiary_example",
                ei_payment_method="ei_payment_method_example",
            ),
            bank_name="bank_name_example",
            bank_iban="bank_iban_example",
            bank_swift_code="bank_swift_code_example",
            shipping_address="shipping_address_example",
            e_invoice=True,
            ei_code="ei_code_example",
            discount_highlight=True,
            default_discount=3.14,
            created_at="created_at_example",
            updated_at="updated_at_example",
        ),
    ) # ModifyClientRequest | The modified Client. First level parameters are managed in delta mode. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Client
        api_response = api_instance.modify_client(company_id, client_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ClientsApi->modify_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Client
        api_response = api_instance.modify_client(company_id, client_id, modify_client_request=modify_client_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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

