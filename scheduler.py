import os
import json

MAX_TIME = 100

# define scheduling function
def fillin_schedule(job, job_type, job_idx, time_line) -> bool:
    new_time_line = time_line.copy()
    if job_type == "Peridodic":
        period, exec_time = job["P"], job["C"]
        for start_time in range(0, MAX_TIME, period):
            cur_t, remain_time = start_time, exec_time
            while cur_t < MAX_TIME and remain_time > 0:
                if new_time_line[cur_t] == "":
                    new_time_line[cur_t] = "P" + str(job_idx)
                    remain_time -= 1
                cur_t += 1
            if remain_time == 0:
                return True, new_time_line

    elif job_type == "Aperiodic":
        pass
    elif job_type == "Sporadic":
        pass



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

    # optimal off-line scheduling in 100 time units




# end of output
print("-1")
exit(0)