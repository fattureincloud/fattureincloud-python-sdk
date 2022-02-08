# PaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | [optional] 
**name** | **str** | Name of the payment method | [optional] 
**type** | [**PaymentMethodType**](PaymentMethodType.md) |  | [optional] 
**is_default** | **bool** | Determines if this is the default payment method. | [optional] 
**default_payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**details** | [**[PaymentMethodDetails]**](PaymentMethodDetails.md) | Method details rows | [optional] 
**bank_iban** | **str** | Bank iban | [optional] 
**bank_name** | **str** | Bank name | [optional] 
**bank_beneficiary** | **str** | Bank beneficiary | [optional] 
**ei_payment_method** | **str** | EInvoice payment method | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


