MAX_TIME = 100

def get_job_info(jobs, job_type) -> list:
    list = [] # list of [arrival_t, deadline, exec_t, name]
    if job_type == "Periodic":
        for idx, job in enumerate(jobs):
            period, exec_t = job["P"], job["C"]
            for cur_t in range(0, MAX_TIME, period):
                name = "P" + str(idx)
                if cur_t+period <= MAX_TIME:
                    list.append([cur_t, cur_t+period, exec_t, name])
    elif job_type == "Sporadic" or job_type == "Aperiodic":
        for idx, job in enumerate(jobs):
            name = job_type[0] + str(idx)
            arrival_t, exec_t = job["A"], job["C"]
            deadline = arrival_t+exec_t if arrival_t+exec_t <= MAX_TIME else MAX_TIME
            if job_type == "Aperiodic":
                deadline = MAX_TIME
            list.append([arrival_t, deadline, exec_t, name])
    return list

def remove_reject_task(job_name, hard_jobs):
    new_hard_jobs = []
    for job in hard_jobs:
        if job[3] != job_name:
            new_hard_jobs.append(job)
    return new_hard_jobs.copy()


# define scheduling function
def fillin_schedule(job, time_line):
    new_time_line = time_line.copy()
    arrive_t, deadline, remain_t, name = job[:]
    for cur_t in range(arrive_t, deadline):
        if remain_t == 0:
            break
        if get_continuous_empty_time(cur_t, time_line) >= remain_t:
            new_time_line[cur_t] = name
            remain_t -= 1
    return [True, new_time_line] if remain_t == 0 else [False, new_time_line]


def get_continuous_empty_time(start_t, time_line):
    cnt = 0
    for cur_t in range(start_t, MAX_TIME):
        if time_line[cur_t] == "None":
            cnt += 1
        else:
            break
    return cnt

        
def show_schedule(time_line):
    cur_job, job_idx, start_t, end_t = time_line[0][0], time_line[0][1:], 0, 0
    for cur_t in range(1, MAX_TIME):
        if time_line[cur_t] != cur_job+job_idx :
            if cur_job != "N":
                print(f"{cur_job} {job_idx} {start_t} {end_t+1} Complete")
            cur_job, job_idx, start_t, end_t = time_line[cur_t][0], time_line[cur_t][1:], cur_t, cur_t
        else:
            end_t += 1
