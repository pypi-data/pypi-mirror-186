from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class TaskTemplateConfig:
    taskName: str
    parameters: List[Dict[str, str]]
    isActive: bool
    properties: Dict[str, str]


@dataclass
class TaskTemplateInvocation:
    templateName: str
    config: Optional[TaskTemplateConfig] = None
    callback: Optional[dict] = None
