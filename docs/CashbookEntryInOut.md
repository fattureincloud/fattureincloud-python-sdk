# CashbookEntryInOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Cashbook unique identifier. | 
**date** | **date** | Cashbook date. | 
**description** | **str** | Cashbook description. | 
**kind** | [**CashbookEntryKind**](CashbookEntryKind.md) |  | 
**type** | [**CashbookEntryType**](CashbookEntryType.md) |  | [optional] 
**entity_name** | **str** | Entity name. | [optional] 
**document** | [**CashbookEntryDataDocument**](CashbookEntryDataDocument.md) |  | [optional] 
**amount_out** | **float** | Total amount out. | [optional] 
**payment_account_out** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**amount_in** | **float** | Total amount in. | [optional] 
**payment_account_in** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


