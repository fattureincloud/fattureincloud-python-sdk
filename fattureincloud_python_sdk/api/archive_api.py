"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.19
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from fattureincloud_python_sdk.api_client import ApiClient, Endpoint as _Endpoint
from fattureincloud_python_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from fattureincloud_python_sdk.model.create_archive_document_request import (
    CreateArchiveDocumentRequest,
)
from fattureincloud_python_sdk.model.create_archive_document_response import (
    CreateArchiveDocumentResponse,
)
from fattureincloud_python_sdk.model.get_archive_document_response import (
    GetArchiveDocumentResponse,
)
from fattureincloud_python_sdk.model.list_archive_documents_response import (
    ListArchiveDocumentsResponse,
)
from fattureincloud_python_sdk.model.modify_archive_document_request import (
    ModifyArchiveDocumentRequest,
)
from fattureincloud_python_sdk.model.modify_archive_document_response import (
    ModifyArchiveDocumentResponse,
)
from fattureincloud_python_sdk.model.upload_archive_attachment_response import (
    UploadArchiveAttachmentResponse,
)


class ArchiveApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_archive_document_endpoint = _Endpoint(
            settings={
                "response_type": (CreateArchiveDocumentResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/archive",
                "operation_id": "create_archive_document",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "create_archive_document_request",
                ],
                "required": [
                    "company_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "company_id": (int,),
                    "create_archive_document_request": (CreateArchiveDocumentRequest,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                },
                "location_map": {
                    "company_id": "path",
                    "create_archive_document_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.delete_archive_document_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/archive/{document_id}",
                "operation_id": "delete_archive_document",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "document_id",
                ],
                "required": [
                    "company_id",
                    "document_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "company_id": (int,),
                    "document_id": (int,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                    "document_id": "document_id",
                },
                "location_map": {
                    "company_id": "path",
                    "document_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": [],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_archive_document_endpoint = _Endpoint(
            settings={
                "response_type": (GetArchiveDocumentResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/archive/{document_id}",
                "operation_id": "get_archive_document",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "document_id",
                    "fields",
                    "fieldset",
                ],
                "required": [
                    "company_id",
                    "document_id",
                ],
                "nullable": [],
                "enum": [
                    "fieldset",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("fieldset",): {"BASIC": "basic", "DETAILED": "detailed"},
                },
                "openapi_types": {
                    "company_id": (int,),
                    "document_id": (int,),
                    "fields": (str,),
                    "fieldset": (str,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                    "document_id": "document_id",
                    "fields": "fields",
                    "fieldset": "fieldset",
                },
                "location_map": {
                    "company_id": "path",
                    "document_id": "path",
                    "fields": "query",
                    "fieldset": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.list_archive_documents_endpoint = _Endpoint(
            settings={
                "response_type": (ListArchiveDocumentsResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/archive",
                "operation_id": "list_archive_documents",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "fields",
                    "fieldset",
                    "sort",
                    "page",
                    "per_page",
                    "q",
                ],
                "required": [
                    "company_id",
                ],
                "nullable": [],
                "enum": [
                    "fieldset",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("fieldset",): {"BASIC": "basic", "DETAILED": "detailed"},
                },
                "openapi_types": {
                    "company_id": (int,),
                    "fields": (str,),
                    "fieldset": (str,),
                    "sort": (str,),
                    "page": (int,),
                    "per_page": (int,),
                    "q": (str,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                    "fields": "fields",
                    "fieldset": "fieldset",
                    "sort": "sort",
                    "page": "page",
                    "per_page": "per_page",
                    "q": "q",
                },
                "location_map": {
                    "company_id": "path",
                    "fields": "query",
                    "fieldset": "query",
                    "sort": "query",
                    "page": "query",
                    "per_page": "query",
                    "q": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.modify_archive_document_endpoint = _Endpoint(
            settings={
                "response_type": (ModifyArchiveDocumentResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/archive/{document_id}",
                "operation_id": "modify_archive_document",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "document_id",
                    "modify_archive_document_request",
                ],
                "required": [
                    "company_id",
                    "document_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "company_id": (int,),
                    "document_id": (int,),
                    "modify_archive_document_request": (ModifyArchiveDocumentRequest,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                    "document_id": "document_id",
                },
                "location_map": {
                    "company_id": "path",
                    "document_id": "path",
                    "modify_archive_document_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.upload_archive_document_attachment_endpoint = _Endpoint(
            settings={
                "response_type": (UploadArchiveAttachmentResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/archive/attachment",
                "operation_id": "upload_archive_document_attachment",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "filename",
                    "attachment",
                ],
                "required": [
                    "company_id",
                ],
                "nullable": [
                    "filename",
                    "attachment",
                ],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "company_id": (int,),
                    "filename": (
                        str,
                        none_type,
                    ),
                    "attachment": (
                        file_type,
                        none_type,
                    ),
                },
                "attribute_map": {
                    "company_id": "company_id",
                    "filename": "filename",
                    "attachment": "attachment",
                },
                "location_map": {
                    "company_id": "path",
                    "filename": "form",
                    "attachment": "form",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["multipart/form-data"],
            },
            api_client=api_client,
        )

    def create_archive_document(self, company_id, **kwargs):
        """Create Archive Document  # noqa: E501

        Creates a new archive document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_archive_document(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            create_archive_document_request (CreateArchiveDocumentRequest): The Archive Document.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CreateArchiveDocumentResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["company_id"] = company_id
        return self.create_archive_document_endpoint.call_with_http_info(**kwargs)

    def delete_archive_document(self, company_id, document_id, **kwargs):
        """Delete Archive Document  # noqa: E501

        Deletes the specified archive document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_archive_document(company_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            document_id (int): The ID of the document.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["company_id"] = company_id
        kwargs["document_id"] = document_id
        return self.delete_archive_document_endpoint.call_with_http_info(**kwargs)

    def get_archive_document(self, company_id, document_id, **kwargs):
        """Get Archive Document  # noqa: E501

        Gets the specified archive document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_archive_document(company_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            document_id (int): The ID of the document.

        Keyword Args:
            fields (str): List of comma-separated fields.. [optional]
            fieldset (str): Name of the fieldset.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetArchiveDocumentResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["company_id"] = company_id
        kwargs["document_id"] = document_id
        return self.get_archive_document_endpoint.call_with_http_info(**kwargs)

    def list_archive_documents(self, company_id, **kwargs):
        """List Archive Documents  # noqa: E501

        Lists the archive documents.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_archive_documents(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            fields (str): List of comma-separated fields.. [optional]
            fieldset (str): Name of the fieldset.. [optional]
            sort (str): List of comma-separated fields for result sorting (minus for desc sorting).. [optional]
            page (int): The page to retrieve.. [optional] if omitted the server will use the default value of 1
            per_page (int): The size of the page.. [optional] if omitted the server will use the default value of 5
            q (str): Query for filtering the results.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ListArchiveDocumentsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["company_id"] = company_id
        return self.list_archive_documents_endpoint.call_with_http_info(**kwargs)

    def modify_archive_document(self, company_id, document_id, **kwargs):
        """Modify Archive Document  # noqa: E501

        Modifies the specified archive document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_archive_document(company_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            document_id (int): The ID of the document.

        Keyword Args:
            modify_archive_document_request (ModifyArchiveDocumentRequest): Modified Archive Document. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ModifyArchiveDocumentResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["company_id"] = company_id
        kwargs["document_id"] = document_id
        return self.modify_archive_document_endpoint.call_with_http_info(**kwargs)

    def upload_archive_document_attachment(self, company_id, **kwargs):
        """Upload Archive Document Attachment  # noqa: E501

        Uploads an attachment destined to an archive document. The actual association between the document and the attachment must be implemented separately, using the returned token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_archive_document_attachment(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            filename (str, none_type): Name of the file.. [optional]
            attachment (file_type, none_type): Valid format: .png, .jpg, .gif, .pdf, .zip, .xls, .xlsx, .doc, .docx. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            UploadArchiveAttachmentResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["company_id"] = company_id
        return self.upload_archive_document_attachment_endpoint.call_with_http_info(
            **kwargs
        )
