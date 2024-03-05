# SendEInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SendEInvoiceResponseData**](SendEInvoiceResponseData.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.send_e_invoice_response import SendEInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendEInvoiceResponse from a JSON string
send_e_invoice_response_instance = SendEInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print SendEInvoiceResponse.to_json()

# convert the object into a dict
send_e_invoice_response_dict = send_e_invoice_response_instance.to_dict()
# create an instance of SendEInvoiceResponse from a dict
send_e_invoice_response_form_dict = send_e_invoice_response.from_dict(send_e_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


