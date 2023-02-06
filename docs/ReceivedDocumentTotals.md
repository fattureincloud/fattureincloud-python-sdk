# ReceivedDocumentTotals



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_net** | **float** | Total net amount. | [optional] 
**amount_vat** | **float** | Total vat amount. | [optional] 
**amount_gross** | **float** | Total gross amount. | [optional] 
**amount_withholding_tax** | **float** | Total withholding tax amount. | [optional] 
**amount_other_withholding_tax** | **float** | Total other withholding tax amount. | [optional] 
**amount_due** | **float** | Total amount due. | [optional] 
**payments_sum** | **float** | Payments sum. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.received_document_totals import ReceivedDocumentTotals

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivedDocumentTotals from a JSON string
received_document_totals_instance = ReceivedDocumentTotals.from_json(json)
# print the JSON string representation of the object
print ReceivedDocumentTotals.to_json()

# convert the object into a dict
received_document_totals_dict = received_document_totals_instance.to_dict()
# create an instance of ReceivedDocumentTotals from a dict
received_document_totals_form_dict = received_document_totals.from_dict(received_document_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


