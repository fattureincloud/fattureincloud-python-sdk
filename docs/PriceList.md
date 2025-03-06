# PriceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Price list id | [optional] 
**name** | **str** | Price list name | [optional] 
**prices_type** | [**PriceListPricesType**](PriceListPricesType.md) |  | [optional] 
**is_default** | **bool** | This entity is default | [optional] 
**valid_from** | **str** | Price list validity start date | [optional] 
**valid_to** | **str** | Price list validity end date | [optional] 
**type** | [**PriceListType**](PriceListType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.price_list import PriceList

# TODO update the JSON string below
json = "{}"
# create an instance of PriceList from a JSON string
price_list_instance = PriceList.from_json(json)
# print the JSON string representation of the object
print(PriceList.to_json())

# convert the object into a dict
price_list_dict = price_list_instance.to_dict()
# create an instance of PriceList from a dict
price_list_from_dict = PriceList.from_dict(price_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


