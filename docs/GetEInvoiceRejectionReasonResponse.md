# GetEInvoiceRejectionReasonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EInvoiceRejectionReason**](EInvoiceRejectionReason.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_e_invoice_rejection_reason_response import GetEInvoiceRejectionReasonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEInvoiceRejectionReasonResponse from a JSON string
get_e_invoice_rejection_reason_response_instance = GetEInvoiceRejectionReasonResponse.from_json(json)
# print the JSON string representation of the object
print(GetEInvoiceRejectionReasonResponse.to_json())

# convert the object into a dict
get_e_invoice_rejection_reason_response_dict = get_e_invoice_rejection_reason_response_instance.to_dict()
# create an instance of GetEInvoiceRejectionReasonResponse from a dict
get_e_invoice_rejection_reason_response_from_dict = GetEInvoiceRejectionReasonResponse.from_dict(get_e_invoice_rejection_reason_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


