from dataclasses import asdict
from typing import List, Optional

from requests import Response

from coiote.utils import ApiEndpoint, api_call, sanitize_request_param, api_call_raw
from coiote.v3.model.setting_values import SettingValue


class SettingValues(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="settingValues")

    @api_call(List[SettingValue])
    def get_all(self, search_criteria: Optional[str]) -> Response:
        return self.session.get(self.get_url(), params={"searchCriteria": search_criteria})

    @api_call_raw
    def upsert_one(self, setting_value: SettingValue):
        return self.session.put(self.get_url(), json=asdict(setting_value))

    @api_call(List[SettingValue])
    def get_device_profile(self, device_id: str, with_device_properties: bool = False) -> Response:
        device_id = sanitize_request_param(device_id)
        params = {"withDeviceProperties": with_device_properties}
        return self.session.get(self.get_url(f"/deviceProfile/{device_id}"), params=params)

    @api_call(List[SettingValue])
    def get_group_profile(self, group_id: str) -> Response:
        group_id = sanitize_request_param(group_id)
        return self.session.get(self.get_url(f"/groupProfile/{group_id}"))
