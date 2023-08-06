import typing_extensions

from vrt_lss_agro.apis.tags import TagValues
from vrt_lss_agro.apis.tags.plan_api import PlanApi
from vrt_lss_agro.apis.tags.system_api import SystemApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PLAN: PlanApi,
        TagValues.SYSTEM: SystemApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PLAN: PlanApi,
        TagValues.SYSTEM: SystemApi,
    }
)
