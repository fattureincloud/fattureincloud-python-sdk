# GetNewIssuedDocumentTotalsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocument**](IssuedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_new_issued_document_totals_request import GetNewIssuedDocumentTotalsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewIssuedDocumentTotalsRequest from a JSON string
get_new_issued_document_totals_request_instance = GetNewIssuedDocumentTotalsRequest.from_json(json)
# print the JSON string representation of the object
print(GetNewIssuedDocumentTotalsRequest.to_json())

# convert the object into a dict
get_new_issued_document_totals_request_dict = get_new_issued_document_totals_request_instance.to_dict()
# create an instance of GetNewIssuedDocumentTotalsRequest from a dict
get_new_issued_document_totals_request_from_dict = GetNewIssuedDocumentTotalsRequest.from_dict(get_new_issued_document_totals_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


