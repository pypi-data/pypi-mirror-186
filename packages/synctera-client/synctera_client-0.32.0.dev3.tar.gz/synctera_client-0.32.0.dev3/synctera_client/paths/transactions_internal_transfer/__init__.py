# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from synctera_client.paths.transactions_internal_transfer import Api

from synctera_client.paths import PathValues

path = PathValues.TRANSACTIONS_INTERNAL_TRANSFER