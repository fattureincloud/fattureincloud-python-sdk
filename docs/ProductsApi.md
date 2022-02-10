# fattureincloud_python_sdk.ProductsApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product**](ProductsApi.md#create_product) | **POST** /c/{company_id}/products | Create Product
[**delete_product**](ProductsApi.md#delete_product) | **DELETE** /c/{company_id}/products/{product_id} | Delete Product
[**get_product**](ProductsApi.md#get_product) | **GET** /c/{company_id}/products/{product_id} | Get Product
[**list_products**](ProductsApi.md#list_products) | **GET** /c/{company_id}/products | List Products
[**modify_product**](ProductsApi.md#modify_product) | **PUT** /c/{company_id}/products/{product_id} | Modify Product


# **create_product**
> CreateProductResponse create_product(company_id)

Create Product

Creates a new product.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import products_api
from fattureincloud_python_sdk.model.create_product_request import CreateProductRequest
from fattureincloud_python_sdk.model.create_product_response import CreateProductResponse
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
    api_instance = products_api.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_product_request = CreateProductRequest(
        data=Product(
            id=1,
            name="name_example",
            code="code_example",
            net_price=3.14,
            gross_price=3.14,
            use_gross_price=True,
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
            net_cost=3.14,
            measure="measure_example",
            description="description_example",
            category="category_example",
            notes="notes_example",
            in_stock=True,
            stock_initial=3.14,
            average_cost=3.14,
            average_price=3.14,
            created_at="created_at_example",
            updated_at="updated_at_example",
        ),
    ) # CreateProductRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Product
        api_response = api_instance.create_product(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ProductsApi->create_product: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Product
        api_response = api_instance.create_product(company_id, create_product_request=create_product_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ProductsApi->create_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **create_product_request** | [**CreateProductRequest**](CreateProductRequest.md)|  | [optional]

### Return type

[**CreateProductResponse**](CreateProductResponse.md)

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

# **delete_product**
> delete_product(company_id, product_id)

Delete Product

Deletes the specified product.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    product_id = 1 # int | The ID of the product.

    # example passing only required values which don't have defaults set
    try:
        # Delete Product
        api_instance.delete_product(company_id, product_id)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ProductsApi->delete_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **product_id** | **int**| The ID of the product. |

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
**200** | Product removed. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> GetProductResponse get_product(company_id, product_id)

Get Product

Gets the specified product.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import products_api
from fattureincloud_python_sdk.model.get_product_response import GetProductResponse
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
    api_instance = products_api.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    product_id = 1 # int | The ID of the product.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Product
        api_response = api_instance.get_product(company_id, product_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_product: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Product
        api_response = api_instance.get_product(company_id, product_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **product_id** | **int**| The ID of the product. |
 **fields** | **str**| List of comma-separated fields. | [optional]
 **fieldset** | **str**| Name of the fieldset. | [optional]

### Return type

[**GetProductResponse**](GetProductResponse.md)

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

# **list_products**
> ListProductsResponse list_products(company_id)

List Products

Lists the products.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import products_api
from fattureincloud_python_sdk.model.list_products_response import ListProductsResponse
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
    api_instance = products_api.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)
    sort = "sort_example" # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) if omitted the server will use the default value of 1
    per_page = 5 # int | The size of the page. (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # List Products
        api_response = api_instance.list_products(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ProductsApi->list_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Products
        api_response = api_instance.list_products(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ProductsApi->list_products: %s\n" % e)
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

[**ListProductsResponse**](ListProductsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Products List. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_product**
> ModifyProductResponse modify_product(company_id, product_id)

Modify Product

Modifies the specified product.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import products_api
from fattureincloud_python_sdk.model.modify_product_response import ModifyProductResponse
from fattureincloud_python_sdk.model.modify_product_request import ModifyProductRequest
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
    api_instance = products_api.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    product_id = 1 # int | The ID of the product.
    modify_product_request = ModifyProductRequest(
        data=Product(
            id=1,
            name="name_example",
            code="code_example",
            net_price=3.14,
            gross_price=3.14,
            use_gross_price=True,
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
            net_cost=3.14,
            measure="measure_example",
            description="description_example",
            category="category_example",
            notes="notes_example",
            in_stock=True,
            stock_initial=3.14,
            average_cost=3.14,
            average_price=3.14,
            created_at="created_at_example",
            updated_at="updated_at_example",
        ),
    ) # ModifyProductRequest | Modified product details. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Product
        api_response = api_instance.modify_product(company_id, product_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ProductsApi->modify_product: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Product
        api_response = api_instance.modify_product(company_id, product_id, modify_product_request=modify_product_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling ProductsApi->modify_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. |
 **product_id** | **int**| The ID of the product. |
 **modify_product_request** | [**ModifyProductRequest**](ModifyProductRequest.md)| Modified product details. | [optional]

### Return type

[**ModifyProductResponse**](ModifyProductResponse.md)

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

