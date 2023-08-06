from dataclasses import dataclass
from typing import Optional


@dataclass
class Domain:
    id: str
    description: Optional[str] = None


@dataclass
class DomainUpdateRequest:
    newDescription: Optional[str]
