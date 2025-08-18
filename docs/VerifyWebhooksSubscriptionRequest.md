# VerifyWebhooksSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VerifyWebhooksSubscription**](VerifyWebhooksSubscription.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.verify_webhooks_subscription_request import VerifyWebhooksSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebhooksSubscriptionRequest from a JSON string
verify_webhooks_subscription_request_instance = VerifyWebhooksSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyWebhooksSubscriptionRequest.to_json())

# convert the object into a dict
verify_webhooks_subscription_request_dict = verify_webhooks_subscription_request_instance.to_dict()
# create an instance of VerifyWebhooksSubscriptionRequest from a dict
verify_webhooks_subscription_request_from_dict = VerifyWebhooksSubscriptionRequest.from_dict(verify_webhooks_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


