from typing import List, Tuple
from .models import Process

def round_robin_scheduling(processes: List[Process], quantum: int) -> Tuple[List[int], List[int]]:
    n = len(processes)
    rem_burst_times = [p.burst_time for p in processes]
    waiting_times = [0] * n
    turnaround_times = [0] * n
    t = 0

    while True:
        done = True
        for i in range(n):
            if rem_burst_times[i] > 0:
                done = False
                if rem_burst_times[i] > quantum:
                    t += quantum
                    rem_burst_times[i] -= quantum
                else:
                    t += rem_burst_times[i]
                    waiting_times[i] = t - processes[i].burst_time
                    rem_burst_times[i] = 0
        if done:
            break

    for i in range(n):
        turnaround_times[i] = processes[i].burst_time + waiting_times[i]
    return waiting_times, turnaround_times
