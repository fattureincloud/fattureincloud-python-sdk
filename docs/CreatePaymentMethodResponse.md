# CreatePaymentMethodResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_payment_method_response import CreatePaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentMethodResponse from a JSON string
create_payment_method_response_instance = CreatePaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print CreatePaymentMethodResponse.to_json()

# convert the object into a dict
create_payment_method_response_dict = create_payment_method_response_instance.to_dict()
# create an instance of CreatePaymentMethodResponse from a dict
create_payment_method_response_form_dict = create_payment_method_response.from_dict(create_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


