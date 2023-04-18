# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.27
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr

from typing import Optional

from fattureincloud_python_sdk.models.create_webhooks_subscription_request import (
    CreateWebhooksSubscriptionRequest,
)
from fattureincloud_python_sdk.models.create_webhooks_subscription_response import (
    CreateWebhooksSubscriptionResponse,
)
from fattureincloud_python_sdk.models.get_webhooks_subscription_response import (
    GetWebhooksSubscriptionResponse,
)
from fattureincloud_python_sdk.models.list_webhooks_subscriptions_response import (
    ListWebhooksSubscriptionsResponse,
)
from fattureincloud_python_sdk.models.modify_webhooks_subscription_request import (
    ModifyWebhooksSubscriptionRequest,
)
from fattureincloud_python_sdk.models.modify_webhooks_subscription_response import (
    ModifyWebhooksSubscriptionResponse,
)

from fattureincloud_python_sdk.api_client import ApiClient
from fattureincloud_python_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError,
)


class WebhooksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_webhooks_subscription(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        create_webhooks_subscription_request: Optional[
            CreateWebhooksSubscriptionRequest
        ] = None,
        **kwargs
    ) -> CreateWebhooksSubscriptionResponse:  # noqa: E501
        """Create a Webhook Subscription  # noqa: E501

        Register some webhooks Subscriptions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_webhooks_subscription(company_id, create_webhooks_subscription_request, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param create_webhooks_subscription_request:
        :type create_webhooks_subscription_request: CreateWebhooksSubscriptionRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateWebhooksSubscriptionResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.create_webhooks_subscription_with_http_info(
            company_id, create_webhooks_subscription_request, **kwargs
        )  # noqa: E501

    @validate_arguments
    def create_webhooks_subscription_with_http_info(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        create_webhooks_subscription_request: Optional[
            CreateWebhooksSubscriptionRequest
        ] = None,
        **kwargs
    ):  # noqa: E501
        """Create a Webhook Subscription  # noqa: E501

        Register some webhooks Subscriptions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_webhooks_subscription_with_http_info(company_id, create_webhooks_subscription_request, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param create_webhooks_subscription_request:
        :type create_webhooks_subscription_request: CreateWebhooksSubscriptionRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CreateWebhooksSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["company_id", "create_webhooks_subscription_request"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_webhooks_subscription" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["company_id"]:
            _path_params["company_id"] = _params["company_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["create_webhooks_subscription_request"]:
            _body_params = _params["create_webhooks_subscription_request"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["OAuth2AuthenticationCodeFlow"]  # noqa: E501

        _response_types_map = {
            "200": "CreateWebhooksSubscriptionResponse",
        }

        return self.api_client.call_api(
            "/c/{company_id}/subscriptions",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def delete_webhooks_subscription(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        subscription_id: Annotated[
            StrictStr, Field(..., description="The ID of the subscription.")
        ],
        **kwargs
    ) -> None:  # noqa: E501
        """Delete Webhooks Subscription  # noqa: E501

        Delete a webhooks subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_webhooks_subscription(company_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param subscription_id: The ID of the subscription. (required)
        :type subscription_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        return self.delete_webhooks_subscription_with_http_info(
            company_id, subscription_id, **kwargs
        )  # noqa: E501

    @validate_arguments
    def delete_webhooks_subscription_with_http_info(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        subscription_id: Annotated[
            StrictStr, Field(..., description="The ID of the subscription.")
        ],
        **kwargs
    ):  # noqa: E501
        """Delete Webhooks Subscription  # noqa: E501

        Delete a webhooks subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_webhooks_subscription_with_http_info(company_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param subscription_id: The ID of the subscription. (required)
        :type subscription_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = ["company_id", "subscription_id"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_webhooks_subscription" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["company_id"]:
            _path_params["company_id"] = _params["company_id"]

        if _params["subscription_id"]:
            _path_params["subscription_id"] = _params["subscription_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ["OAuth2AuthenticationCodeFlow"]  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/c/{company_id}/subscriptions/{subscription_id}",
            "DELETE",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def get_webhooks_subscription(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        subscription_id: Annotated[
            StrictStr, Field(..., description="The ID of the subscription.")
        ],
        **kwargs
    ) -> GetWebhooksSubscriptionResponse:  # noqa: E501
        """Get Webhooks Subscription  # noqa: E501

        Get a webhooks subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_webhooks_subscription(company_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param subscription_id: The ID of the subscription. (required)
        :type subscription_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetWebhooksSubscriptionResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.get_webhooks_subscription_with_http_info(
            company_id, subscription_id, **kwargs
        )  # noqa: E501

    @validate_arguments
    def get_webhooks_subscription_with_http_info(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        subscription_id: Annotated[
            StrictStr, Field(..., description="The ID of the subscription.")
        ],
        **kwargs
    ):  # noqa: E501
        """Get Webhooks Subscription  # noqa: E501

        Get a webhooks subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_webhooks_subscription_with_http_info(company_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param subscription_id: The ID of the subscription. (required)
        :type subscription_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetWebhooksSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["company_id", "subscription_id"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhooks_subscription" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["company_id"]:
            _path_params["company_id"] = _params["company_id"]

        if _params["subscription_id"]:
            _path_params["subscription_id"] = _params["subscription_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["OAuth2AuthenticationCodeFlow"]  # noqa: E501

        _response_types_map = {
            "200": "GetWebhooksSubscriptionResponse",
        }

        return self.api_client.call_api(
            "/c/{company_id}/subscriptions/{subscription_id}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def list_webhooks_subscriptions(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        **kwargs
    ) -> ListWebhooksSubscriptionsResponse:  # noqa: E501
        """List Webhooks Subscriptions  # noqa: E501

        List active webhooks subscriptions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_webhooks_subscriptions(company_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListWebhooksSubscriptionsResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.list_webhooks_subscriptions_with_http_info(
            company_id, **kwargs
        )  # noqa: E501

    @validate_arguments
    def list_webhooks_subscriptions_with_http_info(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        **kwargs
    ):  # noqa: E501
        """List Webhooks Subscriptions  # noqa: E501

        List active webhooks subscriptions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_webhooks_subscriptions_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListWebhooksSubscriptionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["company_id"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_webhooks_subscriptions" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["company_id"]:
            _path_params["company_id"] = _params["company_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["OAuth2AuthenticationCodeFlow"]  # noqa: E501

        _response_types_map = {
            "200": "ListWebhooksSubscriptionsResponse",
        }

        return self.api_client.call_api(
            "/c/{company_id}/subscriptions",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def modify_webhooks_subscription(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        subscription_id: Annotated[
            StrictStr, Field(..., description="The ID of the subscription.")
        ],
        modify_webhooks_subscription_request: Optional[
            ModifyWebhooksSubscriptionRequest
        ] = None,
        **kwargs
    ) -> ModifyWebhooksSubscriptionResponse:  # noqa: E501
        """Modify Webhooks Subscription  # noqa: E501

        Edit a webhooks subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_webhooks_subscription(company_id, subscription_id, modify_webhooks_subscription_request, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param subscription_id: The ID of the subscription. (required)
        :type subscription_id: str
        :param modify_webhooks_subscription_request:
        :type modify_webhooks_subscription_request: ModifyWebhooksSubscriptionRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ModifyWebhooksSubscriptionResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.modify_webhooks_subscription_with_http_info(
            company_id, subscription_id, modify_webhooks_subscription_request, **kwargs
        )  # noqa: E501

    @validate_arguments
    def modify_webhooks_subscription_with_http_info(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        subscription_id: Annotated[
            StrictStr, Field(..., description="The ID of the subscription.")
        ],
        modify_webhooks_subscription_request: Optional[
            ModifyWebhooksSubscriptionRequest
        ] = None,
        **kwargs
    ):  # noqa: E501
        """Modify Webhooks Subscription  # noqa: E501

        Edit a webhooks subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_webhooks_subscription_with_http_info(company_id, subscription_id, modify_webhooks_subscription_request, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param subscription_id: The ID of the subscription. (required)
        :type subscription_id: str
        :param modify_webhooks_subscription_request:
        :type modify_webhooks_subscription_request: ModifyWebhooksSubscriptionRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ModifyWebhooksSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            "company_id",
            "subscription_id",
            "modify_webhooks_subscription_request",
        ]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_webhooks_subscription" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["company_id"]:
            _path_params["company_id"] = _params["company_id"]

        if _params["subscription_id"]:
            _path_params["subscription_id"] = _params["subscription_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["modify_webhooks_subscription_request"]:
            _body_params = _params["modify_webhooks_subscription_request"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["OAuth2AuthenticationCodeFlow"]  # noqa: E501

        _response_types_map = {
            "200": "ModifyWebhooksSubscriptionResponse",
        }

        return self.api_client.call_api(
            "/c/{company_id}/subscriptions/{subscription_id}",
            "PUT",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
