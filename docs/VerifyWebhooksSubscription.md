# VerifyWebhooksSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Webhooks subscription id | [optional] 
**verification_method** | [**WebhooksSubscriptionVerificationMethod**](WebhooksSubscriptionVerificationMethod.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.verify_webhooks_subscription import VerifyWebhooksSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebhooksSubscription from a JSON string
verify_webhooks_subscription_instance = VerifyWebhooksSubscription.from_json(json)
# print the JSON string representation of the object
print(VerifyWebhooksSubscription.to_json())

# convert the object into a dict
verify_webhooks_subscription_dict = verify_webhooks_subscription_instance.to_dict()
# create an instance of VerifyWebhooksSubscription from a dict
verify_webhooks_subscription_from_dict = VerifyWebhooksSubscription.from_dict(verify_webhooks_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


