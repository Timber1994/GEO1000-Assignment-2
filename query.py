# GEO1000 - Assignment 2
# Authors: Timber Groeneveld
# Studentnumbers: 4213513


from nominatim import nominatim
# from nominatim_offline import nominatim # can be used for testing if you are offline
                                          # or if the online Nominatim service does not work
from dms import format_dd_as_dms
from distance import haversin


def query(first=True):
    """Query the WGS'84 coordinates of 2 places and compute the distance
        between them."""
    # Displays a message when calling the function for the first time
    if first:
        print("I will find the distance for you between 2 places.")

    # Asks the user to input a place name, if the user writes 'quit' it returns "Bye bye." and terminates the function
    print("Enter place 1?")
    place1=input().strip()
    if place1 == 'quit':
        print("Bye bye.")
        return

    print("Enter place 2?")
    place2 = input().strip()
    if place2 == 'quit':
        print("Bye bye.")
        return

    # Looks up the coordinate using the nominatim function and either prints the correct coordinates or gives an error
    coord1 = nominatim(place1)
    if not coord1:
        print(f"I did not understand this place: {place1}")
    else:
        print(f"Coordinates for {place1}: {format_dd_as_dms(coord1)}")

    coord2 = nominatim(place2)
    if not coord2:
        print(f"I did not understand this place:{place2}")
    else:
        print(f"Coordinates for {place2}: {format_dd_as_dms(coord2)}")

    # Calculates and prints the distance between the places using the haversin function
    if coord1 and coord2:
        print(f"The distance between {place1} and {place2} is {haversin(coord1, coord2):.1f} km")

    # Recursion skipping the first message
    query(first=False)


if __name__ == "__main__":
    query()
