# VerifyEInvoiceXmlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VerifyEInvoiceXmlResponseData**](VerifyEInvoiceXmlResponseData.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.verify_e_invoice_xml_response import VerifyEInvoiceXmlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEInvoiceXmlResponse from a JSON string
verify_e_invoice_xml_response_instance = VerifyEInvoiceXmlResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyEInvoiceXmlResponse.to_json())

# convert the object into a dict
verify_e_invoice_xml_response_dict = verify_e_invoice_xml_response_instance.to_dict()
# create an instance of VerifyEInvoiceXmlResponse from a dict
verify_e_invoice_xml_response_from_dict = VerifyEInvoiceXmlResponse.from_dict(verify_e_invoice_xml_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


