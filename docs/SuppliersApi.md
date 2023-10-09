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
> CreateSupplierResponse create_supplier(company_id, create_supplier_request=create_supplier_request)

Create Supplier

Creates a new supplier.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_supplier_request import CreateSupplierRequest
from fattureincloud_python_sdk.models.create_supplier_response import CreateSupplierResponse
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
    api_instance = fattureincloud_python_sdk.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_supplier_request = {"data":{"id":12345,"code":"AE86","name":"Mario Rossi S.R.L.","type":"company","first_name":"Mario","last_name":"Rossi","contact_person":"","vat_number":"111222333","tax_code":"111122233","address_street":"Corso Magellano, 46","address_postal_code":"20146","address_city":"Milano","address_province":"MI","address_extra":"","country":"Italia","email":"mario.rossi@example.com","certified_email":"mario.rossi@pec.example.com","phone":"1234567890","fax":"123456789","notes":""}} # CreateSupplierRequest | The supplier to create (optional)

    try:
        # Create Supplier
        api_response = api_instance.create_supplier(company_id, create_supplier_request=create_supplier_request)
        print("The response of SuppliersApi->create_supplier:\n")
        pprint(api_response)
    except Exception as e:
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
    api_instance = fattureincloud_python_sdk.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    supplier_id = 56 # int | The ID of the supplier.

    try:
        # Delete Supplier
        api_instance.delete_supplier(company_id, supplier_id)
    except Exception as e:
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
> GetSupplierResponse get_supplier(company_id, supplier_id, fields=fields, fieldset=fieldset)

Get Supplier

Gets the specified supplier.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_supplier_response import GetSupplierResponse
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
    api_instance = fattureincloud_python_sdk.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    supplier_id = 56 # int | The ID of the supplier.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get Supplier
        api_response = api_instance.get_supplier(company_id, supplier_id, fields=fields, fieldset=fieldset)
        print("The response of SuppliersApi->get_supplier:\n")
        pprint(api_response)
    except Exception as e:
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
> ListSuppliersResponse list_suppliers(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)

List Suppliers

Lists the suppliers.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_suppliers_response import ListSuppliersResponse
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
    api_instance = fattureincloud_python_sdk.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)
    sort = 'sort_example' # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)
    page = 1 # int | The page to retrieve. (optional) (default to 1)
    per_page = 5 # int | The size of the page. (optional) (default to 5)
    q = 'q_example' # str | Query for filtering the results. (optional)

    try:
        # List Suppliers
        api_response = api_instance.list_suppliers(company_id, fields=fields, fieldset=fieldset, sort=sort, page=page, per_page=per_page, q=q)
        print("The response of SuppliersApi->list_suppliers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppliersApi->list_suppliers: %s\n" % e)
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
> ModifySupplierResponse modify_supplier(company_id, supplier_id, modify_supplier_request=modify_supplier_request)

Modify Supplier

Modifies the specified supplier.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_supplier_request import ModifySupplierRequest
from fattureincloud_python_sdk.models.modify_supplier_response import ModifySupplierResponse
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
    api_instance = fattureincloud_python_sdk.SuppliersApi(api_client)
    company_id = 12345 # int | The ID of the company.
    supplier_id = 56 # int | The ID of the supplier.
    modify_supplier_request = {"data":{"id":12345,"code":"AE86","name":"Mario Rossi S.R.L.","type":"company","first_name":"Mario","last_name":"Rossi","contact_person":"","vat_number":"111222333","tax_code":"111122233","address_street":"Corso Magellano, 46","address_postal_code":"20146","address_city":"Milano","address_province":"MI","address_extra":"","country":"Italia","email":"mario.rossi@example.com","certified_email":"mario.rossi@pec.example.com","phone":"1234567890","fax":"123456789","notes":""}} # ModifySupplierRequest | The modified Supplier. First level parameters are managed in delta mode. (optional)

    try:
        # Modify Supplier
        api_response = api_instance.modify_supplier(company_id, supplier_id, modify_supplier_request=modify_supplier_request)
        print("The response of SuppliersApi->modify_supplier:\n")
        pprint(api_response)
    except Exception as e:
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

