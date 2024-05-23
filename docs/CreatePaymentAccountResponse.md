# CreatePaymentAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_payment_account_response import CreatePaymentAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentAccountResponse from a JSON string
create_payment_account_response_instance = CreatePaymentAccountResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentAccountResponse.to_json())

# convert the object into a dict
create_payment_account_response_dict = create_payment_account_response_instance.to_dict()
# create an instance of CreatePaymentAccountResponse from a dict
create_payment_account_response_from_dict = CreatePaymentAccountResponse.from_dict(create_payment_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


