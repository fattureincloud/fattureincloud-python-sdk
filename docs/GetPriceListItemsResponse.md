# GetPriceListItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Dict[str, PriceListItem]**](PriceListItem.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_price_list_items_response import GetPriceListItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPriceListItemsResponse from a JSON string
get_price_list_items_response_instance = GetPriceListItemsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPriceListItemsResponse.to_json())

# convert the object into a dict
get_price_list_items_response_dict = get_price_list_items_response_instance.to_dict()
# create an instance of GetPriceListItemsResponse from a dict
get_price_list_items_response_from_dict = GetPriceListItemsResponse.from_dict(get_price_list_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


