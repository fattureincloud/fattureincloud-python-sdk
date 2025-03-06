# EntityClientPreCreateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries_list** | **List[str]** | Countries list | [optional] 
**payment_methods_list** | [**List[PaymentMethod]**](PaymentMethod.md) | Entity payment methods list | [optional] 
**payment_accounts_list** | [**List[PaymentAccount]**](PaymentAccount.md) | Entity payment accounts list | [optional] 
**vat_types_list** | [**List[VatType]**](VatType.md) | Vat types list | [optional] 
**price_lists** | [**List[PriceList]**](PriceList.md) | Entity price lists | [optional] 
**limit** | **float** | Entity limit | [optional] 
**usage** | **float** | Entity usage | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.entity_client_pre_create_info import EntityClientPreCreateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntityClientPreCreateInfo from a JSON string
entity_client_pre_create_info_instance = EntityClientPreCreateInfo.from_json(json)
# print the JSON string representation of the object
print(EntityClientPreCreateInfo.to_json())

# convert the object into a dict
entity_client_pre_create_info_dict = entity_client_pre_create_info_instance.to_dict()
# create an instance of EntityClientPreCreateInfo from a dict
entity_client_pre_create_info_from_dict = EntityClientPreCreateInfo.from_dict(entity_client_pre_create_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


