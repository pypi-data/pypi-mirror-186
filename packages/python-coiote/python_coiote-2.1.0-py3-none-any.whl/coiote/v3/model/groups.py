from dataclasses import dataclass
from typing import Optional


@dataclass
class Group:
    id: str
    description: Optional[str] = None


@dataclass
class GroupUpdateRequest:
    description: Optional[str]
