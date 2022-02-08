# Product


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Product name. | 
**id** | **int** | Unique identifier. | [optional] 
**code** | **str, none_type** | Product code. | [optional] 
**net_price** | **float, none_type** | Net sale price (used if use_gross_price is false, otherwise it&#39;s competed automatically). | [optional] 
**gross_price** | **float, none_type** | Gross sale price (used if use_gross_price is false, otherwise it&#39;s competed automatically). | [optional] 
**use_gross_price** | **bool** | Determine which price to use for calculations. | [optional] 
**default_vat** | [**VatType**](VatType.md) |  | [optional] 
**net_cost** | **float, none_type** | Net cost of the product (used for received documents). | [optional] 
**measure** | **str, none_type** | Unit of measure. | [optional] 
**description** | **str, none_type** | Product description. | [optional] 
**category** | **str** | Product category. | [optional] 
**notes** | **str, none_type** | Extra notes. | [optional] 
**in_stock** | **bool** | Determine if the product is in stock. | [optional] 
**stock_initial** | **float** | Product initial stock. | [optional] 
**stock_current** | **float** | [Read Only] Product current stock. | [optional] [readonly] 
**average_cost** | **float** | Product average cost. | [optional] 
**average_price** | **float** | Product average price. | [optional] 
**created_at** | **str, none_type** |  | [optional] 
**updated_at** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


