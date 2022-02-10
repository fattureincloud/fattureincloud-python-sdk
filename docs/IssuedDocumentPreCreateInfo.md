# IssuedDocumentPreCreateInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numerations** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Next numbers by year and numeration name (for the given document type). | [optional] 
**dn_numerations** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Next numbers by year and numeration name (for delivery_notes). | [optional] 
**default_values** | [**IssuedDocumentPreCreateInfoDefaultValues**](IssuedDocumentPreCreateInfoDefaultValues.md) |  | [optional] 
**extra_data_default_values** | [**IssuedDocumentPreCreateInfoExtraDataDefaultValues**](IssuedDocumentPreCreateInfoExtraDataDefaultValues.md) |  | [optional] 
**items_default_values** | [**IssuedDocumentPreCreateInfoItemsDefaultValues**](IssuedDocumentPreCreateInfoItemsDefaultValues.md) |  | [optional] 
**countries_list** | **[str]** | Countries list. | [optional] 
**currencies_list** | [**[Currency]**](Currency.md) | Currencies list. | [optional] 
**templates_list** | [**[DocumentTemplate]**](DocumentTemplate.md) | Document templates list. | [optional] 
**dn_templates_list** | [**[DocumentTemplate]**](DocumentTemplate.md) | Delivery note templates list. | [optional] 
**ai_templates_list** | [**[DocumentTemplate]**](DocumentTemplate.md) | Accompanying invoice templates list. | [optional] 
**payment_methods_list** | [**[PaymentMethod]**](PaymentMethod.md) | Payment methods list. | [optional] 
**payment_accounts_list** | [**[PaymentAccount]**](PaymentAccount.md) | Payment accounts list. | [optional] 
**vat_types_list** | [**[VatType]**](VatType.md) | Vat types list. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


