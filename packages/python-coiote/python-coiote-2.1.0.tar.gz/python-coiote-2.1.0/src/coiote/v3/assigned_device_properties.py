from dataclasses import asdict
from typing import List, Optional

from requests import Response

from coiote.utils import ApiEndpoint, StringResult, api_call, sanitize_request_param, api_call_raw
from coiote.v3.model.assigned_device_properties import AssignedDeviceProperty, AssignedDevicePropertyUpsertRequest, \
    AssignedDevicePropertyUpdateRequest


class AssignedDeviceProperties(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="assignedDeviceProperties")

    @api_call(List[str])
    def get_all(self, search_criteria: Optional[str] = None) -> Response:
        return self.session.get(self.get_url(), params={"searchCriteria": search_criteria})

    @api_call(StringResult)
    def upsert_property(self, property_id: str, property: AssignedDevicePropertyUpsertRequest) -> Response:
        property_id = sanitize_request_param(property_id)
        return self.session.put(self.get_url(f"/{property_id}"), json=asdict(property))

    @api_call(AssignedDeviceProperty)
    def get_one(self, property_id: str) -> Response:
        property_id = sanitize_request_param(property_id)
        return self.session.get(self.get_url(f"/{property_id}"))

    @api_call_raw
    def delete_one(self, property_id: str) -> Response:
        property_id = sanitize_request_param(property_id)
        return self.session.delete(self.get_url(f"/{property_id}"))

    @api_call(AssignedDeviceProperty)
    def update_one(self, property_id: str, update: AssignedDevicePropertyUpdateRequest) -> Response:
        property_id = sanitize_request_param(property_id)
        return self.session.patch(self.get_url(f"/{property_id}"), json=asdict(update))
