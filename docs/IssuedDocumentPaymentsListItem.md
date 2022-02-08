# IssuedDocumentPaymentsListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. | [optional] 
**due_date** | **date** | Due date. | [optional] 
**amount** | **float** | Payment amount. | [optional] 
**status** | [**IssuedDocumentStatus**](IssuedDocumentStatus.md) |  | [optional] 
**payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**paid_date** | **date** | Payment date. [Only if status is paid] | [optional] 
**ei_raw** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Advanced raw attributes for e-invoices. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


