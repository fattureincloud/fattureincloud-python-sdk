# WebhooksSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier | [optional] 
**sink** | **str** | Webhooks callback uri. | [optional] 
**verified** | **bool** | [Read Only] True if the webhooks subscription has been verified. | [optional] 
**types** | [**List[EventType]**](EventType.md) | Webhooks events types. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.webhooks_subscription import WebhooksSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksSubscription from a JSON string
webhooks_subscription_instance = WebhooksSubscription.from_json(json)
# print the JSON string representation of the object
print WebhooksSubscription.to_json()

# convert the object into a dict
webhooks_subscription_dict = webhooks_subscription_instance.to_dict()
# create an instance of WebhooksSubscription from a dict
webhooks_subscription_form_dict = webhooks_subscription.from_dict(webhooks_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


