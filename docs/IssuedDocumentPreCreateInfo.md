# IssuedDocumentPreCreateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numerations** | **Dict[str, Dict[str, int]]** |  | [optional] 
**dn_numerations** | **Dict[str, Dict[str, int]]** |  | [optional] 
**default_values** | [**IssuedDocumentPreCreateInfoDefaultValues**](IssuedDocumentPreCreateInfoDefaultValues.md) |  | [optional] 
**extra_data_default_values** | [**IssuedDocumentPreCreateInfoExtraDataDefaultValues**](IssuedDocumentPreCreateInfoExtraDataDefaultValues.md) |  | [optional] 
**items_default_values** | [**IssuedDocumentPreCreateInfoItemsDefaultValues**](IssuedDocumentPreCreateInfoItemsDefaultValues.md) |  | [optional] 
**countries_list** | **List[str]** | Countries list | [optional] 
**currencies_list** | [**List[Currency]**](Currency.md) | Currencies list | [optional] 
**templates_list** | [**List[DocumentTemplate]**](DocumentTemplate.md) | Document templates list | [optional] 
**dn_templates_list** | [**List[DocumentTemplate]**](DocumentTemplate.md) | Delivery note templates list | [optional] 
**ai_templates_list** | [**List[DocumentTemplate]**](DocumentTemplate.md) | Accompanying invoice templates list | [optional] 
**payment_methods_list** | [**List[PaymentMethod]**](PaymentMethod.md) | Payment methods list | [optional] 
**payment_accounts_list** | [**List[PaymentAccount]**](PaymentAccount.md) | Payment accounts list | [optional] 
**vat_types_list** | [**List[VatType]**](VatType.md) | Vat types list | [optional] 
**languages_list** | [**List[Language]**](Language.md) | Languages list | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_pre_create_info import IssuedDocumentPreCreateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentPreCreateInfo from a JSON string
issued_document_pre_create_info_instance = IssuedDocumentPreCreateInfo.from_json(json)
# print the JSON string representation of the object
print(IssuedDocumentPreCreateInfo.to_json())

# convert the object into a dict
issued_document_pre_create_info_dict = issued_document_pre_create_info_instance.to_dict()
# create an instance of IssuedDocumentPreCreateInfo from a dict
issued_document_pre_create_info_from_dict = IssuedDocumentPreCreateInfo.from_dict(issued_document_pre_create_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


