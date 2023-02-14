# GetPaymentMethodResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_payment_method_response import GetPaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethodResponse from a JSON string
get_payment_method_response_instance = GetPaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print GetPaymentMethodResponse.to_json()

# convert the object into a dict
get_payment_method_response_dict = get_payment_method_response_instance.to_dict()
# create an instance of GetPaymentMethodResponse from a dict
get_payment_method_response_form_dict = get_payment_method_response.from_dict(get_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


