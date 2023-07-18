# IssuedDocumentPaymentsListItemPaymentTerms


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | Issued document payment number of days by which the payment must be made | [optional] 
**type** | [**PaymentTermsType**](PaymentTermsType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_payments_list_item_payment_terms import IssuedDocumentPaymentsListItemPaymentTerms

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentPaymentsListItemPaymentTerms from a JSON string
issued_document_payments_list_item_payment_terms_instance = IssuedDocumentPaymentsListItemPaymentTerms.from_json(json)
# print the JSON string representation of the object
print IssuedDocumentPaymentsListItemPaymentTerms.to_json()

# convert the object into a dict
issued_document_payments_list_item_payment_terms_dict = issued_document_payments_list_item_payment_terms_instance.to_dict()
# create an instance of IssuedDocumentPaymentsListItemPaymentTerms from a dict
issued_document_payments_list_item_payment_terms_form_dict = issued_document_payments_list_item_payment_terms.from_dict(issued_document_payments_list_item_payment_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


