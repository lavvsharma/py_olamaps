from enum import Enum


class Api(Enum):
    Protocol = "https://"
    Host = "api.olamaps.io"
    Routing_Directions_Endpoint = "/routing/v1/directions"
