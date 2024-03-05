# GetNewReceivedDocumentTotalsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceivedDocumentTotals**](ReceivedDocumentTotals.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_new_received_document_totals_response import GetNewReceivedDocumentTotalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewReceivedDocumentTotalsResponse from a JSON string
get_new_received_document_totals_response_instance = GetNewReceivedDocumentTotalsResponse.from_json(json)
# print the JSON string representation of the object
print GetNewReceivedDocumentTotalsResponse.to_json()

# convert the object into a dict
get_new_received_document_totals_response_dict = get_new_received_document_totals_response_instance.to_dict()
# create an instance of GetNewReceivedDocumentTotalsResponse from a dict
get_new_received_document_totals_response_form_dict = get_new_received_document_totals_response.from_dict(get_new_received_document_totals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


