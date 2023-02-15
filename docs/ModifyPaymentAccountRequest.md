# ModifyPaymentAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_payment_account_request import ModifyPaymentAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPaymentAccountRequest from a JSON string
modify_payment_account_request_instance = ModifyPaymentAccountRequest.from_json(json)
# print the JSON string representation of the object
print ModifyPaymentAccountRequest.to_json()

# convert the object into a dict
modify_payment_account_request_dict = modify_payment_account_request_instance.to_dict()
# create an instance of ModifyPaymentAccountRequest from a dict
modify_payment_account_request_form_dict = modify_payment_account_request.from_dict(modify_payment_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


