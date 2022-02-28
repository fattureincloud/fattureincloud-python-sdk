# IssuedDocumentItemsListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Unique identifier. | [optional] 
**product_id** | **int, none_type** | Unique identifier of the product. | [optional] 
**code** | **str, none_type** | Product code. | [optional] 
**name** | **str, none_type** | Product name. | [optional] 
**category** | **str, none_type** | Product category | [optional] 
**description** | **str, none_type** | Product description. | [optional] 
**qty** | **float, none_type** | Items quantity, | [optional] 
**measure** | **str, none_type** | Item measure. | [optional] 
**net_price** | **float, none_type** | Net price. | [optional] 
**gross_price** | **float, none_type** | Gross price. | [optional] 
**vat** | [**VatType**](VatType.md) |  | [optional] 
**not_taxable** | **bool, none_type** |  | [optional] 
**apply_withholding_taxes** | **bool, none_type** | Apply withholding taxes, rivalsa and cassa. | [optional] 
**discount** | **float, none_type** | Discount percentual value. | [optional] 
**discount_highlight** | **bool, none_type** |  | [optional] 
**in_ddt** | **bool, none_type** |  | [optional] 
**stock** | **bool, none_type** |  | [optional] 
**ei_raw** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Advanced raw attributes for e-invoices. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


