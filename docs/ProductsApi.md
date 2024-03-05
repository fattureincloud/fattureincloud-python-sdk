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
> CreateProductResponse create_product(company_id, create_product_request=create_product_request)

Create Product

Creates a new product.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_product_request import CreateProductRequest
from fattureincloud_python_sdk.models.create_product_response import CreateProductResponse
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
    api_instance = fattureincloud_python_sdk.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_product_request = {"data":{"name":"Tavolo di marmo","code":"TAVOLO003","net_price":240,"net_cost":0,"measure":"","description":"Tavolo in marmo pregiato","category":"arredamento","in_stock":true,"default_vat":{"id":3,"value":22,"description":"Non imponibile art. 123","notes":"IVA non imponibile ai sensi dell'articolo 123, comma 2","is_disabled":false}}} # CreateProductRequest |  (optional)

    try:
        # Create Product
        api_response = api_instance.create_product(company_id, create_product_request=create_product_request)
        print("The response of ProductsApi->create_product:\n")
        pprint(api_response)
    except Exception as e:
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
    api_instance = fattureincloud_python_sdk.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    product_id = 56 # int | The ID of the product.

    try:
        # Delete Product
        api_instance.delete_product(company_id, product_id)
    except Exception as e:
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
> GetProductResponse get_product(company_id, product_id, fields=fields, fieldset=fieldset)

Get Product

Gets the specified product.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_product_response import GetProductResponse
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
    api_instance = fattureincloud_python_sdk.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    product_id = 56 # int | The ID of the product.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get Product
        api_response = api_instance.get_product(company_id, product_id, fields=fields, fieldset=fieldset)
        print("The response of ProductsApi->get_product:\n")
        pprint(api_response)
    except Exception as e:
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
> ListProductsResponse list_products(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)

List Products

Lists the products.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_products_response import ListProductsResponse
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
    api_instance = fattureincloud_python_sdk.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)
    sort = 'sort_example' # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) (default to 1)
    per_page = 5 # int | The size of the page. (optional) (default to 5)
    q = 'q_example' # str | Query for filtering the results. (optional)

    try:
        # List Products
        api_response = api_instance.list_products(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)
        print("The response of ProductsApi->list_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->list_products: %s\n" % e)
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
> ModifyProductResponse modify_product(company_id, product_id, modify_product_request=modify_product_request)

Modify Product

Modifies the specified product.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_product_request import ModifyProductRequest
from fattureincloud_python_sdk.models.modify_product_response import ModifyProductResponse
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
    api_instance = fattureincloud_python_sdk.ProductsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    product_id = 56 # int | The ID of the product.
    modify_product_request = {"data":{"name":"Tavolo di marmo","code":"TAVOLO003","net_price":240,"net_cost":0,"measure":"","description":"Tavolo in marmo pregiato","category":"arredamento","in_stock":true,"default_vat":{"id":3,"value":22,"description":"Non imponibile art. 123","notes":"IVA non imponibile ai sensi dell'articolo 123, comma 2","is_disabled":false}}} # ModifyProductRequest | Modified product details. (optional)

    try:
        # Modify Product
        api_response = api_instance.modify_product(company_id, product_id, modify_product_request=modify_product_request)
        print("The response of ProductsApi->modify_product:\n")
        pprint(api_response)
    except Exception as e:
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

