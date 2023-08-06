import typing_extensions

from chain_app_client_sdk.paths import PathValues
from chain_app_client_sdk.apis.paths.auth_signup import AuthSignup
from chain_app_client_sdk.apis.paths.auth_signin import AuthSignin
from chain_app_client_sdk.apis.paths.main_pool_get_pool_size_history import MainPoolGetPoolSizeHistory
from chain_app_client_sdk.apis.paths.main_pool_get_info import MainPoolGetInfo
from chain_app_client_sdk.apis.paths.user_info_get_staked_bind_by_user_id import UserInfoGetStakedBindByUserId
from chain_app_client_sdk.apis.paths.user_info_get_unstakable_bind_by_user_id import UserInfoGetUnstakableBindByUserId
from chain_app_client_sdk.apis.paths.user_info_get_locked_bind_by_user_id import UserInfoGetLockedBindByUserId
from chain_app_client_sdk.apis.paths.user_info_get_release_date_by_user_id import UserInfoGetReleaseDateByUserId
from chain_app_client_sdk.apis.paths.mass_claiming_mass_claiming import MassClaimingMassClaiming
from chain_app_client_sdk.apis.paths.mass_claiming_get_claimable_bind import MassClaimingGetClaimableBind
from chain_app_client_sdk.apis.paths.staking_on_behalf_stake import StakingOnBehalfStake
from chain_app_client_sdk.apis.paths.main_pool_actions_unstake_token import MainPoolActionsUnstakeToken

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH_SIGNUP: AuthSignup,
        PathValues.AUTH_SIGNIN: AuthSignin,
        PathValues.MAIN_POOL_GET_POOL_SIZE_HISTORY: MainPoolGetPoolSizeHistory,
        PathValues.MAIN_POOL_GET_INFO: MainPoolGetInfo,
        PathValues.USER_INFO_GET_STAKED_BIND_BY_USER_ID: UserInfoGetStakedBindByUserId,
        PathValues.USER_INFO_GET_UNSTAKABLE_BIND_BY_USER_ID: UserInfoGetUnstakableBindByUserId,
        PathValues.USER_INFO_GET_LOCKED_BIND_BY_USER_ID: UserInfoGetLockedBindByUserId,
        PathValues.USER_INFO_GET_RELEASE_DATE_BY_USER_ID: UserInfoGetReleaseDateByUserId,
        PathValues.MASS_CLAIMING_MASS_CLAIMING: MassClaimingMassClaiming,
        PathValues.MASS_CLAIMING_GET_CLAIMABLE_BIND: MassClaimingGetClaimableBind,
        PathValues.STAKING_ON_BEHALF_STAKE: StakingOnBehalfStake,
        PathValues.MAIN_POOL_ACTIONS_UNSTAKE_TOKEN: MainPoolActionsUnstakeToken,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH_SIGNUP: AuthSignup,
        PathValues.AUTH_SIGNIN: AuthSignin,
        PathValues.MAIN_POOL_GET_POOL_SIZE_HISTORY: MainPoolGetPoolSizeHistory,
        PathValues.MAIN_POOL_GET_INFO: MainPoolGetInfo,
        PathValues.USER_INFO_GET_STAKED_BIND_BY_USER_ID: UserInfoGetStakedBindByUserId,
        PathValues.USER_INFO_GET_UNSTAKABLE_BIND_BY_USER_ID: UserInfoGetUnstakableBindByUserId,
        PathValues.USER_INFO_GET_LOCKED_BIND_BY_USER_ID: UserInfoGetLockedBindByUserId,
        PathValues.USER_INFO_GET_RELEASE_DATE_BY_USER_ID: UserInfoGetReleaseDateByUserId,
        PathValues.MASS_CLAIMING_MASS_CLAIMING: MassClaimingMassClaiming,
        PathValues.MASS_CLAIMING_GET_CLAIMABLE_BIND: MassClaimingGetClaimableBind,
        PathValues.STAKING_ON_BEHALF_STAKE: StakingOnBehalfStake,
        PathValues.MAIN_POOL_ACTIONS_UNSTAKE_TOKEN: MainPoolActionsUnstakeToken,
    }
)
