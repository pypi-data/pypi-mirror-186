from dataclasses import dataclass, field
from typing import Optional, Union, List


@dataclass
class ObservedDevice:
    DeviceId: str


@dataclass
class ObservedGroup:
    GroupId: str


@dataclass
class EntityObservationData:
    targetEntity: Union[ObservedDevice, ObservedGroup]
    path: str


@dataclass
class ObservationAttribute:
    name: str
    value: str


@dataclass
class ObservationData:
    deviceId: str
    path: str
    attributes: List[ObservationAttribute] = field(default_factory=list)


@dataclass
class SetObservationRequest:
    attributes: List[ObservationAttribute] = field(default_factory=list)
    createEnsureObserveIfNotExists: bool = False


@dataclass
class BasicSetObservationRequest:
    minPeriod: Optional[int] = None
    maxPeriod: Optional[int] = None
    createEnsureObserveIfNotExists: bool = False
