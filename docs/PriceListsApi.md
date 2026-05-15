# fattureincloud_python_sdk.PriceListsApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_price_list_items**](PriceListsApi.md#get_price_list_items) | **GET** /c/{company_id}/price_lists/{price_list_id}/items | Get PriceList Items List
[**get_price_lists**](PriceListsApi.md#get_price_lists) | **GET** /c/{company_id}/price_lists | Get PriceLists


# **get_price_list_items**
> GetPriceListItemsResponse get_price_list_items(company_id, price_list_id)

Get PriceList Items List

Retrieves all the Items of a PriceList

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_price_list_items_response import GetPriceListItemsResponse
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
    api_instance = fattureincloud_python_sdk.PriceListsApi(api_client)
    company_id = 12345 # int | The ID of the company.
    price_list_id = 'price_list_id_example' # str | The ID of the price

    try:
        # Get PriceList Items List
        api_response = api_instance.get_price_list_items(company_id, price_list_id)
        print("The response of PriceListsApi->get_price_list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **price_list_id** | **str**| The ID of the price | 

### Return type

[**GetPriceListItemsResponse**](GetPriceListItemsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  * RateLimit-HourlyRemaining -  <br>  * RateLimit-HourlyLimit -  <br>  * RateLimit-MonthlyRemaining -  <br>  * RateLimit-MonthlyLimit -  <br>  |
**400** | ErrorResponse |  * Retry-After -  <br>  |
**401** | ErrorResponse |  * Retry-After -  <br>  |
**403** | ErrorResponse |  * Retry-After -  <br>  |
**404** | ErrorResponse |  * Retry-After -  <br>  |
**405** | ErrorResponse |  * Retry-After -  <br>  |
**409** | ErrorResponse |  * Retry-After -  <br>  |
**422** | ErrorResponse |  * Retry-After -  <br>  |
**429** | ErrorResponse |  * Retry-After -  <br>  |
**500** | ErrorResponse |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_lists**
> ListPriceListsResponse get_price_lists(company_id)

Get PriceLists

Retrieves all price lists of the company

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):

```python
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_price_lists_response import ListPriceListsResponse
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
    api_instance = fattureincloud_python_sdk.PriceListsApi(api_client)
    company_id = 12345 # int | The ID of the company.

    try:
        # Get PriceLists
        api_response = api_instance.get_price_lists(company_id)
        print("The response of PriceListsApi->get_price_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 

### Return type

[**ListPriceListsResponse**](ListPriceListsResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  * RateLimit-HourlyRemaining -  <br>  * RateLimit-HourlyLimit -  <br>  * RateLimit-MonthlyRemaining -  <br>  * RateLimit-MonthlyLimit -  <br>  |
**400** | ErrorResponse |  * Retry-After -  <br>  |
**401** | ErrorResponse |  * Retry-After -  <br>  |
**403** | ErrorResponse |  * Retry-After -  <br>  |
**404** | ErrorResponse |  * Retry-After -  <br>  |
**405** | ErrorResponse |  * Retry-After -  <br>  |
**409** | ErrorResponse |  * Retry-After -  <br>  |
**422** | ErrorResponse |  * Retry-After -  <br>  |
**429** | ErrorResponse |  * Retry-After -  <br>  |
**500** | ErrorResponse |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

