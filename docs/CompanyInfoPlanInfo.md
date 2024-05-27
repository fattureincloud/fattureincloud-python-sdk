# CompanyInfoPlanInfo

Company plan info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**CompanyInfoPlanInfoLimits**](CompanyInfoPlanInfoLimits.md) |  | [optional] 
**functions** | [**CompanyInfoPlanInfoFunctions**](CompanyInfoPlanInfoFunctions.md) |  | [optional] 
**functions_status** | [**CompanyInfoPlanInfoFunctionsStatus**](CompanyInfoPlanInfoFunctionsStatus.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.company_info_plan_info import CompanyInfoPlanInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInfoPlanInfo from a JSON string
company_info_plan_info_instance = CompanyInfoPlanInfo.from_json(json)
# print the JSON string representation of the object
print(CompanyInfoPlanInfo.to_json())

# convert the object into a dict
company_info_plan_info_dict = company_info_plan_info_instance.to_dict()
# create an instance of CompanyInfoPlanInfo from a dict
company_info_plan_info_from_dict = CompanyInfoPlanInfo.from_dict(company_info_plan_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


