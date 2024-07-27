import datetime
import os
from http import HTTPStatus

import requests

from py_olamaps import resources
from py_olamaps.exceptions import OlaMapsError
from py_olamaps.utils.CommonEnums import OAuth


class OlaMaps:
    def __init__(self,
                 api_key: str = None,
                 client_id: str = None,
                 client_secret: str = None):
        """
        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `OLA_MAPS_API_KEY`
        - `client_id` from `OLA_MAPS_CLIENT_ID`
        - `client_secret` from `OLA_MAPS_CLIENT_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("OLA_MAPS_API_KEY")

        if client_id is None:
            client_id = os.environ.get("OLA_MAPS_CLIENT_ID")

        if client_secret is None:
            client_secret = os.environ.get("OLA_MAPS_CLIENT_SECRET")

        if not api_key and not (client_id and client_secret):
            raise OlaMapsError(
                "You must provide either an api_key or both client_id and client_secret. "
                "Set the OLA_MAPS_API_KEY environment variable or pass the api_key, or set both "
                "OLA_MAPS_CLIENT_ID and OLA_MAPS_CLIENT_SECRET environment variables or pass the client_id and client_secret."
            )

        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

        self.access_token = None
        self.token_expiry = None
        self.access_token = self.generate_access_token()

        self.routing = resources.Routing(self)
        self.places = resources.Places(self)
        self.map_tiles = resources.MapTiles(self)

    def generate_access_token(self):
        try:
            if self.access_token and self.token_expiry > datetime.datetime.utcnow():
                return self.access_token

            url = OAuth.Protocol.value + OAuth.Host.value + OAuth.Route.value
            data = {
                "grant_type": OAuth.Grant_Type.value,
                "scope": OAuth.Scope.value,
                "client_id": self.client_id,
                "client_secret": self.client_secret
            }

            response = requests.post(url, data=data)
            if response.status_code == HTTPStatus.OK:
                oauth_response = response.json()
                if "access_token" in oauth_response:
                    self.access_token = oauth_response["access_token"]
                    if "expires_in" in oauth_response:
                        expires_in = oauth_response["expires_in"]
                        self.token_expiry = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
            return self.access_token
        except Exception:
            raise
