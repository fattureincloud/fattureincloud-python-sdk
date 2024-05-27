# ModifyWebhooksSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhooksSubscription**](WebhooksSubscription.md) |  | [optional] 
**warnings** | **List[str]** | Webhooks registration warnings | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_webhooks_subscription_response import ModifyWebhooksSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyWebhooksSubscriptionResponse from a JSON string
modify_webhooks_subscription_response_instance = ModifyWebhooksSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyWebhooksSubscriptionResponse.to_json())

# convert the object into a dict
modify_webhooks_subscription_response_dict = modify_webhooks_subscription_response_instance.to_dict()
# create an instance of ModifyWebhooksSubscriptionResponse from a dict
modify_webhooks_subscription_response_from_dict = ModifyWebhooksSubscriptionResponse.from_dict(modify_webhooks_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


