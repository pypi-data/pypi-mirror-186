from alas_tools3.common.clients.client_base import EntityClientBase


class ShipperOrderClient(EntityClientBase):
    entity_endpoint_base_url = 'integration/shipper/shipperorder/'


class WebhookClient(EntityClientBase):
    entity_endpoint_base_url = 'integration/shipper/webhooks/'