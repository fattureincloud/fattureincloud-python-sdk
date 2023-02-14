# Client



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | [optional] 
**code** | **str** | Client code. | [optional] 
**name** | **str** | Client name | [optional] 
**type** | [**ClientType**](ClientType.md) |  | [optional] 
**first_name** | **str** | Client first name. | [optional] 
**last_name** | **str** | Client last name. | [optional] 
**contact_person** | **str** |  | [optional] 
**vat_number** | **str** | Client vat number | [optional] 
**tax_code** | **str** | Client tax code. | [optional] 
**address_street** | **str** | Client street address. | [optional] 
**address_postal_code** | **str** | Client postal code. | [optional] 
**address_city** | **str** | Client city. | [optional] 
**address_province** | **str** | Client province. | [optional] 
**address_extra** | **str** | Client address extra info. | [optional] 
**country** | **str** | Client country | [optional] 
**email** | **str** | Client email. | [optional] 
**certified_email** | **str** | Client certified email. | [optional] 
**phone** | **str** | Client phone. | [optional] 
**fax** | **str** | Client fax. | [optional] 
**notes** | **str** | Extra notes. | [optional] 
**default_vat** | [**VatType**](VatType.md) |  | [optional] 
**default_payment_terms** | **int** |  | [optional] 
**default_payment_terms_type** | [**PaymentTermsType**](PaymentTermsType.md) |  | [optional] 
**default_payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**bank_name** | **str** | Client bank name. | [optional] 
**bank_iban** | **str** | Client iban. | [optional] 
**bank_swift_code** | **str** | Client bank swift code. | [optional] 
**shipping_address** | **str** | Client shipping address. | [optional] 
**e_invoice** | **bool** | Use e-invoices for this entity | [optional] 
**ei_code** | **str** | E-invoice code | [optional] 
**discount_highlight** | **bool** | Discount Highlight. | [optional] 
**default_discount** | **float** | Default discount. | [optional] 
**has_intent_declaration** | **bool** | Has intent declaration. | [optional] 
**intent_declaration_protocol_number** | **str** | Intent declaration protocol number. | [optional] 
**intent_declaration_protocol_date** | **date** | Intent declaration protocol date. | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.client import Client

# TODO update the JSON string below
json = "{}"
# create an instance of Client from a JSON string
client_instance = Client.from_json(json)
# print the JSON string representation of the object
print Client.to_json()

# convert the object into a dict
client_dict = client_instance.to_dict()
# create an instance of Client from a dict
client_form_dict = client.from_dict(client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


