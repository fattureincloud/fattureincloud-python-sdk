# CreateWebhooksSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhooksSubscription**](WebhooksSubscription.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_webhooks_subscription_request import CreateWebhooksSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhooksSubscriptionRequest from a JSON string
create_webhooks_subscription_request_instance = CreateWebhooksSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print CreateWebhooksSubscriptionRequest.to_json()

# convert the object into a dict
create_webhooks_subscription_request_dict = create_webhooks_subscription_request_instance.to_dict()
# create an instance of CreateWebhooksSubscriptionRequest from a dict
create_webhooks_subscription_request_form_dict = create_webhooks_subscription_request.from_dict(create_webhooks_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


