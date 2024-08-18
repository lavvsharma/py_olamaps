from http import HTTPStatus

import requests

from py_olamaps.exceptions import APIException
from py_olamaps.utils.CommonEnums import Api, GeocodeApi


class Geocode:
    def __init__(self,
                 client):
        self._api_key = client.api_key
        self._access_token = client.access_token

    def forward_geocode(self,
                        address: str,
                        bounds: str = None,
                        language: str = None,
                        x_request_id: str = None,
                        x_correlation_id: str = None) -> dict:
        """
        Description: Provides probable geographic coordinates and detailed location information including formatted
        address for the given address as input.

        :param address: string
        Description: The address to be geocoded. It cannot be empty.
        Example: Mumbai

        :param bounds: string
        Description: Pipe ("|") separated lat,lng pairs of two corner points of a bounding box.
        Example: 12.905004590071838,77.60793990913315|12.90221233024448,77.60555810753645
        Default value: None

        :param language: string
        Description: The language in which to return the results. Currently only accepts English.
        Example: English
        Default value : None

        :param x_request_id: string
        Description: A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        Description: A UUIDv4 unique over a series of requests and responses, identifying a transaction.
        Default value: None

        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        query_params["address"] = address

        if language is not None:
            query_params["language"] = language

        if bounds is not None:
            query_params["bounds"] = bounds

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        geocode_api_url = Api.Protocol.value + Api.Host.value + GeocodeApi.Forward_Geocode_Endpoint.value
        response = requests.get(geocode_api_url, headers=headers, params=query_params)

        if response.status_code == HTTPStatus.OK:
            return response.json()
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            raise APIException(HTTPStatus.BAD_REQUEST.description, response, query_params)
        elif response.status_code == HTTPStatus.UNAUTHORIZED:
            raise APIException(HTTPStatus.UNAUTHORIZED.description, response, query_params)
        elif response.status_code == HTTPStatus.FORBIDDEN:
            raise APIException(HTTPStatus.FORBIDDEN.description, response, query_params)
        elif response.status_code == HTTPStatus.NOT_FOUND:
            raise APIException(HTTPStatus.NOT_FOUND.description, response, query_params)
        elif response.status_code == HTTPStatus.CONFLICT:
            raise APIException(HTTPStatus.CONFLICT.description, response, query_params)
        elif response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            raise APIException(HTTPStatus.UNPROCESSABLE_ENTITY.description, response, query_params)
        elif response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
            raise APIException(HTTPStatus.TOO_MANY_REQUESTS.value, response, query_params)
        elif response.status_code >= HTTPStatus.INTERNAL_SERVER_ERROR:
            raise APIException(HTTPStatus.INTERNAL_SERVER_ERROR.description, response, query_params)
        else:
            raise APIException("Unknown Error", response, query_params)

    def reverse_geocode(self,
                        latitude_longitude: str,
                        x_request_id: str = None,
                        x_correlation_id: str = None) -> dict:
        """
        Description: This API converts geographic coordinates back into readable addresses or place names based upon
        the satisfying criteria with a reasonable probability.

        :param latitude_longitude: string
        Description: The coordinates of which you want to do the reverse geocoding to get the address.
        Example: 12.931316595874005,77.61649243443775

        :param x_request_id: string
        Description: A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        Description: A UUIDv4 unique over a series of requests and responses, identifying a transaction.Default value: None


        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        query_params["latlng"] = latitude_longitude

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        reverse_geocode_api_url = Api.Protocol.value + Api.Host.value + GeocodeApi.Reverse_Geocode_Endpoint.value
        response = requests.get(reverse_geocode_api_url, headers=headers, params=query_params)

        if response.status_code == HTTPStatus.OK:
            return response.json()
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            raise APIException(HTTPStatus.BAD_REQUEST.description, response, query_params)
        elif response.status_code == HTTPStatus.UNAUTHORIZED:
            raise APIException(HTTPStatus.UNAUTHORIZED.description, response, query_params)
        elif response.status_code == HTTPStatus.FORBIDDEN:
            raise APIException(HTTPStatus.FORBIDDEN.description, response, query_params)
        elif response.status_code == HTTPStatus.NOT_FOUND:
            raise APIException(HTTPStatus.NOT_FOUND.description, response, query_params)
        elif response.status_code == HTTPStatus.CONFLICT:
            raise APIException(HTTPStatus.CONFLICT.description, response, query_params)
        elif response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            raise APIException(HTTPStatus.UNPROCESSABLE_ENTITY.description, response, query_params)
        elif response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
            raise APIException(HTTPStatus.TOO_MANY_REQUESTS.value, response, query_params)
        elif response.status_code >= HTTPStatus.INTERNAL_SERVER_ERROR:
            raise APIException(HTTPStatus.INTERNAL_SERVER_ERROR.description, response, query_params)
        else:
            raise APIException("Unknown Error", response, query_params)
