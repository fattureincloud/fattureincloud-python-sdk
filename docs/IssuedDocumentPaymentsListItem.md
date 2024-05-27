# IssuedDocumentPaymentsListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Issued document payment item id | [optional] 
**due_date** | **date** | Issued document payment due date | [optional] 
**amount** | **float** | Issued document payment amount | [optional] 
**status** | [**IssuedDocumentStatus**](IssuedDocumentStatus.md) |  | [optional] 
**payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**paid_date** | **date** | Issued document payment date [Only if status is paid] | [optional] 
**ei_raw** | **object** | Issued document payment advanced raw attributes for e-invoices | [optional] 
**payment_terms** | [**IssuedDocumentPaymentsListItemPaymentTerms**](IssuedDocumentPaymentsListItemPaymentTerms.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_payments_list_item import IssuedDocumentPaymentsListItem

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentPaymentsListItem from a JSON string
issued_document_payments_list_item_instance = IssuedDocumentPaymentsListItem.from_json(json)
# print the JSON string representation of the object
print(IssuedDocumentPaymentsListItem.to_json())

# convert the object into a dict
issued_document_payments_list_item_dict = issued_document_payments_list_item_instance.to_dict()
# create an instance of IssuedDocumentPaymentsListItem from a dict
issued_document_payments_list_item_from_dict = IssuedDocumentPaymentsListItem.from_dict(issued_document_payments_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


