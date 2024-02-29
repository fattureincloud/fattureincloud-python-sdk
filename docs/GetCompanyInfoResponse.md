# GetCompanyInfoResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CompanyInfo**](CompanyInfo.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_company_info_response import GetCompanyInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanyInfoResponse from a JSON string
get_company_info_response_instance = GetCompanyInfoResponse.from_json(json)
# print the JSON string representation of the object
print GetCompanyInfoResponse.to_json()

# convert the object into a dict
get_company_info_response_dict = get_company_info_response_instance.to_dict()
# create an instance of GetCompanyInfoResponse from a dict
get_company_info_response_form_dict = get_company_info_response.from_dict(get_company_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


