# IssuedDocumentTotals


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_net** | **float** | Total net amount. | [optional] 
**amount_rivalsa** | **float** | Rivalsa amount. | [optional] 
**amount_net_with_rivalsa** | **float** | Net amount with rivalsa. | [optional] 
**amount_cassa** | **float** | Cassa amount. | [optional] 
**taxable_amount** | **float** | Taxable amount. | [optional] 
**not_taxable_amount** | **float** | Not taxable amount. | [optional] 
**amount_vat** | **float** | Total vat amount. | [optional] 
**amount_gross** | **float** | Total grosas amount. | [optional] 
**taxable_amount_withholding_tax** | **float** | Taxable withholding tax amount. | [optional] 
**amount_withholding_tax** | **float** | Withholding tax amount. | [optional] 
**taxable_amount_other_withholding_tax** | **float** | Other withholding tax taxable amount. | [optional] 
**amount_other_withholding_tax** | **float** | Other withholding tax amount. | [optional] 
**stamp_duty** | **float** | Stamp duty value [0 if not present]. | [optional] 
**amount_due** | **float** | Total amount due. | [optional] 
**is_enasarco_maximal_exceeded** | **bool** |  | [optional] 
**payments_sum** | **float** | Payments sum. | [optional] 
**vat_list** | [**Dict[str, VatItem]**](VatItem.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_totals import IssuedDocumentTotals

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentTotals from a JSON string
issued_document_totals_instance = IssuedDocumentTotals.from_json(json)
# print the JSON string representation of the object
print IssuedDocumentTotals.to_json()

# convert the object into a dict
issued_document_totals_dict = issued_document_totals_instance.to_dict()
# create an instance of IssuedDocumentTotals from a dict
issued_document_totals_form_dict = issued_document_totals.from_dict(issued_document_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


