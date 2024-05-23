# ListF24ResponsePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[F24]**](F24.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_f24_response_page import ListF24ResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListF24ResponsePage from a JSON string
list_f24_response_page_instance = ListF24ResponsePage.from_json(json)
# print the JSON string representation of the object
print(ListF24ResponsePage.to_json())

# convert the object into a dict
list_f24_response_page_dict = list_f24_response_page_instance.to_dict()
# create an instance of ListF24ResponsePage from a dict
list_f24_response_page_from_dict = ListF24ResponsePage.from_dict(list_f24_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


