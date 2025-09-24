def wkt(p1, p2, p3, p4):
    wtk_string = f"{p1:.6f},{p2:.6f},{p3:.6f},{p4:.6f}"
    return wtk_string


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