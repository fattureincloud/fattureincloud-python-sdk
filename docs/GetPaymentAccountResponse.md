# GetPaymentAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_payment_account_response import GetPaymentAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentAccountResponse from a JSON string
get_payment_account_response_instance = GetPaymentAccountResponse.from_json(json)
# print the JSON string representation of the object
print(GetPaymentAccountResponse.to_json())

# convert the object into a dict
get_payment_account_response_dict = get_payment_account_response_instance.to_dict()
# create an instance of GetPaymentAccountResponse from a dict
get_payment_account_response_from_dict = GetPaymentAccountResponse.from_dict(get_payment_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


