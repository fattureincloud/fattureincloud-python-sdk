# ControlledCompany



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Company unique identifier. | [optional] 
**name** | **str** | Company name. | [optional] 
**type** | [**CompanyType**](CompanyType.md) |  | [optional] 
**access_token** | **str** | CompanyAuthentication token for this company. [Only if type&#x3D;company] | [optional] 
**connection_id** | **float** | Company connection id. | [optional] 
**tax_code** | **str** | Tax code. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.controlled_company import ControlledCompany

# TODO update the JSON string below
json = "{}"
# create an instance of ControlledCompany from a JSON string
controlled_company_instance = ControlledCompany.from_json(json)
# print the JSON string representation of the object
print ControlledCompany.to_json()

# convert the object into a dict
controlled_company_dict = controlled_company_instance.to_dict()
# create an instance of ControlledCompany from a dict
controlled_company_form_dict = controlled_company.from_dict(controlled_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


