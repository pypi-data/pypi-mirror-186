# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from vrt_lss_account.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACCOUNT_TOKEN_GENERATION = "/account/token/generation"
    ACCOUNT_TOKEN_VALIDATION = "/account/token/validation"
    ACCOUNT_PASSWORD = "/account/password"
    ACCOUNT_INFO = "/account/info"
    ACCOUNT_STATISTICS = "/account/statistics"
    ACCOUNT_REPORT = "/account/report"
    ACCOUNT_QUOTA = "/account/quota"
    ACCOUNT_AUDIT = "/account/audit"
    ACCOUNT_DATA_TRACECODE = "/account/data/{tracecode}"
    ACCOUNT_SYSTEM_CHECK = "/account/system/check"
    ACCOUNT_SYSTEM_VERSION = "/account/system/version"
    ACCOUNT_FILE_FILENAME = "/account/file/{filename}"
