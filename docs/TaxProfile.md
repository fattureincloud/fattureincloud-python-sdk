# TaxProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_type** | **str** | The company type | [optional] 
**company_subtype** | **str** | The company subtype | [optional] 
**profession** | **str** | The profession | [optional] 
**regime** | **str** | The applied regime | [optional] 
**rivalsa_name** | **str** | The name of the rivalsa | [optional] 
**default_rivalsa** | **float** | The default rivalsa amount | [optional] 
**cassa_name** | **str** | The name of the cassa | [optional] 
**default_cassa** | **float** | The default cassa amount | [optional] 
**default_cassa_taxable** | **float** | The default taxable amount for the cassa | [optional] 
**cassa2_name** | **str** | The name of the second cassa | [optional] 
**default_cassa2** | **float** | The default second cassa amount | [optional] 
**default_cassa2_taxable** | **float** | The default taxable amount for the second cassa | [optional] 
**default_withholding_tax** | **float** | The default withholding tax | [optional] 
**default_withholding_tax_taxable** | **float** | The default taxable amount for the withholding tax | [optional] 
**default_other_withholding_tax** | **float** | The default other withholding tax | [optional] 
**enasarco** | **bool** | If it has enasarco | [optional] 
**enasarco_type** | **str** | The enasarco type | [optional] 
**contributions_percentage** | **float** | The contributions percentage | [optional] 
**profit_coefficient** | **float** | The profit coefficient | [optional] 
**med** | **bool** | If the health card system is active | [optional] 
**default_vat** | [**VatType**](VatType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.tax_profile import TaxProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TaxProfile from a JSON string
tax_profile_instance = TaxProfile.from_json(json)
# print the JSON string representation of the object
print(TaxProfile.to_json())

# convert the object into a dict
tax_profile_dict = tax_profile_instance.to_dict()
# create an instance of TaxProfile from a dict
tax_profile_from_dict = TaxProfile.from_dict(tax_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


