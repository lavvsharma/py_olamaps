from http import HTTPStatus

import requests

from py_olamaps.exceptions import APIException
from py_olamaps.utils.CommonEnums import Api, PlacesApi


class Places:
    def __init__(self,
                 client):
        self._api_key = client.api_key
        self._access_token = client.access_token

    def autocomplete(self,
                     input: str,
                     origin: str = None,
                     location: str = None,
                     radius: int = 0,
                     strictbounds: bool = None,
                     x_request_id: str = None,
                     x_correlation_id: str = None) -> dict:
        """
        Description: Provides Autocomplete suggestions for a given substring satisfying the given criteria.
        Helpful Tip: Use with a debounce function to reduce number of calls

        :param input: string
        Description: The text string on which to search. The Place Autocomplete service will return candidate matches
        based on this string and order results based on their perceived relevance
        Example: kempe

        :param origin: string
        Description: The origin point from which to calculate straight-line distance to the destination (returned as
        distance_meters). If this value is omitted, straight-line distance will be calculated from provided user
        location. Must be specified as latitude,longitude.
        Example: 12.931316595874005,77.61649243443775
        Default value: None

        :param location: string
        Description: Location parameter helps in fetching more location specific results. This parameter must be
        specified as latitude,longitude. Note : If the location parameter is not specified, only name match is
        given priority.
        Example: 12.931316595874005,77.61649243443775
        Default value: None

        :param radius: integer
        Description: Defines the distance (in meters) within which to return place results. This is obeyed when the
        param strictbounds is set to true.
        Default value: 0

        :param strictbounds: boolean
        Description: Returns only those places that are strictly within the radius defined by location and radius. This
        is a restriction, rather than a bias, meaning that results outside this radius will not be returned even if
        they match the user input.
        Default value: None

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

        query_params["input"] = input

        if origin is not None:
            query_params["origin"] = origin

        if location is not None:
            query_params["location"] = location

        if radius != 0:
            query_params["radius"] = radius

        if strictbounds is not None:
            query_params["strictbounds"] = strictbounds

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        autocomplete_api_url = Api.Protocol.value + Api.Host.value + PlacesApi.Autocomplete_Endpoint.value
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

    def place_details(self,
                      place_id: str,
                      x_request_id: str = None,
                      x_correlation_id: str = None) -> dict:
        """
        Description: Provides Place Details of a particular Place/POI whose place_id necessarily needs to be given as
        an input.

        :param place_id: string
        Description: Place Id of the Place/POI whose details are to be fetched.
        Example: ola-platform:a79ed32419962a11a588ea92b83ca78e

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

        query_params["place_id"] = place_id

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        place_details_api_url = Api.Protocol.value + Api.Host.value + PlacesApi.Place_Details_Endpoint.value
        response = requests.get(place_details_api_url, headers=headers, params=query_params)

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

    def nearby_search(self,
                      layers: str,
                      location: str,
                      types: str = None,
                      radius: int = 0,
                      strictbounds: bool = None,
                      with_centroid: bool = None,
                      limit: int = 5,
                      x_request_id: str = None,
                      x_correlation_id: str = None) -> dict:
        """
        Description: The Nearby Search Api provides nearby places of a particular category/type as requested in input
        based on the given input location.

        :param layers: string
        Description: POI layer on which user needs to search. Multiple values can be provided separated by a comma.
        Note: The API may return zero_results if no layer is matched.
        Example: venue

        :param location: string
        Description: The latitude/longitude around which to retrieve nearby places information.
        Example: 12.931544865377818,77.61638622280486

        :param types: string
        Description: Restricts the results to places matching the specified category.Multiple values can be provided separated by a comma.
        Note: The API may return zero_results if no type is matched.
        Example: restaurant
        Default value: None

        :param radius: integer
        Description: The distance (in meters) within which to return place results.
        Example: 6000
        Default value: 0

        :param strictbounds: boolean
        Description: Whether the places returned will be strictly within the region defined by origin and radius.
        Example: true or false
        Default value: None

        :param with_centroid: boolean
        Description: Whether the places returned will have geometry (centroid) information.
        Example: true or false
        Default value: None

        :param limit: integer
        Description: The maximum number of results to return in response.
        Note: Minimum value is 5 and Maximum is 50.
        Example: 6000
        Default value: 5

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

        query_params["layers"] = layers
        query_params["location"] = location

        if types is not None:
            query_params["types"] = types

        if radius != 0:
            query_params["radius"] = radius

        if strictbounds is not None:
            query_params["strictbounds"] = strictbounds

        if with_centroid is not None:
            query_params["withCentroid"] = with_centroid

        query_params["limit"] = limit

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        nearby_search_api_url = Api.Protocol.value + Api.Host.value + PlacesApi.Nearby_Search_Endpoint.value
        response = requests.get(nearby_search_api_url, headers=headers, params=query_params)

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

    def text_search(self,
                    input: str,
                    location: str = None,
                    radius: int = 0,
                    types: str = None,
                    size: int = 0,
                    x_request_id: str = None,
                    x_correlation_id: str = None) -> dict:
        """
        Description: Provides a list of places based on textual queries without need of actual location coordinates.
        For eg: "Cafes in Koramangala" or "Restaurants near Bangalore".

        :param input: string
        Description: The text query on which to search. The query must be a string.
        Example: Cafes in Koramangala

        :param location: string
        Description: Optionally, you can specify a location to search around that particular location. The location
        must be a string in the format of 'latitude,longitude'.
        Note: Location will be overridden if some place is mentioned in the input query.
        Example: 12.93142,77.61645
        Default value: None

        :param radius: integer
        Description: Radius will be used if you want to restrict the search results to a certain radius around
        the location.
        Note: Radius should be given along with the location.
        Example: 5000
        Default value: 0

        :param types: string
        Description: Restricts the results to places matching the specified type. Multiple values can be provided
        separated by a comma (,).
        Example: cafe
        Default value: None

        :param size: integer
        Description: The maximum number of results to return in response.
        Example: 5
        Default value: 0

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

        query_params["input"] = input

        if location is not None:
            query_params["location"] = location

        if radius != 0:
            query_params["radius"] = types

        if types is not None:
            query_params["types"] = types

        if size != 0:
            query_params["size"] = size

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        text_search_api_url = Api.Protocol.value + Api.Host.value + PlacesApi.Text_Search_Endpoint.value
        response = requests.get(text_search_api_url, headers=headers, params=query_params)

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
