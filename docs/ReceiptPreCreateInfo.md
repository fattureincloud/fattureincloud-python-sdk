# ReceiptPreCreateInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numerations** | **Dict[str, Dict[str, int]]** |  | [optional] 
**numerations_list** | **List[str]** | Receipt used numerations list | [optional] 
**rc_centers_list** | **List[str]** | Receipt used revenue centers list | [optional] 
**payment_accounts_list** | [**List[PaymentAccount]**](PaymentAccount.md) | Payment accounts list | [optional] 
**categories_list** | **List[str]** | Receipt categories list | [optional] 
**vat_types_list** | [**List[VatType]**](VatType.md) | Vat types list | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.receipt_pre_create_info import ReceiptPreCreateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptPreCreateInfo from a JSON string
receipt_pre_create_info_instance = ReceiptPreCreateInfo.from_json(json)
# print the JSON string representation of the object
print ReceiptPreCreateInfo.to_json()

# convert the object into a dict
receipt_pre_create_info_dict = receipt_pre_create_info_instance.to_dict()
# create an instance of ReceiptPreCreateInfo from a dict
receipt_pre_create_info_form_dict = receipt_pre_create_info.from_dict(receipt_pre_create_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


