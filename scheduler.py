import os
import json
from functions import *

MAX_TIME = 100

# get the json filename to schedule
input_file = input("Enter the json filename to schedule: ")
if os.path.exists(input_file) == False:
    print("File does not exist")
    exit(1)

# load the json file
schedules = json.load(open(input_file))

# print number of schedules
print(len(schedules))
for idx, schedule in enumerate(schedules):
    print(idx)  # print schedule number
    periodic_jobs = schedule["Periodic"]
    aperiodic_jobs = schedule["Aperiodic"]
    sporadic_jobs = schedule["Sporadic"]

    # init time line
    time_line = ["None"] * MAX_TIME

    # optimal off-line scheduling in 100 time units
    task_group = [
        ("Periodic", periodic_jobs),
        ("Sporadic", sporadic_jobs), 
        ("Aperiodic", aperiodic_jobs)
    ]
    for job_type, jobs in task_group:
        for i, job in enumerate(jobs):
            res, new_time_line = fillin_schedule(job, job_type, i, time_line)
            if res == True:
                time_line = new_time_line
            else:
                print(f"{job_type[0]} {i} -1 -1 Reject")

    show_schedule(time_line)
    # print the detail of the time line
    # for i in range(0, 10):
    #     print(i, end=": ")
    #     print(time_line[i*10:(i+1)*10])

# end of output
print("-1")
exit(0)