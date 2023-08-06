from dataclasses import asdict

from requests import Response

from coiote.utils import ApiEndpoint, api_call, sanitize_request_param, api_call_raw
from coiote.v3.model.tasks import *


class Tasks(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="tasks")

    @api_call(str)
    def run_device_config_task(self, device_id: str, task_definition: ConfigurationTaskDefinition) -> Response:
        return self.session.post(self.get_url(f"/configure/{device_id}"),
                                 json={'taskDefinition': asdict(task_definition)})

    @api_call(List[str])
    def get_all(self, search_criteria: Optional[str] = None) -> Response:
        params = {"searchCriteria": search_criteria}
        return self.session.get(self.get_url(), params=params)

    @api_call_raw
    def delete_callback(self, task_id: str, callback_id: str):
        task_id = sanitize_request_param(task_id)
        callback_id = sanitize_request_param(callback_id)
        return self.session.delete(self.get_url(f"/callback/{task_id}/{callback_id}"))

    @api_call(str)
    def run_device_fota_task(self,
                             device_id: str,
                             firmware_resource_id: str,
                             transfer_method: TransferMethod = TransferMethod.Pull,
                             transfer_protocol: TransferProtocol = TransferProtocol.HTTP,
                             timeout: str = "20m",
                             use_quota: bool = True,
                             upgrade_strategy: UpgradeStrategy = UpgradeStrategy.WithoutObservations,
                             blocking: bool = True,
                             use_cache_for_initial_state_read: bool = False,
                             check_delivery_and_protocol: bool = True,
                             resume_after_downlink_failure: bool = False,
                             execute_immediately: bool = False
                             ) -> Response:
        params = {
            "executeImmediately": execute_immediately,
            "resumeAfterDownlinkFailure": resume_after_downlink_failure,
            "checkDeliveryAndProtocol": check_delivery_and_protocol,
            "useCacheForInitialStateRead": use_cache_for_initial_state_read,
            "blocking": blocking,
            "upgradeStrategy": upgrade_strategy,
            "useQuota": use_quota,
            "timeout": timeout,
            "transferProtocol": transfer_protocol,
            "transferMethod": transfer_method
        }
        device_id = sanitize_request_param(device_id)
        firmware_resource_id = sanitize_request_param(firmware_resource_id)
        return self.session.post(self.get_url(f"/upgrade/{device_id}/{firmware_resource_id}"), params=params)

    @api_call(Task)
    def get_one(self, task_id: str) -> Response:
        task_id = sanitize_request_param(task_id)
        return self.session.get(self.get_url(f"/{task_id}"))

    @api_call_raw
    def update_one(self, task_id: str, config: TaskConfig):
        task_id = sanitize_request_param(task_id)
        return self.session.put(self.get_url(f"/{task_id}"), json=asdict(config))

    @api_call_raw
    def delete_one(self, task_id: str):
        task_id = sanitize_request_param(task_id)
        return self.session.delete(self.get_url(f"/{task_id}"))
