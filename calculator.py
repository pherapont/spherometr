""" Модуль расчетов радиусов поверхностей и стрелок кривизны
    на основаниие данных пользователя
"""

from math import sqrt

from data import SPHEROMETR


def concave_height(radius: float, kind: str, ring: str) -> float:
    spher = SPHEROMETR[kind][ring]
    diff = radius - spher["ball"]
    sqr_diff = sqrt(diff**2 - spher["radius"]**2)
    return round(diff - sqr_diff, 3)

def convex_height(radius: float, kind: str, ring: str) -> float:
    spher = SPHEROMETR[kind][ring]
    tmp_sum = radius + spher["ball"]
    sqr_diff = sqrt(tmp_sum**2 - spher["radius"]**2)
    return round(tmp_sum - sqr_diff, 3)

if __name__ == "__main__":
    spher = "BIG"
    ring = "RING_1"
    print(SPHEROMETR[spher][ring]["ball"])
    height_1 = convex_height(100, "SMALL", "RING_4")
    height_2 = concave_height(100, "SMALL", "RING_4")
    print(height_1)
    print(height_2)
