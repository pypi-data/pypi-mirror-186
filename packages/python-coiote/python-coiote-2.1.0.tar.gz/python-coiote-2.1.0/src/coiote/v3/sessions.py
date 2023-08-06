from typing import Optional

from coiote.utils import ApiEndpoint, sanitize_request_param, api_call_raw


class Sessions(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="sessions")

    @api_call_raw
    def start_for_device(self, device_id: str, task_id: Optional[str] = None, allow_deregistered=False):
        device_id = sanitize_request_param(device_id)
        params = {"taskId": task_id}
        if allow_deregistered:
            path = f"/{device_id}/allow-deregistered"
        else:
            path = f"/{device_id}"
        return self.session.post(self.get_url(path), params=params)
