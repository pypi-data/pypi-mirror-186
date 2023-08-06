from dataclasses import asdict
from typing import List, Dict

from requests import Response

from coiote.utils import ApiEndpoint, api_call, sanitize_request_param, api_call_raw
from coiote.v3.model.device_tests import DeviceTestSchedule, TestExecutionReport


class DeviceTests(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="protocolTests")

    @api_call_raw
    def run_for_device(self, device_id: str, tests: List[str] = None):
        if tests is None:
            tests = []
        device_id = sanitize_request_param(device_id)
        tests = DeviceTestSchedule(tests)
        return self.session.post(self.get_url(f"/schedule/device/{device_id}"), json=asdict(tests))

    @api_call_raw
    def run_for_group(self, group_id: str, tests: List[str] = None):
        if tests is None:
            tests = []
        group_id = sanitize_request_param(group_id)
        tests = DeviceTestSchedule(tests)
        return self.session.post(self.get_url(f"/schedule/group/{group_id}"), json=asdict(tests))

    @api_call(TestExecutionReport)
    def get_report_for_device(self, device_id: str, tests: List[str] = None) -> Response:
        if tests is None:
            tests = []
        device_id = sanitize_request_param(device_id)
        tests = DeviceTestSchedule(tests)
        return self.session.post(self.get_url(f"/report/device/{device_id}"), json=asdict(tests))

    @api_call(Dict[str, TestExecutionReport])
    def get_report_for_group(self, group_id: str, tests: List[str] = None) -> Response:
        if tests is None:
            tests = []
        group_id = sanitize_request_param(group_id)
        return self.session.post(self.get_url(f"/report/group/{group_id}"), json=asdict(DeviceTestSchedule(tests)))
