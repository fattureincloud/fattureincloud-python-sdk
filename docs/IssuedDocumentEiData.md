# IssuedDocumentEiData

Issued document e-invoice data [Only if e_invoice=true]

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vat_kind** | [**VatKind**](VatKind.md) |  | [optional] 
**original_document_type** | [**OriginalDocumentType**](OriginalDocumentType.md) |  | [optional] 
**od_number** | **str** | E-invoice original document number | [optional] 
**od_date** | **date** | E-invoice original document date | [optional] 
**cig** | **str** | E-invoice CIG | [optional] 
**cup** | **str** | E-invoice CUP | [optional] 
**payment_method** | **str** | E-invoice payment method [required for e-invoices](see https://www.fatturapa.gov.it/export/documenti/fatturapa/v1.2.2/Rappresentazione_Tabellare_FattOrdinaria_V1.2.2.pdf for the accepted values of ModalitaPagamento) | [optional] 
**bank_name** | **str** | E-invoice bank name | [optional] 
**bank_iban** | **str** | E-invoice bank IBAN | [optional] 
**bank_beneficiary** | **str** | E-invoice bank beneficiary | [optional] 
**invoice_number** | **str** | E-invoice invoice number | [optional] 
**invoice_date** | **date** | E-invoice invoice date | [optional] 

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


