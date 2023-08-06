from alas_tools3.clients.management.task import TaskClient
from alas_tools3.common.clients.client_base import ApiClientBase


class MaintenanceClient(ApiClientBase):
    def process_operation(self, operation, params):
        return TaskClient(**self.args).enqueue('maintenance', {
            'operation': operation,
            'params': params
        })
