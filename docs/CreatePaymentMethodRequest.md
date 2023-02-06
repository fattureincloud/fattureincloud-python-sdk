# CreatePaymentMethodRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_payment_method_request import CreatePaymentMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentMethodRequest from a JSON string
create_payment_method_request_instance = CreatePaymentMethodRequest.from_json(json)
# print the JSON string representation of the object
print CreatePaymentMethodRequest.to_json()

# convert the object into a dict
create_payment_method_request_dict = create_payment_method_request_instance.to_dict()
# create an instance of CreatePaymentMethodRequest from a dict
create_payment_method_request_form_dict = create_payment_method_request.from_dict(create_payment_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


