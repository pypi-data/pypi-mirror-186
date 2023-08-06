from typing import List

from requests import Response

from coiote.utils import ApiEndpoint, api_call, sanitize_request_param
from coiote.v3.model.device_resources import Lwm2mObjectDefinition, Lwm2mResourceData


class DeviceResources(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="instantiatedResources")

    @api_call(List[Lwm2mObjectDefinition])
    def get_defined_resources(self, device_id: str, objects: List[str]) -> Response:
        device_id = sanitize_request_param(device_id)
        parameters = {"parameters": objects}
        return self.session.get(self.get_url(f"/dataModelDefinition/{device_id}"), params=parameters)

    @api_call(List[Lwm2mResourceData])
    def get_resources_data(self, device_id: str, objects: List[str]) -> Response:
        device_id = sanitize_request_param(device_id)
        parameters = {"parameters": objects}
        return self.session.get(self.get_url(f"/resourcesData/{device_id}"), params=parameters)
