# CashbookEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Cashbook unique identifier. | [optional] 
**date** | **date, none_type** | Cashbook date. | [optional] 
**description** | **str, none_type** | Cashbook description. | [optional] 
**kind** | [**CashbookEntryKind**](CashbookEntryKind.md) |  | [optional] 
**type** | [**CashbookEntryType**](CashbookEntryType.md) |  | [optional] 
**entity_name** | **str, none_type** | Entity name. | [optional] 
**document** | [**CashbookEntryDocument**](CashbookEntryDocument.md) |  | [optional] 
**amount_in** | **float, none_type** | [Only for cashbook entry in] Total amount in. | [optional] 
**payment_account_in** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**amount_out** | **float, none_type** | [Only for cashbook entry out] Total amount out. | [optional] 
**payment_account_out** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


