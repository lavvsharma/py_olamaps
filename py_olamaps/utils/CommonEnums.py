from enum import Enum


class Api(Enum):
    Protocol = "https://"
    Host = "api.olamaps.io"


class OAuth(Enum):
    Protocol = "https://"
    Host = "account.olamaps.io"
    Route = "/realms/olamaps/protocol/openid-connect/token"
    Grant_Type = "client_credentials"
    Scope = "openid"


class RoutingApi(Enum):
    Directions_Endpoint = "/routing/v1/directions"
    Distance_Matrix_Endpoint = "/routing/v1/distanceMatrix"


class RoadsApi(Enum):
    Snap_To_Road_Endpoint = "/routing/v1/snapToRoad"
    Nearest_Roads_Endpoint = "/routing/v1/nearestRoads"


class PlacesApi(Enum):
    Autocomplete_Endpoint = "/places/v1/autocomplete"
    Place_Details_Endpoint = "/places/v1/details"
    Nearby_Search_Endpoint = "/places/v1/nearbysearch"
    Text_Search_Endpoint = "/places/v1/textsearch"


class GeocodeApi(Enum):
    Forward_Geocode_Endpoint = "/places/v1/geocode"
    Reverse_Geocode_Endpoint = "/places/v1/reverse-geocode"


class MapTilesApi(Enum):
    Get_Array_Of_Data_Endpoint = "/tiles/vector/v1/data/{datasetName}.json"
    Get_Map_Endpoint = "/tiles/vector/v1/styles.json"
    Get_Style_Endpoint = "/tiles/vector/v1/styles/{styleName}/style.json"
    Static_Map_Image_Based_On_Center_Point_Endpoint = "/tiles/v1/styles/{styleName}/static/{lon},{lat},{zoom}/{width}x{height}.{format}"
    Static_Map_Image_Based_On_Bounding_Box_Endpoint = "/tiles/v1/styles/{styleName}/static/{minx},{miny},{maxx},{maxy}/{width}x{height}.{format}"
    Static_Map_Image_Based_Endpoint = "/tiles/v1/styles/{styleName}/static/auto/{width}x{height}.{format}"
