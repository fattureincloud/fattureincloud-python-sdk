# SendEInvoiceRequestOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | If set to true the e-invoice will not be sent to the SDI. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.send_e_invoice_request_options import SendEInvoiceRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SendEInvoiceRequestOptions from a JSON string
send_e_invoice_request_options_instance = SendEInvoiceRequestOptions.from_json(json)
# print the JSON string representation of the object
print SendEInvoiceRequestOptions.to_json()

# convert the object into a dict
send_e_invoice_request_options_dict = send_e_invoice_request_options_instance.to_dict()
# create an instance of SendEInvoiceRequestOptions from a dict
send_e_invoice_request_options_form_dict = send_e_invoice_request_options.from_dict(send_e_invoice_request_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


