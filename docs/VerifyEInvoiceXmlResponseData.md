# VerifyEInvoiceXmlResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Determine if the invoice XML is valid. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.verify_e_invoice_xml_response_data import VerifyEInvoiceXmlResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEInvoiceXmlResponseData from a JSON string
verify_e_invoice_xml_response_data_instance = VerifyEInvoiceXmlResponseData.from_json(json)
# print the JSON string representation of the object
print VerifyEInvoiceXmlResponseData.to_json()

# convert the object into a dict
verify_e_invoice_xml_response_data_dict = verify_e_invoice_xml_response_data_instance.to_dict()
# create an instance of VerifyEInvoiceXmlResponseData from a dict
verify_e_invoice_xml_response_data_form_dict = verify_e_invoice_xml_response_data.from_dict(verify_e_invoice_xml_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


