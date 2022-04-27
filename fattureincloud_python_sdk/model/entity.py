"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.15
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
    from fattureincloud_python_sdk.model.default_payment_terms_type import (
        DefaultPaymentTermsType,
    )
    from fattureincloud_python_sdk.model.entity_type import EntityType
    from fattureincloud_python_sdk.model.payment_method import PaymentMethod
    from fattureincloud_python_sdk.model.vat_type import VatType

    globals()["DefaultPaymentTermsType"] = DefaultPaymentTermsType
    globals()["EntityType"] = EntityType
    globals()["PaymentMethod"] = PaymentMethod
    globals()["VatType"] = VatType


class Entity(ModelNormal):
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
            "id": (
                int,
                none_type,
            ),  # noqa: E501
            "code": (
                str,
                none_type,
            ),  # noqa: E501
            "name": (
                str,
                none_type,
            ),  # noqa: E501
            "type": (EntityType,),  # noqa: E501
            "first_name": (
                str,
                none_type,
            ),  # noqa: E501
            "last_name": (
                str,
                none_type,
            ),  # noqa: E501
            "contact_person": (
                str,
                none_type,
            ),  # noqa: E501
            "vat_number": (
                str,
                none_type,
            ),  # noqa: E501
            "tax_code": (
                str,
                none_type,
            ),  # noqa: E501
            "address_street": (
                str,
                none_type,
            ),  # noqa: E501
            "address_postal_code": (
                str,
                none_type,
            ),  # noqa: E501
            "address_city": (
                str,
                none_type,
            ),  # noqa: E501
            "address_province": (
                str,
                none_type,
            ),  # noqa: E501
            "address_extra": (
                str,
                none_type,
            ),  # noqa: E501
            "country": (
                str,
                none_type,
            ),  # noqa: E501
            "email": (
                str,
                none_type,
            ),  # noqa: E501
            "certified_email": (
                str,
                none_type,
            ),  # noqa: E501
            "phone": (
                str,
                none_type,
            ),  # noqa: E501
            "fax": (
                str,
                none_type,
            ),  # noqa: E501
            "notes": (
                str,
                none_type,
            ),  # noqa: E501
            "default_vat": (VatType,),  # noqa: E501
            "default_payment_terms": (
                int,
                none_type,
            ),  # noqa: E501
            "default_payment_terms_type": (DefaultPaymentTermsType,),  # noqa: E501
            "default_payment_method": (PaymentMethod,),  # noqa: E501
            "bank_name": (
                str,
                none_type,
            ),  # noqa: E501
            "bank_iban": (
                str,
                none_type,
            ),  # noqa: E501
            "bank_swift_code": (
                str,
                none_type,
            ),  # noqa: E501
            "shipping_address": (
                str,
                none_type,
            ),  # noqa: E501
            "e_invoice": (
                bool,
                none_type,
            ),  # noqa: E501
            "ei_code": (
                str,
                none_type,
            ),  # noqa: E501
            "has_intent_declaration": (bool,),  # noqa: E501
            "intent_declaration_protocol_number": (
                date,
                none_type,
            ),  # noqa: E501
            "intent_declaration_protocol_date": (
                str,
                none_type,
            ),  # noqa: E501
            "created_at": (
                str,
                none_type,
            ),  # noqa: E501
            "updated_at": (
                str,
                none_type,
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "id": "id",  # noqa: E501
        "code": "code",  # noqa: E501
        "name": "name",  # noqa: E501
        "type": "type",  # noqa: E501
        "first_name": "first_name",  # noqa: E501
        "last_name": "last_name",  # noqa: E501
        "contact_person": "contact_person",  # noqa: E501
        "vat_number": "vat_number",  # noqa: E501
        "tax_code": "tax_code",  # noqa: E501
        "address_street": "address_street",  # noqa: E501
        "address_postal_code": "address_postal_code",  # noqa: E501
        "address_city": "address_city",  # noqa: E501
        "address_province": "address_province",  # noqa: E501
        "address_extra": "address_extra",  # noqa: E501
        "country": "country",  # noqa: E501
        "email": "email",  # noqa: E501
        "certified_email": "certified_email",  # noqa: E501
        "phone": "phone",  # noqa: E501
        "fax": "fax",  # noqa: E501
        "notes": "notes",  # noqa: E501
        "default_vat": "default_vat",  # noqa: E501
        "default_payment_terms": "default_payment_terms",  # noqa: E501
        "default_payment_terms_type": "default_payment_terms_type",  # noqa: E501
        "default_payment_method": "default_payment_method",  # noqa: E501
        "bank_name": "bank_name",  # noqa: E501
        "bank_iban": "bank_iban",  # noqa: E501
        "bank_swift_code": "bank_swift_code",  # noqa: E501
        "shipping_address": "shipping_address",  # noqa: E501
        "e_invoice": "e_invoice",  # noqa: E501
        "ei_code": "ei_code",  # noqa: E501
        "has_intent_declaration": "has_intent_declaration",  # noqa: E501
        "intent_declaration_protocol_number": "intent_declaration_protocol_number",  # noqa: E501
        "intent_declaration_protocol_date": "intent_declaration_protocol_date",  # noqa: E501
        "created_at": "created_at",  # noqa: E501
        "updated_at": "updated_at",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Entity - a model defined in OpenAPI

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
            id (int, none_type): Unique identifier. [optional]  # noqa: E501
            code (str, none_type): Code.. [optional]  # noqa: E501
            name (str, none_type): Name. [optional]  # noqa: E501
            type (EntityType): [optional]  # noqa: E501
            first_name (str, none_type): First name.. [optional]  # noqa: E501
            last_name (str, none_type): Last name.. [optional]  # noqa: E501
            contact_person (str, none_type): [optional]  # noqa: E501
            vat_number (str, none_type): Vat number. [optional]  # noqa: E501
            tax_code (str, none_type): Tax code.. [optional]  # noqa: E501
            address_street (str, none_type): Street address.. [optional]  # noqa: E501
            address_postal_code (str, none_type): Postal code.. [optional]  # noqa: E501
            address_city (str, none_type): City.. [optional]  # noqa: E501
            address_province (str, none_type): Province.. [optional]  # noqa: E501
            address_extra (str, none_type): Address extra info.. [optional]  # noqa: E501
            country (str, none_type): Country. [optional]  # noqa: E501
            email (str, none_type): Email.. [optional]  # noqa: E501
            certified_email (str, none_type): Certified email.. [optional]  # noqa: E501
            phone (str, none_type): Phone.. [optional]  # noqa: E501
            fax (str, none_type): Fax.. [optional]  # noqa: E501
            notes (str, none_type): Extra notes.. [optional]  # noqa: E501
            default_vat (VatType): [optional]  # noqa: E501
            default_payment_terms (int, none_type): [Only for client] Default payment terms.. [optional]  # noqa: E501
            default_payment_terms_type (DefaultPaymentTermsType): [optional]  # noqa: E501
            default_payment_method (PaymentMethod): [optional]  # noqa: E501
            bank_name (str, none_type): [Only for client] Bank name.. [optional]  # noqa: E501
            bank_iban (str, none_type): [Only for client] Iban.. [optional]  # noqa: E501
            bank_swift_code (str, none_type): [Only for client] Bank swift code.. [optional]  # noqa: E501
            shipping_address (str, none_type): [Only for client] Shipping address.. [optional]  # noqa: E501
            e_invoice (bool, none_type): [Only for client] Use e-invoices.. [optional]  # noqa: E501
            ei_code (str, none_type): [Only for client] E-invoices code.. [optional]  # noqa: E501
            has_intent_declaration (bool): [Only for client] Has intent declaration.. [optional]  # noqa: E501
            intent_declaration_protocol_number (date, none_type): [Only for client] Intent declaration protocol number.. [optional]  # noqa: E501
            intent_declaration_protocol_date (str, none_type): [Only for client] Intent declaration protocol date.. [optional]  # noqa: E501
            created_at (str, none_type): [optional]  # noqa: E501
            updated_at (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
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
        """Entity - a model defined in OpenAPI

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
            id (int, none_type): Unique identifier. [optional]  # noqa: E501
            code (str, none_type): Code.. [optional]  # noqa: E501
            name (str, none_type): Name. [optional]  # noqa: E501
            type (EntityType): [optional]  # noqa: E501
            first_name (str, none_type): First name.. [optional]  # noqa: E501
            last_name (str, none_type): Last name.. [optional]  # noqa: E501
            contact_person (str, none_type): [optional]  # noqa: E501
            vat_number (str, none_type): Vat number. [optional]  # noqa: E501
            tax_code (str, none_type): Tax code.. [optional]  # noqa: E501
            address_street (str, none_type): Street address.. [optional]  # noqa: E501
            address_postal_code (str, none_type): Postal code.. [optional]  # noqa: E501
            address_city (str, none_type): City.. [optional]  # noqa: E501
            address_province (str, none_type): Province.. [optional]  # noqa: E501
            address_extra (str, none_type): Address extra info.. [optional]  # noqa: E501
            country (str, none_type): Country. [optional]  # noqa: E501
            email (str, none_type): Email.. [optional]  # noqa: E501
            certified_email (str, none_type): Certified email.. [optional]  # noqa: E501
            phone (str, none_type): Phone.. [optional]  # noqa: E501
            fax (str, none_type): Fax.. [optional]  # noqa: E501
            notes (str, none_type): Extra notes.. [optional]  # noqa: E501
            default_vat (VatType): [optional]  # noqa: E501
            default_payment_terms (int, none_type): [Only for client] Default payment terms.. [optional]  # noqa: E501
            default_payment_terms_type (DefaultPaymentTermsType): [optional]  # noqa: E501
            default_payment_method (PaymentMethod): [optional]  # noqa: E501
            bank_name (str, none_type): [Only for client] Bank name.. [optional]  # noqa: E501
            bank_iban (str, none_type): [Only for client] Iban.. [optional]  # noqa: E501
            bank_swift_code (str, none_type): [Only for client] Bank swift code.. [optional]  # noqa: E501
            shipping_address (str, none_type): [Only for client] Shipping address.. [optional]  # noqa: E501
            e_invoice (bool, none_type): [Only for client] Use e-invoices.. [optional]  # noqa: E501
            ei_code (str, none_type): [Only for client] E-invoices code.. [optional]  # noqa: E501
            has_intent_declaration (bool): [Only for client] Has intent declaration.. [optional]  # noqa: E501
            intent_declaration_protocol_number (date, none_type): [Only for client] Intent declaration protocol number.. [optional]  # noqa: E501
            intent_declaration_protocol_date (str, none_type): [Only for client] Intent declaration protocol date.. [optional]  # noqa: E501
            created_at (str, none_type): [optional]  # noqa: E501
            updated_at (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
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
