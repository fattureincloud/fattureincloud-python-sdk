# PaymentAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Payment account id | [optional] 
**name** | **str** | Payment account name | [optional] 
**type** | [**PaymentAccountType**](PaymentAccountType.md) |  | [optional] 
**iban** | **str** | Payment account iban | [optional] 
**sia** | **str** | Payment account sia | [optional] 
**cuc** | **str** | Payment account cuc | [optional] 
**virtual** | **bool** | Payment method is virtual | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.payment_account import PaymentAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccount from a JSON string
payment_account_instance = PaymentAccount.from_json(json)
# print the JSON string representation of the object
print(PaymentAccount.to_json())

# convert the object into a dict
payment_account_dict = payment_account_instance.to_dict()
# create an instance of PaymentAccount from a dict
payment_account_from_dict = PaymentAccount.from_dict(payment_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


