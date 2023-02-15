# VatItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_net** | **float** |  | [optional] 
**amount_vat** | **float** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.vat_item import VatItem

# TODO update the JSON string below
json = "{}"
# create an instance of VatItem from a JSON string
vat_item_instance = VatItem.from_json(json)
# print the JSON string representation of the object
print VatItem.to_json()

# convert the object into a dict
vat_item_dict = vat_item_instance.to_dict()
# create an instance of VatItem from a dict
vat_item_form_dict = vat_item.from_dict(vat_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


