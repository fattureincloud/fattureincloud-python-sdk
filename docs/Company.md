# Company


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Company id | [optional] 
**name** | **str** | Company name | [optional] 
**type** | [**CompanyType**](CompanyType.md) |  | [optional] 
**access_token** | **str** | Company authentication token for this company. [Only if type&#x3D;company] | [optional] 
**controlled_companies** | [**List[ControlledCompany]**](ControlledCompany.md) | Company list of controlled companies [Only if type&#x3D;accountant] | [optional] 
**fic_license_expire** | **date** |  | [optional] 
**fic_plan** | [**FattureInCloudPlanType**](FattureInCloudPlanType.md) |  | [optional] 
**connection_id** | **int** | Company connection id | [optional] 
**tax_code** | **str** | Company tax code | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print Company.to_json()

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_form_dict = company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


