# GetCompanyPlanUsageResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CompanyPlanUsage**](CompanyPlanUsage.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_company_plan_usage_response import GetCompanyPlanUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCompanyPlanUsageResponse from a JSON string
get_company_plan_usage_response_instance = GetCompanyPlanUsageResponse.from_json(json)
# print the JSON string representation of the object
print(GetCompanyPlanUsageResponse.to_json())

# convert the object into a dict
get_company_plan_usage_response_dict = get_company_plan_usage_response_instance.to_dict()
# create an instance of GetCompanyPlanUsageResponse from a dict
get_company_plan_usage_response_from_dict = GetCompanyPlanUsageResponse.from_dict(get_company_plan_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


