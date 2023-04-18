# ModifyWebhooksSubscriptionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhooksSubscription**](WebhooksSubscription.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_webhooks_subscription_request import ModifyWebhooksSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyWebhooksSubscriptionRequest from a JSON string
modify_webhooks_subscription_request_instance = ModifyWebhooksSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print ModifyWebhooksSubscriptionRequest.to_json()

# convert the object into a dict
modify_webhooks_subscription_request_dict = modify_webhooks_subscription_request_instance.to_dict()
# create an instance of ModifyWebhooksSubscriptionRequest from a dict
modify_webhooks_subscription_request_form_dict = modify_webhooks_subscription_request.from_dict(modify_webhooks_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


