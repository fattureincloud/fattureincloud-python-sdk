# ModifyPaymentAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_payment_account_response import ModifyPaymentAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPaymentAccountResponse from a JSON string
modify_payment_account_response_instance = ModifyPaymentAccountResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyPaymentAccountResponse.to_json())

# convert the object into a dict
modify_payment_account_response_dict = modify_payment_account_response_instance.to_dict()
# create an instance of ModifyPaymentAccountResponse from a dict
modify_payment_account_response_from_dict = ModifyPaymentAccountResponse.from_dict(modify_payment_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


