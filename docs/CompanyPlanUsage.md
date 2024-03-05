# CompanyPlanUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | Plan limit | [optional] 
**usage** | **float** | Plan usage | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.company_plan_usage import CompanyPlanUsage

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyPlanUsage from a JSON string
company_plan_usage_instance = CompanyPlanUsage.from_json(json)
# print the JSON string representation of the object
print CompanyPlanUsage.to_json()

# convert the object into a dict
company_plan_usage_dict = company_plan_usage_instance.to_dict()
# create an instance of CompanyPlanUsage from a dict
company_plan_usage_form_dict = company_plan_usage.from_dict(company_plan_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


