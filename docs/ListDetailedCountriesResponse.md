# ListDetailedCountriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DetailedCountry]**](DetailedCountry.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_detailed_countries_response import ListDetailedCountriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDetailedCountriesResponse from a JSON string
list_detailed_countries_response_instance = ListDetailedCountriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListDetailedCountriesResponse.to_json())

# convert the object into a dict
list_detailed_countries_response_dict = list_detailed_countries_response_instance.to_dict()
# create an instance of ListDetailedCountriesResponse from a dict
list_detailed_countries_response_from_dict = ListDetailedCountriesResponse.from_dict(list_detailed_countries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


