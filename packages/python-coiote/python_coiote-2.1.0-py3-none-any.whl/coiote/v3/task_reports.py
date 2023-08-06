from datetime import datetime
from typing import List, Optional

from requests import Response

from coiote.utils import ApiEndpoint, api_call, ISO_INSTANT_FORMAT, sanitize_request_param
from coiote.v3.model.task_reports import ExecutedTaskInfo, TaskReportBatch, TasksSummary, TaskReport


class TaskReports(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="taskReports")

    @api_call(List[ExecutedTaskInfo])
    def get_reports(self, query: str) -> Response:
        return self.session.get(self.get_url(""), params={"searchCriteria": query})

    @api_call(int)
    def get_reports_cursor(self, query: str) -> Response:
        return self.session.get(self.get_url("/findReports"), params={"searchCriteria": query})

    @api_call(TaskReportBatch)
    def get_next_reports_batch(self, cursor_id: int, count: int) -> Response:
        return self.session.get(self.get_url("/moreReports"), params={"cursor": cursor_id, "count": count})

    @api_call(List[TaskReport])
    def find_reports_since(self,
                           since: datetime,
                           taskId: Optional[str] = None,
                           device_id: Optional[str] = None,
                           limit: int = 512,
                           polling_interval_seconds: Optional[int] = None,
                           only_direct_tasks: bool = False) -> Response:
        params = {
            "lastUpdateTime": since.strftime(ISO_INSTANT_FORMAT),
            "taskId": taskId,
            "deviceId": device_id,
            "limit": limit,
            "pollingInterval": polling_interval_seconds,
            "directTasksOnly": only_direct_tasks
        }
        return self.session.get(self.get_url("/findSince"), params=params)

    @api_call(TasksSummary)
    def get_task_summary(self, task_id: str) -> Response:
        return self.session.get(self.get_url("/summary"), params={"taskId": task_id})

    @api_call(TaskReport)
    def get_report_for_device_task(self, task_id: str, device_id: str) -> Response:
        task_id = sanitize_request_param(task_id)
        device_id = sanitize_request_param(device_id)
        return self.session.get(self.get_url(f"/{task_id}/{device_id}"))
