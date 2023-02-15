# ReceivedDocumentEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Entity unique identifier. | [optional] 
**name** | **str** | Entity name. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.received_document_entity import ReceivedDocumentEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivedDocumentEntity from a JSON string
received_document_entity_instance = ReceivedDocumentEntity.from_json(json)
# print the JSON string representation of the object
print ReceivedDocumentEntity.to_json()

# convert the object into a dict
received_document_entity_dict = received_document_entity_instance.to_dict()
# create an instance of ReceivedDocumentEntity from a dict
received_document_entity_form_dict = received_document_entity.from_dict(received_document_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


