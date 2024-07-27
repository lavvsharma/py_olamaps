from http import HTTPStatus

import requests

from py_olamaps.exceptions import APIException
from py_olamaps.utils.CommonEnums import Api


class Places:
    def __init__(self,
                 client):
        self._api_key = client.api_key
        self._access_token = client.access_token

    def autocomplete(self,
                     input: str,
                     x_request_id: str = None,
                     x_correlation_id: str = None,
                     origin: str = None,
                     location: str = None,
                     radius: int = None,
                     strictbounds: bool = None) -> dict:
        """
        Description: Provides Autocomplete suggestions for a given substring satisfying the given criteria.

        :param input: string
        The text string on which to search. The Place Autocomplete service will return candidate matches based on this string and order results based on their perceived relevance.
        Example: kempe

        :param x_request_id: string
        A UUIDv4 unique to that HTTP request and response combination.

        :param x_correlation_id: string
        A UUIDv4 unique over a series of requests and responses, identifying a transaction.

        :param origin: string
        The origin point from which to calculate straight-line distance to the destination (returned as distance_meters). If this value is omitted, straight-line distance will be calculated from provided user location. Must be specified as latitude,longitude.
        Example : 12.931316595874005,77.61649243443775

        :param location: string
        The point around which to retrieve place information. This must be specified as latitude,longitude.
        Example : 12.931316595874005,77.61649243443775

        :param radius: integer
        Defines the distance (in meters) within which to return place results. This is obeyed when the param strictbounds is set to true.

        :param strictbounds: boolean
        Returns only those places that are strictly within the radius defined by location and radius. This is a restriction, rather than a bias, meaning that results outside this radius will not be returned even if they match the user input.

        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        query_params["input"] = input

        if origin is not None:
            query_params["origin"] = origin

        if location is not None:
            query_params["location"] = location

        if radius is not None:
            query_params["radius"] = radius

        if strictbounds is not None:
            query_params["strictbounds"] = strictbounds

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        autocomplete_api_url = Api.Protocol.value + Api.Host.value + Api.Places_Autocomplete_Endpoint.value
        response = requests.get(autocomplete_api_url, headers=headers, params=query_params)

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

    def geocode(self,
                address: str,
                bounds: str = None,
                language: str = "English",
                x_request_id: str = None,
                x_correlation_id: str = None) -> dict:
        """
        Description: Returns the geocoded address based on the provided parameters.

        :param address: string
        The address to be geocoded. It cannot be empty.

        :param bounds: string
        Pipe ("|") separated lat,lng pairs of two corner points of a bounding box.
        Example: 12.905004590071838,77.60793990913315|12.90221233024448,77.60555810753645

        :param language: string
        The language in which to return the results. Currently only accepts English.
        Default value : English

        :param x_request_id: string
        A UUIDv4 unique to that HTTP request and response combination.

        :param x_correlation_id: string
        A UUIDv4 unique over a series of requests and responses, identifying a transaction.

        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        query_params["address"] = address
        query_params["language"] = language

        if bounds is not None:
            query_params["bounds"] = bounds

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        geocode_api_url = Api.Protocol.value + Api.Host.value + Api.Places_Geocode_Endpoint.value
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
                        latlng: str,
                        x_request_id: str = None,
                        x_correlation_id: str = None) -> dict:
        """
        Description: Provides information of a place based on the location provided satisfying the given criteria.

        :param latlng: string
        The coordinates of which you want to do the reverse geocoding to get the address.
        Example: 12.931316595874005,77.61649243443775

        :param x_request_id: string
        A UUIDv4 unique to that HTTP request and response combination.

        :param x_correlation_id: string
        A UUIDv4 unique over a series of requests and responses, identifying a transaction.

        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        query_params["latlng"] = latlng

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        reverse_geocode_api_url = Api.Protocol.value + Api.Host.value + Api.Places_Reverse_Geocode_Endpoint.value
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
