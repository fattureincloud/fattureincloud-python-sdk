# ListCitiesResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[City]**](City.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_cities_response import ListCitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCitiesResponse from a JSON string
list_cities_response_instance = ListCitiesResponse.from_json(json)
# print the JSON string representation of the object
print ListCitiesResponse.to_json()

# convert the object into a dict
list_cities_response_dict = list_cities_response_instance.to_dict()
# create an instance of ListCitiesResponse from a dict
list_cities_response_form_dict = list_cities_response.from_dict(list_cities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


