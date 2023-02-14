# ListSuppliersResponsePage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Supplier]**](Supplier.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_suppliers_response_page import ListSuppliersResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListSuppliersResponsePage from a JSON string
list_suppliers_response_page_instance = ListSuppliersResponsePage.from_json(json)
# print the JSON string representation of the object
print ListSuppliersResponsePage.to_json()

# convert the object into a dict
list_suppliers_response_page_dict = list_suppliers_response_page_instance.to_dict()
# create an instance of ListSuppliersResponsePage from a dict
list_suppliers_response_page_form_dict = list_suppliers_response_page.from_dict(list_suppliers_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


