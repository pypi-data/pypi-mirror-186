from coiote.v3.data_model import DeviceDataEntry
from coiote.v3.model.tasks import *


class DeviceClient:
    def __init__(self, device_id: str, coiote_client: 'Coiote') -> None:
        self.device_id = device_id
        self.coiote_client = coiote_client

    def get_all_data(self) -> List[DeviceDataEntry]:
        return self.coiote_client.data_model.get_device_datamodel(self.device_id)

    def write_to_resource(self, human_readable_path: str, value: str) -> str:
        return self.coiote_client.tasks.run_device_config_task(
            device_id=self.device_id,
            task_definition=ConfigurationTaskDefinition(
                name="write-device-dc-api",
                operations=[WriteOperation(
                    write=WriteDefinition(key=human_readable_path, value=value))]
            )
        )

    def execute_resource(self, human_readable_path: str, arguments: List[ExecuteArg] = None) -> str:
        if arguments is None:
            arguments = []
        return self.coiote_client.tasks.run_device_config_task(
            device_id=self.device_id,
            task_definition=ConfigurationTaskDefinition(
                name="execute-device-dc-api",
                operations=[ExecuteOperation(
                    execute=ExecuteDefinition(key=human_readable_path, argumentList=arguments))]
            )
        )

    def read_resource(self, human_readable_path: str) -> str:
        return self.coiote_client.tasks.run_device_config_task(
            device_id=self.device_id,
            task_definition=ConfigurationTaskDefinition(
                name="read-device-dc-api",
                operations=[ReadOperation(
                    read=ReadDefinition(key=human_readable_path))]
            )
        )

    def get_device_data(self) -> List[DeviceDataEntry]:
        return self.coiote_client.data_model.get_device_datamodel(self.device_id)

    def get_resource_value(self, human_readable_path: str) -> Optional[DeviceDataEntry]:
        result = self.coiote_client.data_model.get_device_datamodel(
            self.device_id, parameters=[human_readable_path])
        matching_result = [
            entry for entry in result if entry.name == human_readable_path]
        if len(matching_result) == 1:
            return matching_result[0]
        else:
            return None

    def reboot_device(self):
        return self.coiote_client.tasks.run_device_config_task(
            device_id=self.device_id,
            task_definition=ConfigurationTaskDefinition(
                name="reboot-device-dc-api",
                operations=[ExecuteOperation(
                    execute=ExecuteDefinition(key="Device.0.Reboot"))]
            )
        )

    def get_location(self):
        return self.coiote_client.data_model.get_device_datamodel(self.device_id, parameters=["Location."])

    def get_task_report(self, task_id: str):
        return self.coiote_client.task_reports.get_report_for_device_task(task_id, self.device_id)
