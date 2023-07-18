# fattureincloud_python_sdk.WebhooksApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhooks_subscription**](WebhooksApi.md#create_webhooks_subscription) | **POST** /c/{company_id}/subscriptions | Create a Webhook Subscription
[**delete_webhooks_subscription**](WebhooksApi.md#delete_webhooks_subscription) | **DELETE** /c/{company_id}/subscriptions/{subscription_id} | Delete Webhooks Subscription
[**get_webhooks_subscription**](WebhooksApi.md#get_webhooks_subscription) | **GET** /c/{company_id}/subscriptions/{subscription_id} | Get Webhooks Subscription
[**list_webhooks_subscriptions**](WebhooksApi.md#list_webhooks_subscriptions) | **GET** /c/{company_id}/subscriptions | List Webhooks Subscriptions
[**modify_webhooks_subscription**](WebhooksApi.md#modify_webhooks_subscription) | **PUT** /c/{company_id}/subscriptions/{subscription_id} | Modify Webhooks Subscription


# **create_webhooks_subscription**
> CreateWebhooksSubscriptionResponse create_webhooks_subscription(company_id, create_webhooks_subscription_request=create_webhooks_subscription_request)

Create a Webhook Subscription

Register some webhooks Subscriptions.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.create_webhooks_subscription_request import CreateWebhooksSubscriptionRequest
from fattureincloud_python_sdk.models.create_webhooks_subscription_response import CreateWebhooksSubscriptionResponse
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
    api_instance = fattureincloud_python_sdk.WebhooksApi(api_client)
    company_id = 12345 # int | The ID of the company.
    create_webhooks_subscription_request = {"data":{"sink":"http://www.test.com","types":["it.fattureincloud.webhooks.entities.create","it.fattureincloud.webhooks.issued_documents.create"]}} # CreateWebhooksSubscriptionRequest |  (optional)

    try:
        # Create a Webhook Subscription
        api_response = api_instance.create_webhooks_subscription(company_id, create_webhooks_subscription_request=create_webhooks_subscription_request)
        print("The response of WebhooksApi->create_webhooks_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhooks_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **create_webhooks_subscription_request** | [**CreateWebhooksSubscriptionRequest**](CreateWebhooksSubscriptionRequest.md)|  | [optional] 

### Return type

[**CreateWebhooksSubscriptionResponse**](CreateWebhooksSubscriptionResponse.md)

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

# **delete_webhooks_subscription**
> delete_webhooks_subscription(company_id, subscription_id)

Delete Webhooks Subscription

Delete a webhooks subscription.

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
    api_instance = fattureincloud_python_sdk.WebhooksApi(api_client)
    company_id = 12345 # int | The ID of the company.
    subscription_id = 'SUB123' # str | The ID of the subscription.

    try:
        # Delete Webhooks Subscription
        api_instance.delete_webhooks_subscription(company_id, subscription_id)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhooks_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **subscription_id** | **str**| The ID of the subscription. | 

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

# **get_webhooks_subscription**
> GetWebhooksSubscriptionResponse get_webhooks_subscription(company_id, subscription_id)

Get Webhooks Subscription

Get a webhooks subscription.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.get_webhooks_subscription_response import GetWebhooksSubscriptionResponse
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
    api_instance = fattureincloud_python_sdk.WebhooksApi(api_client)
    company_id = 12345 # int | The ID of the company.
    subscription_id = 'SUB123' # str | The ID of the subscription.

    try:
        # Get Webhooks Subscription
        api_response = api_instance.get_webhooks_subscription(company_id, subscription_id)
        print("The response of WebhooksApi->get_webhooks_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhooks_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **subscription_id** | **str**| The ID of the subscription. | 

### Return type

[**GetWebhooksSubscriptionResponse**](GetWebhooksSubscriptionResponse.md)

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

# **list_webhooks_subscriptions**
> ListWebhooksSubscriptionsResponse list_webhooks_subscriptions(company_id)

List Webhooks Subscriptions

List active webhooks subscriptions.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.list_webhooks_subscriptions_response import ListWebhooksSubscriptionsResponse
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
    api_instance = fattureincloud_python_sdk.WebhooksApi(api_client)
    company_id = 12345 # int | The ID of the company.

    try:
        # List Webhooks Subscriptions
        api_response = api_instance.list_webhooks_subscriptions(company_id)
        print("The response of WebhooksApi->list_webhooks_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhooks_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 

### Return type

[**ListWebhooksSubscriptionsResponse**](ListWebhooksSubscriptionsResponse.md)

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

# **modify_webhooks_subscription**
> ModifyWebhooksSubscriptionResponse modify_webhooks_subscription(company_id, subscription_id, modify_webhooks_subscription_request=modify_webhooks_subscription_request)

Modify Webhooks Subscription

Edit a webhooks subscription.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.modify_webhooks_subscription_request import ModifyWebhooksSubscriptionRequest
from fattureincloud_python_sdk.models.modify_webhooks_subscription_response import ModifyWebhooksSubscriptionResponse
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
    api_instance = fattureincloud_python_sdk.WebhooksApi(api_client)
    company_id = 12345 # int | The ID of the company.
    subscription_id = 'SUB123' # str | The ID of the subscription.
    modify_webhooks_subscription_request = fattureincloud_python_sdk.ModifyWebhooksSubscriptionRequest() # ModifyWebhooksSubscriptionRequest |  (optional)

    try:
        # Modify Webhooks Subscription
        api_response = api_instance.modify_webhooks_subscription(company_id, subscription_id, modify_webhooks_subscription_request=modify_webhooks_subscription_request)
        print("The response of WebhooksApi->modify_webhooks_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->modify_webhooks_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **subscription_id** | **str**| The ID of the subscription. | 
 **modify_webhooks_subscription_request** | [**ModifyWebhooksSubscriptionRequest**](ModifyWebhooksSubscriptionRequest.md)|  | [optional] 

### Return type

[**ModifyWebhooksSubscriptionResponse**](ModifyWebhooksSubscriptionResponse.md)

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

