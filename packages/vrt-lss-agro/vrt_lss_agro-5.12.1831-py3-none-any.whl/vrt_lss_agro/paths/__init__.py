# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from vrt_lss_agro.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AGRO_PLAN_CALCULATION = "/agro/plan/calculation"
    AGRO_PLAN_CALCULATION_ASYNC = "/agro/plan/calculation_async"
    AGRO_PLAN_CALCULATION_ASYNC_ID = "/agro/plan/calculation_async/{id}"
    AGRO_PLAN_RESULT_ID = "/agro/plan/result/{id}"
    AGRO_PLAN_VALIDATION = "/agro/plan/validation"
    AGRO_SYSTEM_CHECK = "/agro/system/check"
    AGRO_SYSTEM_VERSION = "/agro/system/version"
    AGRO_FILE_FILENAME = "/agro/file/{filename}"
