from alas_tools3.clients.cn_admin.service_api_client import ServiceApiClient
from alas_tools3.common.clients import api_client as clients


class ClientB2BApiServiceClient(ServiceApiClient):
    service_endpoint_base_url = '/api/services/app/ClientB2B/'

    def __get_contacts(self, **kwargs):
        url = self.service_endpoint_base_url + 'GetContactClientB2B'
        if 'id' in kwargs and kwargs['id'] is not None:
            url = "{}?ClientB2BId={id}".format(url, **kwargs)

        request = clients.ApiClientRequest(url, self.auth)
        response = self.http_get(request)
        return response

    def get_contacts(self, b2b_id):
        # type: (str) -> ApiClientResponse
        """

        :rtype: ApiClientResponse
        """
        return self.process_request(self.__get_contacts, **{
            'id': b2b_id
        })
