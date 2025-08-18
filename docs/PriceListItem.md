# PriceListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.price_list_item import PriceListItem

# TODO update the JSON string below
json = "{}"
# create an instance of PriceListItem from a JSON string
price_list_item_instance = PriceListItem.from_json(json)
# print the JSON string representation of the object
print(PriceListItem.to_json())

# convert the object into a dict
price_list_item_dict = price_list_item_instance.to_dict()
# create an instance of PriceListItem from a dict
price_list_item_from_dict = PriceListItem.from_dict(price_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


