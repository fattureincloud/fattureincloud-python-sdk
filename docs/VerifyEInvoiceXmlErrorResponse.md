# VerifyEInvoiceXmlErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**VerifyEInvoiceXmlErrorResponseError**](VerifyEInvoiceXmlErrorResponseError.md) |  | [optional] 
**extra** | [**VerifyEInvoiceXmlErrorResponseExtra**](VerifyEInvoiceXmlErrorResponseExtra.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.verify_e_invoice_xml_error_response import VerifyEInvoiceXmlErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEInvoiceXmlErrorResponse from a JSON string
verify_e_invoice_xml_error_response_instance = VerifyEInvoiceXmlErrorResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyEInvoiceXmlErrorResponse.to_json())

# convert the object into a dict
verify_e_invoice_xml_error_response_dict = verify_e_invoice_xml_error_response_instance.to_dict()
# create an instance of VerifyEInvoiceXmlErrorResponse from a dict
verify_e_invoice_xml_error_response_from_dict = VerifyEInvoiceXmlErrorResponse.from_dict(verify_e_invoice_xml_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


