"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.23
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from fattureincloud_python_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel,
)
from fattureincloud_python_sdk.exceptions import ApiAttributeError


def lazy_import():
    from fattureincloud_python_sdk.model.vat_list import VatList

    globals()["VatList"] = VatList


class IssuedDocumentTotals(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = True

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "amount_net": (
                float,
                none_type,
            ),  # noqa: E501
            "amount_rivalsa": (
                float,
                none_type,
            ),  # noqa: E501
            "amount_net_with_rivalsa": (
                float,
                none_type,
            ),  # noqa: E501
            "amount_cassa": (
                float,
                none_type,
            ),  # noqa: E501
            "taxable_amount": (
                float,
                none_type,
            ),  # noqa: E501
            "not_taxable_amount": (
                float,
                none_type,
            ),  # noqa: E501
            "amount_vat": (
                float,
                none_type,
            ),  # noqa: E501
            "amount_gross": (
                float,
                none_type,
            ),  # noqa: E501
            "taxable_amount_withholding_tax": (
                float,
                none_type,
            ),  # noqa: E501
            "amount_withholding_tax": (
                float,
                none_type,
            ),  # noqa: E501
            "taxable_amount_other_withholding_tax": (
                float,
                none_type,
            ),  # noqa: E501
            "amount_other_withholding_tax": (
                float,
                none_type,
            ),  # noqa: E501
            "stamp_duty": (
                float,
                none_type,
            ),  # noqa: E501
            "amount_due": (
                float,
                none_type,
            ),  # noqa: E501
            "is_enasarco_maximal_exceeded": (
                bool,
                none_type,
            ),  # noqa: E501
            "payments_sum": (
                float,
                none_type,
            ),  # noqa: E501
            "vat_list": (VatList,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "amount_net": "amount_net",  # noqa: E501
        "amount_rivalsa": "amount_rivalsa",  # noqa: E501
        "amount_net_with_rivalsa": "amount_net_with_rivalsa",  # noqa: E501
        "amount_cassa": "amount_cassa",  # noqa: E501
        "taxable_amount": "taxable_amount",  # noqa: E501
        "not_taxable_amount": "not_taxable_amount",  # noqa: E501
        "amount_vat": "amount_vat",  # noqa: E501
        "amount_gross": "amount_gross",  # noqa: E501
        "taxable_amount_withholding_tax": "taxable_amount_withholding_tax",  # noqa: E501
        "amount_withholding_tax": "amount_withholding_tax",  # noqa: E501
        "taxable_amount_other_withholding_tax": "taxable_amount_other_withholding_tax",  # noqa: E501
        "amount_other_withholding_tax": "amount_other_withholding_tax",  # noqa: E501
        "stamp_duty": "stamp_duty",  # noqa: E501
        "amount_due": "amount_due",  # noqa: E501
        "is_enasarco_maximal_exceeded": "is_enasarco_maximal_exceeded",  # noqa: E501
        "payments_sum": "payments_sum",  # noqa: E501
        "vat_list": "vat_list",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """IssuedDocumentTotals - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            amount_net (float, none_type): Total net amount.. [optional]  # noqa: E501
            amount_rivalsa (float, none_type): Rivalsa amount.. [optional]  # noqa: E501
            amount_net_with_rivalsa (float, none_type): Net amount with rivalsa.. [optional]  # noqa: E501
            amount_cassa (float, none_type): Cassa amount.. [optional]  # noqa: E501
            taxable_amount (float, none_type): Taxable amount.. [optional]  # noqa: E501
            not_taxable_amount (float, none_type): Not taxable amount.. [optional]  # noqa: E501
            amount_vat (float, none_type): Total vat amount.. [optional]  # noqa: E501
            amount_gross (float, none_type): Total grosas amount.. [optional]  # noqa: E501
            taxable_amount_withholding_tax (float, none_type): Taxable withholding tax amount.. [optional]  # noqa: E501
            amount_withholding_tax (float, none_type): Withholding tax amount.. [optional]  # noqa: E501
            taxable_amount_other_withholding_tax (float, none_type): Other withholding tax taxable amount.. [optional]  # noqa: E501
            amount_other_withholding_tax (float, none_type): Other withholding tax amount.. [optional]  # noqa: E501
            stamp_duty (float, none_type): Stamp duty value [0 if not present].. [optional]  # noqa: E501
            amount_due (float, none_type): Total amount due.. [optional]  # noqa: E501
            is_enasarco_maximal_exceeded (bool, none_type): [optional]  # noqa: E501
            payments_sum (float, none_type): Payments sum.. [optional]  # noqa: E501
            vat_list (VatList): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", True)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """IssuedDocumentTotals - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            amount_net (float, none_type): Total net amount.. [optional]  # noqa: E501
            amount_rivalsa (float, none_type): Rivalsa amount.. [optional]  # noqa: E501
            amount_net_with_rivalsa (float, none_type): Net amount with rivalsa.. [optional]  # noqa: E501
            amount_cassa (float, none_type): Cassa amount.. [optional]  # noqa: E501
            taxable_amount (float, none_type): Taxable amount.. [optional]  # noqa: E501
            not_taxable_amount (float, none_type): Not taxable amount.. [optional]  # noqa: E501
            amount_vat (float, none_type): Total vat amount.. [optional]  # noqa: E501
            amount_gross (float, none_type): Total grosas amount.. [optional]  # noqa: E501
            taxable_amount_withholding_tax (float, none_type): Taxable withholding tax amount.. [optional]  # noqa: E501
            amount_withholding_tax (float, none_type): Withholding tax amount.. [optional]  # noqa: E501
            taxable_amount_other_withholding_tax (float, none_type): Other withholding tax taxable amount.. [optional]  # noqa: E501
            amount_other_withholding_tax (float, none_type): Other withholding tax amount.. [optional]  # noqa: E501
            stamp_duty (float, none_type): Stamp duty value [0 if not present].. [optional]  # noqa: E501
            amount_due (float, none_type): Total amount due.. [optional]  # noqa: E501
            is_enasarco_maximal_exceeded (bool, none_type): [optional]  # noqa: E501
            payments_sum (float, none_type): Payments sum.. [optional]  # noqa: E501
            vat_list (VatList): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
