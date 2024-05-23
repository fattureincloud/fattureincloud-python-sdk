# ListLanguagesResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Language]**](Language.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_languages_response import ListLanguagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListLanguagesResponse from a JSON string
list_languages_response_instance = ListLanguagesResponse.from_json(json)
# print the JSON string representation of the object
print(ListLanguagesResponse.to_json())

# convert the object into a dict
list_languages_response_dict = list_languages_response_instance.to_dict()
# create an instance of ListLanguagesResponse from a dict
list_languages_response_from_dict = ListLanguagesResponse.from_dict(list_languages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


