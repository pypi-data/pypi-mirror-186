import typing_extensions

from vrt_lss_routing.apis.tags import TagValues
from vrt_lss_routing.apis.tags.route_api import RouteApi
from vrt_lss_routing.apis.tags.matrix_api import MatrixApi
from vrt_lss_routing.apis.tags.system_api import SystemApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ROUTE: RouteApi,
        TagValues.MATRIX: MatrixApi,
        TagValues.SYSTEM: SystemApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ROUTE: RouteApi,
        TagValues.MATRIX: MatrixApi,
        TagValues.SYSTEM: SystemApi,
    }
)
