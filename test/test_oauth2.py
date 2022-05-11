import unittest
import unittest.mock

from fattureincloud_python_sdk.oauth2.oauth2 import (
    OAuth2AuthorizationCodeParams,
    OAuth2AuthorizationCodeTokenResponse,
    OAuth2AuthorizationCodeError,
    OAuth2AuthorizationCodeManager,
)
from fattureincloud_python_sdk.oauth2.scopes import Scope


class TestOAuth2(unittest.TestCase):
    """OAuth2 unit test stubs"""

    def setUp(self):
        self.oa2 = OAuth2AuthorizationCodeManager(
            "CLIENT_ID", "CLIENT_SECRET", "http://localhost:3000/redirect"
        )
        pass

    def tearDown(self):
        pass

    def testOAuth2AuthorizationCodeParams(self):
        params = OAuth2AuthorizationCodeParams("EXAMPLE_CODE", "EXAMPLE_STATE")
        assert params.authorization_code == "EXAMPLE_CODE"
        assert params.state == "EXAMPLE_STATE"

    def testOAuth2AuthorizationCodeTokenResponse(self):
        params = OAuth2AuthorizationCodeTokenResponse(
            "bearer", "EXAMPLE_ACCESS_TOKEN", "EXAMPLE_REFRESH_TOKEN", 86400
        )
        assert params.token_type == "bearer"
        assert params.access_token == "EXAMPLE_ACCESS_TOKEN"
        assert params.refresh_token == "EXAMPLE_REFRESH_TOKEN"
        assert params.expires_in == 86400

    def testOAuth2AuthorizationCodeError(self):
        err = OAuth2AuthorizationCodeError(
            418, "I'm a teapot", "I'm a teapot, but a really evil one."
        )
        assert err.status == 418
        assert err.error == "I'm a teapot"
        assert err.error_description == "I'm a teapot, but a really evil one."

    def testOAuth2AuthorizationCode(self):
        assert self.oa2.client_id == "CLIENT_ID"
        assert self.oa2.client_secret == "CLIENT_SECRET"
        assert self.oa2.redirect_uri == "http://localhost:3000/redirect"
        assert self.oa2.base_uri == "https://api-v2.fattureincloud.it"

    def testGetScopeStr(self):
        scopes = [Scope.SETTINGS_ALL, Scope.ISSUED_DOCUMENTS_INVOICES_READ]
        scopes_str = OAuth2AuthorizationCodeManager._get_scope_str(scopes)

        assert scopes_str == "settings:a issued_documents.invoices:r"

    def testGetAuthorizationUrl(self):
        scopes = [Scope.SETTINGS_ALL, Scope.ISSUED_DOCUMENTS_INVOICES_READ]
        url = self.oa2.get_authorization_url(scopes, "EXAMPLE_STATE")

        assert (
            url
            == "https://api-v2.fattureincloud.it/oauth/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fredirect&scope=settings%3Aa+issued_documents.invoices%3Ar&state=EXAMPLE_STATE"
        )

    def testGetParamsFromUrl(self):
        url = "http://localhost:3000/redirect?state=EXAMPLE_STATE&code=c%2FEXAMPLE_CODE"
        params = self.oa2.get_params_from_url(url)

        assert params.authorization_code == "c/EXAMPLE_CODE"
        assert params.state == "EXAMPLE_STATE"

    def testFetchToken(self):
        resp = unittest.mock.MagicMock(
            status=200,
            data=b'{"token_type": "bearer", "access_token": "a/ACCESS_TOKEN", "refresh_token": "r/REFRESH_TOKEN", "expires_in": 86400}',
            reason="OK",
        )

        self.oa2._http.request = unittest.mock.MagicMock(return_value=resp)

        result = self.oa2.fetch_token("EXAMPLE_CODE")
        print(result)
        assert result.token_type == "bearer"
        assert result.access_token == "a/ACCESS_TOKEN"
        assert result.refresh_token == "r/REFRESH_TOKEN"
        assert result.expires_in == 86400

        exp_body = b'{"grant_type": "authorization_code", "client_id": "CLIENT_ID", "client_secret": "CLIENT_SECRET", "redirect_uri": "http://localhost:3000/redirect", "code": "EXAMPLE_CODE"}'

        self.oa2._http.request.assert_called_once_with(
            "POST",
            "https://api-v2.fattureincloud.it/oauth/token",
            body=exp_body,
            headers={"Content-Type": "application/json"},
        )

        resp = unittest.mock.MagicMock(
            status=418,
            data=b'{"error": "I\'m a teapot", "error_description": "I\'m a teapot"}',
            reason="I'm a teapot",
        )

        self.oa2._http.request = unittest.mock.MagicMock(return_value=resp)

        with self.assertRaises(OAuth2AuthorizationCodeError) as context:
            self.oa2.fetch_token("EXAMPLE_ERR_CODE")
        assert "An error occurred while retrieving token: I'm a teapot" == "{0}".format(
            context.exception
        )

    def testRefreshToken(self):
        resp = unittest.mock.MagicMock(
            status=200,
            data=b'{"token_type": "bearer", "access_token": "a/ACCESS_TOKEN", "refresh_token": "r/REFRESH_TOKEN", "expires_in": 86400}',
            reason="OK",
        )

        self.oa2._http.request = unittest.mock.MagicMock(return_value=resp)

        result = self.oa2.refresh_token("r/RT")
        print(result)
        assert result.token_type == "bearer"
        assert result.access_token == "a/ACCESS_TOKEN"
        assert result.refresh_token == "r/REFRESH_TOKEN"
        assert result.expires_in == 86400

        exp_body = b'{"grant_type": "refresh_token", "client_id": "CLIENT_ID", "client_secret": "CLIENT_SECRET", "refresh_token": "r/RT"}'

        self.oa2._http.request.assert_called_once_with(
            "POST",
            "https://api-v2.fattureincloud.it/oauth/token",
            body=exp_body,
            headers={"Content-Type": "application/json"},
        )

        resp = unittest.mock.MagicMock(
            status=418,
            data=b'{"error": "I\'m a teapot", "error_description": "I\'m a teapot"}',
            reason="I'm a teapot",
        )

        self.oa2._http.request = unittest.mock.MagicMock(return_value=resp)

        with self.assertRaises(OAuth2AuthorizationCodeError) as context:
            self.oa2.refresh_token("r/ERR_RT")
        assert "An error occurred while retrieving token: I'm a teapot" == "{0}".format(
            context.exception
        )


if __name__ == "__main__":
    unittest.main()
