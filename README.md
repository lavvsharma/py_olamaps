# Ola Maps Python API Wrapper Library (Unofficial)

<p align="center">
<a href="https://pypi.org/project/py-olamaps" target="_blank">
    <img src="https://img.shields.io/pypi/v/py-olamaps?color=%2334D058&label=pypi%20package" alt="Package version">
</a>

<a href="https://pypistats.org/packages/py-olamaps" target="_blank">
    <img src="https://img.shields.io/pypi/dm/py-olamaps" alt="Downloads">
</a>
</p>

The Ola Maps Python library provides convenient access to the Ola Maps API from any Python 3.9+ application. The library
currently includes type definitions
for Routing APIs, Roads APIs, Places APIs, Geocoding and Maps Tiles details can be
found [here](https://cloud.olakrutrim.com/console/maps?section=map-docs).

## Installation

```sh
# install from PyPI
pip install py_olamaps
```

## Postman Collection

[Download Postman Collection](https://github.com/lavvsharma/py_olamaps/blob/main/Ola%20Maps.postman_collection.json)

## Generate API Key

Follow the official documentation of [Ola Maps](https://maps.olakrutrim.com/docs) to generate the API Key.

## Usage

1. [Routing APIs](#routing-api)
    1. [Directions API](#directions-api)
    2. [Distance Matrix API](#distance-matrix-api)
2. [Roads API](#roads-api)
    1. [Snap To Road API](#snap-to-road-api)
    2. [Nearest Roads API](#nearest-roads-api)
3. [Places API](#places-api)
    1. [Autocomplete API](#autocomplete-api)
    2. [Place Details API](#place-details-api)
    3. [Nearby Search API](#nearby-search-api)
    4. [Text Search API](#text-search-api)
4. [Geocode API](#geocode-api)
    1. [Forward Geocode](#forward-geocode-api)
    2. [Reverse Geocode](#reverse-geocode-api)
5. [Maps Tiles API](#map-tiles-api)
    1. [Vector Map Tiles API](#vector-map-tiles-api)
        1. [Array of data API](#array-of-data-api)
        2. [Styles API](#styles-api)
        3. [Detail of Style API](#detail-of-a-style-api)
    2. [Static Map Tiles API](#static-map-tiles-api)
        1. [Static Map Image based on Center Point API](#static-map-image-based-on-center-point-api)
        2. [Static Map Image based on Bounding Box API](#static-map-image-based-on-bounding-box-api)
        3. [Static Map Images API](#static-map-image)

## Initialize Client

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

# OR

client = OlaMaps(client_id=os.environ.get("OLA_MAPS_CLIENT_ID"),
                 client_secret=os.environ.get("OLA_MAPS_CLIENT_SECRET"))
```

### Routing API

#### Directions API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

routing_direction = client.routing.directions(
    "12.993103152916301,77.54332622119354",
    "12.972006793201695,77.5800850011884"
)
```

#### Distance Matrix API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

distance_matrix = client.routing.distance_matrix(
    "28.71866756826579,77.03699668376802|28.638555357785652,76.96550156007675",
    "28.638555357785652,76.96550156007675|28.53966907108812,77.05190669909288"
)
```

### Roads API

#### Snap To Road API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

snap_to_Road = client.roads.snap_to_road(
    "12.99927894246456,77.67323803525812|12.992086564113583,77.65899014102202|12.992567456375086,77.65989136324778|12.992672238708593,77.64337109685341|12.99127113597667,77.65716623889841",
)
```

#### Nearest Roads API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

nearest_roads = client.roads.nearest_roads(
    "12.99927894246456,77.67323803525812|12.992086564113583,77.65899014102202|12.992567456375086,77.65989136324778",
)
```

### Places API

#### Autocomplete API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

autocomplete = client.places.autocomplete(
    "kempe"
)
```

#### Place Details API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

place_details = client.places.place_details(
    "ola-platform:a79ed32419962a11a588ea92b83ca78e"
)
```

#### Nearby Search API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

nearby_search = client.places.nearby_search(
    "venue",
    "12.931544865377818,77.61638622280486"
)
```

#### Text Search API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

text_search = client.places.text_search(
    "Cafes in Koramangala"
)
```

### Geocode API

#### Forward Geocode API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

forward_geocode = client.geocode.forward_geocode("Mumbai")
```

#### Reverse Geocode API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

reverse_geocode = client.geocode.reverse_geocode("12.931316595874005,77.61649243443775")
```

### Map Tiles API

#### Vector Map Tiles API

##### Array of data API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

array_of_data = client.map_tiles.array_of_data("planet")
```

##### Styles API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

styles = client.map_tiles.get_map_style()
```

##### Detail of a style API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

detail_of_style = client.map_tiles.get_style_details("default-light-standard")
```

#### Static Map Tiles API

##### Static Map Image based on Center Point API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

# note - the below returns an object as it contains an image
smi_center_point = client.map_tiles.static_map_image_based_on_center_point("default-light-standard", 77.61, 12.93, 15,
                                                                           800, 600, "png")
```

##### Static Map Image based on Bounding Box API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

# note - the below returns an object as it contains an image
smi_bounding_box = client.map_tiles.static_map_image_based_on_bounding_box("default-light-standard", 77.611182859373,
                                                                           12.93219851203095, 77.61513567417848,
                                                                           12.935739723360513, 800, 600, "png")
``` 

##### Static Map Image

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

# note - the below returns an object as it contains an image
static_map_image = client.map_tiles.static_map_image("default-light-standard", 800, 600, "png",
                                                     "77.61,12.93|77.61190639293811,12.937637130956137|width:6|stroke:#00ff44")
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `OLA_MAPS_API_KEY="My API Key"` or `OLA_MAPS_CLIENT_ID="My Client Id"`
and `OLA_MAPS_CLIENT_SECRET="My Client Secret"` to your `.env` file
so that your API Key is not stored in source control.

## Handling errors

Error codes are as followed:

| Status Code | Error Type             |
|-------------|------------------------|
| 400         | `Bad Request`          |
| 401         | `Unauthorized`         |
| 403         | `Forbidden`            |
| 404         | `Not Found`            |
| 409         | `Conflict`             |
| 422         | `Unprocessable Entity` |
| 429         | `Too Many Requests`    |
| >=500       | `InternalServerError`  |

### Retries

Coming Soon...

### Timeouts

Coming Soon...

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain
backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please
   open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://github.com/lavvsharma/py_olamaps/issues) with
questions, bugs, or suggestions.

## Requirements

Python 3.9 or higher.
