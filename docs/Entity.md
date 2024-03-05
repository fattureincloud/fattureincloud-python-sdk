# Entity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Entity id | [optional] 
**code** | **str** | Entity code | [optional] 
**name** | **str** | Entity name | [optional] 
**type** | [**EntityType**](EntityType.md) |  | [optional] 
**first_name** | **str** | Entity first name | [optional] 
**last_name** | **str** | Entity last name | [optional] 
**contact_person** | **str** | Entity contact person | [optional] 
**vat_number** | **str** | Entity vat number | [optional] 
**tax_code** | **str** | Entity tax code | [optional] 
**address_street** | **str** | Entitity address street | [optional] 
**address_postal_code** | **str** | Entity address postal code | [optional] 
**address_city** | **str** | Entity address city | [optional] 
**address_province** | **str** | Entity address province | [optional] 
**address_extra** | **str** | Entity address extra info | [optional] 
**country** | **str** | Entity country | [optional] 
**country_iso** | **str** | Entity country iso code | [optional] 
**email** | **str** | Entity email | [optional] 
**certified_email** | **str** | Entity certified email | [optional] 
**phone** | **str** | Entity phone | [optional] 
**fax** | **str** | Entity fax | [optional] 
**notes** | **str** | Entity extra | [optional] 
**default_payment_terms** | **int** | [Only for client] Client default payment terms | [optional] 
**default_vat** | [**VatType**](VatType.md) |  | [optional] 
**default_payment_terms_type** | [**PaymentTermsType**](PaymentTermsType.md) |  | [optional] 
**default_payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**bank_name** | **str** | [Only for client] Client bank name | [optional] 
**bank_iban** | **str** | [Only for client] Client bank iban | [optional] 
**bank_swift_code** | **str** | [Only for client] Client bank swift code | [optional] 
**shipping_address** | **str** | [Only for client] Client Shipping address | [optional] 
**e_invoice** | **bool** | [Only for client] Use e-invoices. | [optional] 
**ei_code** | **str** | [Only for client] E-invoices code. | [optional] 
**has_intent_declaration** | **bool** | [Only for client] Has intent declaration. | [optional] 
**intent_declaration_protocol_number** | **str** | [Only for client] Client intent declaration protocol number | [optional] 
**intent_declaration_protocol_date** | **date** | [Only for client] Client intent declaration protocol date | [optional] 
**created_at** | **str** | Entity creation date | [optional] 
**updated_at** | **str** | Entity last update date | [optional] 

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


