# GetExistingReceivedDocumentTotalsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceivedDocumentTotals**](ReceivedDocumentTotals.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_existing_received_document_totals_response import GetExistingReceivedDocumentTotalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExistingReceivedDocumentTotalsResponse from a JSON string
get_existing_received_document_totals_response_instance = GetExistingReceivedDocumentTotalsResponse.from_json(json)
# print the JSON string representation of the object
print GetExistingReceivedDocumentTotalsResponse.to_json()

# convert the object into a dict
get_existing_received_document_totals_response_dict = get_existing_received_document_totals_response_instance.to_dict()
# create an instance of GetExistingReceivedDocumentTotalsResponse from a dict
get_existing_received_document_totals_response_form_dict = get_existing_received_document_totals_response.from_dict(get_existing_received_document_totals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


