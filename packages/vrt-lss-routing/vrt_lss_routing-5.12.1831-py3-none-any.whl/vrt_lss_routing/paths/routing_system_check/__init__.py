# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from vrt_lss_routing.paths.routing_system_check import Api

from vrt_lss_routing.paths import PathValues

path = PathValues.ROUTING_SYSTEM_CHECK