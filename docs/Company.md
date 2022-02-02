# Company



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Company unique identifier. | [optional] 
**name** | **str** | Company name. | [optional] 
**type** | [**CompanyType**](CompanyType.md) |  | [optional] 
**access_token** | **str** | CompanyAuthentication token for this company. [Only if type&#x3D;company] | [optional] 
**controlled_companies** | [**[ControlledCompany]**](ControlledCompany.md) | List of controlled companies. [Only if type&#x3D;accountant] | [optional] 
**connection_id** | **int** | Company connection id. | [optional] 
**tax_code** | **str** | Tax code. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


