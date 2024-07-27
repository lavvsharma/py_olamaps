from enum import Enum


class Api(Enum):
    Protocol = "https://"
    Host = "api.olamaps.io"
    Routing_Directions_Endpoint = "/routing/v1/directions"
    Places_Autocomplete_Endpoint = "/places/v1/autocomplete"
    Places_Geocode_Endpoint = "/places/v1/geocode"
    Places_Reverse_Geocode_Endpoint = "/places/v1/reverse-geocode"
    Get_Tile_Endpoint = "/tiles/vector/v1/data"
    Get_Map_Endpoint = "/tiles/vector/v1/styles.json"
    Get_Style_Endpoint = "/tiles/vector/v1/styles"
    Get_Glyph_Endpoint = "/tiles/vector/v1/fonts"


class OAuth(Enum):
    Protocol = "https://"
    Host = "account.olamaps.io"
    Route = "/realms/olamaps/protocol/openid-connect/token"
    Grant_Type = "client_credentials"
    Scope = "openid"
