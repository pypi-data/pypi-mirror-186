from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class DeviceTestSchedule:
    testCases: List[str] = field(default_factory=list)


@dataclass
class TestExecutionReport:
    passedSuccessfully: List[str] = field(default_factory=list)
    waitingForExecution: List[str] = field(default_factory=list)
    passedWithWarning: Dict[str, str] = field(default_factory=dict)
    failed: Dict[str, str] = field(default_factory=dict)