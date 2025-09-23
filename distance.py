# GEO1000 - Assignment 2
# Authors: Timber Groeneveld
# Studentnumbers: 4213513

from math import radians, cos, sin, asin, sqrt


def haversin(latlon1, latlon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    
    arguments:
        latlon1 - tuple (lat, lon)
        latlon2 - tuple (lat, lon)

    returns:
        distance between the two coordinates (as float, *not* rounded)
    """
    lat1, lon1 = latlon1            # Unpack tuple
    lat2, lon2 = latlon2
    lat1=radians(lat1)              # Convert degrees to radians
    lat2=radians(lat2)
    lon1=radians(lon1)
    lon2=radians(lon2)
    d_lat = lat2-lat1               # Calculate the difference between the two places' coordinates
    d_lon = lon2-lon1
    # Use the haversin formula to calculate the distance and return it
    distance = 6371.0*(2*asin(sqrt(sin(0.5*d_lat)*sin(0.5*d_lat)+cos(lat1)*cos(lat2)*sin(0.5*d_lon)*sin(0.5*d_lon))))
    return distance

def _test():
    # You can use this function to test the distance calculation
    print(haversin((40.7128,-74.0060),(51.5074,-0.1278)))


if __name__ == "__main__":
    _test()
