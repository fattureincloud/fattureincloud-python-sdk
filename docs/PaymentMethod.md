# PaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | [optional] 
**name** | **str** | Name of the payment method | [optional] 
**type** | [**PaymentMethodType**](PaymentMethodType.md) |  | [optional] 
**is_default** | **bool** | Determines if this is the default payment method. | [optional] 
**default_payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**details** | [**List[PaymentMethodDetails]**](PaymentMethodDetails.md) | Method details rows | [optional] 
**bank_iban** | **str** | Bank iban | [optional] 
**bank_name** | **str** | Bank name | [optional] 
**bank_beneficiary** | **str** | Bank beneficiary | [optional] 
**ei_payment_method** | **str** | E-invoice payment method | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.payment_method import PaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethod from a JSON string
payment_method_instance = PaymentMethod.from_json(json)
# print the JSON string representation of the object
print PaymentMethod.to_json()

# convert the object into a dict
payment_method_dict = payment_method_instance.to_dict()
# create an instance of PaymentMethod from a dict
payment_method_form_dict = payment_method.from_dict(payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


