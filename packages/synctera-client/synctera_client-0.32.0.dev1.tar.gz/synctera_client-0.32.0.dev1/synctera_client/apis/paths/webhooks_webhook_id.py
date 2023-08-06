from synctera_client.paths.webhooks_webhook_id.get import ApiForget
from synctera_client.paths.webhooks_webhook_id.put import ApiForput
from synctera_client.paths.webhooks_webhook_id.delete import ApiFordelete


class WebhooksWebhookId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
