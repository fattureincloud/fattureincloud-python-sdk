# IssuedDocumentPreCreateInfoDefaultValues

Default values for the document.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_template** | [**DocumentTemplate**](DocumentTemplate.md) |  | [optional] 
**dn_template** | [**DocumentTemplate**](DocumentTemplate.md) |  | [optional] 
**ai_template** | [**DocumentTemplate**](DocumentTemplate.md) |  | [optional] 
**notes** | **str** | Default notes. | [optional] 
**rivalsa** | **float** | Default rivalsa percentage. | [optional] 
**cassa** | **float** | Default cassa percentage. | [optional] 
**withholding_tax** | **float** | Default withholding tax percentage. | [optional] 
**withholding_tax_taxable** | **float** | Default withholding tax taxable percentage. | [optional] 
**other_withholding_tax** | **float** | Default other withholding tax percentage. | [optional] 
**use_gross_prices** | **bool** | Use gross price by default. | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_pre_create_info_default_values import IssuedDocumentPreCreateInfoDefaultValues

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentPreCreateInfoDefaultValues from a JSON string
issued_document_pre_create_info_default_values_instance = IssuedDocumentPreCreateInfoDefaultValues.from_json(json)
# print the JSON string representation of the object
print IssuedDocumentPreCreateInfoDefaultValues.to_json()

# convert the object into a dict
issued_document_pre_create_info_default_values_dict = issued_document_pre_create_info_default_values_instance.to_dict()
# create an instance of IssuedDocumentPreCreateInfoDefaultValues from a dict
issued_document_pre_create_info_default_values_form_dict = issued_document_pre_create_info_default_values.from_dict(issued_document_pre_create_info_default_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


