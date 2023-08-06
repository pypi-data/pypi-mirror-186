import typing_extensions

from vrt_lss_account.apis.tags import TagValues
from vrt_lss_account.apis.tags.auth_api import AuthApi
from vrt_lss_account.apis.tags.info_api import InfoApi
from vrt_lss_account.apis.tags.statistics_api import StatisticsApi
from vrt_lss_account.apis.tags.audit_api import AuditApi
from vrt_lss_account.apis.tags.data_api import DataApi
from vrt_lss_account.apis.tags.quotas_api import QuotasApi
from vrt_lss_account.apis.tags.system_api import SystemApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTH: AuthApi,
        TagValues.INFO: InfoApi,
        TagValues.STATISTICS: StatisticsApi,
        TagValues.AUDIT: AuditApi,
        TagValues.DATA: DataApi,
        TagValues.QUOTAS: QuotasApi,
        TagValues.SYSTEM: SystemApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTH: AuthApi,
        TagValues.INFO: InfoApi,
        TagValues.STATISTICS: StatisticsApi,
        TagValues.AUDIT: AuditApi,
        TagValues.DATA: DataApi,
        TagValues.QUOTAS: QuotasApi,
        TagValues.SYSTEM: SystemApi,
    }
)
