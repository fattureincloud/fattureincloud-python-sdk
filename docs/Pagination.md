# Pagination



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** | Current page number. | [optional] 
**first_page_url** | **str** | First page url. | [optional] 
**var_from** | **int** | First result of the page. | [optional] 
**last_page** | **int** | Last page number. | [optional] 
**last_page_url** | **str** | Last page url. | [optional] 
**next_page_url** | **str** | Next page url | [optional] 
**path** | **str** | Request path. | [optional] 
**per_page** | **int** | Number of result per page. | [optional] 
**prev_page_url** | **str** | Previous page url. | [optional] 
**to** | **int** | Last result of the page. | [optional] 
**total** | **int** | Total number of results | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print Pagination.to_json()

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_form_dict = pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


