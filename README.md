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
for [Routing APIs](https://maps.olakrutrim.com/apidocs/routing), [Places APIs](https://maps.olakrutrim.com/apidocs/places)
and [Maps Tiles](https://maps.olakrutrim.com/apidocs/tiles).

## Installation

```sh
# install from PyPI
pip install py_olamaps
```

## Generate API Key

Follow the official documentation of [Ola Maps](https://maps.olakrutrim.com/docs) to generate the API Key. We will soon
publish a documentation from our end.

## Usage

1. [Routing APIs](#routing)
    1. [Directions API](#directions-api)
2. [Places APIs](#places)
    1. [Autocomplete API](#autocomplete-api)
    2. [Geocode API](#geocode-api)
    3. [Reverse Geocode API](#reverse-geocode-api)
3. [Maps Tiles API](#map-tiles)
    1. [Array of data's TileJSONs](#array-of-datas-tilejsons)
    2. [PBF file for data](#pbf-file-for-data)
    3. [Styles](#styles)
    4. [Detail of a style](#detail-of-a-style)
    5. [Glyph range](#glyph-range)

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

### Routing

#### Directions API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

routing_direction = client.routing.directions(
    origin="12.993103152916301,77.54332622119354",
    destination="12.972006793201695,77.5800850011884"
)
```

### Places

#### Autocomplete API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

autocomplete = client.places.autocomplete(
    input='kempe'
)
```

#### Geocode API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

geocode = client.places.geocode(
    address='Mumbai'
)
```

#### Reverse Geocode API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

reverse_geocode = client.places.reverse_geocode(
    latlng='12.931316595874005,77.61649243443775'
)
```

### Map Tiles

#### Array of data's TileJSONs

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

array_of_data = client.map_tiles.get_tilejson_array("planet")
```

#### PBF file for data

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

pbf_file = client.map_tiles.get_pbf_file("planet", 14, 110, 1010)
```

#### Styles

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

styles = client.map_tiles.get_map_style()
```

#### Detail of a style

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

detail_of_style = client.map_tiles.get_style_details("default-light-standard")
```

#### Glyph range

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

glyph_range = client.map_tiles.get_glyph_range("Noto Sans Bold", 0, 255)
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

### Limitation

1. Currently, only api key is being used for sending request to Ola Maps API. Soon, the support for sending API request
   with
   client
   id and client secret will be added.
2. This is because I am facing a issue with Reverse Geocode API which is a part of Places API. The issue is raised with
   Ola Maps team for the same.

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
