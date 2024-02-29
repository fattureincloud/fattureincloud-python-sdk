# ListUserCompaniesResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ListUserCompaniesResponseData**](ListUserCompaniesResponseData.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_user_companies_response import ListUserCompaniesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserCompaniesResponse from a JSON string
list_user_companies_response_instance = ListUserCompaniesResponse.from_json(json)
# print the JSON string representation of the object
print ListUserCompaniesResponse.to_json()

# convert the object into a dict
list_user_companies_response_dict = list_user_companies_response_instance.to_dict()
# create an instance of ListUserCompaniesResponse from a dict
list_user_companies_response_form_dict = list_user_companies_response.from_dict(list_user_companies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


