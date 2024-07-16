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
currently includes type definitions for [Routing APIs](https://maps.olakrutrim.com/apidocs/routing)
and, [Places APIs](https://maps.olakrutrim.com/apidocs/places).

## Installation

```sh
# install from PyPI
pip install py_olamaps
```

## Generate API Key

Follow the official documentation of [Ola Maps](https://maps.olakrutrim.com/docs) to generate the API Key. We will soon
publish an documentation from our end.

## Usage

1. [Routing APIs](#routing)
    1. [Directions API](#directions-api)
2. [Places APIs](#places)
    1. [Autocomplete API](#autocomplete-api)
    2. [Geocode API](#geocode-api)
    3. [Reverse Geocode API](#reverse-geocode-api)

### Routing

#### Directions API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    # This is the default and can be omitted
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

routing_direction = client.routing.directions(
    origin="12.993103152916301,77.54332622119354",
    destination="12.972006793201695,77.5800850011884"
)

print(routing_direction)
# {'status': 'SUCCESS', 'geocoded_waypoints': [{'geocoder_status': 'OK', 'place_id': 'tdr1ut366', 'types': []}, {'geocoder_status': 'OK', 'place_id': 'tdr1v3kp7', 'types': []}], 'routes': [{'summary': '', 'legs': [{'steps': [{'instructions': 'Head west', 'distance': 24, 'readable_distance': '0 km 24 metres', 'maneuver': 'depart', 'duration': 1, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.99312, 'lng': 77.54332}, 'end_location': {'lat': 12.99307, 'lng': 77.54311}, 'bearing_before': 0, 'bearing_after': 257}, {'instructions': 'Go straight onto 10th Main Road', 'distance': 94, 'readable_distance': '0 km 94 metres', 'maneuver': 'continue', 'duration': 26, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.99307, 'lng': 77.54311}, 'end_location': {'lat': 12.99316, 'lng': 77.54223999999999}, 'bearing_before': 255, 'bearing_after': 275}, {'instructions': 'Turn left', 'distance': 132, 'readable_distance': '0 km 132 metres', 'maneuver': 'turn-left', 'duration': 27, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.99316, 'lng': 77.54224}, 'end_location': {'lat': 12.991969999999998, 'lng': 77.54211999999998}, 'bearing_before': 275, 'bearing_after': 192}, {'instructions': 'Turn left', 'distance': 419, 'readable_distance': '0 km 419 metres', 'maneuver': 'turn-left', 'duration': 87, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.99197, 'lng': 77.54212}, 'end_location': {'lat': 12.992030000000002, 'lng': 77.54599}, 'bearing_before': 185, 'bearing_after': 91}, {'instructions': 'Turn right onto Sri M Thimmaiah Road', 'distance': 311, 'readable_distance': '0 km 311 metres', 'maneuver': 'turn-right', 'duration': 67, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.99203, 'lng': 77.54599}, 'end_location': {'lat': 12.989259999999996, 'lng': 77.54567000000002}, 'bearing_before': 87, 'bearing_after': 168}, {'instructions': 'Turn left to stay on Sri M Thimmaiah Road', 'distance': 453, 'readable_distance': '0 km 453 metres', 'maneuver': 'turn-left', 'duration': 81, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.98926, 'lng': 77.54567}, 'end_location': {'lat': 12.987960000000001, 'lng': 77.54962}, 'bearing_before': 185, 'bearing_after': 102}, {'instructions': 'Keep left onto Sri M Thimmaiah Road', 'distance': 126, 'readable_distance': '0 km 126 metres', 'maneuver': 'turn-slight-left', 'duration': 26, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.98796, 'lng': 77.54962}, 'end_location': {'lat': 12.98768, 'lng': 77.55075000000001}, 'bearing_before': 112, 'bearing_after': 98}, {'instructions': 'Make a slight right to stay on Vatal Nagaraj Road', 'distance': 1094, 'readable_distance': '1 km 94 metres', 'maneuver': 'turn-slight-right', 'duration': 155, 'readable_duration': '0 hours 3 minutes', 'start_location': {'lat': 12.98768, 'lng': 77.55075}, 'end_location': {'lat': 12.983710000000004, 'lng': 77.55814}, 'bearing_before': 104, 'bearing_after': 154}, {'instructions': 'Continue onto Rajajinagar Entrance Underpass', 'distance': 393, 'readable_distance': '0 km 393 metres', 'maneuver': 'continue', 'duration': 53, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.98371, 'lng': 77.55814}, 'end_location': {'lat': 12.982680000000002, 'lng': 77.56149999999998}, 'bearing_before': 116, 'bearing_after': 112}, {'instructions': 'Go straight onto Vatal Nagaraj Road', 'distance': 514, 'readable_distance': '0 km 514 metres', 'maneuver': 'continue', 'duration': 91, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.98268, 'lng': 77.5615}, 'end_location': {'lat': 12.981990000000001, 'lng': 77.56617000000001}, 'bearing_before': 101, 'bearing_after': 102}, {'instructions': 'Continue slightly left onto Old Mysuru Road', 'distance': 362, 'readable_distance': '0 km 362 metres', 'maneuver': 'turn-slight-left', 'duration': 67, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.98199, 'lng': 77.56617}, 'end_location': {'lat': 12.982919999999998, 'lng': 77.56934000000001}, 'bearing_before': 116, 'bearing_after': 94}, {'instructions': 'Keep right onto Old Mysuru Road', 'distance': 339, 'readable_distance': '0 km 339 metres', 'maneuver': 'turn-slight-right', 'duration': 80, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.98292, 'lng': 77.56934}, 'end_location': {'lat': 12.980400000000001, 'lng': 77.57092000000003}, 'bearing_before': 95, 'bearing_after': 109}, {'instructions': 'Keep left at the fork', 'distance': 66, 'readable_distance': '0 km 66 metres', 'maneuver': 'turn-slight-left', 'duration': 10, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.9804, 'lng': 77.57092}, 'end_location': {'lat': 12.98019, 'lng': 77.57148000000001}, 'bearing_before': 137, 'bearing_after': 126}, {'instructions': 'Go straight onto Seshadri Road', 'distance': 103, 'readable_distance': '0 km 103 metres', 'maneuver': 'continue', 'duration': 17, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.98019, 'lng': 77.57148}, 'end_location': {'lat': 12.980360000000001, 'lng': 77.57240999999999}, 'bearing_before': 95, 'bearing_after': 78}, {'instructions': 'Continue onto Sheshadri Road', 'distance': 139, 'readable_distance': '0 km 139 metres', 'maneuver': 'continue', 'duration': 17, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.98036, 'lng': 77.57241}, 'end_location': {'lat': 12.98059, 'lng': 77.57367}, 'bearing_before': 78, 'bearing_after': 78}, {'instructions': 'Continue onto Ananda Rao Flyover', 'distance': 647, 'readable_distance': '0 km 647 metres', 'maneuver': 'continue', 'duration': 59, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.98059, 'lng': 77.57367}, 'end_location': {'lat': 12.98041, 'lng': 77.57962}, 'bearing_before': 78, 'bearing_after': 81}, {'instructions': 'Continue onto Sheshadri Road', 'distance': 259, 'readable_distance': '0 km 259 metres', 'maneuver': 'continue', 'duration': 47, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.98041, 'lng': 77.57962}, 'end_location': {'lat': 12.9797, 'lng': 77.58184000000001}, 'bearing_before': 94, 'bearing_after': 92}, {'instructions': 'Turn right', 'distance': 394, 'readable_distance': '0 km 394 metres', 'maneuver': 'turn-right', 'duration': 91, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.9797, 'lng': 77.58184}, 'end_location': {'lat': 12.976719999999997, 'lng': 77.57998999999998}, 'bearing_before': 122, 'bearing_after': 157}, {'instructions': 'Continue onto Kalidasa Road', 'distance': 327, 'readable_distance': '0 km 327 metres', 'maneuver': 'continue', 'duration': 74, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.97672, 'lng': 77.57999}, 'end_location': {'lat': 12.97433, 'lng': 77.57825}, 'bearing_before': 240, 'bearing_after': 237}, {'instructions': 'Continue onto B.V.K. Iyengar Road', 'distance': 201, 'readable_distance': '0 km 201 metres', 'maneuver': 'continue', 'duration': 49, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.97433, 'lng': 77.57825}, 'end_location': {'lat': 12.9728, 'lng': 77.57726000000001}, 'bearing_before': 213, 'bearing_after': 210}, {'instructions': 'Turn left', 'distance': 318, 'readable_distance': '0 km 318 metres', 'maneuver': 'turn-left', 'duration': 72, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.9728, 'lng': 77.57726}, 'end_location': {'lat': 12.971870000000001, 'lng': 77.58003}, 'bearing_before': 213, 'bearing_after': 109}, {'instructions': 'You have arrived at your destination, on the left', 'distance': 0, 'readable_distance': '0 km 0 metres', 'maneuver': 'arrive', 'duration': 0, 'readable_duration': '0 hours 0 minutes', 'start_location': {'lat': 12.97187, 'lng': 77.58003}, 'end_location': {'lat': 12.97187, 'lng': 77.58003}, 'bearing_before': 110, 'bearing_after': 0}], 'distance': 6723, 'readable_distance': '6.72', 'duration': 1208, 'readable_duration': '0 hours 21 minutes', 'start_location': {'lat': 12.993117, 'lng': 77.543323}, 'end_location': {'lat': 12.971865, 'lng': 77.580032}, 'start_address': '12.993117,77.543323', 'end_address': '12.971865,77.580032'}], 'overview_polyline': '_vhnAwdhxMHh@QlDl@JP@r@@ZB^?Z?`@BBgA@{A?aAAqBEsDIyFXCf@GZCf@?`@FnARVFd@Hv@D|@Ft@Jt@DP@Ju@Jy@Fg@\\uAT{@jA{ERkAVw@ZcAJc@Nc@Di@?AJe@d@oClAc@bAC`AE`AETELERMDOB_A?W?g@?i@@_@?]Fa@DUJOdAmAz@q@lAiA`@g@\\k@Fi@Es@EOoB_EK]?q@@w@FUbA}AjB{A@AhAqBFKFSDOFk@H{E@W@WD[@KBODIBIDIl@}@HITYNSLYLWHYFWHg@Fc@?EFwA?ICg@?K?OB]?IDe@BUNqB^{EJw@^gDFm@JU@]?OCOG_@_AgECIOg@EQK]Mk@EKGMSc@KWGUCSCY?S@O?GBKFKFIFE`@OLI^a@NK\\UHIDIBIDEHGdAk@NIp@YNENCNAN?P?N?LALERKLKJIDCJQR]D[Bc@Ee@OoAASAEGi@AOIkAQgAOwAMkBGmAAk@?m@F}CNcE?m@BuCBiAHiBHkBFkADmBJmALw@Po@Xq@t@sAJQFBVINHnBjADBxGnDbCnAN\\NXn@`@VPNHZPRNtBnAzBvA^Td@VBBHFHDDA@@zDxBbBdAH]\\wABMNk@Pu@FUNm@Ps@Je@Ha@Ja@Lk@Ja@DS', 'travel_advisory': '', 'bounds': {}, 'copyrights': 'OLA Map data ©2024', 'warnings': []}], 'source_from': 'Ola Maps'}
```

### Places

#### Autocomplete API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    # This is the default and can be omitted
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

autocomplete = client.places.autocomplete(
    input='kempe'
)

print(autocomplete)
# {'error_message': '', 'info_messages': [], 'predictions': [{'reference': 'a1e99e3bd07b545284643f7bde183120', 'types': ['route'], 'matched_substrings': [{'offset': 12, 'length': 5}, {'offset': 47, 'length': 5}], 'terms': [{'offset': 0, 'value': 'Nada Prabhu Kempe Gowda Main Road'}, {'offset': 35, 'value': 'Nada Prabhu Kempe Gowda Main Rd'}, {'offset': 68, 'value': 'Mariyannapalya'}, {'offset': 84, 'value': 'Hebbal Kempapura'}, {'offset': 102, 'value': 'Bengaluru'}, {'offset': 113, 'value': 'Karnataka'}, {'offset': 124, 'value': '560024'}, {'offset': 132, 'value': 'India'}], 'distance_meters': 13357, 'structured_formatting': {'main_text_matched_substrings': [{'offset': 12, 'length': 5}], 'secondary_text_matched_substrings': [{'offset': 12, 'length': 5}], 'secondary_text': 'Nada Prabhu Kempe Gowda Main Rd, Mariyannapalya, Hebbal Kempapura, Bengaluru, Karnataka, 560024, India', 'main_text': 'Nada Prabhu Kempe Gowda Main Road'}, 'description': 'Nada Prabhu Kempe Gowda Main Road, Nada Prabhu Kempe Gowda Main Rd, Mariyannapalya, Hebbal Kempapura, Bengaluru, Karnataka, 560024, India', 'geometry': {'location': {'lng': 77.61194, 'lat': 13.05155}}, 'place_id': 'ola-platform:a1e99e3bd07b545284643f7bde183120', 'layer': ['venue']}, {'reference': '617f8e0a5d3379eff5e964a90ab33765', 'types': ['point_of_interest', 'establishment'], 'matched_substrings': [{'offset': 0, 'length': 5}, {'offset': 67, 'length': 5}], 'terms': [{'offset': 0, 'value': 'Kempe Gowda Metro Station Bangalore'}, {'offset': 37, 'value': 'Bus Station 02'}, {'offset': 53, 'value': 'Tank Bund Rd'}, {'offset': 67, 'value': 'Kempegowda'}, {'offset': 79, 'value': 'Majestic'}, {'offset': 89, 'value': 'Bengaluru'}, {'offset': 100, 'value': 'Karnataka'}, {'offset': 111, 'value': '560009'}, {'offset': 119, 'value': 'India'}], 'distance_meters': 6897, 'structured_formatting': {'main_text_matched_substrings': [{'offset': 0, 'length': 5}], 'secondary_text_matched_substrings': [{'offset': 30, 'length': 5}], 'secondary_text': 'Bus Station 02, Tank Bund Rd, Kempegowda, Majestic, Bengaluru, Karnataka, 560009, India', 'main_text': 'Kempe Gowda Metro Station Bangalore'}, 'description': 'Kempe Gowda Metro Station Bangalore, Bus Station 02, Tank Bund Rd, Kempegowda, Majestic, Bengaluru, Karnataka, 560009, India', 'geometry': {'location': {'lng': 77.57194, 'lat': 12.97589}}, 'place_id': 'ola-platform:617f8e0a5d3379eff5e964a90ab33765', 'layer': ['venue']}, {'reference': 'a4f15340f49ea2391951e1114d88a42d', 'types': ['route'], 'matched_substrings': [{'offset': 12, 'length': 5}, {'offset': 47, 'length': 5}], 'terms': [{'offset': 0, 'value': 'Nada Prabhu Kempe Gowda Main Road'}, {'offset': 35, 'value': 'Nada Prabhu Kempe Gowda Main Rd'}, {'offset': 68, 'value': 'Fortune Valley'}, {'offset': 84, 'value': 'Thanisandra'}, {'offset': 97, 'value': 'Bengaluru'}, {'offset': 108, 'value': 'Karnataka'}, {'offset': 119, 'value': '560024'}, {'offset': 127, 'value': 'India'}], 'distance_meters': 13416, 'structured_formatting': {'main_text_matched_substrings': [{'offset': 12, 'length': 5}], 'secondary_text_matched_substrings': [{'offset': 12, 'length': 5}], 'secondary_text': 'Nada Prabhu Kempe Gowda Main Rd, Fortune Valley, Thanisandra, Bengaluru, Karnataka, 560024, India', 'main_text': 'Nada Prabhu Kempe Gowda Main Road'}, 'description': 'Nada Prabhu Kempe Gowda Main Road, Nada Prabhu Kempe Gowda Main Rd, Fortune Valley, Thanisandra, Bengaluru, Karnataka, 560024, India', 'geometry': {'location': {'lng': 77.61193, 'lat': 13.05208}}, 'place_id': 'ola-platform:a4f15340f49ea2391951e1114d88a42d', 'layer': ['venue']}, {'reference': '9ecaf543e02a1bb748984584f777ba23', 'types': ['route'], 'matched_substrings': [{'offset': 0, 'length': 5}, {'offset': 18, 'length': 5}], 'terms': [{'offset': 0, 'value': 'Kempe Gowda Road'}, {'offset': 18, 'value': 'Kempe Gowda Rd'}, {'offset': 34, 'value': 'Chikkanna Layout'}, {'offset': 52, 'value': 'HBR Layout'}, {'offset': 64, 'value': 'Bengaluru'}, {'offset': 75, 'value': 'Karnataka'}, {'offset': 86, 'value': '560043'}, {'offset': 94, 'value': 'India'}], 'distance_meters': 12281, 'structured_formatting': {'main_text_matched_substrings': [{'offset': 0, 'length': 5}], 'secondary_text_matched_substrings': [{'offset': 0, 'length': 5}], 'secondary_text': 'Kempe Gowda Rd, Chikkanna Layout, HBR Layout, Bengaluru, Karnataka, 560043, India', 'main_text': 'Kempe Gowda Road'}, 'description': 'Kempe Gowda Road, Kempe Gowda Rd, Chikkanna Layout, HBR Layout, Bengaluru, Karnataka, 560043, India', 'geometry': {'location': {'lng': 77.63878, 'lat': 13.0398}}, 'place_id': 'ola-platform:9ecaf543e02a1bb748984584f777ba23', 'layer': ['venue']}, {'reference': '6d111c6615ba5f74139c7723391b45e4', 'types': ['point_of_interest', 'establishment'], 'matched_substrings': [{'offset': 0, 'length': 5}, {'offset': 35, 'length': 5}], 'terms': [{'offset': 0, 'value': 'Kempe Gowda Nagar'}, {'offset': 19, 'value': 'Telecom Colony'}, {'offset': 0, 'value': 'Kempe Gowda Nagar'}, {'offset': 54, 'value': 'Bengaluru'}, {'offset': 65, 'value': 'Karnataka'}, {'offset': 76, 'value': '560097'}, {'offset': 84, 'value': 'India'}], 'distance_meters': 15830, 'structured_formatting': {'main_text_matched_substrings': [{'offset': 0, 'length': 5}], 'secondary_text_matched_substrings': [{'offset': 16, 'length': 5}], 'secondary_text': 'Telecom Colony, Kempe Gowda Nagar, Bengaluru, Karnataka, 560097, India', 'main_text': 'Kempe Gowda Nagar'}, 'description': 'Kempe Gowda Nagar, Telecom Colony, Kempe Gowda Nagar, Bengaluru, Karnataka, 560097, India', 'geometry': {'location': {'lng': 77.56671, 'lat': 13.06534}}, 'place_id': 'ola-platform:6d111c6615ba5f74139c7723391b45e4', 'layer': ['venue']}], 'status': 'ok'}
```

#### Geocode API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    # This is the default and can be omitted
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

geocode = client.places.geocode(
    address='Mumbai'
)

print(geocode)
# {'geocodingResults': [{'formatted_address': 'Mumbai, Mumbai Suburban, Maharashtra, India', 'types': [], 'name': 'Mumbai', 'geometry': {'viewport': {'southwest': {'lng': 72.87232696702962, 'lat': 19.114096358602232}, 'northeast': {'lng': 72.87498903297039, 'lat': 19.116611641397768}}, 'location': {'lng': 72.873658, 'lat': 19.115354}, 'location_type': 'geometric_center'}, 'address_components': [{'types': ['country'], 'short_name': 'India', 'long_name': 'India'}, {'types': ['administrative_area_level_1'], 'short_name': 'Maharashtra', 'long_name': 'Maharashtra'}, {'types': ['administrative_area_level_3'], 'short_name': 'Mumbai Suburban', 'long_name': 'Mumbai Suburban'}, {'types': ['locality'], 'short_name': 'Mumbai', 'long_name': 'Mumbai'}, {'types': ['postal_code'], 'short_name': '400059', 'long_name': '400059'}, {'types': ['street_address'], 'short_name': 'Road Number 16', 'long_name': 'Road Number 16'}], 'plus_code': {'compound_code': 'NA', 'global_code': 'NA'}, 'place_id': 'ola-platform:1', 'layer': ['locality']}], 'status': 'ok'}
```

#### Reverse Geocode API

```python
import os
from py_olamaps.OlaMaps import OlaMaps

client = OlaMaps(
    # This is the default and can be omitted
    api_key=os.environ.get("OLA_MAPS_API_KEY"),
)

reverse_geocode = client.places.reverse_geocode(
    latlng='12.931316595874005,77.61649243443775'
)

print(reverse_geocode)
# {'error_message': '', 'info_messages': [], 'results': [{'formatted_address': '2, Hosur Rd, Koramangala Industrial Layout, Koramangala, Bengaluru, Karnataka, 560095, India', 'types': [], 'name': '2, Hosur Rd', 'geometry': {'viewport': {'southwest': {'lng': 77.61518963363605, 'lat': 12.930062358602232}, 'northeast': {'lng': 77.61777036636394, 'lat': 12.932577641397767}}, 'location': {'lng': 77.61648, 'lat': 12.93132}, 'location_type': 'approximate'}, 'address_components': [{'types': ['country'], 'short_name': 'India', 'long_name': 'India'}, {'types': ['administrative_area_level_1'], 'short_name': 'KARNATAKA', 'long_name': 'KARNATAKA'}, {'types': ['administrative_area_level_2'], 'short_name': 'Bangalore', 'long_name': 'Bangalore'}, {'types': ['administrative_area_level_3'], 'short_name': 'Bengaluru South', 'long_name': 'Bengaluru South'}, {'types': ['locality'], 'short_name': 'Bengaluru', 'long_name': 'Bengaluru'}, {'types': ['sublocality'], 'short_name': 'Koramangala', 'long_name': 'Koramangala'}, {'types': ['neighborhood'], 'short_name': 'Koramangala Industrial Layout', 'long_name': 'Koramangala Industrial Layout'}, {'types': ['postal_code'], 'short_name': '560095', 'long_name': '560095'}], 'plus_code': {'compound_code': 'NA', 'global_code': 'NA'}, 'place_id': 'ola-platform:89ea4b400c0dd7a73137226759c1e3d2', 'layer': ['venue']}, {'formatted_address': 'Veerabhadra Realtors, Prestige Star Tech A-Block, Koramangala Industrial Layout, Koramangala, Bengaluru, Karnataka, 560095, India', 'types': [], 'name': 'Veerabhadra Realtors', 'geometry': {'viewport': {'southwest': {'lng': 77.61517963368777, 'lat': 12.930052358602232}, 'northeast': {'lng': 77.61776036631224, 'lat': 12.932567641397767}}, 'location': {'lng': 77.61647, 'lat': 12.93131}, 'location_type': 'approximate'}, 'address_components': [{'types': ['country'], 'short_name': 'India', 'long_name': 'India'}, {'types': ['administrative_area_level_1'], 'short_name': 'KARNATAKA', 'long_name': 'KARNATAKA'}, {'types': ['administrative_area_level_2'], 'short_name': 'Bangalore', 'long_name': 'Bangalore'}, {'types': ['administrative_area_level_3'], 'short_name': 'Bengaluru South', 'long_name': 'Bengaluru South'}, {'types': ['locality'], 'short_name': 'Bengaluru', 'long_name': 'Bengaluru'}, {'types': ['sublocality'], 'short_name': 'Koramangala', 'long_name': 'Koramangala'}, {'types': ['neighborhood'], 'short_name': 'Koramangala Industrial Layout', 'long_name': 'Koramangala Industrial Layout'}, {'types': ['postal_code'], 'short_name': '560095', 'long_name': '560095'}], 'plus_code': {'compound_code': 'NA', 'global_code': 'NA'}, 'place_id': 'ola-platform:86036238497f74cc5a41e6132591fb9f', 'layer': ['venue']}, {'formatted_address': 'Indivillage Tech Solutions LLP, No. 139, 2, Hosur Rd, Koramangala Industrial Layout, Koramangala, Bengaluru, Karnataka, 560095, India', 'types': [], 'name': 'Indivillage Tech Solutions LLP', 'geometry': {'viewport': {'southwest': {'lng': 77.61517963342922, 'lat': 12.930102358602232}, 'northeast': {'lng': 77.61776036657079, 'lat': 12.932617641397767}}, 'location': {'lng': 77.61647, 'lat': 12.93136}, 'location_type': 'approximate'}, 'address_components': [{'types': ['country'], 'short_name': 'India', 'long_name': 'India'}, {'types': ['administrative_area_level_1'], 'short_name': 'KARNATAKA', 'long_name': 'KARNATAKA'}, {'types': ['administrative_area_level_2'], 'short_name': 'Bangalore', 'long_name': 'Bangalore'}, {'types': ['administrative_area_level_3'], 'short_name': 'Bengaluru South', 'long_name': 'Bengaluru South'}, {'types': ['locality'], 'short_name': 'Bengaluru', 'long_name': 'Bengaluru'}, {'types': ['sublocality'], 'short_name': 'Koramangala', 'long_name': 'Koramangala'}, {'types': ['neighborhood'], 'short_name': 'Koramangala Industrial Layout', 'long_name': 'Koramangala Industrial Layout'}, {'types': ['postal_code'], 'short_name': '560095', 'long_name': '560095'}], 'plus_code': {'compound_code': 'NA', 'global_code': 'NA'}, 'place_id': 'ola-platform:67b85e9a429cca30a2ab5327944475be', 'layer': ['venue']}, {'formatted_address': 'Ola Campus(c - Wing), 140, Koramangala Industrial Layout, Koramangala, Bengaluru, Karnataka, 560095, India', 'types': [], 'name': 'Ola Campus(c - Wing)', 'geometry': {'viewport': {'southwest': {'lng': 77.61525963373947, 'lat': 12.930042358602233}, 'northeast': {'lng': 77.61784036626054, 'lat': 12.932557641397768}}, 'location': {'lng': 77.61655, 'lat': 12.9313}, 'location_type': 'approximate'}, 'address_components': [{'types': ['country'], 'short_name': 'India', 'long_name': 'India'}, {'types': ['administrative_area_level_1'], 'short_name': 'KARNATAKA', 'long_name': 'KARNATAKA'}, {'types': ['administrative_area_level_2'], 'short_name': 'Bangalore', 'long_name': 'Bangalore'}, {'types': ['administrative_area_level_3'], 'short_name': 'Bengaluru South', 'long_name': 'Bengaluru South'}, {'types': ['locality'], 'short_name': 'Bengaluru', 'long_name': 'Bengaluru'}, {'types': ['sublocality'], 'short_name': 'Koramangala', 'long_name': 'Koramangala'}, {'types': ['neighborhood'], 'short_name': 'Koramangala Industrial Layout', 'long_name': 'Koramangala Industrial Layout'}, {'types': ['postal_code'], 'short_name': '560095', 'long_name': '560095'}], 'plus_code': {'compound_code': 'NA', 'global_code': 'NA'}, 'place_id': 'ola-platform:c266014b05bf1a94780b98b426bb732c', 'layer': ['venue']}, {'formatted_address': 'Ola Electric, 2, Hosur Rd, Koramangala Industrial Layout, Koramangala, Bengaluru, Karnataka, 560095, India', 'types': [], 'name': 'Ola Electric', 'geometry': {'viewport': {'southwest': {'lng': 77.6151796332741, 'lat': 12.930132358602233}, 'northeast': {'lng': 77.61776036672592, 'lat': 12.932647641397768}}, 'location': {'lng': 77.61647, 'lat': 12.93139}, 'location_type': 'approximate'}, 'address_components': [{'types': ['country'], 'short_name': 'India', 'long_name': 'India'}, {'types': ['administrative_area_level_1'], 'short_name': 'KARNATAKA', 'long_name': 'KARNATAKA'}, {'types': ['administrative_area_level_2'], 'short_name': 'Bangalore', 'long_name': 'Bangalore'}, {'types': ['administrative_area_level_3'], 'short_name': 'Bengaluru South', 'long_name': 'Bengaluru South'}, {'types': ['locality'], 'short_name': 'Bengaluru', 'long_name': 'Bengaluru'}, {'types': ['sublocality'], 'short_name': 'Koramangala', 'long_name': 'Koramangala'}, {'types': ['neighborhood'], 'short_name': 'Koramangala Industrial Layout', 'long_name': 'Koramangala Industrial Layout'}, {'types': ['postal_code'], 'short_name': '560095', 'long_name': '560095'}], 'plus_code': {'compound_code': 'NA', 'global_code': 'NA'}, 'place_id': 'ola-platform:a79ed32419962a11a588ea92b83ca78e', 'layer': ['venue']}], 'plus_code': {'compound_code': 'NA', 'global_code': 'NA'}, 'status': 'ok'}
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `OLA_MAPS_API_KEY="My API Key"` to your `.env` file
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
