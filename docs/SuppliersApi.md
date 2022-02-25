# fattureincloud_python_sdk.SuppliersApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplier**](SuppliersApi.md#create_supplier) | **POST** /c/{company_id}/entities/suppliers | Create Supplier
[**delete_supplier**](SuppliersApi.md#delete_supplier) | **DELETE** /c/{company_id}/entities/suppliers/{supplier_id} | Delete Supplier
[**get_supplier**](SuppliersApi.md#get_supplier) | **GET** /c/{company_id}/entities/suppliers/{supplier_id} | Get Supplier
[**list_suppliers**](SuppliersApi.md#list_suppliers) | **GET** /c/{company_id}/entities/suppliers | List Suppliers
[**modify_supplier**](SuppliersApi.md#modify_supplier) | **PUT** /c/{company_id}/entities/suppliers/{supplier_id} | Modify Supplier


# **create_supplier**
> CreateSupplierResponse create_supplier(company_id)

Create Supplier

Creates a new supplier.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import suppliers_api
from fattureincloud_python_sdk.model.create_supplier_request import CreateSupplierRequest
from fattureincloud_python_sdk.model.create_supplier_response import CreateSupplierResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_supplier_request = CreateSupplierRequest(
        data=Supplier(
            id=1,
            code="123",
            name="Rossi S.r.l.",
            type=SupplierType("company"),
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
            created_at="created_at_example",
            updated_at="updated_at_example",
        ),
    ) # CreateSupplierRequest | The supplier to create (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Supplier
        api_response = api_instance.create_supplier(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->create_supplier: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Supplier
        api_response = api_instance.create_supplier(company_id, create_supplier_request=create_supplier_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->create_supplier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **create_supplier_request** | [**CreateSupplierRequest**](CreateSupplierRequest.md)| The supplier to create | [optional]

### Return type

[**CreateSupplierResponse**](CreateSupplierResponse.md)

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

# **delete_supplier**
> delete_supplier(company_id, supplier_id)

Delete Supplier

Deletes the specified supplier.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import suppliers_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    supplier_id = 1 # int | The ID of the supplier.

    # example passing only required values which don't have defaults set
    try:
        # Delete Supplier
        api_instance.delete_supplier(company_id, supplier_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->delete_supplier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **supplier_id** | **int**| The ID of the supplier. |

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

# **get_supplier**
> GetSupplierResponse get_supplier(company_id, supplier_id)

Get Supplier

Gets the specified supplier.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import suppliers_api
from fattureincloud_python_sdk.model.get_supplier_response import GetSupplierResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    supplier_id = 1 # int | The ID of the supplier.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Supplier
        api_response = api_instance.get_supplier(company_id, supplier_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->get_supplier: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Supplier
        api_response = api_instance.get_supplier(company_id, supplier_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->get_supplier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **supplier_id** | **int**| The ID of the supplier. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]

### Return type

[**GetSupplierResponse**](GetSupplierResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_suppliers**
> ListSuppliersResponse list_suppliers(company_id)

List Suppliers

Lists the suppliers.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import suppliers_api
from fattureincloud_python_sdk.model.list_suppliers_response import ListSuppliersResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)
    sort = "sort_example" # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) if omitted the server will use the default value of 1
    per_page = 5 # int | The size of the page. (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # List Suppliers
        api_response = api_instance.list_suppliers(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->list_suppliers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Suppliers
        api_response = api_instance.list_suppliers(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->list_suppliers: %s\n" % e)
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

[**ListSuppliersResponse**](ListSuppliersResponse.md)

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

# **modify_supplier**
> ModifySupplierResponse modify_supplier(company_id, supplier_id)

Modify Supplier

Modifies the specified supplier.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import suppliers_api
from fattureincloud_python_sdk.model.modify_supplier_request import ModifySupplierRequest
from fattureincloud_python_sdk.model.modify_supplier_response import ModifySupplierResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    supplier_id = 1 # int | The ID of the supplier.
    modify_supplier_request = ModifySupplierRequest(
        data=Supplier(
            id=1,
            code="123",
            name="Rossi S.r.l.",
            type=SupplierType("company"),
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
            created_at="created_at_example",
            updated_at="updated_at_example",
        ),
    ) # ModifySupplierRequest | The modified Supplier. First level parameters are managed in delta mode. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Supplier
        api_response = api_instance.modify_supplier(company_id, supplier_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->modify_supplier: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Supplier
        api_response = api_instance.modify_supplier(company_id, supplier_id, modify_supplier_request=modify_supplier_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->modify_supplier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **supplier_id** | **int**| The ID of the supplier. |
 **modify_supplier_request** | [**ModifySupplierRequest**](ModifySupplierRequest.md)| The modified Supplier. First level parameters are managed in delta mode. | [optional]

### Return type

[**ModifySupplierResponse**](ModifySupplierResponse.md)

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

