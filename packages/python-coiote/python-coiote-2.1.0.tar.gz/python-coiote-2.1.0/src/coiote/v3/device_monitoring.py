from dataclasses import asdict
from datetime import datetime
from typing import Optional

from requests import Response

from coiote.utils import ApiEndpoint, api_call, ISO_INSTANT_FORMAT, sanitize_request_param, api_call_raw
from coiote.v3.model.device_monitoring import MonitoringStatus, MonitoringDataResponse, SetResourceAliasRequest


class DeviceMonitoring(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="deviceMonitoring")

    @api_call_raw
    def set_resource_alias(self, device_id: str, resource: str, alias: str):
        device_id = sanitize_request_param(device_id)
        body = SetResourceAliasRequest(lwm2mUrl=resource, alias=alias)
        return self.session.post(self.get_url(f"/configuration/device/{device_id}/alias"), json=asdict(body))

    @api_call_raw
    def delete_resource_alias(self, device_id: str, resource: str):
        device_id = sanitize_request_param(device_id)
        resource = sanitize_request_param(resource)
        return self.session.delete(self.get_url(f"/configuration/device/{device_id}/resourceUrl/{resource}"))

    @api_call_raw
    def get_aliases_for_device(self, device_id: str) -> Response:
        device_id = sanitize_request_param(device_id)
        return self.session.get(self.get_url(f"/configuration/device/{device_id}/aliases"))

    @api_call_raw
    def toggle_monitoring_for_device(self, device_id: str, enabled: bool = True):
        device_id = sanitize_request_param(device_id)
        if enabled:
            url = self.get_url(f"/configuration/device/{device_id}/enable")
        else:
            url = self.get_url(f"/configuration/device/{device_id}/disable")
        return self.session.post(url)

    @api_call_raw
    def toggle_monitoring_for_group(self, group_id: str, enabled: bool = True):
        group_id = sanitize_request_param(group_id)
        if enabled:
            url = self.get_url(f"/configuration/group/{group_id}/enable")
        else:
            url = self.get_url(f"/configuration/group/{group_id}/disable")
        return self.session.post(url)

    @api_call(MonitoringStatus)
    def is_device_monitored(self, device_id: str) -> Response:
        return self.session.get(self.get_url(f"/configuration/device/{device_id}/enabled"))

    @api_call(MonitoringDataResponse)
    def get_data_batch(self,
                       device_id: str,
                       lwm2m_url: Optional[str],
                       alias: Optional[str],
                       start_time: datetime,
                       end_time: Optional[datetime],
                       limit=2048
                       ) -> Response:
        if lwm2m_url is not None:
            safe_lwm2m_url = sanitize_request_param(lwm2m_url)
            url = self.get_url(f"/data/{device_id}/resourceUrl/{safe_lwm2m_url}")
        elif alias is not None:
            safe_alias = sanitize_request_param(alias)
            url = self.get_url(f"/data/{device_id}/alias/{safe_alias}")
        else:
            raise ValueError("You must specify either LwM2M URL or alias of the resource")
        params = {"timeRangeStart": start_time.strftime(ISO_INSTANT_FORMAT), "limit": limit}
        if end_time:
            params["timeRangeEnd"] = end_time.strftime(ISO_INSTANT_FORMAT)
        return self.session.get(url, params=params)
