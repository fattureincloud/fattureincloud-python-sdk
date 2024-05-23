# IssuedDocumentTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_net** | **float** | Issued document total net amount | [optional] 
**amount_rivalsa** | **float** | Issued document rivalsa amount | [optional] 
**amount_net_with_rivalsa** | **float** | Issued document net amount with rivalsa | [optional] 
**amount_cassa** | **float** | Issued document cassa amount | [optional] 
**taxable_amount** | **float** | Issued document taxable amount | [optional] 
**not_taxable_amount** | **float** | Issued document not taxable amount | [optional] 
**amount_vat** | **float** | Issued document total vat amount | [optional] 
**amount_gross** | **float** | Issued document total gross amount | [optional] 
**taxable_amount_withholding_tax** | **float** | Issued document Taxable withholding tax amount | [optional] 
**amount_withholding_tax** | **float** | Issued document withholding tax amount | [optional] 
**taxable_amount_other_withholding_tax** | **float** | Issued document other withholding tax taxable amount | [optional] 
**amount_other_withholding_tax** | **float** | Issued document other withholding tax amount | [optional] 
**stamp_duty** | **float** | Issued document stamp duty value [0 if not present]. | [optional] 
**amount_due** | **float** | Issued document total amount due | [optional] 
**is_enasarco_maximal_exceeded** | **bool** | Is enasarco maximal excedeed | [optional] 
**payments_sum** | **float** | Issued document payments sum | [optional] 
**vat_list** | [**Dict[str, VatItem]**](VatItem.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_totals import IssuedDocumentTotals

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentTotals from a JSON string
issued_document_totals_instance = IssuedDocumentTotals.from_json(json)
# print the JSON string representation of the object
print(IssuedDocumentTotals.to_json())

# convert the object into a dict
issued_document_totals_dict = issued_document_totals_instance.to_dict()
# create an instance of IssuedDocumentTotals from a dict
issued_document_totals_from_dict = IssuedDocumentTotals.from_dict(issued_document_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


