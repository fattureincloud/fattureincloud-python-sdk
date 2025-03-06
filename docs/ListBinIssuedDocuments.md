# ListBinIssuedDocuments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IssuedDocument]**](IssuedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_bin_issued_documents import ListBinIssuedDocuments

# TODO update the JSON string below
json = "{}"
# create an instance of ListBinIssuedDocuments from a JSON string
list_bin_issued_documents_instance = ListBinIssuedDocuments.from_json(json)
# print the JSON string representation of the object
print(ListBinIssuedDocuments.to_json())

# convert the object into a dict
list_bin_issued_documents_dict = list_bin_issued_documents_instance.to_dict()
# create an instance of ListBinIssuedDocuments from a dict
list_bin_issued_documents_from_dict = ListBinIssuedDocuments.from_dict(list_bin_issued_documents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


