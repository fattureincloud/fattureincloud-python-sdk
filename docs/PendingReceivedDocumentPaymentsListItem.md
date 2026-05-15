# PendingReceivedDocumentPaymentsListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Pending received document payment total amount | [optional] 
**due_date** | **date** | Due date | [optional] 
**paid_date** | **date** | Pending received document payment paid date | [optional] 
**payment_terms** | [**PendingReceivedDocumentPaymentsListItemPaymentTerms**](PendingReceivedDocumentPaymentsListItemPaymentTerms.md) |  | [optional] 
**status** | **str** | Pending received document payment status | [optional] 
**paid_with_ts_pay** | **bool** | True if paid with TS Pay | [optional] 
**payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.pending_received_document_payments_list_item import PendingReceivedDocumentPaymentsListItem

# TODO update the JSON string below
json = "{}"
# create an instance of PendingReceivedDocumentPaymentsListItem from a JSON string
pending_received_document_payments_list_item_instance = PendingReceivedDocumentPaymentsListItem.from_json(json)
# print the JSON string representation of the object
print(PendingReceivedDocumentPaymentsListItem.to_json())

# convert the object into a dict
pending_received_document_payments_list_item_dict = pending_received_document_payments_list_item_instance.to_dict()
# create an instance of PendingReceivedDocumentPaymentsListItem from a dict
pending_received_document_payments_list_item_from_dict = PendingReceivedDocumentPaymentsListItem.from_dict(pending_received_document_payments_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


