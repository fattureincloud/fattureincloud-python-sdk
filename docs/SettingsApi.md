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
> CreatePaymentAccountResponse create_payment_account(company_id)

Create Payment Account

Creates a new payment account.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from fattureincloud_python_sdk.model.create_payment_account_response import CreatePaymentAccountResponse
from fattureincloud_python_sdk.model.create_payment_account_request import CreatePaymentAccountRequest
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_payment_account_request = CreatePaymentAccountRequest(
        data=PaymentAccount(
            id=1,
            name="Conto Banca Intesa",
            type=PaymentAccountType("standard"),
            iban="iban_example",
            sia="sia_example",
            cuc="cuc_example",
            virtual=True,
        ),
    ) # CreatePaymentAccountRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Payment Account
        api_response = api_instance.create_payment_account(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->create_payment_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Payment Account
        api_response = api_instance.create_payment_account(company_id, create_payment_account_request=create_payment_account_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
> CreatePaymentMethodResponse create_payment_method(company_id)

Create Payment Method

Creates a new payment method.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from fattureincloud_python_sdk.model.create_payment_method_response import CreatePaymentMethodResponse
from fattureincloud_python_sdk.model.create_payment_method_request import CreatePaymentMethodRequest
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_payment_method_request = CreatePaymentMethodRequest(
        data=PaymentMethod(
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
    ) # CreatePaymentMethodRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Payment Method
        api_response = api_instance.create_payment_method(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->create_payment_method: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Payment Method
        api_response = api_instance.create_payment_method(company_id, create_payment_method_request=create_payment_method_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
> CreateVatTypeResponse create_vat_type(company_id)

Create Vat Type

Creates a vat type.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from fattureincloud_python_sdk.model.create_vat_type_response import CreateVatTypeResponse
from fattureincloud_python_sdk.model.create_vat_type_request import CreateVatTypeRequest
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_vat_type_request = CreateVatTypeRequest(
        data=VatType(
            id=1,
            value=22,
            description="Non imponibile art. 123",
            notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
            e_invoice=True,
            ei_type="2",
            ei_description="ei_description_example",
            is_disabled=True,
        ),
    ) # CreateVatTypeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Vat Type
        api_response = api_instance.create_vat_type(company_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->create_vat_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Vat Type
        api_response = api_instance.create_vat_type(company_id, create_vat_type_request=create_vat_type_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_account_id = 1 # int | The Referred Payment Account Id.

    # example passing only required values which don't have defaults set
    try:
        # Delete Payment Account
        api_instance.delete_payment_account(company_id, payment_account_id)
    except fattureincloud_python_sdk.ApiException as e:
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
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_method_id = 1 # int | The Referred Payment Method Id.

    # example passing only required values which don't have defaults set
    try:
        # Delete Payment Method
        api_instance.delete_payment_method(company_id, payment_method_id)
    except fattureincloud_python_sdk.ApiException as e:
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
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    vat_type_id = 1 # int | The Referred Vat Type Id.

    # example passing only required values which don't have defaults set
    try:
        # Delete Vat Type
        api_instance.delete_vat_type(company_id, vat_type_id)
    except fattureincloud_python_sdk.ApiException as e:
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
> GetPaymentAccountResponse get_payment_account(company_id, payment_account_id)

Get Payment Account

Gets the specified payment account.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from fattureincloud_python_sdk.model.get_payment_account_response import GetPaymentAccountResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_account_id = 1 # int | The Referred Payment Account Id.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Payment Account
        api_response = api_instance.get_payment_account(company_id, payment_account_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->get_payment_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payment Account
        api_response = api_instance.get_payment_account(company_id, payment_account_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
> GetPaymentMethodResponse get_payment_method(company_id, payment_method_id)

Get Payment Method

Gets the specified payment method.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from fattureincloud_python_sdk.model.get_payment_method_response import GetPaymentMethodResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_method_id = 1 # int | The Referred Payment Method Id.
    fields = "fields_example" # str | List of comma-separated fields. (optional)
    fieldset = "basic" # str | Name of the fieldset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Payment Method
        api_response = api_instance.get_payment_method(company_id, payment_method_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->get_payment_method: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payment Method
        api_response = api_instance.get_payment_method(company_id, payment_method_id, fields=fields, fieldset=fieldset)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from fattureincloud_python_sdk.model.get_vat_type_response import GetVatTypeResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    vat_type_id = 1 # int | The Referred Vat Type Id.

    # example passing only required values which don't have defaults set
    try:
        # Get Vat Type
        api_response = api_instance.get_vat_type(company_id, vat_type_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
> ModifyPaymentAccountResponse modify_payment_account(company_id, payment_account_id)

Modify Payment Account

Modifies the specified payment account.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from fattureincloud_python_sdk.model.modify_payment_account_request import ModifyPaymentAccountRequest
from fattureincloud_python_sdk.model.modify_payment_account_response import ModifyPaymentAccountResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_account_id = 1 # int | The Referred Payment Account Id.
    modify_payment_account_request = ModifyPaymentAccountRequest(
        data=PaymentAccount(
            id=1,
            name="Conto Banca Intesa",
            type=PaymentAccountType("standard"),
            iban="iban_example",
            sia="sia_example",
            cuc="cuc_example",
            virtual=True,
        ),
    ) # ModifyPaymentAccountRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Payment Account
        api_response = api_instance.modify_payment_account(company_id, payment_account_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->modify_payment_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Payment Account
        api_response = api_instance.modify_payment_account(company_id, payment_account_id, modify_payment_account_request=modify_payment_account_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
> ModifyPaymentMethodResponse modify_payment_method(company_id, payment_method_id)

Modify Payment Method

Modifies the specified payment method.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from fattureincloud_python_sdk.model.modify_payment_method_request import ModifyPaymentMethodRequest
from fattureincloud_python_sdk.model.modify_payment_method_response import ModifyPaymentMethodResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    payment_method_id = 1 # int | The Referred Payment Method Id.
    modify_payment_method_request = ModifyPaymentMethodRequest(
        data=PaymentMethod(
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
    ) # ModifyPaymentMethodRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Payment Method
        api_response = api_instance.modify_payment_method(company_id, payment_method_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->modify_payment_method: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Payment Method
        api_response = api_instance.modify_payment_method(company_id, payment_method_id, modify_payment_method_request=modify_payment_method_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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
> ModifyVatTypeResponse modify_vat_type(company_id, vat_type_id)

Modify Vat Type

Modifies the specified vat type.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import time
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api import settings_api
from fattureincloud_python_sdk.model.modify_vat_type_request import ModifyVatTypeRequest
from fattureincloud_python_sdk.model.modify_vat_type_response import ModifyVatTypeResponse
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2AuthenticationCodeFlow
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    vat_type_id = 1 # int | The Referred Vat Type Id.
    modify_vat_type_request = ModifyVatTypeRequest(
        data=VatType(
            id=1,
            value=22,
            description="Non imponibile art. 123",
            notes="IVA non imponibile ai sensi dell'articolo 123, comma 2",
            e_invoice=True,
            ei_type="2",
            ei_description="ei_description_example",
            is_disabled=True,
        ),
    ) # ModifyVatTypeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify Vat Type
        api_response = api_instance.modify_vat_type(company_id, vat_type_id)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->modify_vat_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify Vat Type
        api_response = api_instance.modify_vat_type(company_id, vat_type_id, modify_vat_type_request=modify_vat_type_request)
        pprint(api_response)
    except fattureincloud_python_sdk.ApiException as e:
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

