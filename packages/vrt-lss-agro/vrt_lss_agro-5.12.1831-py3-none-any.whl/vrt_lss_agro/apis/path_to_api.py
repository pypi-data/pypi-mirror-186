import typing_extensions

from vrt_lss_agro.paths import PathValues
from vrt_lss_agro.apis.paths.agro_plan_calculation import AgroPlanCalculation
from vrt_lss_agro.apis.paths.agro_plan_calculation_async import AgroPlanCalculationAsync
from vrt_lss_agro.apis.paths.agro_plan_calculation_async_id import AgroPlanCalculationAsyncId
from vrt_lss_agro.apis.paths.agro_plan_result_id import AgroPlanResultId
from vrt_lss_agro.apis.paths.agro_plan_validation import AgroPlanValidation
from vrt_lss_agro.apis.paths.agro_system_check import AgroSystemCheck
from vrt_lss_agro.apis.paths.agro_system_version import AgroSystemVersion
from vrt_lss_agro.apis.paths.agro_file_filename import AgroFileFilename

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AGRO_PLAN_CALCULATION: AgroPlanCalculation,
        PathValues.AGRO_PLAN_CALCULATION_ASYNC: AgroPlanCalculationAsync,
        PathValues.AGRO_PLAN_CALCULATION_ASYNC_ID: AgroPlanCalculationAsyncId,
        PathValues.AGRO_PLAN_RESULT_ID: AgroPlanResultId,
        PathValues.AGRO_PLAN_VALIDATION: AgroPlanValidation,
        PathValues.AGRO_SYSTEM_CHECK: AgroSystemCheck,
        PathValues.AGRO_SYSTEM_VERSION: AgroSystemVersion,
        PathValues.AGRO_FILE_FILENAME: AgroFileFilename,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AGRO_PLAN_CALCULATION: AgroPlanCalculation,
        PathValues.AGRO_PLAN_CALCULATION_ASYNC: AgroPlanCalculationAsync,
        PathValues.AGRO_PLAN_CALCULATION_ASYNC_ID: AgroPlanCalculationAsyncId,
        PathValues.AGRO_PLAN_RESULT_ID: AgroPlanResultId,
        PathValues.AGRO_PLAN_VALIDATION: AgroPlanValidation,
        PathValues.AGRO_SYSTEM_CHECK: AgroSystemCheck,
        PathValues.AGRO_SYSTEM_VERSION: AgroSystemVersion,
        PathValues.AGRO_FILE_FILENAME: AgroFileFilename,
    }
)
