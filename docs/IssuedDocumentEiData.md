# IssuedDocumentEiData

E-invoice data. [Only if e_invoice=true]

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vat_kind** | [**VatKind**](VatKind.md) |  | [optional] 
**original_document_type** | [**OriginalDocumentType**](OriginalDocumentType.md) |  | [optional] 
**od_number** | **str** | Original document number. | [optional] 
**od_date** | **date** | Original document date. | [optional] 
**cig** | **str** | CIG. | [optional] 
**cup** | **str** | CUP. | [optional] 
**payment_method** | **str** | Payment method (see https://www.fatturapa.gov.it/export/documenti/fatturapa/v1.2.1/Rappresentazione-tabellare-fattura-ordinaria.pdf for the accepted values of ModalitaPagamento). | [optional] 
**bank_name** | **str** | Bank name. | [optional] 
**bank_iban** | **str** | IBAN. | [optional] 
**bank_beneficiary** | **str** | Bank beneficiary. | [optional] 
**invoice_number** | **str** | Invoice number. | [optional] 
**invoice_date** | **date** | Invoice date. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_ei_data import IssuedDocumentEiData

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentEiData from a JSON string
issued_document_ei_data_instance = IssuedDocumentEiData.from_json(json)
# print the JSON string representation of the object
print IssuedDocumentEiData.to_json()

# convert the object into a dict
issued_document_ei_data_dict = issued_document_ei_data_instance.to_dict()
# create an instance of IssuedDocumentEiData from a dict
issued_document_ei_data_form_dict = issued_document_ei_data.from_dict(issued_document_ei_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


