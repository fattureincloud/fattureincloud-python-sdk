# ModifyPaymentMethodRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_payment_method_request import ModifyPaymentMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPaymentMethodRequest from a JSON string
modify_payment_method_request_instance = ModifyPaymentMethodRequest.from_json(json)
# print the JSON string representation of the object
print(ModifyPaymentMethodRequest.to_json())

# convert the object into a dict
modify_payment_method_request_dict = modify_payment_method_request_instance.to_dict()
# create an instance of ModifyPaymentMethodRequest from a dict
modify_payment_method_request_from_dict = ModifyPaymentMethodRequest.from_dict(modify_payment_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


