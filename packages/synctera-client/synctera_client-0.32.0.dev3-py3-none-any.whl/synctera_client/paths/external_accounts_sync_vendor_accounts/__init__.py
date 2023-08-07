# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from synctera_client.paths.external_accounts_sync_vendor_accounts import Api

from synctera_client.paths import PathValues

path = PathValues.EXTERNAL_ACCOUNTS_SYNC_VENDOR_ACCOUNTS