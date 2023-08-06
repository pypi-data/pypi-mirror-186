import typing_extensions

from vrt_lss_packer.apis.tags import TagValues
from vrt_lss_packer.apis.tags.pack_api import PackApi
from vrt_lss_packer.apis.tags.convert_api import ConvertApi
from vrt_lss_packer.apis.tags.system_api import SystemApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PACK: PackApi,
        TagValues.CONVERT: ConvertApi,
        TagValues.SYSTEM: SystemApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PACK: PackApi,
        TagValues.CONVERT: ConvertApi,
        TagValues.SYSTEM: SystemApi,
    }
)
