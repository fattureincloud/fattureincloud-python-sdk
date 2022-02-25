# IssuedDocumentEiData

E-invoice data. [Only if e_invoice=true]

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vat_kind** | [**VatKind**](VatKind.md) |  | [optional] 
**original_document_type** | [**OriginalDocumentType**](OriginalDocumentType.md) |  | [optional] 
**od_number** | **str, none_type** | Original document number. | [optional] 
**od_date** | **date, none_type** | Original document date. | [optional] 
**cig** | **str, none_type** | CIG. | [optional] 
**cup** | **str, none_type** | CUP. | [optional] 
**payment_method** | **str, none_type** | Payment method (see https://www.fatturapa.gov.it/export/documenti/fatturapa/v1.2.1/Rappresentazione-tabellare-fattura-ordinaria.pdf for the accepted values of ModalitaPagamento). | [optional] 
**bank_name** | **str, none_type** | Bank name. | [optional] 
**bank_iban** | **str, none_type** | IBAN. | [optional] 
**bank_beneficiary** | **str, none_type** | Bank beneficiary. | [optional] 
**invoice_number** | **str, none_type** | Invoice number. | [optional] 
**invoice_date** | **date, none_type** | Invoice date. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


