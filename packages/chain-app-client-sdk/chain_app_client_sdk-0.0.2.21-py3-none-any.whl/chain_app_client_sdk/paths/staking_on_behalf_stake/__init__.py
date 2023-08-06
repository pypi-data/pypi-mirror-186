# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from chain_app_client_sdk.paths.staking_on_behalf_stake import Api

from chain_app_client_sdk.paths import PathValues

path = PathValues.STAKING_ON_BEHALF_STAKE