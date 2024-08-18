from http import HTTPStatus

import requests

from py_olamaps.exceptions import APIException
from py_olamaps.utils.CommonEnums import Api, RoutingApi


class Routing:
    def __init__(self,
                 client):
        self._api_key = client.api_key
        self._access_token = client.access_token

    def directions(self,
                   origin: str,
                   destination: str,
                   waypoints: str = None,
                   mode: str = None,
                   alternatives: bool = None,
                   steps: bool = None,
                   overview: str = None,
                   languages: str = None,
                   traffic_metadata: bool = None,
                   x_request_id: str = None,
                   x_correlation_id: str = None
                   ) -> dict:
        """
        Description: Provides routable path between two or more points. Accepts coordinates in lat,long format.

        :param origin: string
        Description: Origin coordinates in the format lat,lng.
        Example: 12.993103152916301,77.54332622119354

        :param destination: string
        Description: Destination coordinates in the format lat,lng.
        Example: 12.972006793201695,77.5800850011884

        :param waypoints: string
        Description: Waypoints joined by separator (currently '|'). supported as lat,lng pairs.
        Example: 12.938399,77.632873|12.938041,77.628285

        :param mode: string
        Description: The mode of travel for which the route has to be provided.
        Example: driving, walking

        :param alternatives: boolean
        Description: True if multiple routes are needed between source and destination.
        Default value: None

        :param steps: boolean
        Description: True if steps are needed between source and destination.
        Default value: None

        :param overview: string
        Description: Overview geometry either full, simplified or false according to highest zoom level it could be
        display on, or not at all.
        Default value: None

        :param languages: string
        Description: Language in which the response is expected. At the moment following languages are supported - kn (Kannada),
        en (English) and hi (Hindi).
        Default value: None

        :param traffic_metadata: boolean
        Description: If this field is true, traffic metadata would be sent in the response which will contain type of congestion.
        (travel_advisory data will only come in response if overview is passed as "full").
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

        query_params["origin"] = origin
        query_params["destination"] = destination

        if waypoints is not None:
            query_params["waypoints"] = waypoints

        if mode is not None:
            query_params["mode"] = mode

        if alternatives is not None:
            query_params["alternatives"] = alternatives

        if steps is not None:
            query_params["steps"] = steps

        if overview is not None:
            query_params["overview"] = overview

        if languages is not None:
            query_params["languages"] = languages

        if traffic_metadata is not None:
            query_params["traffic_metadata"] = traffic_metadata

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        directions_api_url = Api.Protocol.value + Api.Host.value + RoutingApi.Directions_Endpoint.value
        response = requests.post(directions_api_url, headers=headers, params=query_params)

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

    def distance_matrix(self,
                        origins: str,
                        destinations: str,
                        x_request_id: str = None,
                        x_correlation_id: str = None) -> dict:
        """
        Description: Provides distance and ETA between different origin and destination points. If there are "x" number
        of origins and "y" number of destinations, the resultant output has "x*y" number of combinations. The origin
        and destination locations are pipe-separated. Please note, as the number of combinations of origins and
        destinations increase, there might be slight degradation in latency metric.

        :param origins: string
        Description: Pipe separated origin coordinates in the format lat1,lng1|lat2,lng2.
        Example: 28.71866756826579,77.03699668376802|28.638555357785652,76.96550156007675

        :param destinations: string
        Description: Pipe separated destination coordinates in the format lat1,lng1|lat2,lng2.
        Example: 28.638555357785652,76.96550156007675|28.53966907108812,77.05190669909288

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

        query_params["origins"] = origins
        query_params["destinations"] = destinations

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        distance_matrix_api_url = Api.Protocol.value + Api.Host.value + RoutingApi.Distance_Matrix_Endpoint.value
        response = requests.get(distance_matrix_api_url, headers=headers, params=query_params)

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
