# ListUserCompaniesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**companies** | [**List[Company]**](Company.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_user_companies_response_data import ListUserCompaniesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserCompaniesResponseData from a JSON string
list_user_companies_response_data_instance = ListUserCompaniesResponseData.from_json(json)
# print the JSON string representation of the object
print(ListUserCompaniesResponseData.to_json())

# convert the object into a dict
list_user_companies_response_data_dict = list_user_companies_response_data_instance.to_dict()
# create an instance of ListUserCompaniesResponseData from a dict
list_user_companies_response_data_from_dict = ListUserCompaniesResponseData.from_dict(list_user_companies_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


