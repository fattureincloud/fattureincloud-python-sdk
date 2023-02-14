# GetNewIssuedDocumentTotalsResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocumentTotals**](IssuedDocumentTotals.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_new_issued_document_totals_response import GetNewIssuedDocumentTotalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewIssuedDocumentTotalsResponse from a JSON string
get_new_issued_document_totals_response_instance = GetNewIssuedDocumentTotalsResponse.from_json(json)
# print the JSON string representation of the object
print GetNewIssuedDocumentTotalsResponse.to_json()

# convert the object into a dict
get_new_issued_document_totals_response_dict = get_new_issued_document_totals_response_instance.to_dict()
# create an instance of GetNewIssuedDocumentTotalsResponse from a dict
get_new_issued_document_totals_response_form_dict = get_new_issued_document_totals_response.from_dict(get_new_issued_document_totals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


