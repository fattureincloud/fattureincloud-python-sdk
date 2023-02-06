# CompanyInfoPlanInfoFunctions

Access to functions for this company.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive** | **bool** |  | [optional] 
**cerved** | **bool** |  | [optional] 
**document_attachments** | **bool** |  | [optional] 
**e_invoice** | **bool** |  | [optional] 
**genius** | **bool** |  | [optional] 
**mail_tracking** | **bool** |  | [optional] 
**payment_notifications** | **bool** |  | [optional] 
**paypal** | **bool** |  | [optional] 
**receipts** | **bool** |  | [optional] 
**recurring** | **bool** |  | [optional] 
**smtp** | **bool** |  | [optional] 
**sofort** | **bool** |  | [optional] 
**stock** | **bool** |  | [optional] 
**subaccounts** | **bool** |  | [optional] 
**tessera_sanitaria** | **bool** |  | [optional] 
**ts_digital** | **bool** |  | [optional] 
**ts_invoice_trading** | **bool** |  | [optional] 
**ts_pay** | **bool** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.company_info_plan_info_functions import CompanyInfoPlanInfoFunctions

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInfoPlanInfoFunctions from a JSON string
company_info_plan_info_functions_instance = CompanyInfoPlanInfoFunctions.from_json(json)
# print the JSON string representation of the object
print CompanyInfoPlanInfoFunctions.to_json()

# convert the object into a dict
company_info_plan_info_functions_dict = company_info_plan_info_functions_instance.to_dict()
# create an instance of CompanyInfoPlanInfoFunctions from a dict
company_info_plan_info_functions_form_dict = company_info_plan_info_functions.from_dict(company_info_plan_info_functions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


