import typing_extensions

from synctera_client.apis.tags import TagValues
from synctera_client.apis.tags.account_products_api import AccountProductsApi
from synctera_client.apis.tags.accounts_api import AccountsApi
from synctera_client.apis.tags.account_templates_api import AccountTemplatesApi
from synctera_client.apis.tags.ach_api import ACHApi
from synctera_client.apis.tags.ach_transaction_simulations_api import ACHTransactionSimulationsApi
from synctera_client.apis.tags.ban_rules_api import BanRulesApi
from synctera_client.apis.tags.businesses_api import BusinessesApi
from synctera_client.apis.tags.cards_api import CardsApi
from synctera_client.apis.tags.external_cards_alpha_api import ExternalCardsAlphaApi
from synctera_client.apis.tags.cash_pickups_alpha_api import CashPickupsAlphaApi
from synctera_client.apis.tags.customers_api import CustomersApi
from synctera_client.apis.tags.disclosures_api import DisclosuresApi
from synctera_client.apis.tags.disclosures_deprecated_api import DisclosuresDeprecatedApi
from synctera_client.apis.tags.documents_api import DocumentsApi
from synctera_client.apis.tags.external_accounts_api import ExternalAccountsApi
from synctera_client.apis.tags.internal_accounts_api import InternalAccountsApi
from synctera_client.apis.tags.kyc_verification_deprecated_api import KYCVerificationDeprecatedApi
from synctera_client.apis.tags.monitoring_api import MonitoringApi
from synctera_client.apis.tags.notes_api import NotesApi
from synctera_client.apis.tags.cronut_api import CronutApi
from synctera_client.apis.tags.persons_api import PersonsApi
from synctera_client.apis.tags.remote_check_deposit_api import RemoteCheckDepositApi
from synctera_client.apis.tags.reconciliations_api import ReconciliationsApi
from synctera_client.apis.tags.relationships_api import RelationshipsApi
from synctera_client.apis.tags.spend_controls_beta_api import SpendControlsBetaApi
from synctera_client.apis.tags.stately_api import StatelyApi
from synctera_client.apis.tags.card_transaction_simulations_api import CardTransactionSimulationsApi
from synctera_client.apis.tags.transactions_api import TransactionsApi
from synctera_client.apis.tags.kyckyb_verifications_api import KYCKYBVerificationsApi
from synctera_client.apis.tags.waitlist_api import WaitlistApi
from synctera_client.apis.tags.watchlist_deprecated_api import WatchlistDeprecatedApi
from synctera_client.apis.tags.card_webhook_simulations_api import CardWebhookSimulationsApi
from synctera_client.apis.tags.webhooks_api import WebhooksApi
from synctera_client.apis.tags.wires_alpha_api import WiresAlphaApi
from synctera_client.apis.tags.digital_wallet_tokens_api import DigitalWalletTokensApi
from synctera_client.apis.tags.internal_transfer_api import InternalTransferApi
from synctera_client.apis.tags.payment_schedules_api import PaymentSchedulesApi
from synctera_client.apis.tags.remote_check_deposit_beta_api import RemoteCheckDepositBetaApi
from synctera_client.apis.tags.sandbox_wipe_alpha_api import SandboxWipeAlphaApi
from synctera_client.apis.tags.statements_api import StatementsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNT_PRODUCTS: AccountProductsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.ACCOUNT_TEMPLATES: AccountTemplatesApi,
        TagValues.ACH: ACHApi,
        TagValues.ACH_TRANSACTION_SIMULATIONS: ACHTransactionSimulationsApi,
        TagValues.BAN_RULES: BanRulesApi,
        TagValues.BUSINESSES: BusinessesApi,
        TagValues.CARDS: CardsApi,
        TagValues.EXTERNAL_CARDS_ALPHA: ExternalCardsAlphaApi,
        TagValues.CASH_PICKUPS_ALPHA: CashPickupsAlphaApi,
        TagValues.CUSTOMERS: CustomersApi,
        TagValues.DISCLOSURES: DisclosuresApi,
        TagValues.DISCLOSURES_DEPRECATED: DisclosuresDeprecatedApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.EXTERNAL_ACCOUNTS: ExternalAccountsApi,
        TagValues.INTERNAL_ACCOUNTS: InternalAccountsApi,
        TagValues.KYC_VERIFICATION_DEPRECATED: KYCVerificationDeprecatedApi,
        TagValues.MONITORING: MonitoringApi,
        TagValues.NOTES: NotesApi,
        TagValues.CRONUT: CronutApi,
        TagValues.PERSONS: PersonsApi,
        TagValues.REMOTE_CHECK_DEPOSIT: RemoteCheckDepositApi,
        TagValues.RECONCILIATIONS: ReconciliationsApi,
        TagValues.RELATIONSHIPS: RelationshipsApi,
        TagValues.SPEND_CONTROLS_BETA: SpendControlsBetaApi,
        TagValues.STATELY: StatelyApi,
        TagValues.CARD_TRANSACTION_SIMULATIONS: CardTransactionSimulationsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.KYC_KYB_VERIFICATIONS: KYCKYBVerificationsApi,
        TagValues.WAITLIST: WaitlistApi,
        TagValues.WATCHLIST_DEPRECATED: WatchlistDeprecatedApi,
        TagValues.CARD_WEBHOOK_SIMULATIONS: CardWebhookSimulationsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.WIRES_ALPHA: WiresAlphaApi,
        TagValues.DIGITAL_WALLET_TOKENS: DigitalWalletTokensApi,
        TagValues.INTERNAL_TRANSFER: InternalTransferApi,
        TagValues.PAYMENT_SCHEDULES: PaymentSchedulesApi,
        TagValues.REMOTE_CHECK_DEPOSIT_BETA: RemoteCheckDepositBetaApi,
        TagValues.SANDBOX_WIPE_ALPHA: SandboxWipeAlphaApi,
        TagValues.STATEMENTS: StatementsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNT_PRODUCTS: AccountProductsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.ACCOUNT_TEMPLATES: AccountTemplatesApi,
        TagValues.ACH: ACHApi,
        TagValues.ACH_TRANSACTION_SIMULATIONS: ACHTransactionSimulationsApi,
        TagValues.BAN_RULES: BanRulesApi,
        TagValues.BUSINESSES: BusinessesApi,
        TagValues.CARDS: CardsApi,
        TagValues.EXTERNAL_CARDS_ALPHA: ExternalCardsAlphaApi,
        TagValues.CASH_PICKUPS_ALPHA: CashPickupsAlphaApi,
        TagValues.CUSTOMERS: CustomersApi,
        TagValues.DISCLOSURES: DisclosuresApi,
        TagValues.DISCLOSURES_DEPRECATED: DisclosuresDeprecatedApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.EXTERNAL_ACCOUNTS: ExternalAccountsApi,
        TagValues.INTERNAL_ACCOUNTS: InternalAccountsApi,
        TagValues.KYC_VERIFICATION_DEPRECATED: KYCVerificationDeprecatedApi,
        TagValues.MONITORING: MonitoringApi,
        TagValues.NOTES: NotesApi,
        TagValues.CRONUT: CronutApi,
        TagValues.PERSONS: PersonsApi,
        TagValues.REMOTE_CHECK_DEPOSIT: RemoteCheckDepositApi,
        TagValues.RECONCILIATIONS: ReconciliationsApi,
        TagValues.RELATIONSHIPS: RelationshipsApi,
        TagValues.SPEND_CONTROLS_BETA: SpendControlsBetaApi,
        TagValues.STATELY: StatelyApi,
        TagValues.CARD_TRANSACTION_SIMULATIONS: CardTransactionSimulationsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.KYC_KYB_VERIFICATIONS: KYCKYBVerificationsApi,
        TagValues.WAITLIST: WaitlistApi,
        TagValues.WATCHLIST_DEPRECATED: WatchlistDeprecatedApi,
        TagValues.CARD_WEBHOOK_SIMULATIONS: CardWebhookSimulationsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.WIRES_ALPHA: WiresAlphaApi,
        TagValues.DIGITAL_WALLET_TOKENS: DigitalWalletTokensApi,
        TagValues.INTERNAL_TRANSFER: InternalTransferApi,
        TagValues.PAYMENT_SCHEDULES: PaymentSchedulesApi,
        TagValues.REMOTE_CHECK_DEPOSIT_BETA: RemoteCheckDepositBetaApi,
        TagValues.SANDBOX_WIPE_ALPHA: SandboxWipeAlphaApi,
        TagValues.STATEMENTS: StatementsApi,
    }
)
