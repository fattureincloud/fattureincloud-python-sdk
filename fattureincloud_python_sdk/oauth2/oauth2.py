from typing import Dict, Iterable
from urllib.parse import urlencode, urlparse, parse_qs
import urllib3
import json

from fattureincloud_python_sdk.oauth2.scopes import Scope


class OAuth2Manager:
    def __init__(
        self,
        client_id: str,
        base_uri: str = "https://api-v2.fattureincloud.it",
    ):
        self._http = urllib3.PoolManager()
        self.client_id = client_id
        self.base_uri = base_uri

    def execute_post(self, uri: str, data: Dict[str, str]):
        body = json.dumps(data).encode("utf-8")

        resp = self._http.request(
            "POST", uri, body=body, headers={"Content-Type": "application/json"}
        )
        res = json.loads(resp.data.decode("utf-8"))
        if resp.status != 200:
            raise OAuth2Error(resp.status, res["error"], res["error_description"])
        return res

    @staticmethod
    def _get_scope_str(scopes: Iterable[Scope]):
        if scopes is None or len(scopes) == 0:
            return " "

        return " ".join(map(lambda x: x.value, scopes))


class OAuth2AuthorizationCodeManager(OAuth2Manager):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        base_uri: str = "https://api-v2.fattureincloud.it",
    ):
        OAuth2Manager.__init__(self, client_id, base_uri)
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

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

        res = self.execute_post(token_uri, data)

        return OAuth2TokenResponse(
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

        res = self.execute_post(token_uri, data)

        return OAuth2TokenResponse(
            res["token_type"],
            res["access_token"],
            res["refresh_token"],
            res["expires_in"],
        )


class OAuth2DeviceCodeManager(OAuth2Manager):
    def __init__(
        self,
        client_id: str,
        base_uri: str = "https://api-v2.fattureincloud.it",
    ):
        OAuth2Manager.__init__(self, client_id, base_uri)

    def get_device_code(self, scopes: Iterable[Scope]):
        token_uri = "{}/oauth/device".format(self.base_uri)
        scope = OAuth2DeviceCodeManager._get_scope_str(scopes)

        data = {
            "client_id": self.client_id,
            "scope": scope,
        }

        res = self.execute_post(token_uri, data)["data"]
        return OAuth2DeviceCodeResponse(
            res["device_code"],
            res["user_code"],
            res["scope"],
            res["verification_uri"],
            res["interval"],
            res["expires_in"],
        )

    def fetch_token(self, code: str):
        token_uri = "{}/oauth/token".format(self.base_uri)
        data = {
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "client_id": self.client_id,
            "device_code": code,
        }

        res = self.execute_post(token_uri, data)

        return OAuth2TokenResponse(
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
            "refresh_token": refresh_token,
        }

        res = self.execute_post(token_uri, data)

        return OAuth2TokenResponse(
            res["token_type"],
            res["access_token"],
            res["refresh_token"],
            res["expires_in"],
        )


class OAuth2AuthorizationCodeParams:
    def __init__(self, authorization_code: str, state: str):
        self.authorization_code = authorization_code
        self.state = state


class OAuth2DeviceCodeResponse:
    def __init__(
        self,
        device_code: str,
        user_code: str,
        scope: Dict[str, str],
        verification_uri: str,
        interval: int,
        expires_in: int,
    ):
        self.device_code = device_code
        self.user_code = user_code
        self.scope = scope
        self.verification_uri = verification_uri
        self.interval = interval
        self.expires_in = expires_in


class OAuth2TokenResponse:
    def __init__(
        self, token_type: str, access_token: str, refresh_token: str, expires_in: int
    ):
        self.token_type = token_type
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in


class OAuth2Error(Exception):
    def __init__(self, status: int, error: str, error_description: str):
        self.status = status
        self.error = error
        self.error_description = error_description
        super().__init__("An error occurred while retrieving token: " + error)
