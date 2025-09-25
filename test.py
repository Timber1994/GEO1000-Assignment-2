def square_corners(center, half_size):
    x_center,y_center=center
    p1=(x_center-half_size,y_center-half_size)
    p2=(x_center+half_size,y_center-half_size)
    p3=(x_center+half_size,y_center+half_size)
    p4=(x_center-half_size,y_center+half_size)
    return p1,p2,p3,p4

def wkt(p1, p2, p3, p4):
    points = [p1, p2, p3, p4]
    wkt_string= f"POLYGON (({p1[0]:.6f} {p1[1]:.6f},{p2[0]:.6f} {p2[1]:.6f},{p3[0]:.6f} {p3[1]:.6f},{p4[0]:.6f} {p4[1]:.6f},{p1[0]:.6f} {p1[1]:.6f}))"
    return wkt_string

def pattern_a(remaining_steps, c, size, scale_factor, file_nm):
    corners=square_corners(c,size)
    wkt_string=wkt(*corners)
    with open(file_nm, "a") as file:
        file.write(wkt_string + "\n")
    if remaining_steps>0:
        for corner in corners:
            pattern_a(remaining_steps-1,corner,size*scale_factor,scale_factor,file_nm)

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

pattern_a(3,(4,4),1,0.5,"polygontest.txt")