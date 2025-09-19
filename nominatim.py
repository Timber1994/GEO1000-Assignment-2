# GEO1000 - Assignment 2

from urllib.request import urlopen, URLError, Request
from urllib.parse import quote
import json


def nominatim(place):
    """Geocode a place name, returns tuple with latitude, longitude 
    returns empty tuple if no place found, or something went wrong.

    Geocoding happens by means of the Nominatim service.
    Please be aware of the rules of using the Nominatim service:

    https://operations.osmfoundation.org/policies/nominatim/

    arguments:
        place - string
    
    returns:
        2-tuple of floats: (latitude, longitude) or
        empty tuple in case of failure
    """
    endpoint = "http://nominatim.openstreetmap.org/search?q="
    params = "&format=json"
    url = endpoint + quote(place) + params
    req = Request(
        url=url,
        data=None,
        headers={"User-Agent": "Nominatim Geocode TU Delft Python GEO1000 Exercise"},
    )
    try:
        # try to fetch
        f = urlopen(req)
        lst = json.loads(f.read().decode("utf-8"))
        loc = tuple(map(float, [lst[0]["lat"], lst[0]["lon"]]))
    except:
        # when something goes wrong,
        # e.g. no place found or timeout: return empty tuple
        return ()
    # otherwise, return the found WGS'84 coordinate
    return loc


def _test():
    # Expected behaviour
    # unknown place leads to empty tuple
    assert nominatim("unknown xxxyyy") == ()
    # delft leads to coordinates of delft
    assert nominatim("delft") == (52.0114017, 4.35839)

    # print output for 4 cities
    for name in ['bratislava', 'delft', 'prague', 'new york']:
        print(name, ":", nominatim(name))


if __name__ == "__main__":
    _test()
