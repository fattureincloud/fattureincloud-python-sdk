# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.1.2
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import json
import unittest
import fattureincloud_python_sdk
from functions import json_serial


from fattureincloud_python_sdk.models.tax_profile import TaxProfile


class TestTaxProfile(unittest.TestCase):
    """TaxProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    

    def testTaxProfile(self):
        """Test TaxProfile"""
        model = TaxProfile(
            company_type="individual",
            company_subtype="artigiani",
            profession="test",
            regime="forfettario_5",
            rivalsa_name="",
            default_rivalsa=0,
            cassa_name="",
            default_cassa=0,
            default_cassa_taxable=100,
            cassa2_name="",
            default_cassa2=0,
            default_cassa2_taxable=0,
            default_withholding_tax=0,
            default_withholding_tax_taxable=100,
            default_other_withholding_tax=0,
            enasarco=False,
            enasarco_type="test",
            contributions_percentage=0,
            med=False,
            default_vat={
                "id": 66,
                "value": 0,
                "description": "Contribuenti forfettari",
                "notes": "Operazione non soggetta a IVA ai sensi dell'art. 1, commi 54-89, Legge n. 190/2014 e succ. modifiche/integrazioni",
                "e_invoice": True,
                "ei_type": "2.2",
                "ei_description": "Non soggetta art. 1/54-89 L. 190/2014 e succ. modifiche/integrazioni",
                "is_disabled": False,
                "default": True,
            }
        )
        
        expected_json = '{"company_type": "individual", "company_subtype": "artigiani", "profession": "test", "regime": "forfettario_5", "rivalsa_name": "", "default_rivalsa": 0, "cassa_name": "", "default_cassa": 0, "default_cassa_taxable": 100, "cassa2_name": "", "default_cassa2": 0, "default_cassa2_taxable": 0, "default_withholding_tax": 0, "default_withholding_tax_taxable": 100, "default_other_withholding_tax": 0, "enasarco": false, "enasarco_type": "test", "contributions_percentage": 0, "med": false, "default_vat": {"id": 66, "value": 0, "description": "Contribuenti forfettari", "notes": "Operazione non soggetta a IVA ai sensi dell\'art. 1, commi 54-89, Legge n. 190/2014 e succ. modifiche/integrazioni", "e_invoice": true, "ei_type": "2.2", "ei_description": "Non soggetta art. 1/54-89 L. 190/2014 e succ. modifiche/integrazioni", "is_disabled": false, "default": true}}';
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()