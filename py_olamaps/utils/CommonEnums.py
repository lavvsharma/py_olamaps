from enum import Enum


class Api(Enum):
    Protocol = "https://"
    Host = "api.olamaps.io"
    Routing_Directions_Endpoint = "/routing/v1/directions"
    Places_Autocomplete_Endpoint = "/places/v1/autocomplete"
    Places_Geocode_Endpoint = "/places/v1/geocode"
    Places_Reverse_Geocode_Endpoint = "/places/v1/reverse-geocode"
