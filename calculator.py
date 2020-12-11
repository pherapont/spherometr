""" Модуль расчетов радиусов поверхностей и стрелок кривизны
    на основаниие данных пользователя
"""

from math import sqrt

from data import SPHEROMETR


def concave_height(radius: float, kind: str, ring: str) -> float:
    """ The function for calculation height of concave
        surface optical detail """

    spher = SPHEROMETR[kind][ring]
    diff = radius - spher["ball"]
    sqr_diff = sqrt(diff**2 - spher["radius"]**2)
    return round(diff - sqr_diff, 3)

def convex_height(radius: float, kind: str, ring: str) -> float:
    """ The function for calculation height of convex
        surface optical detail """

    spher = SPHEROMETR[kind][ring]
    tmp_sum = radius + spher["ball"]
    sqr_diff = sqrt(tmp_sum**2 - spher["radius"]**2)
    return round(tmp_sum - sqr_diff, 3)

def concave_radius(height: float, kind:str, ring:str) -> float:
    """ The function for calculation radius of concave
        surface optical detail """

    spher = SPHEROMETR[kind][ring]
    first_term = spher["radius"]**2 / 2 / height
    second_term = height / 2
    return round(first_term + second_term + spher["ball"], 1)

def convex_radius(height: float, kind:str, ring:str) -> float:
    """ The function for calculation radius of convex
        surface optical detail """

    spher = SPHEROMETR[kind][ring]
    print(height, type(height))
    first_term = spher["radius"]**2 / 2 / height
    second_term = height / 2
    return round(first_term + second_term - spher["ball"], 1)

if __name__ == "__main__":
    spher = "BIG"
    ring = "RING_1"
    print(SPHEROMETR[spher][ring]["ball"])
    height_1 = convex_height(100, "SMALL", "RING_4")
    height_2 = concave_height(100, "SMALL", "RING_4")
    radius_1 = concave_radius(0.135, "SMALL", "RING_7")
    radius_2 = convex_radius(0.135, "SMALL", "RING_7")
    print("height_1", height_1)
    print("height_2", height_2)
    print("radius_1", radius_1)
    print("radius_3", radius_2)
