from dataclasses import dataclass
from enum import auto
from typing import List, Union

from coiote.utils import AutoNamedEnum


class InstanceType(AutoNamedEnum):
    Single = auto()
    Multiple = auto()


class Lwm2mResourceType(AutoNamedEnum):
    String = auto()
    Integer = auto()
    UnsignedInteger = auto()
    Float = auto()
    Boolean = auto()
    Opaque = auto()
    Time = auto()
    Objlnk = auto()
    Corelnk = auto()
    NoneType = "None"


class Lwm2mResourceOperationType(AutoNamedEnum):
    Read = auto()
    Write = auto()
    Execute = auto()


@dataclass
class Lwm2mResourceDefinition:
    id: int
    name: str
    operations: List[Lwm2mResourceOperationType]
    instanceType: InstanceType
    mandatory: bool
    type: Lwm2mResourceType
    range: str
    units: str
    description: str


@dataclass
class SingleInstanceResourceData:
    value: str


@dataclass
class MultiInstanceResourceData:
    values: List[str]


@dataclass
class SingleInstanceResourceValue:
    Single: SingleInstanceResourceData

    def get_value(self) -> str:
        return self.Single.value


@dataclass
class MultipleInstanceResourceValue:
    Multiple: MultiInstanceResourceData

    def get_value(self) -> List[str]:
        return self.Multiple.values


@dataclass
class Lwm2mResourceData:
    path: str
    value: Union[SingleInstanceResourceValue, MultipleInstanceResourceValue]
    resourceId: int
    operations: List[Lwm2mResourceOperationType]
    mandatory: bool
    type: Lwm2mResourceType
    range: str
    units: str
    description: str


@dataclass
class Lwm2mObjectDefinition:
    id: int
    name: str
    objectVersion: str
    instanceType: InstanceType
    mandatory: bool
    resourceDefinitions: List[Lwm2mResourceDefinition]
