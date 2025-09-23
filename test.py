def dd_dms(decdegrees):
    """Returns tuple (degrees, minutes, seconds) for a value in decimal degrees
    Arguments:
    decdegrees -- float that represents a latitude or longitude value
    returns:
    3-tuple of *not* rounded floats (degrees, minutes, seconds)"""
    decdegrees_abs=abs(float(decdegrees))
    degrees=int(decdegrees_abs)
    min_sec=decdegrees_abs-degrees
    minutes=int(min_sec*60)
    seconds=(min_sec*3600)%60
    if decdegrees<0:
        degrees=-degrees
    return degrees, minutes, seconds

#print(dd_dms(-15.45893649))

def format_dms(dms, is_latitude):
    """Returns a formatted string for *one* part of the coordinate.
    Arguments:
    dms -- tuple of floats (degrees, minutes, seconds)
           that represents a latitude or longitude value
    is_latitude -- boolean that specifies whether ordinate is latitude or longitude
    If is_latitude == True dms represents latitude (north/south)
    If is_latitude == False dms represents longitude (east/west)
    returns:
    Formatted string
    """
    degrees, minutes, seconds=dms
    direction = (
        "N" if (is_latitude and degrees >= 0) else
        "S" if (is_latitude and degrees < 0) else
        "E" if (not is_latitude and degrees >= 0) else
        "W")

    single_coordinate_string=f"""{direction} {degrees}° {minutes}' {seconds:.4f}" """
    return single_coordinate_string

print(format_dms((-3,15,25) ,is_latitude=False))
