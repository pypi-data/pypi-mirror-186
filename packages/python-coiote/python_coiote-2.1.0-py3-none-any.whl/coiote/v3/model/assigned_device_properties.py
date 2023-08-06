from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, List


@dataclass
class AssignedDevicePropertyTarget:
    key: str
    value: str


@dataclass
class AssignedDeviceProperty:
    externalId: str
    creationTime: datetime
    isActive: bool
    wasApplied: bool
    lastApplication: Optional[datetime]
    properties: Dict[str, str]
    multiShot: bool
    lastMatchedDevice: Optional[str]
    target: AssignedDevicePropertyTarget


@dataclass
class AssignedDevicePropertyUpsertRequest:
    target: AssignedDevicePropertyTarget
    isActive: bool
    properties: Dict[str, str]
    multiShot: bool


@dataclass
class AssignedDevicePropertyUpdateRequest:
    isActive: bool
    multiShot: bool
    reapply: bool = False
    putProperties: Dict[str, str] = field(default_factory=dict)
    removeProperties: List[str] = field(default_factory=list)
