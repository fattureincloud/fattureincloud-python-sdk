# VatType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Vat type id | [optional] 
**value** | **float** | [Read Only] Vat type percentual value | [optional] 
**description** | **str** | Vat type short description | [optional] 
**notes** | **str** | Vat type notes shown in documents | [optional] 
**e_invoice** | **bool** | Vat type is usable for e-invoices | [optional] 
**ei_type** | **str** | Vat type e-invoice type (natura) | [optional] 
**ei_description** | **str** | Vat type e-invoice description | [optional] 
**editable** | **bool** | [Read Only] Is the vat type is editable. | [optional] [readonly] 
**is_disabled** | **bool** | Is the vat type disabled | [optional] 
**default** | **bool** | If the vat type is default | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.vat_type import VatType

# TODO update the JSON string below
json = "{}"
# create an instance of VatType from a JSON string
vat_type_instance = VatType.from_json(json)
# print the JSON string representation of the object
print(VatType.to_json())

# convert the object into a dict
vat_type_dict = vat_type_instance.to_dict()
# create an instance of VatType from a dict
vat_type_from_dict = VatType.from_dict(vat_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


