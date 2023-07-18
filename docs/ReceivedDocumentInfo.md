# ReceivedDocumentInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | [**ReceivedDocumentInfoDefaultValues**](ReceivedDocumentInfoDefaultValues.md) |  | [optional] 
**items_default_values** | [**ReceivedDocumentInfoItemsDefaultValues**](ReceivedDocumentInfoItemsDefaultValues.md) |  | [optional] 
**countries_list** | **List[str]** | Countries list | [optional] 
**currencies_list** | [**List[Currency]**](Currency.md) | Currencies list | [optional] 
**categories_list** | **List[str]** | Categories list | [optional] 
**payment_accounts_list** | [**List[PaymentAccount]**](PaymentAccount.md) | Payments accounts list | [optional] 
**vat_types_list** | [**List[VatType]**](VatType.md) | Vat types list | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.received_document_info import ReceivedDocumentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivedDocumentInfo from a JSON string
received_document_info_instance = ReceivedDocumentInfo.from_json(json)
# print the JSON string representation of the object
print ReceivedDocumentInfo.to_json()

# convert the object into a dict
received_document_info_dict = received_document_info_instance.to_dict()
# create an instance of ReceivedDocumentInfo from a dict
received_document_info_form_dict = received_document_info.from_dict(received_document_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


