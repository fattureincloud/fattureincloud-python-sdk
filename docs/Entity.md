# Entity



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**id** | **int** | Unique identifier | [optional] 
**code** | **str** | Code. | [optional] 
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
**country** | **str** | Country | [optional]  if omitted the server will use the default value of "Italia"
**email** | **str** | Email. | [optional] 
**certified_email** | **str** | Certified email. | [optional] 
**phone** | **str** | Phone. | [optional] 
**fax** | **str** | Fax. | [optional] 
**notes** | **str** | Extra notes. | [optional] 
**default_vat** | [**VatType**](VatType.md) |  | [optional] 
**default_payment_terms** | **int, none_type** | [Only for client] Default payment terms. | [optional] 
**default_payment_terms_type** | [**DefaultPaymentTermsType**](DefaultPaymentTermsType.md) |  | [optional] 
**default_payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**bank_name** | **str, none_type** | [Only for client] Bank name. | [optional] 
**bank_iban** | **str, none_type** | [Only for client] Iban. | [optional] 
**bank_swift_code** | **str, none_type** | [Only for client] Bank swift code. | [optional] 
**shipping_address** | **str, none_type** | [Only for client] Shipping address. | [optional] 
**e_invoice** | **bool, none_type** | [Only for client] Use e-invoices. | [optional]  if omitted the server will use the default value of False
**ei_code** | **str, none_type** | [Only for client] E-invoices code. | [optional] 
**created_at** | **str, none_type** |  | [optional] 
**updated_at** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


