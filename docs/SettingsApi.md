# fattureincloud_python_sdk.SettingsApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_account**](SettingsApi.md#create_payment_account) | **POST** /c/{company_id}/settings/payment_accounts | Create Payment Account
[**create_payment_method**](SettingsApi.md#create_payment_method) | **POST** /c/{company_id}/settings/payment_methods | Create Payment Method
[**create_vat_type**](SettingsApi.md#create_vat_type) | **POST** /c/{company_id}/settings/vat_types | Create Vat Type
[**delete_payment_account**](SettingsApi.md#delete_payment_account) | **DELETE** /c/{company_id}/settings/payment_accounts/{payment_account_id} | Delete Payment Account
[**delete_payment_method**](SettingsApi.md#delete_payment_method) | **DELETE** /c/{company_id}/settings/payment_methods/{payment_method_id} | Delete Payment Method
[**delete_vat_type**](SettingsApi.md#delete_vat_type) | **DELETE** /c/{company_id}/settings/vat_types/{vat_type_id} | Delete Vat Type
[**get_payment_account**](SettingsApi.md#get_payment_account) | **GET** /c/{company_id}/settings/payment_accounts/{payment_account_id} | Get Payment Account
[**get_payment_method**](SettingsApi.md#get_payment_method) | **GET** /c/{company_id}/settings/payment_methods/{payment_method_id} | Get Payment Method
[**get_vat_type**](SettingsApi.md#get_vat_type) | **GET** /c/{company_id}/settings/vat_types/{vat_type_id} | Get Vat Type
[**modify_payment_account**](SettingsApi.md#modify_payment_account) | **PUT** /c/{company_id}/settings/payment_accounts/{payment_account_id} | Modify Payment Account
[**modify_payment_method**](SettingsApi.md#modify_payment_method) | **PUT** /c/{company_id}/settings/payment_methods/{payment_method_id} | Modify Payment Method
[**modify_vat_type**](SettingsApi.md#modify_vat_type) | **PUT** /c/{company_id}/settings/vat_types/{vat_type_id} | Modify Vat Type


# **create_payment_account**
> CreatePaymentAccountResponse create_payment_account(company_id, create_payment_account_request=create_payment_account_request)

Create Payment Account

Creates a new payment account.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_payment_account_request import CreatePaymentAccountRequest
from fattureincloud_python_sdk.models.create_payment_account_response import CreatePaymentAccountResponse
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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_payment_account_request = {"data":{"id":12345,"name":"Indesa","type":"bank","iban":"IT17Q0051343200000003497636","sia":"T1234","virtual":false}} # CreatePaymentAccountRequest |  (optional)

    try:
        # Create Payment Account
        api_response = api_instance.create_payment_account(company_id, create_payment_account_request=create_payment_account_request)
        print("The response of SettingsApi->create_payment_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->create_payment_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **create_payment_account_request** | [**CreatePaymentAccountRequest**](CreatePaymentAccountRequest.md)|  | [optional] 

### Return type

[**CreatePaymentAccountResponse**](CreatePaymentAccountResponse.md)

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

# **create_payment_method**
> CreatePaymentMethodResponse create_payment_method(company_id, create_payment_method_request=create_payment_method_request)

Create Payment Method

Creates a new payment method.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_payment_method_request import CreatePaymentMethodRequest
from fattureincloud_python_sdk.models.create_payment_method_response import CreatePaymentMethodResponse
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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_payment_method_request = {"data":{"id":386683,"name":"Bonifico bancario","is_default":true,"type":"standard","details":[{"title":"Banca","description":"Sao Paulo"}],"default_payment_account":{"id":12345,"name":"conto banca SP"}}} # CreatePaymentMethodRequest |  (optional)

    try:
        # Create Payment Method
        api_response = api_instance.create_payment_method(company_id, create_payment_method_request=create_payment_method_request)
        print("The response of SettingsApi->create_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->create_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **create_payment_method_request** | [**CreatePaymentMethodRequest**](CreatePaymentMethodRequest.md)|  | [optional] 

### Return type

[**CreatePaymentMethodResponse**](CreatePaymentMethodResponse.md)

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

# **create_vat_type**
> CreateVatTypeResponse create_vat_type(company_id, create_vat_type_request=create_vat_type_request)

Create Vat Type

Creates a vat type.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_vat_type_request import CreateVatTypeRequest
from fattureincloud_python_sdk.models.create_vat_type_response import CreateVatTypeResponse
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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_vat_type_request = {"data":{"id":0,"value":22,"description":"Non imponibile art. 123","notes":"IVA non imponibile ai sensi dell'articolo 123, comma 2","e_invoice":true,"ei_type":2,"ei_description":"string","editable":true,"is_disabled":true}} # CreateVatTypeRequest |  (optional)

    try:
        # Create Vat Type
        api_response = api_instance.create_vat_type(company_id, create_vat_type_request=create_vat_type_request)
        print("The response of SettingsApi->create_vat_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->create_vat_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **create_vat_type_request** | [**CreateVatTypeRequest**](CreateVatTypeRequest.md)|  | [optional] 

### Return type

[**CreateVatTypeResponse**](CreateVatTypeResponse.md)

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

# **delete_payment_account**
> delete_payment_account(company_id, payment_account_id)

Delete Payment Account

Deletes the specified payment account.

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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_account_id = 56 # int | The Referred Payment Account Id.

    try:
        # Delete Payment Account
        api_instance.delete_payment_account(company_id, payment_account_id)
    except Exception as e:
        print("Exception when calling SettingsApi->delete_payment_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **payment_account_id** | **int**| The Referred Payment Account Id. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> delete_payment_method(company_id, payment_method_id)

Delete Payment Method

Deletes the specified payment method.

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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_method_id = 56 # int | The Referred Payment Method Id.

    try:
        # Delete Payment Method
        api_instance.delete_payment_method(company_id, payment_method_id)
    except Exception as e:
        print("Exception when calling SettingsApi->delete_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **payment_method_id** | **int**| The Referred Payment Method Id. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vat_type**
> delete_vat_type(company_id, vat_type_id)

Delete Vat Type

Deletes the specified vat type.

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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    vat_type_id = 56 # int | The Referred Vat Type Id.

    try:
        # Delete Vat Type
        api_instance.delete_vat_type(company_id, vat_type_id)
    except Exception as e:
        print("Exception when calling SettingsApi->delete_vat_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **vat_type_id** | **int**| The Referred Vat Type Id. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_account**
> GetPaymentAccountResponse get_payment_account(company_id, payment_account_id, fields=fields, fieldset=fieldset)

Get Payment Account

Gets the specified payment account.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_payment_account_response import GetPaymentAccountResponse
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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_account_id = 56 # int | The Referred Payment Account Id.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get Payment Account
        api_response = api_instance.get_payment_account(company_id, payment_account_id, fields=fields, fieldset=fieldset)
        print("The response of SettingsApi->get_payment_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_payment_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **payment_account_id** | **int**| The Referred Payment Account Id. | 
 **fields** | **str**| List of comma-separated fields. | [optional] 
 **fieldset** | **str**| Name of the fieldset. | [optional] 

### Return type

[**GetPaymentAccountResponse**](GetPaymentAccountResponse.md)

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

# **get_payment_method**
> GetPaymentMethodResponse get_payment_method(company_id, payment_method_id, fields=fields, fieldset=fieldset)

Get Payment Method

Gets the specified payment method.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_payment_method_response import GetPaymentMethodResponse
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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_method_id = 56 # int | The Referred Payment Method Id.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # Get Payment Method
        api_response = api_instance.get_payment_method(company_id, payment_method_id, fields=fields, fieldset=fieldset)
        print("The response of SettingsApi->get_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **payment_method_id** | **int**| The Referred Payment Method Id. | 
 **fields** | **str**| List of comma-separated fields. | [optional] 
 **fieldset** | **str**| Name of the fieldset. | [optional] 

### Return type

[**GetPaymentMethodResponse**](GetPaymentMethodResponse.md)

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

# **get_vat_type**
> GetVatTypeResponse get_vat_type(company_id, vat_type_id)

Get Vat Type

Gets the specified vat type.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_vat_type_response import GetVatTypeResponse
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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    vat_type_id = 56 # int | The Referred Vat Type Id.

    try:
        # Get Vat Type
        api_response = api_instance.get_vat_type(company_id, vat_type_id)
        print("The response of SettingsApi->get_vat_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_vat_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **vat_type_id** | **int**| The Referred Vat Type Id. | 

### Return type

[**GetVatTypeResponse**](GetVatTypeResponse.md)

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

# **modify_payment_account**
> ModifyPaymentAccountResponse modify_payment_account(company_id, payment_account_id, modify_payment_account_request=modify_payment_account_request)

Modify Payment Account

Modifies the specified payment account.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_payment_account_request import ModifyPaymentAccountRequest
from fattureincloud_python_sdk.models.modify_payment_account_response import ModifyPaymentAccountResponse
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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_account_id = 56 # int | The Referred Payment Account Id.
    modify_payment_account_request = {"data":{"id":0,"name":"Conto Banca Intesa","type":"standard","iban":"string","sia":"string","cuc":"string","virtual":true}} # ModifyPaymentAccountRequest |  (optional)

    try:
        # Modify Payment Account
        api_response = api_instance.modify_payment_account(company_id, payment_account_id, modify_payment_account_request=modify_payment_account_request)
        print("The response of SettingsApi->modify_payment_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->modify_payment_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **payment_account_id** | **int**| The Referred Payment Account Id. | 
 **modify_payment_account_request** | [**ModifyPaymentAccountRequest**](ModifyPaymentAccountRequest.md)|  | [optional] 

### Return type

[**ModifyPaymentAccountResponse**](ModifyPaymentAccountResponse.md)

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

# **modify_payment_method**
> ModifyPaymentMethodResponse modify_payment_method(company_id, payment_method_id, modify_payment_method_request=modify_payment_method_request)

Modify Payment Method

Modifies the specified payment method.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_payment_method_request import ModifyPaymentMethodRequest
from fattureincloud_python_sdk.models.modify_payment_method_response import ModifyPaymentMethodResponse
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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_method_id = 56 # int | The Referred Payment Method Id.
    modify_payment_method_request = {"data":{"id":386683,"name":"Bonifico bancario","is_default":true,"type":"standard","details":[{"title":"Banca","description":"Sao Paulo"}],"default_payment_account":{"id":12345,"name":"conto banca SP"}}} # ModifyPaymentMethodRequest |  (optional)

    try:
        # Modify Payment Method
        api_response = api_instance.modify_payment_method(company_id, payment_method_id, modify_payment_method_request=modify_payment_method_request)
        print("The response of SettingsApi->modify_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->modify_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **payment_method_id** | **int**| The Referred Payment Method Id. | 
 **modify_payment_method_request** | [**ModifyPaymentMethodRequest**](ModifyPaymentMethodRequest.md)|  | [optional] 

### Return type

[**ModifyPaymentMethodResponse**](ModifyPaymentMethodResponse.md)

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

# **modify_vat_type**
> ModifyVatTypeResponse modify_vat_type(company_id, vat_type_id, modify_vat_type_request=modify_vat_type_request)

Modify Vat Type

Modifies the specified vat type.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_vat_type_request import ModifyVatTypeRequest
from fattureincloud_python_sdk.models.modify_vat_type_response import ModifyVatTypeResponse
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
    api_instance = fattureincloud_python_sdk.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    vat_type_id = 56 # int | The Referred Vat Type Id.
    modify_vat_type_request = {"data":{"id":0,"value":22,"description":"Non imponibile art. 123","notes":"IVA non imponibile ai sensi dell'articolo 123, comma 2","e_invoice":true,"ei_type":2,"ei_description":"string","editable":true,"is_disabled":true}} # ModifyVatTypeRequest |  (optional)

    try:
        # Modify Vat Type
        api_response = api_instance.modify_vat_type(company_id, vat_type_id, modify_vat_type_request=modify_vat_type_request)
        print("The response of SettingsApi->modify_vat_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->modify_vat_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **vat_type_id** | **int**| The Referred Vat Type Id. | 
 **modify_vat_type_request** | [**ModifyVatTypeRequest**](ModifyVatTypeRequest.md)|  | [optional] 

### Return type

[**ModifyVatTypeResponse**](ModifyVatTypeResponse.md)

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

