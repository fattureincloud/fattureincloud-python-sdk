# VatType



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | [optional] 
**value** | **float** | [Read Only] Percentual value. | [optional] 
**description** | **str** | Short description. | [optional] 
**notes** | **str** | Long description and notes shown in documents. | [optional] 
**e_invoice** | **bool** | Usable for e-invoices. | [optional] 
**ei_type** | **str** | E-invoice type (natura). | [optional] 
**ei_description** | **str** | E-invoice description. | [optional] 
**editable** | **bool** | [Read Only] Determine if this vat type is editable. | [optional] [readonly] 
**is_disabled** | **bool** | Determine if the vat type is disabled. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.vat_type import VatType

# TODO update the JSON string below
json = "{}"
# create an instance of VatType from a JSON string
vat_type_instance = VatType.from_json(json)
# print the JSON string representation of the object
print VatType.to_json()

# convert the object into a dict
vat_type_dict = vat_type_instance.to_dict()
# create an instance of VatType from a dict
vat_type_form_dict = vat_type.from_dict(vat_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


