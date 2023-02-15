# ReceiptPreCreateInfo



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numerations** | **Dict[str, Dict]** |  | [optional] 
**numerations_list** | **List[str]** | List of series used in the past. | [optional] 
**rc_centers_list** | **List[str]** | List of revenue centers used in the past. | [optional] 
**payment_accounts_list** | [**List[PaymentAccount]**](PaymentAccount.md) | User payment accounts list. | [optional] 
**categories_list** | **List[str]** | List of categories used in the past. | [optional] 
**vat_types_list** | [**List[VatType]**](VatType.md) | List of user vat types with the default 22%, 10%, 4% and 0% vats. | [optional] 

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


