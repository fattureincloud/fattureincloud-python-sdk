# Entity



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | [optional] 
**code** | **str** | Code. | [optional] 
**name** | **str** | Name | [optional] 
**type** | [**EntityType**](EntityType.md) |  | [optional] 
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**contact_person** | **str** |  | [optional] 
**vat_number** | **str** | Vat number | [optional] 
**tax_code** | **str** | Tax code. | [optional] 
**address_street** | **str** | Street address. | [optional] 
**address_postal_code** | **str** | Postal code. | [optional] 
**address_city** | **str** | City. | [optional] 
**address_province** | **str** | Province. | [optional] 
**address_extra** | **str** | Address extra info. | [optional] 
**country** | **str** | Country | [optional] 
**country_iso** | **str** | Country Iso | [optional] 
**email** | **str** | Email. | [optional] 
**certified_email** | **str** | Certified email. | [optional] 
**phone** | **str** | Phone. | [optional] 
**fax** | **str** | Fax. | [optional] 
**notes** | **str** | Extra notes. | [optional] 
**default_vat** | [**VatType**](VatType.md) |  | [optional] 
**default_payment_terms** | **int** | [Only for client] Default payment terms. | [optional] 
**default_payment_terms_type** | [**PaymentTermsType**](PaymentTermsType.md) |  | [optional] 
**default_payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**bank_name** | **str** | [Only for client] Bank name. | [optional] 
**bank_iban** | **str** | [Only for client] Iban. | [optional] 
**bank_swift_code** | **str** | [Only for client] Bank swift code. | [optional] 
**shipping_address** | **str** | [Only for client] Shipping address. | [optional] 
**e_invoice** | **bool** | [Only for client] Use e-invoices. | [optional] 
**ei_code** | **str** | [Only for client] E-invoices code. | [optional] 
**has_intent_declaration** | **bool** | [Only for client] Has intent declaration. | [optional] 
**intent_declaration_protocol_number** | **str** | [Only for client] Intent declaration protocol number. | [optional] 
**intent_declaration_protocol_date** | **date** | [Only for client] Intent declaration protocol date. | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.entity import Entity

# TODO update the JSON string below
json = "{}"
# create an instance of Entity from a JSON string
entity_instance = Entity.from_json(json)
# print the JSON string representation of the object
print Entity.to_json()

# convert the object into a dict
entity_dict = entity_instance.to_dict()
# create an instance of Entity from a dict
entity_form_dict = entity.from_dict(entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


