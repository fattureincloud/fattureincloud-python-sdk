# CompanyInfo



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Company unique identifier. | [optional] 
**name** | **str** | Company name. | [optional] 
**email** | **str** | Company email. | [optional] 
**type** | [**CompanyType**](CompanyType.md) |  | [optional] 
**access_info** | [**CompanyInfoAccessInfo**](CompanyInfoAccessInfo.md) |  | [optional] 
**plan_info** | [**CompanyInfoPlanInfo**](CompanyInfoPlanInfo.md) |  | [optional] 
**accountant_id** | **int** | Accountant unique identifier. | [optional] 
**is_accountant** | **bool** | Determine if the logged account is an accountant. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.company_info import CompanyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInfo from a JSON string
company_info_instance = CompanyInfo.from_json(json)
# print the JSON string representation of the object
print CompanyInfo.to_json()

# convert the object into a dict
company_info_dict = company_info_instance.to_dict()
# create an instance of CompanyInfo from a dict
company_info_form_dict = company_info.from_dict(company_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


