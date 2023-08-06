import typing_extensions

from chain_app_client_sdk.apis.tags import TagValues
from chain_app_client_sdk.apis.tags.auth_api import AuthApi
from chain_app_client_sdk.apis.tags.main_api import MainApi
from chain_app_client_sdk.apis.tags.main_pool_api import MainPoolApi
from chain_app_client_sdk.apis.tags.mass_claiming_api import MassClaimingApi
from chain_app_client_sdk.apis.tags.user_info_api import UserInfoApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTH: AuthApi,
        TagValues.MAIN: MainApi,
        TagValues.MAIN_POOL: MainPoolApi,
        TagValues.MASS_CLAIMING: MassClaimingApi,
        TagValues.USER_INFO: UserInfoApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTH: AuthApi,
        TagValues.MAIN: MainApi,
        TagValues.MAIN_POOL: MainPoolApi,
        TagValues.MASS_CLAIMING: MassClaimingApi,
        TagValues.USER_INFO: UserInfoApi,
    }
)
