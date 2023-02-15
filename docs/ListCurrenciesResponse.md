# ListCurrenciesResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Currency]**](Currency.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_currencies_response import ListCurrenciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCurrenciesResponse from a JSON string
list_currencies_response_instance = ListCurrenciesResponse.from_json(json)
# print the JSON string representation of the object
print ListCurrenciesResponse.to_json()

# convert the object into a dict
list_currencies_response_dict = list_currencies_response_instance.to_dict()
# create an instance of ListCurrenciesResponse from a dict
list_currencies_response_form_dict = list_currencies_response.from_dict(list_currencies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


