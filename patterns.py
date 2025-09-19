# GEO1000 - Assignment 2 (part 3)
# Authors: Timber Groeneveld
# Studentnumbers:


def square_corners(center, half_size):
    """
    Computes the four corners of a square given its center and half side length.

    Arguments:
        center: tuple of floats (x, y) - center coordinates of the square
        half_size: float - half the length of one side of the square

    Returns:
        tuple of 4 points (p1, p2, p3, p4) in counterclockwise order:
            p1 = bottom left
            p2 = bottom right
            p3 = top right
            p4 = top left
    """
    pass


def wkt(p1, p2, p3, p4):
    """
    Returns the Well Known Text (WKT) representation of a square defined by four corner points.

    Arguments:
        p1--p4: 2-tuples of floats representing the square corners in counterclockwise order:
            p1 = bottom left
            p2 = bottom right
            p3 = top right
            p4 = top left

    Returns:
        str: WKT string in the format:
            POLYGON((x1 y1, x2 y2, x3 y3, x4 y4, x1 y1))
            with coordinates formatted to six decimal places.
    """
    pass


def pattern_a(remaining_steps, c, size, scale_factor, file_nm):
    """
    Recursively draws squares in all four corners of the current square.

    Arguments:
        remaining_steps: int - number of recursive steps left
        c: tuple - center coordinates of the current square
        size: float - half side length of the current square
        scale_factor: float - multiplier to determine size of next square (e.g. 0.75 shrinks)
        file_nm: str - output file name

    Returns:
        None
    """
    pass


def pattern_b(remaining_steps, c, size, scale_factor, file_nm):
    """
    Recursively draws squares in all four corners, then writes the current square.

    Arguments:
        remaining_steps: int - number of recursive steps left
        c: tuple - center coordinates of the current square
        size: float - half side length of the current square
        scale_factor: float - multiplier to determine size of next square
        file_nm: str - output file name

    Returns:
        None
    """
    pass


def pattern_c(remaining_steps, c, size, scale_factor, file_nm):
    """
    Recursively draws squares in top corners first, writes the current square, then bottom corners.

    Arguments:
        remaining_steps: int - number of recursive steps left
        c: tuple - center coordinates of the current square
        size: float - half side length of the current square
        scale_factor: float - multiplier to determine size of next square
        file_nm: str - output file name

    Returns:
        None
    """
    pass


# note, main has optional arguments, see Sec 13.5 of ThinkPython2
def main(n=3, c=(0.0, 0.0), size=10.0, scale_factor=0.45):
    """
    Entry point of the program. Initializes output files and triggers square drawing patterns.

    Arguments:
        n: int - number of recursive steps to perform
        c: tuple - center coordinates of the initial square
        size: float - half side length of the initial square
        scale_factor: float - multiplier to determine size of next square (default 0.45)

    Output:
        Each output file begins with a header line:
            steps_left;geometry
        The order of lines corresponds to drawing order in QGIS:
        squares listed later will be rendered on top of earlier ones.
    """
    funcs = [pattern_a, pattern_b, pattern_c]
    file_nms = ["pattern_a.txt", "pattern_b.txt", "pattern_c.txt"]

    for func, file_nm_out in zip(funcs, file_nms):
        # Finish this function (do *not* change the lines already given,
        # but replace the pass statement below in this function
        # and remove this comment)
        pass


if __name__ == "__main__":
    main(3)
