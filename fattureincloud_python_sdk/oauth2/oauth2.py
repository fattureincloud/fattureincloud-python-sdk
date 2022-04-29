from typing import Iterable
from urllib.parse import urlencode, urlparse, parse_qs
import urllib3
import json

from fattureincloud_python_sdk.oauth2.scopes import Scope


class OAuth2AuthorizationCodeManager:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        base_uri: str = "https://api-v2.fattureincloud.it",
    ):
        self._http = urllib3.PoolManager()
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.base_uri = base_uri

    def get_authorization_url(self, scopes: Iterable[Scope], state: str = None):
        authorization_uri = "{}/oauth/authorize".format(self.base_uri)
        scope = OAuth2AuthorizationCodeManager._get_scope_str(scopes)

        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": scope,
            "state": state,
        }

        query = urlencode(params)
        authorize_url = authorization_uri + "?" + query
        return authorize_url

    def get_params_from_url(self, url: str):
        parsed_url = urlparse(url)

        code = parse_qs(parsed_url.query)["code"][0]
        state = parse_qs(parsed_url.query)["state"][0]
        return OAuth2AuthorizationCodeParams(code, state)

    def fetch_token(self, code: str):
        token_uri = "{}/oauth/token".format(self.base_uri)
        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "code": code,
        }

        body = json.dumps(data).encode("utf-8")

        resp = self._http.request(
            "POST", token_uri, body=body, headers={"Content-Type": "application/json"}
        )
        res = json.loads(resp.data.decode("utf-8"))
        if resp.status != 200:
            raise OAuth2AuthorizationCodeError(
                resp.status, res["error"], res["error_description"]
            )
        return OAuth2AuthorizationCodeTokenResponse(
            res["token_type"],
            res["access_token"],
            res["refresh_token"],
            res["expires_in"],
        )

    def refresh_token(self, refresh_token: str):
        token_uri = "{}/oauth/token".format(self.base_uri)

        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
        }

        body = json.dumps(data).encode("utf-8")

        resp = self._http.request(
            "POST", token_uri, body=body, headers={"Content-Type": "application/json"}
        )
        res = json.loads(resp.data.decode("utf-8"))
        if resp.status != 200:
            raise OAuth2AuthorizationCodeError(
                resp.status, res["error"], res["error_description"]
            )
        return OAuth2AuthorizationCodeTokenResponse(
            res["token_type"],
            res["access_token"],
            res["refresh_token"],
            res["expires_in"],
        )

    @staticmethod
    def _get_scope_str(scopes: Iterable[Scope]):
        if scopes is None or len(scopes) == 0:
            return " "

        return " ".join(map(lambda x: x.value, scopes))


class OAuth2AuthorizationCodeParams:
    def __init__(self, authorization_code: str, state: str):
        self.authorization_code = authorization_code
        self.state = state


class OAuth2AuthorizationCodeTokenResponse:
    def __init__(
        self, token_type: str, access_token: str, refresh_token: str, expires_in: int
    ):
        self.token_type = token_type
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in


class OAuth2AuthorizationCodeError(Exception):
    def __init__(self, status: int, error: str, error_description: str):
        self.status = status
        self.error = error
        self.error_description = error_description
        super().__init__("An error occurred while retrieving token: " + error)
