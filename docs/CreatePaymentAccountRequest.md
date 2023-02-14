# CreatePaymentAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_payment_account_request import CreatePaymentAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentAccountRequest from a JSON string
create_payment_account_request_instance = CreatePaymentAccountRequest.from_json(json)
# print the JSON string representation of the object
print CreatePaymentAccountRequest.to_json()

# convert the object into a dict
create_payment_account_request_dict = create_payment_account_request_instance.to_dict()
# create an instance of CreatePaymentAccountRequest from a dict
create_payment_account_request_form_dict = create_payment_account_request.from_dict(create_payment_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


