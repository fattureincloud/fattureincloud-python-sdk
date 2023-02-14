# Supplier



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | [optional] 
**code** | **str** | Supplier code. | [optional] 
**name** | **str** | Supplier name. | [optional] 
**type** | [**SupplierType**](SupplierType.md) |  | [optional] 
**first_name** | **str** | Supplier first name. | [optional] 
**last_name** | **str** | Supplier last name. | [optional] 
**contact_person** | **str** |  | [optional] 
**vat_number** | **str** | Supplier vat number. | [optional] 
**tax_code** | **str** | Supplier tax code. | [optional] 
**address_street** | **str** | Supplier street address. | [optional] 
**address_postal_code** | **str** | Supplier postal code. | [optional] 
**address_city** | **str** | Supplier city. | [optional] 
**address_province** | **str** | Supplier province. | [optional] 
**address_extra** | **str** | Supplier address extra info. | [optional] 
**country** | **str** | Supplier country. | [optional] 
**email** | **str** | Supplier email. | [optional] 
**certified_email** | **str** | Supplier certified email. | [optional] 
**phone** | **str** | Supplier phone. | [optional] 
**fax** | **str** | Supplier fax. | [optional] 
**notes** | **str** | Supplier extra notes. | [optional] 
**bank_iban** | **str** | Supplier bank IBAN. | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.supplier import Supplier

# TODO update the JSON string below
json = "{}"
# create an instance of Supplier from a JSON string
supplier_instance = Supplier.from_json(json)
# print the JSON string representation of the object
print Supplier.to_json()

# convert the object into a dict
supplier_dict = supplier_instance.to_dict()
# create an instance of Supplier from a dict
supplier_form_dict = supplier.from_dict(supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


