import typing_extensions

from vrt_lss_routing.paths import PathValues
from vrt_lss_routing.apis.paths.routing_route_calculation import RoutingRouteCalculation
from vrt_lss_routing.apis.paths.routing_matrix_calculation import RoutingMatrixCalculation
from vrt_lss_routing.apis.paths.routing_system_check import RoutingSystemCheck
from vrt_lss_routing.apis.paths.routing_system_version import RoutingSystemVersion
from vrt_lss_routing.apis.paths.routing_file_filename import RoutingFileFilename

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ROUTING_ROUTE_CALCULATION: RoutingRouteCalculation,
        PathValues.ROUTING_MATRIX_CALCULATION: RoutingMatrixCalculation,
        PathValues.ROUTING_SYSTEM_CHECK: RoutingSystemCheck,
        PathValues.ROUTING_SYSTEM_VERSION: RoutingSystemVersion,
        PathValues.ROUTING_FILE_FILENAME: RoutingFileFilename,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ROUTING_ROUTE_CALCULATION: RoutingRouteCalculation,
        PathValues.ROUTING_MATRIX_CALCULATION: RoutingMatrixCalculation,
        PathValues.ROUTING_SYSTEM_CHECK: RoutingSystemCheck,
        PathValues.ROUTING_SYSTEM_VERSION: RoutingSystemVersion,
        PathValues.ROUTING_FILE_FILENAME: RoutingFileFilename,
    }
)
