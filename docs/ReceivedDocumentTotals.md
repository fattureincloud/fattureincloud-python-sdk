# ReceivedDocumentTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_net** | **float** | Received document total net amount | [optional] 
**amount_vat** | **float** | Received document total vat amount | [optional] 
**amount_gross** | **float** | Received document total gross amount | [optional] 
**amount_withholding_tax** | **float** | Received document withholding tax amount | [optional] 
**amount_other_withholding_tax** | **float** | Received document other withholding tax amount | [optional] 
**amount_due** | **float** | Received document total amount due | [optional] 
**payments_sum** | **float** | Received document payments sum | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.received_document_totals import ReceivedDocumentTotals

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivedDocumentTotals from a JSON string
received_document_totals_instance = ReceivedDocumentTotals.from_json(json)
# print the JSON string representation of the object
print(ReceivedDocumentTotals.to_json())

# convert the object into a dict
received_document_totals_dict = received_document_totals_instance.to_dict()
# create an instance of ReceivedDocumentTotals from a dict
received_document_totals_from_dict = ReceivedDocumentTotals.from_dict(received_document_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


