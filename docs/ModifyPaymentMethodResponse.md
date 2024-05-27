# ModifyPaymentMethodResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_payment_method_response import ModifyPaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPaymentMethodResponse from a JSON string
modify_payment_method_response_instance = ModifyPaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyPaymentMethodResponse.to_json())

# convert the object into a dict
modify_payment_method_response_dict = modify_payment_method_response_instance.to_dict()
# create an instance of ModifyPaymentMethodResponse from a dict
modify_payment_method_response_from_dict = ModifyPaymentMethodResponse.from_dict(modify_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


