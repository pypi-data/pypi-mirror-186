from dataclasses import dataclass
from typing import Union


@dataclass
class AzureDpsConfig:
    scopeId: str
    enrollmentGroupSymmetricKey: str
    dpsEndpoint: str


@dataclass
class AzureIotCentralConfig:
    apiToken: str
    iotCentralHost: str
    dpsHost: str
    syncEnabled: bool


@dataclass
class AzureIotHubConfig:
    connectionString: str
    storageConnectionString: str
    syncEnabled: bool


@dataclass
class AzureExtensionConfig:
    config: Union[AzureDpsConfig, AzureIotCentralConfig, AzureIotHubConfig]


@dataclass
class ExportConfig:
    groupId: str
    excludeIntegrated: bool = False
