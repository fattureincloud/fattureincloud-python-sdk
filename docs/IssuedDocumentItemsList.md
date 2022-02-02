# IssuedDocumentItemsList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Unique identifier of the product. | [optional] 
**code** | **str** | Product code. | [optional] 
**name** | **str** | Product name. | [optional] 
**category** | **str** | Product category | [optional] 
**description** | **str** | Product description. | [optional] 
**qty** | **float** | Items quantity, | [optional] 
**measure** | **str** | Item measure. | [optional] 
**net_price** | **float** | Net price. | [optional] 
**gross_price** | **float** | Gross price. | [optional] 
**vat** | [**VatType**](VatType.md) |  | [optional] 
**not_taxable** | **bool** |  | [optional]  if omitted the server will use the default value of False
**apply_withholding_taxes** | **bool** | Apply withholding taxes, rivalsa and cassa. | [optional]  if omitted the server will use the default value of True
**discount** | **float** | Discount percentual value. | [optional] 
**discount_highlight** | **bool** |  | [optional]  if omitted the server will use the default value of False
**in_ddt** | **bool** |  | [optional]  if omitted the server will use the default value of True
**stock** | **bool** |  | [optional] 
**ei_raw** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Advanced raw attributes for e-invoices. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


