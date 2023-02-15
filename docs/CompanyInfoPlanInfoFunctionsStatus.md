# CompanyInfoPlanInfoFunctionsStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ts_digital** | [**FunctionStatus**](FunctionStatus.md) |  | [optional] 
**ts_pay** | [**FunctionStatus**](FunctionStatus.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.company_info_plan_info_functions_status import CompanyInfoPlanInfoFunctionsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInfoPlanInfoFunctionsStatus from a JSON string
company_info_plan_info_functions_status_instance = CompanyInfoPlanInfoFunctionsStatus.from_json(json)
# print the JSON string representation of the object
print CompanyInfoPlanInfoFunctionsStatus.to_json()

# convert the object into a dict
company_info_plan_info_functions_status_dict = company_info_plan_info_functions_status_instance.to_dict()
# create an instance of CompanyInfoPlanInfoFunctionsStatus from a dict
company_info_plan_info_functions_status_form_dict = company_info_plan_info_functions_status.from_dict(company_info_plan_info_functions_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


