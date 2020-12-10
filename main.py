""" The function that defines how to work with users and
    passes data for calculation """

from spherometr_cli import print_header, get_surface_type, get_surface_radius
from spherometr_cli import get_calculations_type, get_surface_height
from spherometr_cli import get_spher_type, get_ring_type, check_response
from calculator import concave_height, convex_height
from user_input_handler import SPHER_TYPE, RING_TYPE


print_header()

calculation_type = get_calculations_type()
surface_type = get_surface_type()
if calculation_type == "1":
    surface_radius = get_surface_radius()
elif calculation_type == "2":
    surface_height = get_surface_height()
spher_type = get_spher_type()
ring_type = get_ring_type()

check_response(calculation_type,
    surface_type, surface_radius, spher_type, ring_type)

kind = SPHER_TYPE[spher_type]
ring = RING_TYPE[ring_type]

if surface_type == "1":
    res = concave_height(surface_radius, kind, ring)
elif surface_type == "2":
    res = convex_height(surface_radius, kind, ring)

print("  Результат:\n\t", res, "мм\n")
