# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from chain_app_client_sdk.paths.user_info_get_release_date_by_user_id import Api

from chain_app_client_sdk.paths import PathValues

path = PathValues.USER_INFO_GET_RELEASE_DATE_BY_USER_ID