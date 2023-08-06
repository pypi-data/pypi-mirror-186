import typing_extensions

from vrt_lss_packer.paths import PathValues
from vrt_lss_packer.apis.paths.packer_pack_calculation import PackerPackCalculation
from vrt_lss_packer.apis.paths.packer_pack_calculation_async import PackerPackCalculationAsync
from vrt_lss_packer.apis.paths.packer_pack_calculation_async_id import PackerPackCalculationAsyncId
from vrt_lss_packer.apis.paths.packer_pack_result_id import PackerPackResultId
from vrt_lss_packer.apis.paths.packer_pack_validation import PackerPackValidation
from vrt_lss_packer.apis.paths.packer_convert_gltf import PackerConvertGltf
from vrt_lss_packer.apis.paths.packer_system_check import PackerSystemCheck
from vrt_lss_packer.apis.paths.packer_system_version import PackerSystemVersion
from vrt_lss_packer.apis.paths.packer_file_filename import PackerFileFilename

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PACKER_PACK_CALCULATION: PackerPackCalculation,
        PathValues.PACKER_PACK_CALCULATION_ASYNC: PackerPackCalculationAsync,
        PathValues.PACKER_PACK_CALCULATION_ASYNC_ID: PackerPackCalculationAsyncId,
        PathValues.PACKER_PACK_RESULT_ID: PackerPackResultId,
        PathValues.PACKER_PACK_VALIDATION: PackerPackValidation,
        PathValues.PACKER_CONVERT_GLTF: PackerConvertGltf,
        PathValues.PACKER_SYSTEM_CHECK: PackerSystemCheck,
        PathValues.PACKER_SYSTEM_VERSION: PackerSystemVersion,
        PathValues.PACKER_FILE_FILENAME: PackerFileFilename,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PACKER_PACK_CALCULATION: PackerPackCalculation,
        PathValues.PACKER_PACK_CALCULATION_ASYNC: PackerPackCalculationAsync,
        PathValues.PACKER_PACK_CALCULATION_ASYNC_ID: PackerPackCalculationAsyncId,
        PathValues.PACKER_PACK_RESULT_ID: PackerPackResultId,
        PathValues.PACKER_PACK_VALIDATION: PackerPackValidation,
        PathValues.PACKER_CONVERT_GLTF: PackerConvertGltf,
        PathValues.PACKER_SYSTEM_CHECK: PackerSystemCheck,
        PathValues.PACKER_SYSTEM_VERSION: PackerSystemVersion,
        PathValues.PACKER_FILE_FILENAME: PackerFileFilename,
    }
)
