from dataclasses import asdict, replace

from requests import Response

from coiote.utils import ApiEndpoint, api_call, api_call_raw
from coiote.v3.model.devices import *


class Devices(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="devices")

    @api_call_raw
    def get_all(self, search_criteria: Optional[str]) -> Response:
        return self.session.get(self.get_url(), params={"searchCriteria": search_criteria})

    @api_call(DevicesBatchAddResponse)
    def create_batch(self, devices: List[Device]) -> Response:
        updated_devices = self._update_endpoint_names(devices)
        return self.session.post(self.get_url("/batch"), json=[asdict(device) for device in updated_devices])

    @staticmethod
    def _update_properties(device_id: Optional[str], properties: Dict[str, str]) -> Dict[str, str]:
        if device_id is None:
            return properties
        else:
            return dict(properties, endpointName=device_id)

    def _update_device(self, device: Device) -> Device:
        return replace(device, id=None, properties=self._update_properties(device.id, device.properties))

    def _update_endpoint_names(self, devices: List[Device]) -> List[Device]:
        return [self._update_device(device) for device in devices]

    @api_call(DevicesFindResponse)
    def get_device_details(self,
                           search_criteria: Optional[str] = None,
                           fields: List[str] = None,
                           limit: int = 100,
                           page_bookmark: Optional[str] = None) -> Response:
        if fields is None:
            fields = []
        params = {
            "searchCriteria": search_criteria,
            "fieldSelection": ",".join(fields),
            "limit": limit,
            "pageBookmark": page_bookmark
        }
        return self.session.get(self.get_url("/find/details"), params=params)

    @api_call(SingleDeviceAddResponse)
    def create_one(self, device: Device) -> Response:
        updated = self._update_device(device)
        return self.session.post(self.get_url(), json=asdict(updated))

    @api_call(Device)
    def get_one(self, device_id: str) -> Response:
        return self.session.get(self.get_url(f"/{device_id}"))

    @api_call_raw
    def update_one(self, device_id, request: DeviceUpdateRequest) -> Response:
        return self.session.put(self.get_url(f"/{device_id}"), json=asdict(request))

    @api_call_raw
    def delete_one(self, device_id) -> Response:
        return self.session.delete(self.get_url(f"/{device_id}"))
