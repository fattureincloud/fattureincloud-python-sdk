# ReceivedDocumentPaymentsListItemPaymentTerms


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | Number of days. | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.received_document_payments_list_item_payment_terms import ReceivedDocumentPaymentsListItemPaymentTerms

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivedDocumentPaymentsListItemPaymentTerms from a JSON string
received_document_payments_list_item_payment_terms_instance = ReceivedDocumentPaymentsListItemPaymentTerms.from_json(json)
# print the JSON string representation of the object
print ReceivedDocumentPaymentsListItemPaymentTerms.to_json()

# convert the object into a dict
received_document_payments_list_item_payment_terms_dict = received_document_payments_list_item_payment_terms_instance.to_dict()
# create an instance of ReceivedDocumentPaymentsListItemPaymentTerms from a dict
received_document_payments_list_item_payment_terms_form_dict = received_document_payments_list_item_payment_terms.from_dict(received_document_payments_list_item_payment_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


