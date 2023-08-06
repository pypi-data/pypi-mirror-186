from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional


@dataclass
class UserCreateRequest:
    login: str
    email: str
    password: str
    domain: str
    emailVerified: bool
    tosAccepted: bool
    roles: List[str] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)


@dataclass
class UserPatchRequest:
    emailVerified: Optional[bool] = None
    userEnabled: Optional[bool] = None
    domain: Optional[str] = None
    password: Optional[str] = None
    tosAccepted: Optional[bool] = None
    roles: List[str] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)


@dataclass
class User:
    userId: str
    login: str
    active: bool
    superUser: bool
    staff: bool
    domain: str
    password: str
    expirationDate: Optional[datetime]
    creationDate: Optional[datetime]
    roles: List[str]
    permissions: List[str]
    fullName: str
    properties: Dict[str, str]
    accessSchedule: Optional[str]
    securityPolicyId: Optional[str]
