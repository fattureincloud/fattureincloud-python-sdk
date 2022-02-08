# ReceiptPreCreateInfo



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numerations** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Next number by year, receipt type and numeration name. | 
**numerations_list** | **[str]** | List of series used in the past. | 
**rc_centers_list** | **[str]** | List of revenue centers used in the past. | 
**payment_accounts_list** | [**[PaymentAccount]**](PaymentAccount.md) | User payment accounts list. | 
**categories_list** | **[str]** | List of categories used in the past. | 
**vat_types_list** | [**[VatType]**](VatType.md) | List of user vat types with the default 22%, 10%, 4% and 0% vats. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


