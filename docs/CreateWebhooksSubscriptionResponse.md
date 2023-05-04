# CreateWebhooksSubscriptionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WebhooksSubscription**](WebhooksSubscription.md) |  | [optional] 
**warnings** | **List[str]** | Webhooks registration warnings | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_webhooks_subscription_response import CreateWebhooksSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhooksSubscriptionResponse from a JSON string
create_webhooks_subscription_response_instance = CreateWebhooksSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print CreateWebhooksSubscriptionResponse.to_json()

# convert the object into a dict
create_webhooks_subscription_response_dict = create_webhooks_subscription_response_instance.to_dict()
# create an instance of CreateWebhooksSubscriptionResponse from a dict
create_webhooks_subscription_response_form_dict = create_webhooks_subscription_response.from_dict(create_webhooks_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


