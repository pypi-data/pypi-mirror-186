from typing import List, Tuple


def point_in_polygon(point: Tuple[float], vertices: List[List[float]]) -> bool:
    """
    Function that calculates if given 2 dimensional point "point" is within area of polygon, which
    is formed from the "vertices" matrix.

    :param point: 2D Point to consider
    :param vertices: Matrix of 2D points form a polygon
    :return: True or False, depends on the outcome
    """

    inside = False
    n = len(vertices)
    x = point[0]
    y = point[1]

    for i in range(n):
        j = (i + 1) % n
        if ((vertices[i][1] > y) != (vertices[j][1] > y)) and (x < (vertices[j][0] - vertices[i][0]) * (y - vertices[i][1]) / (vertices[j][1] - vertices[i][1]) + vertices[i][0]):
            inside = not inside

    return inside
