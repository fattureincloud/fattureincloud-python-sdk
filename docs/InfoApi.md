# fattureincloud_python_sdk.InfoApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_archive_categories**](InfoApi.md#list_archive_categories) | **GET** /c/{company_id}/info/archive_categories | List Archive Categories
[**list_cities**](InfoApi.md#list_cities) | **GET** /info/cities | List Cities
[**list_cost_centers**](InfoApi.md#list_cost_centers) | **GET** /c/{company_id}/info/cost_centers | List Cost Centers
[**list_countries**](InfoApi.md#list_countries) | **GET** /info/countries | List Countries
[**list_currencies**](InfoApi.md#list_currencies) | **GET** /info/currencies | List Currencies
[**list_delivery_notes_default_causals**](InfoApi.md#list_delivery_notes_default_causals) | **GET** /info/dn_causals | List Delivery Notes Default Causals
[**list_detailed_countries**](InfoApi.md#list_detailed_countries) | **GET** /info/detailed_countries | List Detailed Countries
[**list_languages**](InfoApi.md#list_languages) | **GET** /info/languages | List Languages
[**list_payment_accounts**](InfoApi.md#list_payment_accounts) | **GET** /c/{company_id}/info/payment_accounts | List Payment Accounts
[**list_payment_methods**](InfoApi.md#list_payment_methods) | **GET** /c/{company_id}/info/payment_methods | List Payment Methods
[**list_product_categories**](InfoApi.md#list_product_categories) | **GET** /c/{company_id}/info/product_categories | List Product Categories
[**list_received_document_categories**](InfoApi.md#list_received_document_categories) | **GET** /c/{company_id}/info/received_document_categories | List Received Document Categories
[**list_revenue_centers**](InfoApi.md#list_revenue_centers) | **GET** /c/{company_id}/info/revenue_centers | List Revenue Centers
[**list_templates**](InfoApi.md#list_templates) | **GET** /info/templates | List Templates
[**list_units_of_measure**](InfoApi.md#list_units_of_measure) | **GET** /info/measures | List Units of Measure
[**list_vat_types**](InfoApi.md#list_vat_types) | **GET** /c/{company_id}/info/vat_types | List Vat Types


# **list_archive_categories**
> ListArchiveCategoriesResponse list_archive_categories(company_id)

List Archive Categories

Lists the archive categories.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_archive_categories_response import ListArchiveCategoriesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    company_id = 12345 # int | The ID of the company.

    try:
        # List Archive Categories
        api_response = api_instance.list_archive_categories(company_id)
        print("The response of InfoApi->list_archive_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_archive_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 

### Return type

[**ListArchiveCategoriesResponse**](ListArchiveCategoriesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Archive Categories list. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cities**
> ListCitiesResponse list_cities(postal_code=postal_code, city=city)

List Cities

Lists the Italian cities.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_cities_response import ListCitiesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    postal_code = 'postal_code_example' # str | Postal code for filtering. (optional)
    city = 'city_example' # str | City for filtering (ignored if postal_code is passed). (optional)

    try:
        # List Cities
        api_response = api_instance.list_cities(postal_code=postal_code, city=city)
        print("The response of InfoApi->list_cities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_cities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_code** | **str**| Postal code for filtering. | [optional] 
 **city** | **str**| City for filtering (ignored if postal_code is passed). | [optional] 

### Return type

[**ListCitiesResponse**](ListCitiesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cities List. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cost_centers**
> ListCostCentersResponse list_cost_centers(company_id)

List Cost Centers

Lists the cost centers.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_cost_centers_response import ListCostCentersResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    company_id = 12345 # int | The ID of the company.

    try:
        # List Cost Centers
        api_response = api_instance.list_cost_centers(company_id)
        print("The response of InfoApi->list_cost_centers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_cost_centers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 

### Return type

[**ListCostCentersResponse**](ListCostCentersResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Cost Centers |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_countries**
> ListCountriesResponse list_countries()

List Countries

Lists the supported countries.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_countries_response import ListCountriesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)

    try:
        # List Countries
        api_response = api_instance.list_countries()
        print("The response of InfoApi->list_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_countries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCountriesResponse**](ListCountriesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of countries |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currencies**
> ListCurrenciesResponse list_currencies()

List Currencies

Lists the supported currencies.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_currencies_response import ListCurrenciesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)

    try:
        # List Currencies
        api_response = api_instance.list_currencies()
        print("The response of InfoApi->list_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_currencies: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCurrenciesResponse**](ListCurrenciesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currencies List. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_notes_default_causals**
> ListDeliveryNotesDefaultCausalsResponse list_delivery_notes_default_causals()

List Delivery Notes Default Causals

Lists the delivery note default causals.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_delivery_notes_default_causals_response import ListDeliveryNotesDefaultCausalsResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)

    try:
        # List Delivery Notes Default Causals
        api_response = api_instance.list_delivery_notes_default_causals()
        print("The response of InfoApi->list_delivery_notes_default_causals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_delivery_notes_default_causals: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDeliveryNotesDefaultCausalsResponse**](ListDeliveryNotesDefaultCausalsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Delivery Notes Default Causals |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_detailed_countries**
> ListDetailedCountriesResponse list_detailed_countries()

List Detailed Countries

Lists the supported countries.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_detailed_countries_response import ListDetailedCountriesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)

    try:
        # List Detailed Countries
        api_response = api_instance.list_detailed_countries()
        print("The response of InfoApi->list_detailed_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_detailed_countries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDetailedCountriesResponse**](ListDetailedCountriesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of detailed countries |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_languages**
> ListLanguagesResponse list_languages()

List Languages

Lists the supported languages.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_languages_response import ListLanguagesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)

    try:
        # List Languages
        api_response = api_instance.list_languages()
        print("The response of InfoApi->list_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_languages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListLanguagesResponse**](ListLanguagesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LanguagesList |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_accounts**
> ListPaymentAccountsResponse list_payment_accounts(company_id, fields=fields, fieldset=fieldset, sort=sort)

List Payment Accounts

Lists the available payment accounts.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_payment_accounts_response import ListPaymentAccountsResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)
    sort = 'sort_example' # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)

    try:
        # List Payment Accounts
        api_response = api_instance.list_payment_accounts(company_id, fields=fields, fieldset=fieldset, sort=sort)
        print("The response of InfoApi->list_payment_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_payment_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **fields** | **str**| List of comma-separated fields. | [optional] 
 **fieldset** | **str**| Name of the fieldset. | [optional] 
 **sort** | **str**| List of comma-separated fields for result sorting (minus for desc sorting). | [optional] 

### Return type

[**ListPaymentAccountsResponse**](ListPaymentAccountsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment accounts list. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_methods**
> ListPaymentMethodsResponse list_payment_methods(company_id, fields=fields, fieldset=fieldset, sort=sort)

List Payment Methods

Lists the available payment methods.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_payment_methods_response import ListPaymentMethodsResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fields = 'fields_example' # str | List of comma-separated fields. (optional)
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)
    sort = 'sort_example' # str | List of comma-separated fields for result sorting (minus for desc sorting). (optional)

    try:
        # List Payment Methods
        api_response = api_instance.list_payment_methods(company_id, fields=fields, fieldset=fieldset, sort=sort)
        print("The response of InfoApi->list_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_payment_methods: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **fields** | **str**| List of comma-separated fields. | [optional] 
 **fieldset** | **str**| Name of the fieldset. | [optional] 
 **sort** | **str**| List of comma-separated fields for result sorting (minus for desc sorting). | [optional] 

### Return type

[**ListPaymentMethodsResponse**](ListPaymentMethodsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment methods list. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product_categories**
> ListProductCategoriesResponse list_product_categories(company_id, context)

List Product Categories

Lists the product categories.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_product_categories_response import ListProductCategoriesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    company_id = 12345 # int | The ID of the company.
    context = 'context_example' # str | 

    try:
        # List Product Categories
        api_response = api_instance.list_product_categories(company_id, context)
        print("The response of InfoApi->list_product_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_product_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **context** | **str**|  | 

### Return type

[**ListProductCategoriesResponse**](ListProductCategoriesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product Categories List |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_received_document_categories**
> ListReceivedDocumentCategoriesResponse list_received_document_categories(company_id)

List Received Document Categories

Lists the received document categories.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_received_document_categories_response import ListReceivedDocumentCategoriesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    company_id = 12345 # int | The ID of the company.

    try:
        # List Received Document Categories
        api_response = api_instance.list_received_document_categories(company_id)
        print("The response of InfoApi->list_received_document_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_received_document_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 

### Return type

[**ListReceivedDocumentCategoriesResponse**](ListReceivedDocumentCategoriesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Received Document Categories List |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_revenue_centers**
> ListRevenueCentersResponse list_revenue_centers(company_id)

List Revenue Centers

Lists the revenue centers.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_revenue_centers_response import ListRevenueCentersResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    company_id = 12345 # int | The ID of the company.

    try:
        # List Revenue Centers
        api_response = api_instance.list_revenue_centers(company_id)
        print("The response of InfoApi->list_revenue_centers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_revenue_centers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 

### Return type

[**ListRevenueCentersResponse**](ListRevenueCentersResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Revenue Centers |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> ListTemplatesResponse list_templates(type=type, by_type=by_type)

List Templates

Lists the available templates.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_templates_response import ListTemplatesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    type = 'all' # str | Type of the templates. (optional) (default to 'all')
    by_type = False # bool | [Only if type=all] If true, splits the list in objects, grouping templates by type. (optional) (default to False)

    try:
        # List Templates
        api_response = api_instance.list_templates(type=type, by_type=by_type)
        print("The response of InfoApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of the templates. | [optional] [default to &#39;all&#39;]
 **by_type** | **bool**| [Only if type&#x3D;all] If true, splits the list in objects, grouping templates by type. | [optional] [default to False]

### Return type

[**ListTemplatesResponse**](ListTemplatesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Templates list. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_units_of_measure**
> ListUnitsOfMeasureResponse list_units_of_measure()

List Units of Measure

Lists the units of measure.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_units_of_measure_response import ListUnitsOfMeasureResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)

    try:
        # List Units of Measure
        api_response = api_instance.list_units_of_measure()
        print("The response of InfoApi->list_units_of_measure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_units_of_measure: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUnitsOfMeasureResponse**](ListUnitsOfMeasureResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Units of measure. |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vat_types**
> ListVatTypesResponse list_vat_types(company_id, fieldset=fieldset)

List Vat Types

Lists the available vat types.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_vat_types_response import ListVatTypesResponse
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
    api_instance = fattureincloud_python_sdk.InfoApi(api_client)
    company_id = 12345 # int | The ID of the company.
    fieldset = 'fieldset_example' # str | Name of the fieldset. (optional)

    try:
        # List Vat Types
        api_response = api_instance.list_vat_types(company_id, fieldset=fieldset)
        print("The response of InfoApi->list_vat_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->list_vat_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **fieldset** | **str**| Name of the fieldset. | [optional] 

### Return type

[**ListVatTypesResponse**](ListVatTypesResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Vat Types. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

