from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class ExecutedTaskInfo:
    taskId: str
    deviceId: str


@dataclass
class TaskReport:
    taskId: str
    deviceId: str
    status: str
    startTime: datetime
    finishTime: datetime
    lastUpdateTime: datetime
    summary: Optional[str]
    blocking: bool
    properties: List[dict]


@dataclass
class TaskReportBatch:
    batch: List[TaskReport]
    nextCursor: int


@dataclass
class TasksSummary:
    totalScheduled: int
    inProgress: int
    completed: int
    successes: int
    failures: int
    notCompleted: int
    completionRate: int
    successRate: int
    failureRate: int
