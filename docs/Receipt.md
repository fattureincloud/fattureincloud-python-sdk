# Receipt



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Receipt unique identifier. | [optional] 
**var_date** | **date** | Receipt date. | [optional] 
**number** | **float** | Receipt number. | [optional] 
**numeration** | **str** | If it&#39;s null or empty string use the default numeration. | [optional] 
**amount_net** | **float** | Total net amount. | [optional] 
**amount_vat** | **float** | Total vat amount. | [optional] 
**amount_gross** | **float** | Total gross amount. | [optional] 
**use_gross_prices** | **bool** |  | [optional] 
**type** | [**ReceiptType**](ReceiptType.md) |  | [optional] 
**description** | **str** | Receipt description. | [optional] 
**rc_center** | **str** | Revenue center. | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**payment_account** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**items_list** | [**List[ReceiptItemsListItem]**](ReceiptItemsListItem.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.receipt import Receipt

# TODO update the JSON string below
json = "{}"
# create an instance of Receipt from a JSON string
receipt_instance = Receipt.from_json(json)
# print the JSON string representation of the object
print Receipt.to_json()

# convert the object into a dict
receipt_dict = receipt_instance.to_dict()
# create an instance of Receipt from a dict
receipt_form_dict = receipt.from_dict(receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


