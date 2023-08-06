from typing import Any, Optional
import requests

from .auth import Authenticator
from .v3.assigned_device_properties import AssignedDeviceProperties
from .v3.aws_integration import AwsIntegration
from .v3.cert_auth import CertAuth
from .v3.device_resources import DeviceResources
from .v3.device_tests import DeviceTests
from .v3.devices import Devices
from .v3.dialects import Dialects
from .v3.domains import Domains
from .v3.data_model import DataModel
from .v3.device_monitoring import DeviceMonitoring
from .v3.extensions import Extensions
from .v3.groups import Groups
from .v3.lifecycle_management import LifecycleManagement
from .v3.observations import Observations
from .v3.resources import Resources
from .v3.sessions import Sessions
from .v3.setting_values import SettingValues
from .v3.task_templates import TaskTemplates
from .v3.tasks import Tasks
from .v3.task_reports import TaskReports
from .device_client import DeviceClient
from .v3.users import Users


class Coiote:
    """
    Represents a connection to Coiote server.
    """
    SUPPORTED_API_VERSIONS = {"v3"}

    def __init__(
            self,
            url: str,
            auth: Optional[Any] = None,
            api_version: str = "v3",
            verify_ssl: bool = True
    ):
        self.url = url
        self.api_version = api_version
        if self.api_version not in Coiote.SUPPORTED_API_VERSIONS:
            raise ValueError("Only v3 API is supported right now")
        self.api_url = f"{url}/api/coiotedm/{api_version}"
        self.session = requests.Session()
        self.session.verify = verify_ssl
        self.authenticator = Authenticator(
            self.url, self.session, auth=auth)

        self.aws_integration: AwsIntegration = self._make_module(AwsIntegration)
        self.assigned_device_properties: AssignedDeviceProperties = self._make_module(AssignedDeviceProperties)
        self.cert_auth: CertAuth = self._make_module(CertAuth)
        self.data_model: DataModel = self._make_module(DataModel)
        self.device_monitoring: DeviceMonitoring = self._make_module(DeviceMonitoring)
        self.device_resources: DeviceResources = self._make_module(DeviceResources)
        self.device_tests: DeviceTests = self._make_module(DeviceTests)
        self.devices: Devices = self._make_module(Devices)
        self.dialects: Dialects = self._make_module(Dialects)
        self.domains: Domains = self._make_module(Domains)
        self.extensions: Extensions = self._make_module(Extensions)
        self.groups: Groups = self._make_module(Groups)
        self.lifecycle_management: LifecycleManagement = self._make_module(LifecycleManagement)
        self.observations: Observations = self._make_module(Observations)
        self.resources: Resources = self._make_module(Resources)
        self.sessions: Sessions = self._make_module(Sessions)
        self.setting_values: SettingValues = self._make_module(SettingValues)
        self.task_reports: TaskReports = self._make_module(TaskReports)
        self.task_templates: TaskTemplates = self._make_module(TaskTemplates)
        self.tasks: Tasks = self._make_module(Tasks)
        self.users: Users = self._make_module(Users)

    def _make_module(self, module_def):
        return module_def(root_url=self.api_url, authenticator=self.authenticator, session=self.session)

    def create_device_client(self, device_id: str) -> DeviceClient:
        return DeviceClient(device_id, self)
