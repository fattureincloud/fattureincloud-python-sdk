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
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


