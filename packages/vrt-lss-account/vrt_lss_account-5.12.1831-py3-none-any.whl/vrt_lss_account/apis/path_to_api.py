import typing_extensions

from vrt_lss_account.paths import PathValues
from vrt_lss_account.apis.paths.account_token_generation import AccountTokenGeneration
from vrt_lss_account.apis.paths.account_token_validation import AccountTokenValidation
from vrt_lss_account.apis.paths.account_password import AccountPassword
from vrt_lss_account.apis.paths.account_info import AccountInfo
from vrt_lss_account.apis.paths.account_statistics import AccountStatistics
from vrt_lss_account.apis.paths.account_report import AccountReport
from vrt_lss_account.apis.paths.account_quota import AccountQuota
from vrt_lss_account.apis.paths.account_audit import AccountAudit
from vrt_lss_account.apis.paths.account_data_tracecode import AccountDataTracecode
from vrt_lss_account.apis.paths.account_system_check import AccountSystemCheck
from vrt_lss_account.apis.paths.account_system_version import AccountSystemVersion
from vrt_lss_account.apis.paths.account_file_filename import AccountFileFilename

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNT_TOKEN_GENERATION: AccountTokenGeneration,
        PathValues.ACCOUNT_TOKEN_VALIDATION: AccountTokenValidation,
        PathValues.ACCOUNT_PASSWORD: AccountPassword,
        PathValues.ACCOUNT_INFO: AccountInfo,
        PathValues.ACCOUNT_STATISTICS: AccountStatistics,
        PathValues.ACCOUNT_REPORT: AccountReport,
        PathValues.ACCOUNT_QUOTA: AccountQuota,
        PathValues.ACCOUNT_AUDIT: AccountAudit,
        PathValues.ACCOUNT_DATA_TRACECODE: AccountDataTracecode,
        PathValues.ACCOUNT_SYSTEM_CHECK: AccountSystemCheck,
        PathValues.ACCOUNT_SYSTEM_VERSION: AccountSystemVersion,
        PathValues.ACCOUNT_FILE_FILENAME: AccountFileFilename,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNT_TOKEN_GENERATION: AccountTokenGeneration,
        PathValues.ACCOUNT_TOKEN_VALIDATION: AccountTokenValidation,
        PathValues.ACCOUNT_PASSWORD: AccountPassword,
        PathValues.ACCOUNT_INFO: AccountInfo,
        PathValues.ACCOUNT_STATISTICS: AccountStatistics,
        PathValues.ACCOUNT_REPORT: AccountReport,
        PathValues.ACCOUNT_QUOTA: AccountQuota,
        PathValues.ACCOUNT_AUDIT: AccountAudit,
        PathValues.ACCOUNT_DATA_TRACECODE: AccountDataTracecode,
        PathValues.ACCOUNT_SYSTEM_CHECK: AccountSystemCheck,
        PathValues.ACCOUNT_SYSTEM_VERSION: AccountSystemVersion,
        PathValues.ACCOUNT_FILE_FILENAME: AccountFileFilename,
    }
)
