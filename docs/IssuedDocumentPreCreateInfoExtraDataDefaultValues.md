# IssuedDocumentPreCreateInfoExtraDataDefaultValues

Issued document extra data default values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ts_communication** | **bool** |  | [optional] 
**ts_tipo_spesa** | **str** |  | [optional] 
**ts_flag_tipo_spesa** | **int** |  | [optional] 
**ts_pagamento_tracciato** | **bool** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_pre_create_info_extra_data_default_values import IssuedDocumentPreCreateInfoExtraDataDefaultValues

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentPreCreateInfoExtraDataDefaultValues from a JSON string
issued_document_pre_create_info_extra_data_default_values_instance = IssuedDocumentPreCreateInfoExtraDataDefaultValues.from_json(json)
# print the JSON string representation of the object
print IssuedDocumentPreCreateInfoExtraDataDefaultValues.to_json()

# convert the object into a dict
issued_document_pre_create_info_extra_data_default_values_dict = issued_document_pre_create_info_extra_data_default_values_instance.to_dict()
# create an instance of IssuedDocumentPreCreateInfoExtraDataDefaultValues from a dict
issued_document_pre_create_info_extra_data_default_values_form_dict = issued_document_pre_create_info_extra_data_default_values.from_dict(issued_document_pre_create_info_extra_data_default_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


