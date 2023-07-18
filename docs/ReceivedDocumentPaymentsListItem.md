# ReceivedDocumentPaymentsListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Received document payment id | [optional] 
**amount** | **float** | Received document payment total amount | [optional] 
**due_date** | **date** | Due date | [optional] 
**paid_date** | **date** | Received document payment paid date | [optional] 
**payment_terms** | [**ReceivedDocumentPaymentsListItemPaymentTerms**](ReceivedDocumentPaymentsListItemPaymentTerms.md) |  | [optional] 
**status** | **str** | Received document payment status | [optional] 
**payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.received_document_payments_list_item import ReceivedDocumentPaymentsListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivedDocumentPaymentsListItem from a JSON string
received_document_payments_list_item_instance = ReceivedDocumentPaymentsListItem.from_json(json)
# print the JSON string representation of the object
print ReceivedDocumentPaymentsListItem.to_json()

# convert the object into a dict
received_document_payments_list_item_dict = received_document_payments_list_item_instance.to_dict()
# create an instance of ReceivedDocumentPaymentsListItem from a dict
received_document_payments_list_item_form_dict = received_document_payments_list_item.from_dict(received_document_payments_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


