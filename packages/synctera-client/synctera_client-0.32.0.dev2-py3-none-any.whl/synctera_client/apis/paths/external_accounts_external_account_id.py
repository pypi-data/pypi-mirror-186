from synctera_client.paths.external_accounts_external_account_id.get import ApiForget
from synctera_client.paths.external_accounts_external_account_id.delete import ApiFordelete
from synctera_client.paths.external_accounts_external_account_id.patch import ApiForpatch


class ExternalAccountsExternalAccountId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
