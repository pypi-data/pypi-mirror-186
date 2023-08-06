from dataclasses import dataclass
from typing import Optional


@dataclass
class SettingValue:
    name: str
    value: str
    groupId: Optional[str] = None
    isSecret: Optional[bool] = False
