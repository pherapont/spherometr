""" The function that defines how to work with users and
    passes data for calculation """

from Views.header import print_header
from Views.input_types import get_calculations_type, get_surface_type
from Views.input_types import get_spher_type, get_ring_type
from Views.input_parametrs import get_surface_radius, get_surface_height
from Views.responses import check_response, result_response
from Views.warnings import radius_warning
from Controller.calculator import concave_height, convex_height
from Controller.calculator import concave_radius, convex_radius
from Controller.check_rings_input import check_ring
from Model.user_input_handler import SPHER_TYPE, RING_TYPE, RADIUS, HEIGHT
from Model.data import SPHEROMETR


print_header()

calculation_type = get_calculations_type()
surface_type = get_surface_type()
spher_type = get_spher_type()
ring_type = get_ring_type(spher_type)

kind = SPHER_TYPE[spher_type]
ring = RING_TYPE[ring_type]

if calculation_type == HEIGHT:
    surface_param = get_surface_radius()
    while check_ring(SPHEROMETR[kind][ring]["radius"], surface_param):
        radius_warning(kind, ring)
        ring_type = get_ring_type(spher_type)
        ring = RING_TYPE[ring_type]
elif calculation_type == RADIUS:
    surface_param = get_surface_height()

check_response(calculation_type,
    surface_type, surface_param, spher_type, ring_type)

if calculation_type == "1":
    if surface_type == "1":
        res = concave_height(surface_param, kind, ring)
    elif surface_type == "2":
        res = convex_height(surface_param, kind, ring)
elif calculation_type == "2":
    if surface_type == "1":
        res = concave_radius(surface_param, kind, ring)
    elif surface_type == "2":
        res = convex_radius(surface_param, kind, ring)

result_response(res)
