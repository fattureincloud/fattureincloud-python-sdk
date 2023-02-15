# SendEInvoiceRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassa_type** | **str** | Value of TipoCassa used (optional, override the company default value). | [optional] 
**withholding_tax_causal** | **str** | Value of CausalePagamento used (optional, override the company default value). | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.send_e_invoice_request_data import SendEInvoiceRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of SendEInvoiceRequestData from a JSON string
send_e_invoice_request_data_instance = SendEInvoiceRequestData.from_json(json)
# print the JSON string representation of the object
print SendEInvoiceRequestData.to_json()

# convert the object into a dict
send_e_invoice_request_data_dict = send_e_invoice_request_data_instance.to_dict()
# create an instance of SendEInvoiceRequestData from a dict
send_e_invoice_request_data_form_dict = send_e_invoice_request_data.from_dict(send_e_invoice_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


