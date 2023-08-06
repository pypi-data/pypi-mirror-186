from dataclasses import asdict
from typing import List

from requests import Response

from coiote.utils import ApiEndpoint, api_call, sanitize_request_param, api_call_raw
from coiote.v3.model.extensions import AzureDpsConfig, AzureExtensionConfig, AzureIotHubConfig, AzureIotCentralConfig, \
    ExportConfig


class Extensions(ApiEndpoint):
    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs, api_url="extensions")

    @api_call(List[str])
    def get_available_extensions(self) -> Response:
        return self.session.get(self.get_url())

    @api_call(AzureDpsConfig)
    def get_azure_dps_config(self) -> Response:
        return self.session.get(self.get_url("/azureDps"))

    @api_call_raw
    def test_azure_dps_config(self, dps_config: AzureDpsConfig):
        return self.session.post(self.get_url("/azureDps/testConfig"), json=asdict(AzureExtensionConfig(dps_config)))

    @api_call_raw
    def setup_azure_dps_extension(self, dps_config: AzureDpsConfig):
        return self.session.post(self.get_url("/azureDps"), json=asdict(AzureExtensionConfig(dps_config)))

    @api_call_raw
    def delete_azure_dps_extension(self):
        return self.session.delete(self.get_url("/azureDps"))

    @api_call(AzureIotHubConfig)
    def get_azure_iot_hub_config(self) -> Response:
        return self.session.get(self.get_url("/azureIotHub"))

    @api_call_raw
    def test_azure_iot_hub_config(self, hub_config: AzureIotHubConfig):
        return self.session.post(self.get_url("/azureIotHub/testConfig"), json=asdict(AzureExtensionConfig(hub_config)))

    @api_call_raw
    def setup_azure_iot_hub_extension(self, hub_config: AzureIotHubConfig):
        return self.session.post(self.get_url("/azureIotHub"), json=asdict(AzureExtensionConfig(hub_config)))

    @api_call_raw
    def delete_azure_iot_hub_extension(self):
        return self.session.delete(self.get_url("/azureIotHub"))

    @api_call(AzureIotCentralConfig)
    def get_azure_iot_central_config(self) -> Response:
        return self.session.get(self.get_url("/azureIotCentral"))

    @api_call_raw
    def test_azure_iot_central_config(self, central_config: AzureIotCentralConfig):
        return self.session.post(self.get_url("/azureIotCentral/testConfig"),
                                 json=asdict(AzureExtensionConfig(central_config)))

    @api_call_raw
    def setup_azure_iot_central_extension(self, central_config: AzureIotCentralConfig):
        return self.session.post(self.get_url("/azureIotCentral"), json=asdict(AzureExtensionConfig(central_config)))

    @api_call_raw
    def delete_azure_iot_central_extension(self):
        return self.session.delete(self.get_url("/azureIotCentral"))

    @api_call(str)
    def export_group_to_hyperscaler(self, config: ExportConfig) -> Response:
        return self.session.post(self.get_url("/hyperscaler/export"), json=asdict(config))

    @api_call(str)
    def get_export_status(self, export_job_id: str) -> Response:
        export_job_id = sanitize_request_param(export_job_id)
        return self.session.get(self.get_url(f"/hyperscaler/export/{export_job_id}"))

    @api_call_raw
    def restart_device_client(self, device_id: str):
        device_id = sanitize_request_param(device_id)
        return self.session.get(self.get_url(f"/hyperscaler/restartClient/{device_id}"))
