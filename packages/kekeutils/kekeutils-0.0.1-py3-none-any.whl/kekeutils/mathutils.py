from .modules.point_in_polygon import point_inside_polygon

def point_within_polygon(point: tuple = None, polygon: list = None):
    """
    The point_within_polygon function checks whether a given point is inside a polygon.
    It returns 1 if the given point is inside the polygon provided, and 0 if the point is outside the polygon.

    :param tuple point: A tuple of x and y coordinates representing a point to be checked for inclusion within a polygon.
    :param list polygon: A list of tuples with x and y values forming a polygon.
   
    :raises TypeError: If point or polygon are given in the wrong format.
    """
    if not isinstance(point, tuple) or not isinstance(polygon, list):
        raise TypeError

    belongs = point_inside_polygon(point, polygon)
    
    return belongs
