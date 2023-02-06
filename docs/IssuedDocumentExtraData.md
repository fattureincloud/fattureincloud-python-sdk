# IssuedDocumentExtraData

Extra data. TS fields follow the technical specifications provided by \"Sistema Tessera Sanitaria\".

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_sofort_button** | **bool** |  | [optional] 
**multifatture_sent** | **int** |  | [optional] 
**ts_communication** | **bool** |  | [optional] 
**ts_flag_tipo_spesa** | **float** | 1 &#x3D;&gt; TK (Ticket di pronto soccorso); 2 &#x3D;&gt; SR (Visita in intramoenia) | [optional] 
**ts_pagamento_tracciato** | **bool** |  | [optional] 
**ts_tipo_spesa** | **str** | Can be [ &#39;TK&#39;, &#39;FC&#39;, &#39;FV&#39;, &#39;SV&#39;, &#39;SP&#39;, &#39;AD&#39;, &#39;AS&#39;, &#39;SR&#39;, &#39;CT&#39;, &#39;PI&#39;, &#39;IC&#39;, &#39;AA&#39; ]. Refer to the technical specifications to learn more. | [optional] 
**ts_opposizione** | **bool** |  | [optional] 
**ts_status** | **int** |  | [optional] 
**ts_file_id** | **str** |  | [optional] 
**ts_sent_date** | **date** |  | [optional] 
**ts_full_amount** | **bool** |  | [optional] 
**imported_by** | **str** |  | [optional] 
**ts_single_sending** | **bool** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_extra_data import IssuedDocumentExtraData

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentExtraData from a JSON string
issued_document_extra_data_instance = IssuedDocumentExtraData.from_json(json)
# print the JSON string representation of the object
print IssuedDocumentExtraData.to_json()

# convert the object into a dict
issued_document_extra_data_dict = issued_document_extra_data_instance.to_dict()
# create an instance of IssuedDocumentExtraData from a dict
issued_document_extra_data_form_dict = issued_document_extra_data.from_dict(issued_document_extra_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


