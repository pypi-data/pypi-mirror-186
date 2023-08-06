try:
    from base64 import encodestring
except ImportError:
    from base64 import b64encode as encodestring

from alas_tools3.common.clients.client_base import ApiClientBase


class ConfigurationClient(ApiClientBase):
    entity_endpoint_base_url = '/management/configurations/'

    def set(self, config_name, content):
        try:
            params = {
                'file_name': config_name,
                'base64_content': encodestring(content)
            }
        except:
            b = encodestring(content.encode('utf-8', error='strict'))
            params = {
                'file_name': config_name,
                'base64_content': b
            }
        return self.http_post_json(self.entity_endpoint_base_url + '_set', params)

    def get(self, config_name):
        return self.http_get(self.entity_endpoint_base_url + config_name)