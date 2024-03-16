from fastapi import FastAPI
from typing import List
from .models import Process, ScheduleRequest, ProcessResponse
from .scheduling import round_robin_scheduling

app = FastAPI()

@app.post("/schedule/", response_model=List[ProcessResponse])
async def schedule(schedule_request: ScheduleRequest):
    processes = schedule_request.processes
    quantum = schedule_request.quantum
    waiting_times, turnaround_times = round_robin_scheduling(processes, quantum)
    response = [
        ProcessResponse(process_id=process.process_id, waiting_time=wt, turnaround_time=tt)
        for process, wt, tt in zip(processes, waiting_times, turnaround_times)
    ]
    return response
