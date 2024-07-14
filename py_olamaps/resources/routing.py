from http import HTTPStatus

import requests

from py_olamaps.exceptions import APIException
from py_olamaps.utils.CommonEnums import Api


class Routing:
    def __init__(self,
                 client):
        self._api_key = client.api_key

    def directions(self,
                   origin: str,
                   destination: str,
                   waypoints: str = None,
                   x_request_id: str = None,
                   x_correlation_id: str = None,
                   alternatives: bool = False,
                   steps: bool = True,
                   overview: str = "full",
                   languages: str = "en",
                   traffic_metadata: bool = False):
        """
        Description: The Directions API is a service that provides directions between two addresses.

        :param origin: string
        Destination coordinates in the format lat,lng e.g: 12.993103152916301,77.54332622119354

        :param destination: string
        Origin coordinates in the format lat,lng e.g: 12.972006793201695,77.5800850011884

        :param waypoints: string
        Waypoints joined by separator (currently '|'). supported as lat,lng pairs - 12.938399,77.632873|12.938041,77.628285
        Default value: None

        :param x_request_id:
        A UUIDv4 unique to that HTTP request and response combination
        Default value: None

        :param x_correlation_id:
        A UUIDv4 unique over a series of requests and responses, identifying a transaction
        Default value: None

        :param alternatives:
        True if multiple routes are needed between source and destination.
        Default value: false

        :param steps:
        True if steps are needed between source and destination.
        Default value: true

        :param overview:
        Overview geometry either full, simplified or false according to highest zoom level it could be display on, or not at all.
        Default value: full

        :param languages:
        Language in which the response is expected. At the moment following languages are supported - kn (Kannada), en (English) and hi (Hindi).
        Default value: en

        :param traffic_metadata:
        If this field is true, traffic metadata would be sent in the response which will contain type of congestion. (travel_advisory data will only come in response if overview is passed as "full").
        Default value: false
        :return:
        """
        try:
            directions_api_url = Api.Protocol.value + Api.Host.value + Api.Routing_Directions_Endpoint.value

            query_params = {
                "api_key": self._api_key,
                "origin": origin,
                "destination": destination,
                "alternatives": alternatives,
                "steps": steps,
                "overview": overview,
                "languages": languages,
                "traffic_metadata": traffic_metadata,
                **({"waypoints": waypoints} if waypoints is not None else {}),
                **({"x_request_id": x_request_id} if x_request_id is not None else {}),
                **({"x_correlation_id": x_correlation_id} if x_correlation_id is not None else {})
            }

            response = requests.post(directions_api_url, params=query_params)

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
        except Exception:
            raise
