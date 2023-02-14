# GetExistingIssuedDocumentTotalsResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocumentTotals**](IssuedDocumentTotals.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_existing_issued_document_totals_response import GetExistingIssuedDocumentTotalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExistingIssuedDocumentTotalsResponse from a JSON string
get_existing_issued_document_totals_response_instance = GetExistingIssuedDocumentTotalsResponse.from_json(json)
# print the JSON string representation of the object
print GetExistingIssuedDocumentTotalsResponse.to_json()

# convert the object into a dict
get_existing_issued_document_totals_response_dict = get_existing_issued_document_totals_response_instance.to_dict()
# create an instance of GetExistingIssuedDocumentTotalsResponse from a dict
get_existing_issued_document_totals_response_form_dict = get_existing_issued_document_totals_response.from_dict(get_existing_issued_document_totals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


