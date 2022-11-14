"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.21
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
from fattureincloud_python_sdk.model.create_cashbook_entry_request import (
    CreateCashbookEntryRequest,
)
from fattureincloud_python_sdk.model.create_cashbook_entry_response import (
    CreateCashbookEntryResponse,
)
from fattureincloud_python_sdk.model.get_cashbook_entry_response import (
    GetCashbookEntryResponse,
)
from fattureincloud_python_sdk.model.list_cashbook_entries_response import (
    ListCashbookEntriesResponse,
)
from fattureincloud_python_sdk.model.modify_cashbook_entry_request import (
    ModifyCashbookEntryRequest,
)
from fattureincloud_python_sdk.model.modify_cashbook_entry_response import (
    ModifyCashbookEntryResponse,
)


class CashbookApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_cashbook_entry_endpoint = _Endpoint(
            settings={
                "response_type": (CreateCashbookEntryResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/cashbook",
                "operation_id": "create_cashbook_entry",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "create_cashbook_entry_request",
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
                    "create_cashbook_entry_request": (CreateCashbookEntryRequest,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                },
                "location_map": {
                    "company_id": "path",
                    "create_cashbook_entry_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.delete_cashbook_entry_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/cashbook/{document_id}",
                "operation_id": "delete_cashbook_entry",
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
                    "document_id": (str,),
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
        self.get_cashbook_entry_endpoint = _Endpoint(
            settings={
                "response_type": (GetCashbookEntryResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/cashbook/{document_id}",
                "operation_id": "get_cashbook_entry",
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
                    "document_id": (str,),
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
        self.list_cashbook_entries_endpoint = _Endpoint(
            settings={
                "response_type": (ListCashbookEntriesResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/cashbook",
                "operation_id": "list_cashbook_entries",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "date_from",
                    "date_to",
                    "year",
                    "type",
                    "payment_account_id",
                ],
                "required": [
                    "company_id",
                    "date_from",
                    "date_to",
                ],
                "nullable": [],
                "enum": [
                    "type",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("type",): {"ALL": "all", "IN": "in", "OUT": "out"},
                },
                "openapi_types": {
                    "company_id": (int,),
                    "date_from": (str,),
                    "date_to": (str,),
                    "year": (int,),
                    "type": (str,),
                    "payment_account_id": (int,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                    "date_from": "date_from",
                    "date_to": "date_to",
                    "year": "year",
                    "type": "type",
                    "payment_account_id": "payment_account_id",
                },
                "location_map": {
                    "company_id": "path",
                    "date_from": "query",
                    "date_to": "query",
                    "year": "query",
                    "type": "query",
                    "payment_account_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.modify_cashbook_entry_endpoint = _Endpoint(
            settings={
                "response_type": (ModifyCashbookEntryResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/cashbook/{document_id}",
                "operation_id": "modify_cashbook_entry",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "document_id",
                    "modify_cashbook_entry_request",
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
                    "document_id": (str,),
                    "modify_cashbook_entry_request": (ModifyCashbookEntryRequest,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                    "document_id": "document_id",
                },
                "location_map": {
                    "company_id": "path",
                    "document_id": "path",
                    "modify_cashbook_entry_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )

    def create_cashbook_entry(self, company_id, **kwargs):
        """Create Cashbook Entry  # noqa: E501

        Creates a new cashbook entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_cashbook_entry(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            create_cashbook_entry_request (CreateCashbookEntryRequest): Cashbook entry. . [optional]
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
            CreateCashbookEntryResponse
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
        return self.create_cashbook_entry_endpoint.call_with_http_info(**kwargs)

    def delete_cashbook_entry(self, company_id, document_id, **kwargs):
        """Delete Cashbook Entry  # noqa: E501

        Deletes the specified cashbook entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_cashbook_entry(company_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            document_id (str): The ID of the document.

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
        return self.delete_cashbook_entry_endpoint.call_with_http_info(**kwargs)

    def get_cashbook_entry(self, company_id, document_id, **kwargs):
        """Get Cashbook Entry  # noqa: E501

        Gets the specified cashbook entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cashbook_entry(company_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            document_id (str): The ID of the document.

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
            GetCashbookEntryResponse
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
        return self.get_cashbook_entry_endpoint.call_with_http_info(**kwargs)

    def list_cashbook_entries(self, company_id, date_from, date_to, **kwargs):
        """List Cashbook Entries  # noqa: E501

        Lists the cashbook entries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_cashbook_entries(company_id, date_from, date_to, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            date_from (str): Start date.
            date_to (str): End date.

        Keyword Args:
            year (int): Filter cashbook by year.. [optional]
            type (str): Filter cashbook by type.. [optional]
            payment_account_id (int): Filter by payment account.. [optional]
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
            ListCashbookEntriesResponse
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
        kwargs["date_from"] = date_from
        kwargs["date_to"] = date_to
        return self.list_cashbook_entries_endpoint.call_with_http_info(**kwargs)

    def modify_cashbook_entry(self, company_id, document_id, **kwargs):
        """Modify Cashbook Entry  # noqa: E501

        Modifies the specified cashbook entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_cashbook_entry(company_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            document_id (str): The ID of the document.

        Keyword Args:
            modify_cashbook_entry_request (ModifyCashbookEntryRequest): Cashbook Entry. [optional]
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
            ModifyCashbookEntryResponse
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
        return self.modify_cashbook_entry_endpoint.call_with_http_info(**kwargs)
