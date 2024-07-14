import os

from py_olamaps import resources
from py_olamaps.exceptions import OlaMapsError


class OlaMaps:
    def __init__(self,
                 api_key: str = None):
        """
        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `OLA_MAPS_API_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("OLA_MAPS_API_KEY")
        if api_key is None:
            raise OlaMapsError(
                "The resources client option must be set either by passing resources to the client or by setting the OLA_MAPS_API_KEY environment variable"
            )
        self.api_key = api_key
        self.routing = resources.Routing(self)
