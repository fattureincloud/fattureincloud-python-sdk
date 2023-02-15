# CompanyInfoAccessInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**UserCompanyRole**](UserCompanyRole.md) |  | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**through_accountant** | **bool** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.company_info_access_info import CompanyInfoAccessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInfoAccessInfo from a JSON string
company_info_access_info_instance = CompanyInfoAccessInfo.from_json(json)
# print the JSON string representation of the object
print CompanyInfoAccessInfo.to_json()

# convert the object into a dict
company_info_access_info_dict = company_info_access_info_instance.to_dict()
# create an instance of CompanyInfoAccessInfo from a dict
company_info_access_info_form_dict = company_info_access_info.from_dict(company_info_access_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


