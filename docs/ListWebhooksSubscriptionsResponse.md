# ListWebhooksSubscriptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WebhooksSubscription]**](WebhooksSubscription.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_webhooks_subscriptions_response import ListWebhooksSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhooksSubscriptionsResponse from a JSON string
list_webhooks_subscriptions_response_instance = ListWebhooksSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print ListWebhooksSubscriptionsResponse.to_json()

# convert the object into a dict
list_webhooks_subscriptions_response_dict = list_webhooks_subscriptions_response_instance.to_dict()
# create an instance of ListWebhooksSubscriptionsResponse from a dict
list_webhooks_subscriptions_response_form_dict = list_webhooks_subscriptions_response.from_dict(list_webhooks_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


