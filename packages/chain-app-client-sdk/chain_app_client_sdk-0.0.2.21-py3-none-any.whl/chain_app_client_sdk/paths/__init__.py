# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from chain_app_client_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AUTH_SIGNUP = "/auth/signup"
    AUTH_SIGNIN = "/auth/signin"
    MAIN_POOL_GET_POOL_SIZE_HISTORY = "/main_pool/get_pool_size_history"
    MAIN_POOL_GET_INFO = "/main_pool/get_info"
    USER_INFO_GET_STAKED_BIND_BY_USER_ID = "/user_info/get_staked_bind_by_user_id"
    USER_INFO_GET_UNSTAKABLE_BIND_BY_USER_ID = "/user_info/get_unstakable_bind_by_user_id"
    USER_INFO_GET_LOCKED_BIND_BY_USER_ID = "/user_info/get_locked_bind_by_user_id"
    USER_INFO_GET_RELEASE_DATE_BY_USER_ID = "/user_info/get_release_date_by_user_id"
    MASS_CLAIMING_MASS_CLAIMING = "/mass_claiming/mass_claiming"
    MASS_CLAIMING_GET_CLAIMABLE_BIND = "/mass_claiming/get_claimable_bind"
    STAKING_ON_BEHALF_STAKE = "/staking_on_behalf/stake"
    MAIN_POOL_ACTIONS_UNSTAKE_TOKEN = "/main_pool_actions/unstake_token"
