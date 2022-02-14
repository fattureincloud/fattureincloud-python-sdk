"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.11
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
    validate_and_convert_types
)
from fattureincloud_python_sdk.model.create_receipt_request import CreateReceiptRequest
from fattureincloud_python_sdk.model.create_receipt_response import CreateReceiptResponse
from fattureincloud_python_sdk.model.get_receipt_pre_create_info_response import GetReceiptPreCreateInfoResponse
from fattureincloud_python_sdk.model.get_receipt_response import GetReceiptResponse
from fattureincloud_python_sdk.model.get_receipts_monthly_totals_response import GetReceiptsMonthlyTotalsResponse
from fattureincloud_python_sdk.model.list_receipts_response import ListReceiptsResponse
from fattureincloud_python_sdk.model.modify_receipt_request import ModifyReceiptRequest
from fattureincloud_python_sdk.model.modify_receipt_response import ModifyReceiptResponse


class ReceiptsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_receipt_endpoint = _Endpoint(
            settings={
                'response_type': (CreateReceiptResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/receipts',
                'operation_id': 'create_receipt',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'create_receipt_request',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'create_receipt_request':
                        (CreateReceiptRequest,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'create_receipt_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_receipt_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/receipts/{document_id}',
                'operation_id': 'delete_receipt',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'document_id',
                ],
                'required': [
                    'company_id',
                    'document_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'document_id':
                        (int,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'document_id': 'document_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'document_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_receipt_endpoint = _Endpoint(
            settings={
                'response_type': (GetReceiptResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/receipts/{document_id}',
                'operation_id': 'get_receipt',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'document_id',
                    'fields',
                    'fieldset',
                ],
                'required': [
                    'company_id',
                    'document_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'fieldset',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('fieldset',): {

                        "BASIC": "basic",
                        "DETAILED": "detailed"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'document_id':
                        (int,),
                    'fields':
                        (str,),
                    'fieldset':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'document_id': 'document_id',
                    'fields': 'fields',
                    'fieldset': 'fieldset',
                },
                'location_map': {
                    'company_id': 'path',
                    'document_id': 'path',
                    'fields': 'query',
                    'fieldset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_receipt_pre_create_info_endpoint = _Endpoint(
            settings={
                'response_type': (GetReceiptPreCreateInfoResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/receipts/info',
                'operation_id': 'get_receipt_pre_create_info',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                },
                'location_map': {
                    'company_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_receipts_monthly_totals_endpoint = _Endpoint(
            settings={
                'response_type': (GetReceiptsMonthlyTotalsResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/receipts/monthly_totals',
                'operation_id': 'get_receipts_monthly_totals',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'type',
                    'year',
                ],
                'required': [
                    'company_id',
                    'type',
                    'year',
                ],
                'nullable': [
                ],
                'enum': [
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('type',): {

                        "SALES_RECEIPT": "sales_receipt",
                        "TILL_RECEIPT": "till_receipt"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'type':
                        (str,),
                    'year':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'type': 'type',
                    'year': 'year',
                },
                'location_map': {
                    'company_id': 'path',
                    'type': 'query',
                    'year': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_receipts_endpoint = _Endpoint(
            settings={
                'response_type': (ListReceiptsResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/receipts',
                'operation_id': 'list_receipts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'fields',
                    'fieldset',
                    'page',
                    'per_page',
                    'sort',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'fieldset',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('fieldset',): {

                        "BASIC": "basic",
                        "DETAILED": "detailed"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'fields':
                        (str,),
                    'fieldset':
                        (str,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'fields': 'fields',
                    'fieldset': 'fieldset',
                    'page': 'page',
                    'per_page': 'per_page',
                    'sort': 'sort',
                },
                'location_map': {
                    'company_id': 'path',
                    'fields': 'query',
                    'fieldset': 'query',
                    'page': 'query',
                    'per_page': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.modify_receipt_endpoint = _Endpoint(
            settings={
                'response_type': (ModifyReceiptResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/receipts/{document_id}',
                'operation_id': 'modify_receipt',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'document_id',
                    'modify_receipt_request',
                ],
                'required': [
                    'company_id',
                    'document_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'document_id':
                        (int,),
                    'modify_receipt_request':
                        (ModifyReceiptRequest,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'document_id': 'document_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'document_id': 'path',
                    'modify_receipt_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_receipt(
        self,
        company_id,
        **kwargs
    ):
        """Create Receipt  # noqa: E501

        Creates a new receipt.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_receipt(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            create_receipt_request (CreateReceiptRequest): The Receipt to create.. [optional]
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
            async_req (bool): execute request asynchronously

        Returns:
            CreateReceiptResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        return self.create_receipt_endpoint.call_with_http_info(**kwargs)

    def delete_receipt(
        self,
        company_id,
        document_id,
        **kwargs
    ):
        """Delete Receipt  # noqa: E501

        Deletes the specified receipt.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_receipt(company_id, document_id, async_req=True)
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
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        kwargs['document_id'] = \
            document_id
        return self.delete_receipt_endpoint.call_with_http_info(**kwargs)

    def get_receipt(
        self,
        company_id,
        document_id,
        **kwargs
    ):
        """Get Receipt  # noqa: E501

        Gets the specified receipt.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_receipt(company_id, document_id, async_req=True)
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
            async_req (bool): execute request asynchronously

        Returns:
            GetReceiptResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        kwargs['document_id'] = \
            document_id
        return self.get_receipt_endpoint.call_with_http_info(**kwargs)

    def get_receipt_pre_create_info(
        self,
        company_id,
        **kwargs
    ):
        """Get Receipt Pre-Create Info  # noqa: E501

        Retrieves the information useful while creating a new receipt.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_receipt_pre_create_info(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

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
            async_req (bool): execute request asynchronously

        Returns:
            GetReceiptPreCreateInfoResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        return self.get_receipt_pre_create_info_endpoint.call_with_http_info(**kwargs)

    def get_receipts_monthly_totals(
        self,
        company_id,
        type,
        year,
        **kwargs
    ):
        """Get Receipts Monthly Totals  # noqa: E501

        Returns the monthly totals by year and receipt type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_receipts_monthly_totals(company_id, type, year, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            type (str): Receipt Type
            year (str): Year for which you want monthly totals

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
            async_req (bool): execute request asynchronously

        Returns:
            GetReceiptsMonthlyTotalsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        kwargs['type'] = \
            type
        kwargs['year'] = \
            year
        return self.get_receipts_monthly_totals_endpoint.call_with_http_info(**kwargs)

    def list_receipts(
        self,
        company_id,
        **kwargs
    ):
        """List Receipts  # noqa: E501

        Lists the receipts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_receipts(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            fields (str): List of comma-separated fields.. [optional]
            fieldset (str): Name of the fieldset.. [optional]
            page (int): The page to retrieve.. [optional] if omitted the server will use the default value of 1
            per_page (int): The size of the page.. [optional] if omitted the server will use the default value of 5
            sort (str): List of comma-separated fields for result sorting (minus for desc sorting).. [optional]
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
            async_req (bool): execute request asynchronously

        Returns:
            ListReceiptsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        return self.list_receipts_endpoint.call_with_http_info(**kwargs)

    def modify_receipt(
        self,
        company_id,
        document_id,
        **kwargs
    ):
        """Modify Receipt  # noqa: E501

        Modifies the specified receipt.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_receipt(company_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            document_id (int): The ID of the document.

        Keyword Args:
            modify_receipt_request (ModifyReceiptRequest): Modified receipt.. [optional]
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
            async_req (bool): execute request asynchronously

        Returns:
            ModifyReceiptResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        kwargs['document_id'] = \
            document_id
        return self.modify_receipt_endpoint.call_with_http_info(**kwargs)

