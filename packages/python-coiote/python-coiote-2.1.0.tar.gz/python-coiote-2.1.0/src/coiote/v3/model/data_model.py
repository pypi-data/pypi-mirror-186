from dataclasses import dataclass
from datetime import datetime


@dataclass
class DeviceDataEntry:
    name: str
    value: str
    updateTime: datetime
    type: str
