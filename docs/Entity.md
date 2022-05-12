# Entity



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Unique identifier | [optional] 
**code** | **str, none_type** | Code. | [optional] 
**name** | **str, none_type** | Name | [optional] 
**type** | [**EntityType**](EntityType.md) |  | [optional] 
**first_name** | **str, none_type** | First name. | [optional] 
**last_name** | **str, none_type** | Last name. | [optional] 
**contact_person** | **str, none_type** |  | [optional] 
**vat_number** | **str, none_type** | Vat number | [optional] 
**tax_code** | **str, none_type** | Tax code. | [optional] 
**address_street** | **str, none_type** | Street address. | [optional] 
**address_postal_code** | **str, none_type** | Postal code. | [optional] 
**address_city** | **str, none_type** | City. | [optional] 
**address_province** | **str, none_type** | Province. | [optional] 
**address_extra** | **str, none_type** | Address extra info. | [optional] 
**country** | **str, none_type** | Country | [optional] 
**email** | **str, none_type** | Email. | [optional] 
**certified_email** | **str, none_type** | Certified email. | [optional] 
**phone** | **str, none_type** | Phone. | [optional] 
**fax** | **str, none_type** | Fax. | [optional] 
**notes** | **str, none_type** | Extra notes. | [optional] 
**default_vat** | [**VatType**](VatType.md) |  | [optional] 
**default_payment_terms** | **int, none_type** | [Only for client] Default payment terms. | [optional] 
**default_payment_terms_type** | [**DefaultPaymentTermsType**](DefaultPaymentTermsType.md) |  | [optional] 
**default_payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**bank_name** | **str, none_type** | [Only for client] Bank name. | [optional] 
**bank_iban** | **str, none_type** | [Only for client] Iban. | [optional] 
**bank_swift_code** | **str, none_type** | [Only for client] Bank swift code. | [optional] 
**shipping_address** | **str, none_type** | [Only for client] Shipping address. | [optional] 
**e_invoice** | **bool, none_type** | [Only for client] Use e-invoices. | [optional] 
**ei_code** | **str, none_type** | [Only for client] E-invoices code. | [optional] 
**has_intent_declaration** | **bool, none_type** | [Only for client] Has intent declaration. | [optional] 
**intent_declaration_protocol_number** | **date, none_type** | [Only for client] Intent declaration protocol number. | [optional] 
**intent_declaration_protocol_date** | **str, none_type** | [Only for client] Intent declaration protocol date. | [optional] 
**created_at** | **str, none_type** |  | [optional] 
**updated_at** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


