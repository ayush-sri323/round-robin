from pydantic import BaseModel
from typing import List

class Process(BaseModel):
    process_id: str
    burst_time: int

class ScheduleRequest(BaseModel):
    processes: List[Process]
    quantum: int

class ProcessResponse(BaseModel):
    process_id: str
    waiting_time: int
    turnaround_time: int
