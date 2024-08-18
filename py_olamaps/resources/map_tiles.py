from http import HTTPStatus

import requests

from py_olamaps.exceptions import APIException
from py_olamaps.utils.CommonEnums import Api, MapTilesApi


class MapTiles:
    def __init__(self,
                 client):
        self._api_key = client.api_key
        self._access_token = client.access_token

    def array_of_data(self,
                      dataset_name: str,
                      x_request_id: str = None,
                      x_correlation_id: str = None) -> dict:
        """
        Description: Get array of data's TileJSONs.

        :param dataset_name: string
        Description: Name of the dataset.
        Example: planet

        :param x_request_id: string
        Description:A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        Description:A UUIDv4 unique over a series of requests and responses, identifying a transaction.
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

        get_array_of_data_url = Api.Protocol.value + Api.Host.value + (
            MapTilesApi.Get_Array_Of_Data_Endpoint.value).format(datasetName=dataset_name)
        response = requests.get(get_array_of_data_url, headers=headers, params=query_params)

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
        {style-name}-lite: The Lite version of the map style will only include a selection of features, with a primary
        focus on Navigation platforms.

        {style-name}-standard: The Standard version will have a more granular level of information than lite which can
        be used for viewing purposes and across all platforms such as mobility, portals, and websites.

        {style-name}-full: Full version will include all the available data of the map features which might not be used
        now but users will have the option to customize according to their preference. Datasets such as glaciers, and
        house numbers. (Currently, the full version is WIP and is a copy of the standard)

        Example: For default light, default-light-lite, default-light-standard & default-light-full will be the
        style names

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

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        get_map_style_url = Api.Protocol.value + Api.Host.value + MapTilesApi.Get_Map_Endpoint.value
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
        Description: Get detail of a style, This is useful for software developers who want to programmatically read
        these resources. It isn't necessary for you to read or understand this reference to design or use
        Mapbox/Maplibre maps. You will need to be familiar with the MapLibre Style Specification to use the Styles API.
        The Maplibre Style Specification defines the structure of map styles and is the open standard that helps
        maplibre communicate with APIs and produce maps that are compatible with Maplibre libraries.

        :param style_name: string
        Description: Name of the style.
        Example: default-light-standard

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

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        get_style_details_url = Api.Protocol.value + Api.Host.value + (MapTilesApi.Get_Style_Endpoint.value).format(
            styleName=style_name)
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

    def static_map_image_based_on_center_point(self,
                                               style_name: str,
                                               longitude: float,
                                               latitude: float,
                                               zoom_level: float,
                                               image_width: int,
                                               image_height: int,
                                               image_format: str,
                                               marker: list[str] = None,
                                               path: str = None,
                                               x_request_id: str = None,
                                               x_correlation_id: str = None) -> object:
        """
        Description: Retrieves a static map image based on the center point and other parameters.

        :param style_name: string
        Description: Name of the style. Currenly we support only "default-light-standard" and "default-dark-standard"
        style names for static images.
        Example: default-light-standard

        :param longitude: float
        Description: Longitude of the center point.
        Example: 77.61

        :param latitude: float
        Description: Latitude of the center point.
        Example: 12.93

        :param zoom_level: integer
        Description: Zoom level. Values range between 0-23. Anything greater than 23, will default to 23.
        Example: 15

        :param image_width: integer
        Description: Image width. Min value is 1 and max value is 2048.
        Example: 800

        :param image_height: integer
        Description: Image height. Min value is 1 and max value is 2048.
        Example: 600

        :param image_format: string
        Description: Image format (e.g., png, jpg).
        Example: png

        :param marker: array[string]
        Description: Add one or more markers to attach to the image at specified locations.
        in format lng,lat|iconColor|option|option|... Currently we ONLY support red and green markers. You can add the
        supported color in the format mentioned above. It takes set of options to customise the marker in the format
        of optionName:optionValue and supports the following options. scale - Factor to scale image by. 0.5 - Scales
        the image to half it's original size offset - Image offset as positive or negative pixel value in format
        [offsetX],[offsetY]. 2,-4 - Image will be moved 2 pixel to the right and 4 pixel in the upwards direction from
        the provided location.
        Example: 77.61,12.93|red|scale:0.9
        Default value: None

        :param path: string
        Description:  Defines a single path of two or more connected points to overlay on the image at specified
        locations. This parameter takes comma-separated lng,lat, pipe-separated pairs. The polyline can also be encoded
        using the 'enc:' prefix. It takes set of options to customise the path in the format of optionName:optionValue
        and supports the following options. width - width of the line path stroke - color of the line path ( Hex Color Value)
        Example: 77.61,12.93|77.61190639293811,12.937637130956137|width:6|stroke:#00ff44
        Default value: None

        :param x_request_id: string
        Description: A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        Description: A UUIDv4 unique over a series of requests and responses, identifying a transaction.
        Default value: None

        :return: object
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        if marker is not None and len(marker) > 0:
            query_params["marker"] = marker

        if path is not None:
            query_params["path"] = path

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        static_image_based_on_center_point_url = Api.Protocol.value + Api.Host.value + (
            MapTilesApi.Static_Map_Image_Based_On_Center_Point_Endpoint.value).format(styleName=style_name,
                                                                                      lon=longitude,
                                                                                      lat=latitude,
                                                                                      zoom=zoom_level,
                                                                                      width=image_width,
                                                                                      height=image_height,
                                                                                      format=image_format)
        response = requests.get(static_image_based_on_center_point_url, headers=headers, params=query_params)

        if response.status_code == HTTPStatus.OK:
            return response
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

    def static_map_image_based_on_bounding_box(self,
                                               style_name: str,
                                               min_x: float,
                                               min_y: float,
                                               max_x: float,
                                               max_y: float,
                                               image_width: int,
                                               image_height: int,
                                               image_format: str,
                                               marker: list[str] = None,
                                               path: str = None,
                                               x_request_id: str = None,
                                               x_correlation_id: str = None) -> object:
        """
        Description: Retrieves a static map image based on the bounding box area and other parameters.

        :param style_name: string
        Description: Name of the style. Currently, we support only "default-light-standard" and "default-dark-standard"
        style names for static images.
        Example: default-light-standard

        :param min_x: float
        Description: Minimum X coordinate (longitude) as part of the bounding box.
        Example: 77.611182859373

        :param min_y: float
        Description: Minimum Y coordinate (latitude) as part of the bounding box.
        Example: 12.93219851203095

        :param max_x: integer
        Description: Maximum X coordinate (longitude) as part of the bounding box.
        Example: 77.61513567417848

        :param max_y: integer
        Description: Maximum Y coordinate (latitude) as part of the bounding box.
        Example: 12.935739723360513

        :param image_width: integer
        Description: Image width. Min value is 1 and max value is 2048.
        Example: 800

        :param image_height: integer
        Description: Image height. Min value is 1 and max value is 2048.
        Example: 600

        :param image_format: string
        Description: Image format (e.g., png, jpg).
        Example: png

        :param marker: array[string]
        Description: Add one or more markers to attach to the image at specified locations. in format
        lng,lat|iconColor|option|option|... Currently we ONLY support red and green markers. You can add the supported
        color in the format mentioned above. It takes set of options to customise the marker in the format of
        optionName:optionValue and supports the following options. scale - Factor to scale image by. 0.5 - Scales the
        image to half it's original size offset - Image offset as positive or negative pixel value in format
        [offsetX],[offsetY]. 2,-4 - Image will be moved 2 pixel to the right and 4 pixel in the upwards direction from
        the provided location.
        Example: 77.61352646534839,12.934719789288083|red|scale:0.9
        Default value: None

        :param path: string
        Description:  Defines a single path of two or more connected points to overlay on the image at specified locations.
        This parameter takes comma-separated lng,lat, pipe-separated pairs. The polyline can also be encoded using the
        'enc:' prefix. It takes set of options to customisze the path in the format of optionName:optionValue and
        supports the following options. width - width of the line path stroke - color of the line path ( Hex Color Value)
        Example: 77.61,12.93|77.61190639293811,12.937637130956137|width:6|stroke:#00ff44
        Default value: None

        :param x_request_id: string
        Description: A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        Description: A UUIDv4 unique over a series of requests and responses, identifying a transaction.
        Default value: None

        :return: object
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        if marker is not None and len(marker) > 0:
            query_params["marker"] = marker

        if path is not None:
            query_params["path"] = path

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        static_image_based_on_bounding_box_url = Api.Protocol.value + Api.Host.value + (
            MapTilesApi.Static_Map_Image_Based_On_Bounding_Box_Endpoint.value).format(styleName=style_name,
                                                                                      minx=min_x,
                                                                                      miny=min_y,
                                                                                      maxx=max_x,
                                                                                      maxy=max_y,
                                                                                      width=image_width,
                                                                                      height=image_height,
                                                                                      format=image_format)
        response = requests.get(static_image_based_on_bounding_box_url, headers=headers, params=query_params)

        if response.status_code == HTTPStatus.OK:
            return response
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

    def static_map_image(self,
                         style_name: str,
                         image_width: int,
                         image_height: int,
                         image_format: str,
                         path: str,
                         marker: list[str] = None,
                         x_request_id: str = None,
                         x_correlation_id: str = None) -> object:
        """
        Description: Retrieves a static map image based on the bounding box area and other parameters.

        :param style_name: string
        Description: Name of the style. Currently, we support only "default-light-standard" and "default-dark-standard"
        style names for static images.
        Example: default-light-standard

        :param image_width: integer
        Description: Image width. Min value is 1 and max value is 2048.
        Example: 800

        :param image_height: integer
        Description: Image height. Min value is 1 and max value is 2048.
        Example: 600

        :param image_format: string
        Description: Image format (e.g., png, jpg).
        Example: png

        :param path: string
        Description: Defines a single path of two or more connected points to overlay on the image at specified locations.
        This parameter takes comma-separated lng,lat, pipe-separated pairs. The polyline can also be encoded using the
        'enc:' prefix. It takes set of options to customize the path in the format of optionName:optionValue and
        supports the following options. width - width of the line path stroke - color of the line path ( Hex Color Value)
        Example: 77.61,12.93|77.61190639293811,12.937637130956137|width:6|stroke:#00ff44

        :param marker: array[string]
        Description: Add one or more markers to attach to the image at specified locations. in format
        lng,lat|iconColor|option|option|... Currently we ONLY support red and green markers. You can add the supported
        color in the format mentioned above. It takes set of options to customise the marker in the format of
        optionName:optionValue and supports the following options. scale - Factor to scale image by. 0.5 - Scales the
        image to half it's original size offset - Image offset as positive or negative pixel value in format
        [offsetX],[offsetY]. 2,-4 - Image will be moved 2 pixel to the right and 4 pixel in the upwards direction from
        the provided location.
        Example: 77.61,12.93|red|scale:0.9
        Default value: None

        :param x_request_id: string
        Description: A UUIDv4 unique to that HTTP request and response combination.
        Default value: None

        :param x_correlation_id: string
        Description: A UUIDv4 unique over a series of requests and responses, identifying a transaction.
        Default value: None

        :return: object
        """
        query_params = dict()
        headers = dict()

        if self._api_key is None:
            headers["Authorization"] = f"Bearer {str(self._access_token)}"
        else:
            query_params["api_key"] = self._api_key

        if marker is not None and len(marker) > 0:
            query_params["marker"] = marker

        if path is not None:
            query_params["path"] = path

        if x_request_id is not None:
            headers["x_request_id"] = x_request_id

        if x_correlation_id is not None:
            headers["x_correlation_id"] = x_correlation_id

        static_image_based_url = Api.Protocol.value + Api.Host.value + (
            MapTilesApi.Static_Map_Image_Based_Endpoint.value).format(styleName=style_name,
                                                                      width=image_width,
                                                                      height=image_height,
                                                                      format=image_format)
        response = requests.get(static_image_based_url, headers=headers, params=query_params)

        if response.status_code == HTTPStatus.OK:
            return response
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
