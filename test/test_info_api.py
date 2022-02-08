"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.10
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.api.info_api import InfoApi  # noqa: E501


class TestInfoApi(unittest.TestCase):
    """InfoApi unit test stubs"""

    def setUp(self):
        self.api = InfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_archive_categories(self):
        """Test case for list_archive_categories

        List Archive Categories  # noqa: E501
        """
        pass

    def test_list_cities(self):
        """Test case for list_cities

        List Cities  # noqa: E501
        """
        pass

    def test_list_cost_centers(self):
        """Test case for list_cost_centers

        List Cost Centers  # noqa: E501
        """
        pass

    def test_list_countries(self):
        """Test case for list_countries

        List Countries  # noqa: E501
        """
        pass

    def test_list_currencies(self):
        """Test case for list_currencies

        List Currencies  # noqa: E501
        """
        pass

    def test_list_delivery_notes_default_causals(self):
        """Test case for list_delivery_notes_default_causals

        List Delivery Notes Default Causals  # noqa: E501
        """
        pass

    def test_list_languages(self):
        """Test case for list_languages

        List Languages  # noqa: E501
        """
        pass

    def test_list_payment_accounts(self):
        """Test case for list_payment_accounts

        List Payment Accounts  # noqa: E501
        """
        pass

    def test_list_payment_methods(self):
        """Test case for list_payment_methods

        List Payment Methods  # noqa: E501
        """
        pass

    def test_list_product_categories(self):
        """Test case for list_product_categories

        List Product Categories  # noqa: E501
        """
        pass

    def test_list_received_document_categories(self):
        """Test case for list_received_document_categories

        List Received Document Categories  # noqa: E501
        """
        pass

    def test_list_revenue_centers(self):
        """Test case for list_revenue_centers

        List Revenue Centers  # noqa: E501
        """
        pass

    def test_list_templates(self):
        """Test case for list_templates

        List Templates  # noqa: E501
        """
        pass

    def test_list_units_of_measure(self):
        """Test case for list_units_of_measure

        List Units of Measure  # noqa: E501
        """
        pass

    def test_list_vat_types(self):
        """Test case for list_vat_types

        List Vat Types  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
