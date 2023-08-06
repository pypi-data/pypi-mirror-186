# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from vrt_lss_account.paths.account_statistics import Api

from vrt_lss_account.paths import PathValues

path = PathValues.ACCOUNT_STATISTICS