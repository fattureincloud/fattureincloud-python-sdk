# PendingReceivedDocumentPaymentsListItemPaymentTerms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | Pending received document payment number of days by which the payment must be made | [optional] 
**type** | [**PaymentTermsType**](PaymentTermsType.md) |  | [optional] [default to PaymentTermsType.STANDARD]

## Example

```python
from fattureincloud_python_sdk.models.pending_received_document_payments_list_item_payment_terms import PendingReceivedDocumentPaymentsListItemPaymentTerms

# TODO update the JSON string below
json = "{}"
# create an instance of PendingReceivedDocumentPaymentsListItemPaymentTerms from a JSON string
pending_received_document_payments_list_item_payment_terms_instance = PendingReceivedDocumentPaymentsListItemPaymentTerms.from_json(json)
# print the JSON string representation of the object
print(PendingReceivedDocumentPaymentsListItemPaymentTerms.to_json())

# convert the object into a dict
pending_received_document_payments_list_item_payment_terms_dict = pending_received_document_payments_list_item_payment_terms_instance.to_dict()
# create an instance of PendingReceivedDocumentPaymentsListItemPaymentTerms from a dict
pending_received_document_payments_list_item_payment_terms_from_dict = PendingReceivedDocumentPaymentsListItemPaymentTerms.from_dict(pending_received_document_payments_list_item_payment_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


