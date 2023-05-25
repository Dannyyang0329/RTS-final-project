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
    periodic_jobs = get_job_info(schedule["Periodic"], "Periodic")
    aperiodic_jobs = get_job_info(schedule["Aperiodic"], "Aperiodic")
    sporadic_jobs = get_job_info(schedule["Sporadic"], "Sporadic")

    hard_jobs = sorted(periodic_jobs+sporadic_jobs, key=lambda job: int(job[1]))
    soft_jobs = sorted(aperiodic_jobs, key=lambda job: int(job[0]))

    # init time line
    empty_time_line = ["None"] * MAX_TIME
    time_line = ["None"] * MAX_TIME

    # optimal off-line scheduling in 100 time units
    reject_list = []
    while True:
        is_finish = True
        print(hard_jobs)
        for h_job in hard_jobs:
            res, new_time_line = fillin_schedule(h_job, time_line)
            if res == True:
                time_line = new_time_line
            else:
                reject_list.append(str(f"{h_job[3][0]} {h_job[3][1:]} -1 -1 Reject"))
                if h_job[3][0] == "P":
                    time_line = empty_time_line.copy()
                    hard_jobs = remove_reject_task(h_job[3], hard_jobs)
                    is_finish = False
                    break
        if is_finish == True:
            break

    for s_job in soft_jobs:
        res, new_time_line = fillin_schedule(s_job, time_line)
        if res == True:
            time_line = new_time_line
        else:
            reject_list.append(str(f"{s_job[3][0]} {s_job[3][1:]} -1 -1 Reject"))

    for reject_job in reject_list:
        print(reject_job)

    show_schedule(time_line)

    # print the detail of the time line
    for i in range(0, 10):
        print(i, end=": ")
        for j in range(i*10, (i+1)*10):
            print("%5s" % time_line[j], end=" ")
        print("")

    # show statistics of "Periodic", "Aperiodic", "Sporadic"
    # periodic_rate = reject_num["Periodic"] / len(periodic_jobs)
    # aperiodic_rate = reject_num["Aperiodic"] / len(aperiodic_jobs)
    # sporadic_jobs = reject_num["Sporadic"] / len(sporadic_jobs)
    # print(f"{periodic_rate} {aperiodic_rate} {sporadic_jobs}")

# end of output
print("-1")
exit(0)


# 1
# 0
# P 1 -1 -1 Reject
# P 0 0 2 Complete
# A 0 5 6 Complete
# S 0 6 25 Complete
# A 1 25 45 Complete
# P 0 50 52 Complete
# S 1 70 95 Complete
# 0.5 0.0 0.0
# -1