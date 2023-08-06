# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from vrt_lss_packer.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    PACKER_PACK_CALCULATION = "/packer/pack/calculation"
    PACKER_PACK_CALCULATION_ASYNC = "/packer/pack/calculation_async"
    PACKER_PACK_CALCULATION_ASYNC_ID = "/packer/pack/calculation_async/{id}"
    PACKER_PACK_RESULT_ID = "/packer/pack/result/{id}"
    PACKER_PACK_VALIDATION = "/packer/pack/validation"
    PACKER_CONVERT_GLTF = "/packer/convert/gltf"
    PACKER_SYSTEM_CHECK = "/packer/system/check"
    PACKER_SYSTEM_VERSION = "/packer/system/version"
    PACKER_FILE_FILENAME = "/packer/file/{filename}"
