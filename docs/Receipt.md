# Receipt



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **date** | Receipt date. | 
**type** | [**ReceiptType**](ReceiptType.md) |  | 
**payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | 
**id** | **int** | Receipt unique identifier. | [optional] 
**number** | **float** | Receipt number. | [optional] 
**numeration** | **str** | If it&#39;s null or empty string use the default numeration. | [optional] 
**amount_net** | **float** | Total net amount. | [optional] 
**amount_vat** | **float** | Total vat amount. | [optional] 
**amount_gross** | **float** | Total gross amount. | [optional] 
**use_gross_prices** | **bool** |  | [optional]  if omitted the server will use the default value of False
**description** | **str** | Receipt description. | [optional] 
**rc_center** | **str** | Revenue center. | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**items_list** | [**[ReceiptItemsListItem]**](ReceiptItemsListItem.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


