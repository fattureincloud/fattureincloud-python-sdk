"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.10
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
from fattureincloud_python_sdk.model.create_product_request import CreateProductRequest
from fattureincloud_python_sdk.model.create_product_response import CreateProductResponse
from fattureincloud_python_sdk.model.get_product_response import GetProductResponse
from fattureincloud_python_sdk.model.list_products_response import ListProductsResponse
from fattureincloud_python_sdk.model.modify_product_request import ModifyProductRequest
from fattureincloud_python_sdk.model.modify_product_response import ModifyProductResponse


class ProductsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_product_endpoint = _Endpoint(
            settings={
                'response_type': (CreateProductResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/products',
                'operation_id': 'create_product',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'create_product_request',
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
                    'create_product_request':
                        (CreateProductRequest,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'create_product_request': 'body',
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
        self.delete_product_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/products/{product_id}',
                'operation_id': 'delete_product',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'product_id',
                ],
                'required': [
                    'company_id',
                    'product_id',
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
                    'product_id':
                        (int,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'product_id': 'product_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'product_id': 'path',
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
        self.get_product_endpoint = _Endpoint(
            settings={
                'response_type': (GetProductResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/products/{product_id}',
                'operation_id': 'get_product',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'product_id',
                    'fields',
                    'fieldset',
                ],
                'required': [
                    'company_id',
                    'product_id',
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
                    'product_id':
                        (int,),
                    'fields':
                        (str,),
                    'fieldset':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'product_id': 'product_id',
                    'fields': 'fields',
                    'fieldset': 'fieldset',
                },
                'location_map': {
                    'company_id': 'path',
                    'product_id': 'path',
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
        self.list_products_endpoint = _Endpoint(
            settings={
                'response_type': (ListProductsResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/products',
                'operation_id': 'list_products',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'fields',
                    'fieldset',
                    'sort',
                    'page',
                    'per_page',
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
                    'sort':
                        (str,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'fields': 'fields',
                    'fieldset': 'fieldset',
                    'sort': 'sort',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'company_id': 'path',
                    'fields': 'query',
                    'fieldset': 'query',
                    'sort': 'query',
                    'page': 'query',
                    'per_page': 'query',
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
        self.modify_product_endpoint = _Endpoint(
            settings={
                'response_type': (ModifyProductResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/products/{product_id}',
                'operation_id': 'modify_product',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'product_id',
                    'modify_product_request',
                ],
                'required': [
                    'company_id',
                    'product_id',
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
                    'product_id':
                        (int,),
                    'modify_product_request':
                        (ModifyProductRequest,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'product_id': 'product_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'product_id': 'path',
                    'modify_product_request': 'body',
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

    def create_product(
        self,
        company_id,
        **kwargs
    ):
        """Create Product  # noqa: E501

        Creates a new product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_product(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            create_product_request (CreateProductRequest): [optional]
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
            CreateProductResponse
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
        return self.create_product_endpoint.call_with_http_info(**kwargs)

    def delete_product(
        self,
        company_id,
        product_id,
        **kwargs
    ):
        """Delete Product  # noqa: E501

        Deletes the specified product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_product(company_id, product_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            product_id (int): The ID of the product.

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
        kwargs['product_id'] = \
            product_id
        return self.delete_product_endpoint.call_with_http_info(**kwargs)

    def get_product(
        self,
        company_id,
        product_id,
        **kwargs
    ):
        """Get Product  # noqa: E501

        Gets the specified product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_product(company_id, product_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            product_id (int): The ID of the product.

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
            GetProductResponse
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
        kwargs['product_id'] = \
            product_id
        return self.get_product_endpoint.call_with_http_info(**kwargs)

    def list_products(
        self,
        company_id,
        **kwargs
    ):
        """List Products  # noqa: E501

        Lists the products.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_products(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            fields (str): List of comma-separated fields.. [optional]
            fieldset (str): Name of the fieldset.. [optional]
            sort (str): List of comma-separated fields for result sorting (minus for desc sorting).. [optional]
            page (int): The page to retrieve.. [optional] if omitted the server will use the default value of 1
            per_page (int): The size of the page.. [optional] if omitted the server will use the default value of 5
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
            ListProductsResponse
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
        return self.list_products_endpoint.call_with_http_info(**kwargs)

    def modify_product(
        self,
        company_id,
        product_id,
        **kwargs
    ):
        """Modify Product  # noqa: E501

        Modifies the specified product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_product(company_id, product_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            product_id (int): The ID of the product.

        Keyword Args:
            modify_product_request (ModifyProductRequest): Modified product details.. [optional]
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
            ModifyProductResponse
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
        kwargs['product_id'] = \
            product_id
        return self.modify_product_endpoint.call_with_http_info(**kwargs)

