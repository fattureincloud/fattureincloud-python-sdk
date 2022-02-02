# Client



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Client name | 
**id** | **int** | Unique identifier | [optional] 
**code** | **str** | Client code. | [optional] 
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
**country** | **str** | Client country | [optional]  if omitted the server will use the default value of "Italia"
**email** | **str** | Client email. | [optional] 
**certified_email** | **str** | Client certified email. | [optional] 
**phone** | **str** | Client phone. | [optional] 
**fax** | **str** | Client fax. | [optional] 
**notes** | **str** | Extra notes. | [optional] 
**default_vat** | [**VatType**](VatType.md) |  | [optional] 
**default_payment_terms** | **int** |  | [optional] 
**default_payment_terms_type** | [**DefaultPaymentTermsType**](DefaultPaymentTermsType.md) |  | [optional] 
**default_payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**bank_name** | **str** | Client bank name. | [optional] 
**bank_iban** | **str** | Client iban. | [optional] 
**bank_swift_code** | **str** | Client bank swift code. | [optional] 
**shipping_address** | **str** | Client shipping address. | [optional] 
**e_invoice** | **bool** | Use e-invoices for this entity | [optional]  if omitted the server will use the default value of False
**ei_code** | **str** | E-invoice code | [optional] 
**discount_highlight** | **bool** | Discount Highlight. | [optional] 
**default_discount** | **float** | Default discount. | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


