# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from chain_app_client_sdk.paths.mass_claiming_get_claimable_bind import Api

from chain_app_client_sdk.paths import PathValues

path = PathValues.MASS_CLAIMING_GET_CLAIMABLE_BIND