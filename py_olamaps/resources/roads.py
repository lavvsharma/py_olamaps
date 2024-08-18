from http import HTTPStatus

import requests

from py_olamaps.exceptions import APIException
from py_olamaps.utils.CommonEnums import Api, RoadsApi


class Roads:
    def __init__(self,
                 client):
        self._api_key = client.api_key
        self._access_token = client.access_token

    def snap_to_road(self,
                     points: str,
                     enhance_path: str = None,
                     x_request_id: str = None,
                     x_correlation_id: str = None) -> dict:
        """
        Description: This API captures a list of geographic coordinates and aligns them to the nearest routable road
        segments. It supports up to 100 latitude/longitude pairs per request. The service can optionally enhance the
        path by adding intermediate points to better match the curvature of the road.

        :param points: string
        Description: The points to be snapped. Accepts a list of latitude/longitude pairs separated by commas.
        Coordinates should be separated by the pipe character.
        Example: 12.99927894246456,77.67323803525812|12.992086564113583,77.65899014102202|12.992567456375086,77.65989136324778|12.992672238708593,77.64337109685341|12.99127113597667,77.65716623889841

        :param enhance_path: string
        Description: If true, response includes additional points between the given snapped points to enrich the path
        and match the road’s curvature.
        Example: false or true
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

        query_params["points"] = points

        if enhance_path is not None:
            query_params["enhancePath"] = enhance_path

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        snap_to_road_api_url = Api.Protocol.value + Api.Host.value + RoadsApi.Snap_To_Road_Endpoint.value
        response = requests.get(snap_to_road_api_url, headers=headers, params=query_params)

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

    def nearest_roads(self,
                      points: str,
                      radius: int = 500,
                      x_request_id: str = None,
                      x_correlation_id: str = None) -> dict:
        """
        Description: API to return nearest snapped points for each given coordinate (max 100 points).

        :param points: string
        Description: (format: "|" separated list of lat,longs). Maximum 100 points supported.
        Example: 12.99927894246456,77.67323803525812|12.992086564113583,77.65899014102202|12.992567456375086,77.65989136324778

        :param radius: integer
        Description: Optional (in meters, default 500 meters). When value of radius is between 0 and 1 then it takes
        the default value of radius.
        Example: 500
        Default value: 500

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

        query_params["points"] = points
        query_params["radius"] = radius

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        nearest_roads_api_url = Api.Protocol.value + Api.Host.value + RoadsApi.Nearest_Roads_Endpoint.value
        response = requests.get(nearest_roads_api_url, headers=headers, params=query_params)

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
