# SendEInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SendEInvoiceRequestData**](SendEInvoiceRequestData.md) |  | [optional] 
**options** | [**SendEInvoiceRequestOptions**](SendEInvoiceRequestOptions.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.send_e_invoice_request import SendEInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendEInvoiceRequest from a JSON string
send_e_invoice_request_instance = SendEInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print SendEInvoiceRequest.to_json()

# convert the object into a dict
send_e_invoice_request_dict = send_e_invoice_request_instance.to_dict()
# create an instance of SendEInvoiceRequest from a dict
send_e_invoice_request_form_dict = send_e_invoice_request.from_dict(send_e_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


