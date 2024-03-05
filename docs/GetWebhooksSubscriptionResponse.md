# GetWebhooksSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhooksSubscription**](WebhooksSubscription.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_webhooks_subscription_response import GetWebhooksSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooksSubscriptionResponse from a JSON string
get_webhooks_subscription_response_instance = GetWebhooksSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print GetWebhooksSubscriptionResponse.to_json()

# convert the object into a dict
get_webhooks_subscription_response_dict = get_webhooks_subscription_response_instance.to_dict()
# create an instance of GetWebhooksSubscriptionResponse from a dict
get_webhooks_subscription_response_form_dict = get_webhooks_subscription_response.from_dict(get_webhooks_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


