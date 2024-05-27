# EInvoiceRejectionReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | E-invoice rejection reason | [optional] 
**ei_status** | **str** | E-invoice status | [optional] 
**solution** | **str** | Error solution. | [optional] 
**code** | **str** | E-invoice rejection error code | [optional] 
**var_date** | **datetime** | E-invoice rejection date | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.e_invoice_rejection_reason import EInvoiceRejectionReason

# TODO update the JSON string below
json = "{}"
# create an instance of EInvoiceRejectionReason from a JSON string
e_invoice_rejection_reason_instance = EInvoiceRejectionReason.from_json(json)
# print the JSON string representation of the object
print(EInvoiceRejectionReason.to_json())

# convert the object into a dict
e_invoice_rejection_reason_dict = e_invoice_rejection_reason_instance.to_dict()
# create an instance of EInvoiceRejectionReason from a dict
e_invoice_rejection_reason_from_dict = EInvoiceRejectionReason.from_dict(e_invoice_rejection_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


