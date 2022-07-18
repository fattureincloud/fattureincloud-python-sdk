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
from fattureincloud_python_sdk.model.get_e_invoice_rejection_reason_response import (
    GetEInvoiceRejectionReasonResponse,
)
from fattureincloud_python_sdk.model.send_e_invoice_request import SendEInvoiceRequest
from fattureincloud_python_sdk.model.send_e_invoice_response import SendEInvoiceResponse
from fattureincloud_python_sdk.model.verify_e_invoice_xml_error_response import (
    VerifyEInvoiceXmlErrorResponse,
)
from fattureincloud_python_sdk.model.verify_e_invoice_xml_response import (
    VerifyEInvoiceXmlResponse,
)


class IssuedEInvoicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_e_invoice_rejection_reason_endpoint = _Endpoint(
            settings={
                "response_type": (GetEInvoiceRejectionReasonResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/issued_documents/{document_id}/e_invoice/error_reason",
                "operation_id": "get_e_invoice_rejection_reason",
                "http_method": "GET",
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
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_e_invoice_xml_endpoint = _Endpoint(
            settings={
                "response_type": (str,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/issued_documents/{document_id}/e_invoice/xml",
                "operation_id": "get_e_invoice_xml",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "document_id",
                    "include_attachment",
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
                    "include_attachment": (bool,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                    "document_id": "document_id",
                    "include_attachment": "include_attachment",
                },
                "location_map": {
                    "company_id": "path",
                    "document_id": "path",
                    "include_attachment": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["text/xml"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.send_e_invoice_endpoint = _Endpoint(
            settings={
                "response_type": (SendEInvoiceResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/issued_documents/{document_id}/e_invoice/send",
                "operation_id": "send_e_invoice",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "company_id",
                    "document_id",
                    "send_e_invoice_request",
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
                    "send_e_invoice_request": (SendEInvoiceRequest,),
                },
                "attribute_map": {
                    "company_id": "company_id",
                    "document_id": "document_id",
                },
                "location_map": {
                    "company_id": "path",
                    "document_id": "path",
                    "send_e_invoice_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.verify_e_invoice_xml_endpoint = _Endpoint(
            settings={
                "response_type": (VerifyEInvoiceXmlResponse,),
                "auth": ["OAuth2AuthenticationCodeFlow"],
                "endpoint_path": "/c/{company_id}/issued_documents/{document_id}/e_invoice/xml_verify",
                "operation_id": "verify_e_invoice_xml",
                "http_method": "GET",
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
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def get_e_invoice_rejection_reason(self, company_id, document_id, **kwargs):
        """Get e-invoice rejection reason  # noqa: E501

        Get e-invoice rejection reason  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_e_invoice_rejection_reason(company_id, document_id, async_req=True)
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
            GetEInvoiceRejectionReasonResponse
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
        return self.get_e_invoice_rejection_reason_endpoint.call_with_http_info(
            **kwargs
        )

    def get_e_invoice_xml(self, company_id, document_id, **kwargs):
        """Get e-invoice XML  # noqa: E501

        Downloads the e-invoice in XML format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_e_invoice_xml(company_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            document_id (int): The ID of the document.

        Keyword Args:
            include_attachment (bool): Include the attachment to the XML e-invoice.. [optional]
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
            str
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
        return self.get_e_invoice_xml_endpoint.call_with_http_info(**kwargs)

    def send_e_invoice(self, company_id, document_id, **kwargs):
        """Send the e-invoice  # noqa: E501

        Sends the e-invoice to SDI.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_e_invoice(company_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            document_id (int): The ID of the document.

        Keyword Args:
            send_e_invoice_request (SendEInvoiceRequest): . [optional]
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
            SendEInvoiceResponse
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
        return self.send_e_invoice_endpoint.call_with_http_info(**kwargs)

    def verify_e_invoice_xml(self, company_id, document_id, **kwargs):
        """Verify e-invoice XML  # noqa: E501

        Verifies the e-invoice XML format. Checks if all of the mandatory fields are filled and compliant to the right format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_e_invoice_xml(company_id, document_id, async_req=True)
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
            VerifyEInvoiceXmlResponse
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
        return self.verify_e_invoice_xml_endpoint.call_with_http_info(**kwargs)
