# SendEInvoiceResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Response message. | [optional] 
**var_date** | **str** | E-invoice sent date. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.send_e_invoice_response_data import SendEInvoiceResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SendEInvoiceResponseData from a JSON string
send_e_invoice_response_data_instance = SendEInvoiceResponseData.from_json(json)
# print the JSON string representation of the object
print(SendEInvoiceResponseData.to_json())

# convert the object into a dict
send_e_invoice_response_data_dict = send_e_invoice_response_data_instance.to_dict()
# create an instance of SendEInvoiceResponseData from a dict
send_e_invoice_response_data_from_dict = SendEInvoiceResponseData.from_dict(send_e_invoice_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


