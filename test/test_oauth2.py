import unittest
import unittest.mock

from fattureincloud_python_sdk.oauth2.oauth2 import OAuth2AuthorizationCodeParams, OAuth2AuthorizationCodeTokenResponse, OAuth2AuthorizationCode
from fattureincloud_python_sdk.oauth2.scopes import Scope


class TestOAuth2(unittest.TestCase):
    """OAuth2 unit test stubs"""

    def setUp(self):
        self.oa2 = OAuth2AuthorizationCode("CLIENT_ID", "CLIENT_SECRET", "http://localhost:3000/redirect")
        pass

    def tearDown(self):
        pass

    def testOAuth2AuthorizationCodeParams(self):
        params = OAuth2AuthorizationCodeParams("EXAMPLE_CODE", "EXAMPLE_STATE")
        assert params.authorization_code == "EXAMPLE_CODE"
        assert params.state == "EXAMPLE_STATE"

    def testOAuth2AuthorizationCodeTokenResponse(self):
        params = OAuth2AuthorizationCodeTokenResponse("bearer", "EXAMPLE_ACCESS_TOKEN", "EXAMPLE_REFRESH_TOKEN", 86400)
        assert params.token_type == "bearer"
        assert params.access_token == "EXAMPLE_ACCESS_TOKEN"
        assert params.refresh_token == "EXAMPLE_REFRESH_TOKEN"
        assert params.expires_in == 86400

    def testOAuth2AuthorizationCode(self):
        assert self.oa2.client_id == "CLIENT_ID"
        assert self.oa2.client_secret == "CLIENT_SECRET"
        assert self.oa2.redirect_uri == "http://localhost:3000/redirect"
        assert self.oa2.base_uri == "https://api-v2.fattureincloud.it"

    def testGetAuthorizationUrl(self):
        scopes = [
            Scope.SETTINGS_ALL,
            Scope.ISSUED_DOCUMENTS_INVOICE_READ
        ]
        url = self.oa2.get_authorization_url(scopes, "EXAMPLE_STATE")

        assert url == "https://api-v2.fattureincloud.it/oauth/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fredirect&scope=settings%3Aa+issued_documents.invoice%3Ar&state=EXAMPLE_STATE"

    def testGetParamsFromUrl(self):
        url = "http://localhost:3000/redirect?state=EXAMPLE_STATE&code=c%2FEXAMPLE_CODE"
        params = self.oa2.get_params_from_url(url)

        assert params.authorization_code == "c/EXAMPLE_CODE"
        assert params.state == "EXAMPLE_STATE"

    # def testFetchToken(self):
    #     resp = {
    #         'status': 200,
    #         'data': '{"token_type": "bearer", "access_token": "a/ACCESS_TOKEN", "refresh_token": "r/REFRESH_TOKEN", "expires_in": 86400}',
    #         'reason': "OK"
    #     }

    #     self.oa2._http.request = unittest.mock.MagicMock(return_value = resp)

    #     result = self.oa2.fetch_token("EXAMPLE_CODE")
    #     assert result.token_type == "bearer"
    #     assert result.access_token == "a/ACCESS_TOKEN"
    #     assert result.refresh_token == "r/REFRESH_TOKEN"
    #     assert result.expires_in == 86400

if __name__ == '__main__':
    unittest.main()
