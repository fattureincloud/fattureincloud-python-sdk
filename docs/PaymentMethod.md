# PaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Payment method id | [optional] 
**name** | **str** | Payment method name | [optional] 
**type** | [**PaymentMethodType**](PaymentMethodType.md) |  | [optional] 
**is_default** | **bool** | Payment method is default | [optional] 
**default_payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**details** | [**List[PaymentMethodDetails]**](PaymentMethodDetails.md) | Payment method details | [optional] 
**bank_iban** | **str** | Payment method bank iban | [optional] 
**bank_name** | **str** | Payment method bank name | [optional] 
**bank_beneficiary** | **str** | Payment method bank beneficiary | [optional] 
**ei_payment_method** | **str** | E-invoice payment method | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.payment_method import PaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethod from a JSON string
payment_method_instance = PaymentMethod.from_json(json)
# print the JSON string representation of the object
print(PaymentMethod.to_json())

# convert the object into a dict
payment_method_dict = payment_method_instance.to_dict()
# create an instance of PaymentMethod from a dict
payment_method_from_dict = PaymentMethod.from_dict(payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


