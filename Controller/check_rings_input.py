INDENT_FROM_THE_EDGE = 5

def check_ring(ring_radius: float, radius: float) -> bool:
    """ Function for checking is the spherometr ring too large
        for mesarment"""

    return ring_radius + INDENT_FROM_THE_EDGE > radius
