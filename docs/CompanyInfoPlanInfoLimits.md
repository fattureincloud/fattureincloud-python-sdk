# CompanyInfoPlanInfoLimits

Company plan limits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | **int** | Company plan clients limits | [optional] 
**suppliers** | **int** | Company plan suppliers limits | [optional] 
**products** | **int** | Company plan products limits | [optional] 
**documents** | **int** | Company plan documents limits | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.company_info_plan_info_limits import CompanyInfoPlanInfoLimits

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInfoPlanInfoLimits from a JSON string
company_info_plan_info_limits_instance = CompanyInfoPlanInfoLimits.from_json(json)
# print the JSON string representation of the object
print(CompanyInfoPlanInfoLimits.to_json())

# convert the object into a dict
company_info_plan_info_limits_dict = company_info_plan_info_limits_instance.to_dict()
# create an instance of CompanyInfoPlanInfoLimits from a dict
company_info_plan_info_limits_from_dict = CompanyInfoPlanInfoLimits.from_dict(company_info_plan_info_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


