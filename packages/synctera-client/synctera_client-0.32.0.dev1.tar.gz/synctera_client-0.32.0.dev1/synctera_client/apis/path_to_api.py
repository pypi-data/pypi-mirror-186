import typing_extensions

from synctera_client.paths import PathValues
from synctera_client.apis.paths.accounts import Accounts
from synctera_client.apis.paths.accounts_account_id import AccountsAccountId
from synctera_client.apis.paths.accounts_account_id_relationships import AccountsAccountIdRelationships
from synctera_client.apis.paths.accounts_account_id_relationships_relationship_id import AccountsAccountIdRelationshipsRelationshipId
from synctera_client.apis.paths.accounts_products import AccountsProducts
from synctera_client.apis.paths.accounts_products_product_id import AccountsProductsProductId
from synctera_client.apis.paths.accounts_templates import AccountsTemplates
from synctera_client.apis.paths.accounts_templates_template_id import AccountsTemplatesTemplateId
from synctera_client.apis.paths.ach import Ach
from synctera_client.apis.paths.ach_transaction_id import AchTransactionId
from synctera_client.apis.paths.ach_transaction_simulations_receiving_return import AchTransactionSimulationsReceivingReturn
from synctera_client.apis.paths.ach_transaction_simulations_receiving_transaction import AchTransactionSimulationsReceivingTransaction
from synctera_client.apis.paths.businesses import Businesses
from synctera_client.apis.paths.businesses_business_id import BusinessesBusinessId
from synctera_client.apis.paths.cards import Cards
from synctera_client.apis.paths.cards_card_id import CardsCardId
from synctera_client.apis.paths.cards_card_id_barcodes import CardsCardIdBarcodes
from synctera_client.apis.paths.cards_card_id_changes import CardsCardIdChanges
from synctera_client.apis.paths.cards_card_id_client_token import CardsCardIdClientToken
from synctera_client.apis.paths.cards_card_id_digital_wallet_tokens_applepay import CardsCardIdDigitalWalletTokensApplepay
from synctera_client.apis.paths.cards_card_id_digital_wallet_tokens_googlepay import CardsCardIdDigitalWalletTokensGooglepay
from synctera_client.apis.paths.cards_card_id_webhook_simulations_fulfillment import CardsCardIdWebhookSimulationsFulfillment
from synctera_client.apis.paths.cards_activate import CardsActivate
from synctera_client.apis.paths.cards_card_widget_url import CardsCardWidgetUrl
from synctera_client.apis.paths.cards_digital_wallet_tokens import CardsDigitalWalletTokens
from synctera_client.apis.paths.cards_digital_wallet_tokens_digital_wallet_token_id import CardsDigitalWalletTokensDigitalWalletTokenId
from synctera_client.apis.paths.cards_gateways import CardsGateways
from synctera_client.apis.paths.cards_gateways_gateway_id import CardsGatewaysGatewayId
from synctera_client.apis.paths.cards_images import CardsImages
from synctera_client.apis.paths.cards_images_card_image_id import CardsImagesCardImageId
from synctera_client.apis.paths.cards_images_card_image_id_data import CardsImagesCardImageIdData
from synctera_client.apis.paths.cards_products import CardsProducts
from synctera_client.apis.paths.cards_single_use_token import CardsSingleUseToken
from synctera_client.apis.paths.cards_transaction_simulations_authorization import CardsTransactionSimulationsAuthorization
from synctera_client.apis.paths.cards_transaction_simulations_authorization_advice import CardsTransactionSimulationsAuthorizationAdvice
from synctera_client.apis.paths.cards_transaction_simulations_clearing import CardsTransactionSimulationsClearing
from synctera_client.apis.paths.cards_transaction_simulations_financial import CardsTransactionSimulationsFinancial
from synctera_client.apis.paths.cards_transaction_simulations_financial_advice import CardsTransactionSimulationsFinancialAdvice
from synctera_client.apis.paths.cards_transaction_simulations_financial_balance_inquiry import CardsTransactionSimulationsFinancialBalanceInquiry
from synctera_client.apis.paths.cards_transaction_simulations_financial_original_credit import CardsTransactionSimulationsFinancialOriginalCredit
from synctera_client.apis.paths.cards_transaction_simulations_financial_withdrawal import CardsTransactionSimulationsFinancialWithdrawal
from synctera_client.apis.paths.cards_transaction_simulations_reversal import CardsTransactionSimulationsReversal
from synctera_client.apis.paths.cash_pickups import CashPickups
from synctera_client.apis.paths.cash_pickups_cash_pickup_id import CashPickupsCashPickupId
from synctera_client.apis.paths.customers import Customers
from synctera_client.apis.paths.customers_customer_id import CustomersCustomerId
from synctera_client.apis.paths.customers_customer_id_disclosures import CustomersCustomerIdDisclosures
from synctera_client.apis.paths.customers_customer_id_employment import CustomersCustomerIdEmployment
from synctera_client.apis.paths.customers_customer_id_employment_employment_id import CustomersCustomerIdEmploymentEmploymentId
from synctera_client.apis.paths.customers_customer_id_prefill import CustomersCustomerIdPrefill
from synctera_client.apis.paths.customers_customer_id_risk_ratings import CustomersCustomerIdRiskRatings
from synctera_client.apis.paths.customers_customer_id_risk_ratings_risk_rating_id import CustomersCustomerIdRiskRatingsRiskRatingId
from synctera_client.apis.paths.customers_customer_id_verifications import CustomersCustomerIdVerifications
from synctera_client.apis.paths.customers_customer_id_verifications_verification_id import CustomersCustomerIdVerificationsVerificationId
from synctera_client.apis.paths.customers_customer_id_verify import CustomersCustomerIdVerify
from synctera_client.apis.paths.customers_customer_id_watchlists_alerts import CustomersCustomerIdWatchlistsAlerts
from synctera_client.apis.paths.customers_customer_id_watchlists_alerts_alert_id import CustomersCustomerIdWatchlistsAlertsAlertId
from synctera_client.apis.paths.customers_customer_id_watchlists_subscriptions import CustomersCustomerIdWatchlistsSubscriptions
from synctera_client.apis.paths.customers_customer_id_watchlists_subscriptions_subscription_id import CustomersCustomerIdWatchlistsSubscriptionsSubscriptionId
from synctera_client.apis.paths.customers_customer_id_watchlists_suppressions import CustomersCustomerIdWatchlistsSuppressions
from synctera_client.apis.paths.disclosures import Disclosures
from synctera_client.apis.paths.disclosures_disclosure_id import DisclosuresDisclosureId
from synctera_client.apis.paths.documents import Documents
from synctera_client.apis.paths.documents_document_id import DocumentsDocumentId
from synctera_client.apis.paths.documents_document_id_contents import DocumentsDocumentIdContents
from synctera_client.apis.paths.documents_document_id_versions import DocumentsDocumentIdVersions
from synctera_client.apis.paths.documents_document_id_versions_document_version import DocumentsDocumentIdVersionsDocumentVersion
from synctera_client.apis.paths.documents_document_id_versions_document_version_contents import DocumentsDocumentIdVersionsDocumentVersionContents
from synctera_client.apis.paths.external_accounts import ExternalAccounts
from synctera_client.apis.paths.external_accounts_external_account_id import ExternalAccountsExternalAccountId
from synctera_client.apis.paths.external_accounts_external_account_id_balance import ExternalAccountsExternalAccountIdBalance
from synctera_client.apis.paths.external_accounts_external_account_id_transactions import ExternalAccountsExternalAccountIdTransactions
from synctera_client.apis.paths.external_accounts_access_tokens import ExternalAccountsAccessTokens
from synctera_client.apis.paths.external_accounts_add_vendor_accounts import ExternalAccountsAddVendorAccounts
from synctera_client.apis.paths.external_accounts_link_tokens import ExternalAccountsLinkTokens
from synctera_client.apis.paths.external_accounts_sync_vendor_accounts import ExternalAccountsSyncVendorAccounts
from synctera_client.apis.paths.external_cards import ExternalCards
from synctera_client.apis.paths.external_cards_external_card_id import ExternalCardsExternalCardId
from synctera_client.apis.paths.external_cards_tokens import ExternalCardsTokens
from synctera_client.apis.paths.external_cards_transfers import ExternalCardsTransfers
from synctera_client.apis.paths.external_cards_transfers_transfer_id import ExternalCardsTransfersTransferId
from synctera_client.apis.paths.external_cards_transfers_transfer_id_reversals import ExternalCardsTransfersTransferIdReversals
from synctera_client.apis.paths.internal_accounts import InternalAccounts
from synctera_client.apis.paths.internal_accounts_internal_account_id import InternalAccountsInternalAccountId
from synctera_client.apis.paths.monitoring_alerts import MonitoringAlerts
from synctera_client.apis.paths.monitoring_alerts_alert_id import MonitoringAlertsAlertId
from synctera_client.apis.paths.monitoring_subscriptions import MonitoringSubscriptions
from synctera_client.apis.paths.monitoring_subscriptions_subscription_id import MonitoringSubscriptionsSubscriptionId
from synctera_client.apis.paths.payment_schedules import PaymentSchedules
from synctera_client.apis.paths.payment_schedules_payment_schedule_id import PaymentSchedulesPaymentScheduleId
from synctera_client.apis.paths.payment_schedules_payments import PaymentSchedulesPayments
from synctera_client.apis.paths.persons import Persons
from synctera_client.apis.paths.persons_person_id import PersonsPersonId
from synctera_client.apis.paths.persons_person_id_prefill import PersonsPersonIdPrefill
from synctera_client.apis.paths.rdc_deposits import RdcDeposits
from synctera_client.apis.paths.rdc_deposits_deposit_id import RdcDepositsDepositId
from synctera_client.apis.paths.reconciliations import Reconciliations
from synctera_client.apis.paths.reconciliations_reconciliation_id import ReconciliationsReconciliationId
from synctera_client.apis.paths.relationships import Relationships
from synctera_client.apis.paths.relationships_relationship_id import RelationshipsRelationshipId
from synctera_client.apis.paths.spend_controls import SpendControls
from synctera_client.apis.paths.spend_controls_spend_control_id import SpendControlsSpendControlId
from synctera_client.apis.paths.statements import Statements
from synctera_client.apis.paths.statements_statement_id import StatementsStatementId
from synctera_client.apis.paths.transactions_internal_transfer import TransactionsInternalTransfer
from synctera_client.apis.paths.transactions_internal_transfer_id import TransactionsInternalTransferId
from synctera_client.apis.paths.transactions_pending import TransactionsPending
from synctera_client.apis.paths.transactions_pending_id import TransactionsPendingId
from synctera_client.apis.paths.transactions_posted import TransactionsPosted
from synctera_client.apis.paths.transactions_posted_id import TransactionsPostedId
from synctera_client.apis.paths.verifications import Verifications
from synctera_client.apis.paths.verifications_verification_id import VerificationsVerificationId
from synctera_client.apis.paths.verifications_adhoc import VerificationsAdhoc
from synctera_client.apis.paths.verifications_verify import VerificationsVerify
from synctera_client.apis.paths.webhooks import Webhooks
from synctera_client.apis.paths.webhooks_webhook_id import WebhooksWebhookId
from synctera_client.apis.paths.webhooks_webhook_id_events import WebhooksWebhookIdEvents
from synctera_client.apis.paths.webhooks_webhook_id_events_event_id import WebhooksWebhookIdEventsEventId
from synctera_client.apis.paths.webhooks_webhook_id_events_event_id_resend import WebhooksWebhookIdEventsEventIdResend
from synctera_client.apis.paths.webhooks_trigger import WebhooksTrigger
from synctera_client.apis.paths.wipe import Wipe
from synctera_client.apis.paths.wires import Wires
from synctera_client.apis.paths.wires_wire_id import WiresWireId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNTS: Accounts,
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_RELATIONSHIPS: AccountsAccountIdRelationships,
        PathValues.ACCOUNTS_ACCOUNT_ID_RELATIONSHIPS_RELATIONSHIP_ID: AccountsAccountIdRelationshipsRelationshipId,
        PathValues.ACCOUNTS_PRODUCTS: AccountsProducts,
        PathValues.ACCOUNTS_PRODUCTS_PRODUCT_ID: AccountsProductsProductId,
        PathValues.ACCOUNTS_TEMPLATES: AccountsTemplates,
        PathValues.ACCOUNTS_TEMPLATES_TEMPLATE_ID: AccountsTemplatesTemplateId,
        PathValues.ACH: Ach,
        PathValues.ACH_TRANSACTION_ID: AchTransactionId,
        PathValues.ACH_TRANSACTION_SIMULATIONS_RECEIVING_RETURN: AchTransactionSimulationsReceivingReturn,
        PathValues.ACH_TRANSACTION_SIMULATIONS_RECEIVING_TRANSACTION: AchTransactionSimulationsReceivingTransaction,
        PathValues.BUSINESSES: Businesses,
        PathValues.BUSINESSES_BUSINESS_ID: BusinessesBusinessId,
        PathValues.CARDS: Cards,
        PathValues.CARDS_CARD_ID: CardsCardId,
        PathValues.CARDS_CARD_ID_BARCODES: CardsCardIdBarcodes,
        PathValues.CARDS_CARD_ID_CHANGES: CardsCardIdChanges,
        PathValues.CARDS_CARD_ID_CLIENT_TOKEN: CardsCardIdClientToken,
        PathValues.CARDS_CARD_ID_DIGITAL_WALLET_TOKENS_APPLEPAY: CardsCardIdDigitalWalletTokensApplepay,
        PathValues.CARDS_CARD_ID_DIGITAL_WALLET_TOKENS_GOOGLEPAY: CardsCardIdDigitalWalletTokensGooglepay,
        PathValues.CARDS_CARD_ID_WEBHOOK_SIMULATIONS_FULFILLMENT: CardsCardIdWebhookSimulationsFulfillment,
        PathValues.CARDS_ACTIVATE: CardsActivate,
        PathValues.CARDS_CARD_WIDGET_URL: CardsCardWidgetUrl,
        PathValues.CARDS_DIGITAL_WALLET_TOKENS: CardsDigitalWalletTokens,
        PathValues.CARDS_DIGITAL_WALLET_TOKENS_DIGITAL_WALLET_TOKEN_ID: CardsDigitalWalletTokensDigitalWalletTokenId,
        PathValues.CARDS_GATEWAYS: CardsGateways,
        PathValues.CARDS_GATEWAYS_GATEWAY_ID: CardsGatewaysGatewayId,
        PathValues.CARDS_IMAGES: CardsImages,
        PathValues.CARDS_IMAGES_CARD_IMAGE_ID: CardsImagesCardImageId,
        PathValues.CARDS_IMAGES_CARD_IMAGE_ID_DATA: CardsImagesCardImageIdData,
        PathValues.CARDS_PRODUCTS: CardsProducts,
        PathValues.CARDS_SINGLE_USE_TOKEN: CardsSingleUseToken,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_AUTHORIZATION: CardsTransactionSimulationsAuthorization,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_AUTHORIZATION_ADVICE: CardsTransactionSimulationsAuthorizationAdvice,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_CLEARING: CardsTransactionSimulationsClearing,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL: CardsTransactionSimulationsFinancial,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL_ADVICE: CardsTransactionSimulationsFinancialAdvice,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL_BALANCE_INQUIRY: CardsTransactionSimulationsFinancialBalanceInquiry,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL_ORIGINAL_CREDIT: CardsTransactionSimulationsFinancialOriginalCredit,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL_WITHDRAWAL: CardsTransactionSimulationsFinancialWithdrawal,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_REVERSAL: CardsTransactionSimulationsReversal,
        PathValues.CASH_PICKUPS: CashPickups,
        PathValues.CASH_PICKUPS_CASH_PICKUP_ID: CashPickupsCashPickupId,
        PathValues.CUSTOMERS: Customers,
        PathValues.CUSTOMERS_CUSTOMER_ID: CustomersCustomerId,
        PathValues.CUSTOMERS_CUSTOMER_ID_DISCLOSURES: CustomersCustomerIdDisclosures,
        PathValues.CUSTOMERS_CUSTOMER_ID_EMPLOYMENT: CustomersCustomerIdEmployment,
        PathValues.CUSTOMERS_CUSTOMER_ID_EMPLOYMENT_EMPLOYMENT_ID: CustomersCustomerIdEmploymentEmploymentId,
        PathValues.CUSTOMERS_CUSTOMER_ID_PREFILL: CustomersCustomerIdPrefill,
        PathValues.CUSTOMERS_CUSTOMER_ID_RISK_RATINGS: CustomersCustomerIdRiskRatings,
        PathValues.CUSTOMERS_CUSTOMER_ID_RISK_RATINGS_RISK_RATING_ID: CustomersCustomerIdRiskRatingsRiskRatingId,
        PathValues.CUSTOMERS_CUSTOMER_ID_VERIFICATIONS: CustomersCustomerIdVerifications,
        PathValues.CUSTOMERS_CUSTOMER_ID_VERIFICATIONS_VERIFICATION_ID: CustomersCustomerIdVerificationsVerificationId,
        PathValues.CUSTOMERS_CUSTOMER_ID_VERIFY: CustomersCustomerIdVerify,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_ALERTS: CustomersCustomerIdWatchlistsAlerts,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_ALERTS_ALERT_ID: CustomersCustomerIdWatchlistsAlertsAlertId,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_SUBSCRIPTIONS: CustomersCustomerIdWatchlistsSubscriptions,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_SUBSCRIPTIONS_SUBSCRIPTION_ID: CustomersCustomerIdWatchlistsSubscriptionsSubscriptionId,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_SUPPRESSIONS: CustomersCustomerIdWatchlistsSuppressions,
        PathValues.DISCLOSURES: Disclosures,
        PathValues.DISCLOSURES_DISCLOSURE_ID: DisclosuresDisclosureId,
        PathValues.DOCUMENTS: Documents,
        PathValues.DOCUMENTS_DOCUMENT_ID: DocumentsDocumentId,
        PathValues.DOCUMENTS_DOCUMENT_ID_CONTENTS: DocumentsDocumentIdContents,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS: DocumentsDocumentIdVersions,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS_DOCUMENT_VERSION: DocumentsDocumentIdVersionsDocumentVersion,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS_DOCUMENT_VERSION_CONTENTS: DocumentsDocumentIdVersionsDocumentVersionContents,
        PathValues.EXTERNAL_ACCOUNTS: ExternalAccounts,
        PathValues.EXTERNAL_ACCOUNTS_EXTERNAL_ACCOUNT_ID: ExternalAccountsExternalAccountId,
        PathValues.EXTERNAL_ACCOUNTS_EXTERNAL_ACCOUNT_ID_BALANCE: ExternalAccountsExternalAccountIdBalance,
        PathValues.EXTERNAL_ACCOUNTS_EXTERNAL_ACCOUNT_ID_TRANSACTIONS: ExternalAccountsExternalAccountIdTransactions,
        PathValues.EXTERNAL_ACCOUNTS_ACCESS_TOKENS: ExternalAccountsAccessTokens,
        PathValues.EXTERNAL_ACCOUNTS_ADD_VENDOR_ACCOUNTS: ExternalAccountsAddVendorAccounts,
        PathValues.EXTERNAL_ACCOUNTS_LINK_TOKENS: ExternalAccountsLinkTokens,
        PathValues.EXTERNAL_ACCOUNTS_SYNC_VENDOR_ACCOUNTS: ExternalAccountsSyncVendorAccounts,
        PathValues.EXTERNAL_CARDS: ExternalCards,
        PathValues.EXTERNAL_CARDS_EXTERNAL_CARD_ID: ExternalCardsExternalCardId,
        PathValues.EXTERNAL_CARDS_TOKENS: ExternalCardsTokens,
        PathValues.EXTERNAL_CARDS_TRANSFERS: ExternalCardsTransfers,
        PathValues.EXTERNAL_CARDS_TRANSFERS_TRANSFER_ID: ExternalCardsTransfersTransferId,
        PathValues.EXTERNAL_CARDS_TRANSFERS_TRANSFER_ID_REVERSALS: ExternalCardsTransfersTransferIdReversals,
        PathValues.INTERNAL_ACCOUNTS: InternalAccounts,
        PathValues.INTERNAL_ACCOUNTS_INTERNAL_ACCOUNT_ID: InternalAccountsInternalAccountId,
        PathValues.MONITORING_ALERTS: MonitoringAlerts,
        PathValues.MONITORING_ALERTS_ALERT_ID: MonitoringAlertsAlertId,
        PathValues.MONITORING_SUBSCRIPTIONS: MonitoringSubscriptions,
        PathValues.MONITORING_SUBSCRIPTIONS_SUBSCRIPTION_ID: MonitoringSubscriptionsSubscriptionId,
        PathValues.PAYMENT_SCHEDULES: PaymentSchedules,
        PathValues.PAYMENT_SCHEDULES_PAYMENT_SCHEDULE_ID: PaymentSchedulesPaymentScheduleId,
        PathValues.PAYMENT_SCHEDULES_PAYMENTS: PaymentSchedulesPayments,
        PathValues.PERSONS: Persons,
        PathValues.PERSONS_PERSON_ID: PersonsPersonId,
        PathValues.PERSONS_PERSON_ID_PREFILL: PersonsPersonIdPrefill,
        PathValues.RDC_DEPOSITS: RdcDeposits,
        PathValues.RDC_DEPOSITS_DEPOSIT_ID: RdcDepositsDepositId,
        PathValues.RECONCILIATIONS: Reconciliations,
        PathValues.RECONCILIATIONS_RECONCILIATION_ID: ReconciliationsReconciliationId,
        PathValues.RELATIONSHIPS: Relationships,
        PathValues.RELATIONSHIPS_RELATIONSHIP_ID: RelationshipsRelationshipId,
        PathValues.SPEND_CONTROLS: SpendControls,
        PathValues.SPEND_CONTROLS_SPEND_CONTROL_ID: SpendControlsSpendControlId,
        PathValues.STATEMENTS: Statements,
        PathValues.STATEMENTS_STATEMENT_ID: StatementsStatementId,
        PathValues.TRANSACTIONS_INTERNAL_TRANSFER: TransactionsInternalTransfer,
        PathValues.TRANSACTIONS_INTERNAL_TRANSFER_ID: TransactionsInternalTransferId,
        PathValues.TRANSACTIONS_PENDING: TransactionsPending,
        PathValues.TRANSACTIONS_PENDING_ID: TransactionsPendingId,
        PathValues.TRANSACTIONS_POSTED: TransactionsPosted,
        PathValues.TRANSACTIONS_POSTED_ID: TransactionsPostedId,
        PathValues.VERIFICATIONS: Verifications,
        PathValues.VERIFICATIONS_VERIFICATION_ID: VerificationsVerificationId,
        PathValues.VERIFICATIONS_ADHOC: VerificationsAdhoc,
        PathValues.VERIFICATIONS_VERIFY: VerificationsVerify,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
        PathValues.WEBHOOKS_WEBHOOK_ID_EVENTS: WebhooksWebhookIdEvents,
        PathValues.WEBHOOKS_WEBHOOK_ID_EVENTS_EVENT_ID: WebhooksWebhookIdEventsEventId,
        PathValues.WEBHOOKS_WEBHOOK_ID_EVENTS_EVENT_ID_RESEND: WebhooksWebhookIdEventsEventIdResend,
        PathValues.WEBHOOKS_TRIGGER: WebhooksTrigger,
        PathValues.WIPE: Wipe,
        PathValues.WIRES: Wires,
        PathValues.WIRES_WIRE_ID: WiresWireId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNTS: Accounts,
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_RELATIONSHIPS: AccountsAccountIdRelationships,
        PathValues.ACCOUNTS_ACCOUNT_ID_RELATIONSHIPS_RELATIONSHIP_ID: AccountsAccountIdRelationshipsRelationshipId,
        PathValues.ACCOUNTS_PRODUCTS: AccountsProducts,
        PathValues.ACCOUNTS_PRODUCTS_PRODUCT_ID: AccountsProductsProductId,
        PathValues.ACCOUNTS_TEMPLATES: AccountsTemplates,
        PathValues.ACCOUNTS_TEMPLATES_TEMPLATE_ID: AccountsTemplatesTemplateId,
        PathValues.ACH: Ach,
        PathValues.ACH_TRANSACTION_ID: AchTransactionId,
        PathValues.ACH_TRANSACTION_SIMULATIONS_RECEIVING_RETURN: AchTransactionSimulationsReceivingReturn,
        PathValues.ACH_TRANSACTION_SIMULATIONS_RECEIVING_TRANSACTION: AchTransactionSimulationsReceivingTransaction,
        PathValues.BUSINESSES: Businesses,
        PathValues.BUSINESSES_BUSINESS_ID: BusinessesBusinessId,
        PathValues.CARDS: Cards,
        PathValues.CARDS_CARD_ID: CardsCardId,
        PathValues.CARDS_CARD_ID_BARCODES: CardsCardIdBarcodes,
        PathValues.CARDS_CARD_ID_CHANGES: CardsCardIdChanges,
        PathValues.CARDS_CARD_ID_CLIENT_TOKEN: CardsCardIdClientToken,
        PathValues.CARDS_CARD_ID_DIGITAL_WALLET_TOKENS_APPLEPAY: CardsCardIdDigitalWalletTokensApplepay,
        PathValues.CARDS_CARD_ID_DIGITAL_WALLET_TOKENS_GOOGLEPAY: CardsCardIdDigitalWalletTokensGooglepay,
        PathValues.CARDS_CARD_ID_WEBHOOK_SIMULATIONS_FULFILLMENT: CardsCardIdWebhookSimulationsFulfillment,
        PathValues.CARDS_ACTIVATE: CardsActivate,
        PathValues.CARDS_CARD_WIDGET_URL: CardsCardWidgetUrl,
        PathValues.CARDS_DIGITAL_WALLET_TOKENS: CardsDigitalWalletTokens,
        PathValues.CARDS_DIGITAL_WALLET_TOKENS_DIGITAL_WALLET_TOKEN_ID: CardsDigitalWalletTokensDigitalWalletTokenId,
        PathValues.CARDS_GATEWAYS: CardsGateways,
        PathValues.CARDS_GATEWAYS_GATEWAY_ID: CardsGatewaysGatewayId,
        PathValues.CARDS_IMAGES: CardsImages,
        PathValues.CARDS_IMAGES_CARD_IMAGE_ID: CardsImagesCardImageId,
        PathValues.CARDS_IMAGES_CARD_IMAGE_ID_DATA: CardsImagesCardImageIdData,
        PathValues.CARDS_PRODUCTS: CardsProducts,
        PathValues.CARDS_SINGLE_USE_TOKEN: CardsSingleUseToken,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_AUTHORIZATION: CardsTransactionSimulationsAuthorization,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_AUTHORIZATION_ADVICE: CardsTransactionSimulationsAuthorizationAdvice,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_CLEARING: CardsTransactionSimulationsClearing,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL: CardsTransactionSimulationsFinancial,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL_ADVICE: CardsTransactionSimulationsFinancialAdvice,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL_BALANCE_INQUIRY: CardsTransactionSimulationsFinancialBalanceInquiry,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL_ORIGINAL_CREDIT: CardsTransactionSimulationsFinancialOriginalCredit,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_FINANCIAL_WITHDRAWAL: CardsTransactionSimulationsFinancialWithdrawal,
        PathValues.CARDS_TRANSACTION_SIMULATIONS_REVERSAL: CardsTransactionSimulationsReversal,
        PathValues.CASH_PICKUPS: CashPickups,
        PathValues.CASH_PICKUPS_CASH_PICKUP_ID: CashPickupsCashPickupId,
        PathValues.CUSTOMERS: Customers,
        PathValues.CUSTOMERS_CUSTOMER_ID: CustomersCustomerId,
        PathValues.CUSTOMERS_CUSTOMER_ID_DISCLOSURES: CustomersCustomerIdDisclosures,
        PathValues.CUSTOMERS_CUSTOMER_ID_EMPLOYMENT: CustomersCustomerIdEmployment,
        PathValues.CUSTOMERS_CUSTOMER_ID_EMPLOYMENT_EMPLOYMENT_ID: CustomersCustomerIdEmploymentEmploymentId,
        PathValues.CUSTOMERS_CUSTOMER_ID_PREFILL: CustomersCustomerIdPrefill,
        PathValues.CUSTOMERS_CUSTOMER_ID_RISK_RATINGS: CustomersCustomerIdRiskRatings,
        PathValues.CUSTOMERS_CUSTOMER_ID_RISK_RATINGS_RISK_RATING_ID: CustomersCustomerIdRiskRatingsRiskRatingId,
        PathValues.CUSTOMERS_CUSTOMER_ID_VERIFICATIONS: CustomersCustomerIdVerifications,
        PathValues.CUSTOMERS_CUSTOMER_ID_VERIFICATIONS_VERIFICATION_ID: CustomersCustomerIdVerificationsVerificationId,
        PathValues.CUSTOMERS_CUSTOMER_ID_VERIFY: CustomersCustomerIdVerify,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_ALERTS: CustomersCustomerIdWatchlistsAlerts,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_ALERTS_ALERT_ID: CustomersCustomerIdWatchlistsAlertsAlertId,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_SUBSCRIPTIONS: CustomersCustomerIdWatchlistsSubscriptions,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_SUBSCRIPTIONS_SUBSCRIPTION_ID: CustomersCustomerIdWatchlistsSubscriptionsSubscriptionId,
        PathValues.CUSTOMERS_CUSTOMER_ID_WATCHLISTS_SUPPRESSIONS: CustomersCustomerIdWatchlistsSuppressions,
        PathValues.DISCLOSURES: Disclosures,
        PathValues.DISCLOSURES_DISCLOSURE_ID: DisclosuresDisclosureId,
        PathValues.DOCUMENTS: Documents,
        PathValues.DOCUMENTS_DOCUMENT_ID: DocumentsDocumentId,
        PathValues.DOCUMENTS_DOCUMENT_ID_CONTENTS: DocumentsDocumentIdContents,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS: DocumentsDocumentIdVersions,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS_DOCUMENT_VERSION: DocumentsDocumentIdVersionsDocumentVersion,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS_DOCUMENT_VERSION_CONTENTS: DocumentsDocumentIdVersionsDocumentVersionContents,
        PathValues.EXTERNAL_ACCOUNTS: ExternalAccounts,
        PathValues.EXTERNAL_ACCOUNTS_EXTERNAL_ACCOUNT_ID: ExternalAccountsExternalAccountId,
        PathValues.EXTERNAL_ACCOUNTS_EXTERNAL_ACCOUNT_ID_BALANCE: ExternalAccountsExternalAccountIdBalance,
        PathValues.EXTERNAL_ACCOUNTS_EXTERNAL_ACCOUNT_ID_TRANSACTIONS: ExternalAccountsExternalAccountIdTransactions,
        PathValues.EXTERNAL_ACCOUNTS_ACCESS_TOKENS: ExternalAccountsAccessTokens,
        PathValues.EXTERNAL_ACCOUNTS_ADD_VENDOR_ACCOUNTS: ExternalAccountsAddVendorAccounts,
        PathValues.EXTERNAL_ACCOUNTS_LINK_TOKENS: ExternalAccountsLinkTokens,
        PathValues.EXTERNAL_ACCOUNTS_SYNC_VENDOR_ACCOUNTS: ExternalAccountsSyncVendorAccounts,
        PathValues.EXTERNAL_CARDS: ExternalCards,
        PathValues.EXTERNAL_CARDS_EXTERNAL_CARD_ID: ExternalCardsExternalCardId,
        PathValues.EXTERNAL_CARDS_TOKENS: ExternalCardsTokens,
        PathValues.EXTERNAL_CARDS_TRANSFERS: ExternalCardsTransfers,
        PathValues.EXTERNAL_CARDS_TRANSFERS_TRANSFER_ID: ExternalCardsTransfersTransferId,
        PathValues.EXTERNAL_CARDS_TRANSFERS_TRANSFER_ID_REVERSALS: ExternalCardsTransfersTransferIdReversals,
        PathValues.INTERNAL_ACCOUNTS: InternalAccounts,
        PathValues.INTERNAL_ACCOUNTS_INTERNAL_ACCOUNT_ID: InternalAccountsInternalAccountId,
        PathValues.MONITORING_ALERTS: MonitoringAlerts,
        PathValues.MONITORING_ALERTS_ALERT_ID: MonitoringAlertsAlertId,
        PathValues.MONITORING_SUBSCRIPTIONS: MonitoringSubscriptions,
        PathValues.MONITORING_SUBSCRIPTIONS_SUBSCRIPTION_ID: MonitoringSubscriptionsSubscriptionId,
        PathValues.PAYMENT_SCHEDULES: PaymentSchedules,
        PathValues.PAYMENT_SCHEDULES_PAYMENT_SCHEDULE_ID: PaymentSchedulesPaymentScheduleId,
        PathValues.PAYMENT_SCHEDULES_PAYMENTS: PaymentSchedulesPayments,
        PathValues.PERSONS: Persons,
        PathValues.PERSONS_PERSON_ID: PersonsPersonId,
        PathValues.PERSONS_PERSON_ID_PREFILL: PersonsPersonIdPrefill,
        PathValues.RDC_DEPOSITS: RdcDeposits,
        PathValues.RDC_DEPOSITS_DEPOSIT_ID: RdcDepositsDepositId,
        PathValues.RECONCILIATIONS: Reconciliations,
        PathValues.RECONCILIATIONS_RECONCILIATION_ID: ReconciliationsReconciliationId,
        PathValues.RELATIONSHIPS: Relationships,
        PathValues.RELATIONSHIPS_RELATIONSHIP_ID: RelationshipsRelationshipId,
        PathValues.SPEND_CONTROLS: SpendControls,
        PathValues.SPEND_CONTROLS_SPEND_CONTROL_ID: SpendControlsSpendControlId,
        PathValues.STATEMENTS: Statements,
        PathValues.STATEMENTS_STATEMENT_ID: StatementsStatementId,
        PathValues.TRANSACTIONS_INTERNAL_TRANSFER: TransactionsInternalTransfer,
        PathValues.TRANSACTIONS_INTERNAL_TRANSFER_ID: TransactionsInternalTransferId,
        PathValues.TRANSACTIONS_PENDING: TransactionsPending,
        PathValues.TRANSACTIONS_PENDING_ID: TransactionsPendingId,
        PathValues.TRANSACTIONS_POSTED: TransactionsPosted,
        PathValues.TRANSACTIONS_POSTED_ID: TransactionsPostedId,
        PathValues.VERIFICATIONS: Verifications,
        PathValues.VERIFICATIONS_VERIFICATION_ID: VerificationsVerificationId,
        PathValues.VERIFICATIONS_ADHOC: VerificationsAdhoc,
        PathValues.VERIFICATIONS_VERIFY: VerificationsVerify,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
        PathValues.WEBHOOKS_WEBHOOK_ID_EVENTS: WebhooksWebhookIdEvents,
        PathValues.WEBHOOKS_WEBHOOK_ID_EVENTS_EVENT_ID: WebhooksWebhookIdEventsEventId,
        PathValues.WEBHOOKS_WEBHOOK_ID_EVENTS_EVENT_ID_RESEND: WebhooksWebhookIdEventsEventIdResend,
        PathValues.WEBHOOKS_TRIGGER: WebhooksTrigger,
        PathValues.WIPE: Wipe,
        PathValues.WIRES: Wires,
        PathValues.WIRES_WIRE_ID: WiresWireId,
    }
)
