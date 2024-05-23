# ListClientsResponsePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Client]**](Client.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_clients_response_page import ListClientsResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListClientsResponsePage from a JSON string
list_clients_response_page_instance = ListClientsResponsePage.from_json(json)
# print the JSON string representation of the object
print(ListClientsResponsePage.to_json())

# convert the object into a dict
list_clients_response_page_dict = list_clients_response_page_instance.to_dict()
# create an instance of ListClientsResponsePage from a dict
list_clients_response_page_from_dict = ListClientsResponsePage.from_dict(list_clients_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


