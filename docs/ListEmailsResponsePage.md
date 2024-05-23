# ListEmailsResponsePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Email]**](Email.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_emails_response_page import ListEmailsResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListEmailsResponsePage from a JSON string
list_emails_response_page_instance = ListEmailsResponsePage.from_json(json)
# print the JSON string representation of the object
print(ListEmailsResponsePage.to_json())

# convert the object into a dict
list_emails_response_page_dict = list_emails_response_page_instance.to_dict()
# create an instance of ListEmailsResponsePage from a dict
list_emails_response_page_from_dict = ListEmailsResponsePage.from_dict(list_emails_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


