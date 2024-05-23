# VerifyEInvoiceXmlErrorResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**validation_result** | [**VerifyEInvoiceXmlErrorResponseErrorValidationResult**](VerifyEInvoiceXmlErrorResponseErrorValidationResult.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.verify_e_invoice_xml_error_response_error import VerifyEInvoiceXmlErrorResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEInvoiceXmlErrorResponseError from a JSON string
verify_e_invoice_xml_error_response_error_instance = VerifyEInvoiceXmlErrorResponseError.from_json(json)
# print the JSON string representation of the object
print(VerifyEInvoiceXmlErrorResponseError.to_json())

# convert the object into a dict
verify_e_invoice_xml_error_response_error_dict = verify_e_invoice_xml_error_response_error_instance.to_dict()
# create an instance of VerifyEInvoiceXmlErrorResponseError from a dict
verify_e_invoice_xml_error_response_error_from_dict = VerifyEInvoiceXmlErrorResponseError.from_dict(verify_e_invoice_xml_error_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


