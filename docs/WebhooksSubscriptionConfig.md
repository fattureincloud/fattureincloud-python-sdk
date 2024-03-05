# WebhooksSubscriptionConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**WebhooksSubscriptionMapping**](WebhooksSubscriptionMapping.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.webhooks_subscription_config import WebhooksSubscriptionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksSubscriptionConfig from a JSON string
webhooks_subscription_config_instance = WebhooksSubscriptionConfig.from_json(json)
# print the JSON string representation of the object
print WebhooksSubscriptionConfig.to_json()

# convert the object into a dict
webhooks_subscription_config_dict = webhooks_subscription_config_instance.to_dict()
# create an instance of WebhooksSubscriptionConfig from a dict
webhooks_subscription_config_form_dict = webhooks_subscription_config.from_dict(webhooks_subscription_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


