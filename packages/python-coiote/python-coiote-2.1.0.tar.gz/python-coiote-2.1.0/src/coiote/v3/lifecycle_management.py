from dataclasses import asdict

from coiote.utils import ApiEndpoint, api_call_raw
from coiote.v3.model.lifecycle_management import FactoryTestingRequest


class LifecycleManagement(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="deviceLifecycleManagement")

    @api_call_raw
    def activate_factory_testing(self, data: FactoryTestingRequest):
        return self.session.post(self.get_url("/factoryTesting/activate"), json=asdict(data))

    @api_call_raw
    def deactivate_factory_testing(self, data: FactoryTestingRequest):
        return self.session.post(self.get_url("/factoryTesting/deactivate"), json=asdict(data))
