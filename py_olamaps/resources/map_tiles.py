from http import HTTPStatus

import requests

from py_olamaps.exceptions import APIException
from py_olamaps.utils.CommonEnums import Api


class MapTiles:
    def __init__(self,
                 client):
        self._api_key = client.api_key
        self._access_token = client.access_token

    def get_tilejson_array(self,
                           dataset_name: str,
                           x_request_id: str = None,
                           x_correlation_id: str = None) -> dict:
        """
        Description: Get array of data's TileJSONs.

        :param dataset_name: string
        Name of the dataset.
        Example: planet

        :param x_request_id: string
        A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        A UUIDv4 unique over a series of requests and responses, identifying a transaction.
        Default value: None

        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        get_tilejson_array_url = Api.Protocol.value + Api.Host.value + Api.Get_Tile_Endpoint.value + f"/{str(dataset_name)}.json"
        response = requests.get(get_tilejson_array_url, headers=headers, params=query_params)

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

    def get_pbf_file(self,
                     dataset_name: str,
                     z: int,
                     x: int,
                     y: int,
                     x_request_id: str = None,
                     x_correlation_id: str = None) -> dict:
        """
        Description: Returns the PBF file for data.

        :param dataset_name: string
        Name of the dataset.
        Example: planet

        :param z: integer
        Mercator tiles's zoom level.
        Example: 14

        :param x: integer
        Specifies the tile's column {x}, as described in the Slippy Map Tilenames specification.
        Example: 110

        :param y: integer
        Specifies the tile's row {y}, as described in the Slippy Map Tilenames specification.
        Example: 1010

        :param x_request_id: string
        A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        A UUIDv4 unique over a series of requests and responses, identifying a transaction.
        Default value: None

        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        get_pdf_file_url = Api.Protocol.value + Api.Host.value + Api.Get_Tile_Endpoint.value + f"/{str(dataset_name)}/{str(z)}/{str(x)}/{str(y)}.pbf"
        response = requests.get(get_pdf_file_url, headers=headers, params=query_params)

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

    def get_map_style(self,
                      x_request_id: str = None,
                      x_correlation_id: str = None) -> dict:
        """
        Description:
        {style-name}-lite: The Lite version of the map style will only include a selection of features, with a primary focus on Navigation platforms.
        {style-name}-standard: The Standard version will have a more granular level of information than lite which can be used for viewing purposes and across all platforms such as mobility, portals, and websites.
        {style-name}-full: Full version will include all the available data of the map features which might not be used now but users will have the option to customize according to their preference. Datasets such as glaciers, and house numbers. (Currently, the full version is WIP and is a copy of the standard)
        Example: For default light, default-light-lite, default-light-standard & default-light-full will be the style names

        :param x_request_id: string
        A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        A UUIDv4 unique over a series of requests and responses, identifying a transaction.
        Default value: None

        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        get_map_style_url = Api.Protocol.value + Api.Host.value + Api.Get_Map_Endpoint.value
        response = requests.get(get_map_style_url, headers=headers, params=query_params)

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

    def get_style_details(self,
                          style_name: str,
                          x_request_id: str = None,
                          x_correlation_id: str = None) -> dict:
        """
        Description: Get detail of a style, This is useful for software developers who want to programmatically read these resources. It isn't necessary for you to read or understand this reference to design or use Mapbox/Maplibre maps. You will need to be familiar with the MapLibre Style Specification to use the Styles API. The Maplibre Style Specification defines the structure of map styles and is the open standard that helps maplibre communicate with APIs and produce maps that are compatible with Maplibre libraries.

        :param style_name: string
        Name of the style.
        Example: default-light-standard

        :param x_request_id: string
        A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        A UUIDv4 unique over a series of requests and responses, identifying a transaction.
        Default value: None

        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        get_style_details_url = Api.Protocol.value + Api.Host.value + Api.Get_Style_Endpoint.value + f"/{str(style_name)}/style.json"
        response = requests.get(get_style_details_url, headers=headers, params=query_params)

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

    def get_glyph_range(self,
                        font_stack: str,
                        start: int,
                        end: int,
                        x_request_id: str = None,
                        x_correlation_id: str = None) -> dict:
        """
        Description: While glyph ranges are usually not of interest unless you're building a map renderer, this is the endpoint you can use to access them. Font glyph ranges are protocol buffer-encoded signed distance fields. They can be used to show fonts at a variety of scales and rotations. One glyph is used at all scales.

        :param font_stack:
        Description: Name of the Font Stack.
        Example: Noto Sans Bold

        :param start: integer
        Description: Start tile number.
        Example: 0

        :param end: integer
        Description: End tile number.
        Example: 255

        :param x_request_id: string
        A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        A UUIDv4 unique over a series of requests and responses, identifying a transaction.
        Default value: None

        :return: dict
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        get_glyph_url = Api.Protocol.value + Api.Host.value + Api.Get_Glyph_Endpoint.value + f"/{str(font_stack)}/{start}-{end}.pbf"
        response = requests.get(get_glyph_url, headers=headers, params=query_params)

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
