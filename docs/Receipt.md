# Receipt



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Receipt unique identifier. | [optional] 
**date** | **date, none_type** | Receipt date. | [optional] 
**number** | **float, none_type** | Receipt number. | [optional] 
**numeration** | **str, none_type** | If it&#39;s null or empty string use the default numeration. | [optional] 
**amount_net** | **float, none_type** | Total net amount. | [optional] 
**amount_vat** | **float, none_type** | Total vat amount. | [optional] 
**amount_gross** | **float, none_type** | Total gross amount. | [optional] 
**use_gross_prices** | **bool, none_type** |  | [optional] 
**type** | [**ReceiptType**](ReceiptType.md) |  | [optional] 
**description** | **str, none_type** | Receipt description. | [optional] 
**rc_center** | **str, none_type** | Revenue center. | [optional] 
**created_at** | **str, none_type** |  | [optional] 
**updated_at** | **str, none_type** |  | [optional] 
**payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**items_list** | [**[ReceiptItemsListItem], none_type**](ReceiptItemsListItem.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


