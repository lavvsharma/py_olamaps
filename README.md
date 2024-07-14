# Ola Maps Python API Wrapper Library (Unofficial)

The Ola Maps Python library provides convenient access to the Ola Maps API from any Python 3.9+ application. The library
currently includes type definitions for [Directions API](https://maps.olakrutrim.com/apidocs/routing) present inside
Routing APIs. Our end goal is to provide all the
endpoints provided by Ola Maps and make it available through this library.

## Installation

```sh
# install from PyPI
pip install py_olamaps
```

## Generate API Key

Follow the official documentation of [Ola Maps](https://maps.olakrutrim.com/docs) to generate the API Key. We will soon
publish an documentation from our end.

## Usage

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