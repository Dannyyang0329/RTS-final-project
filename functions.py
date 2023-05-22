
MAX_TIME = 100

# define scheduling function
def fillin_schedule(job, job_type, job_idx, time_line):
    new_time_line = time_line.copy()
    if job_type == "Periodic":
        period, exec_time = job["P"], job["C"]
        for arrive_time in range(0, MAX_TIME, period):
            deadline = min(arrive_time+exec_time, MAX_TIME)
            cur_t, remain_time = arrive_time, exec_time
            while cur_t < deadline and remain_time > 0:
                if new_time_line[cur_t] == "None":
                    new_time_line[cur_t] = "P" + str(job_idx)
                    remain_time -= 1
                cur_t += 1
            if remain_time > 0:
                return False, time_line
        return True, new_time_line
    elif job_type == "Aperiodic" or job_type == "Sporadic":
        arrive_time, exec_time = job["A"], job["C"]
        deadline = min(arrive_time+exec_time, MAX_TIME)
        cur_t, remain_time = arrive_time, exec_time
        while cur_t < deadline and remain_time > 0:
            if new_time_line[cur_t] == "None":
                new_time_line[cur_t] = job_type[0] + str(job_idx)
                remain_time -= 1
            cur_t += 1
        if remain_time > 0:
            return False, time_line
        else:
            return True, new_time_line
        
def show_schedule(time_line):
    cur_job, job_idx, start_t, end_t = time_line[0][0], time_line[0][1:], 0, 0
    for cur_t in range(1, MAX_TIME):
        if time_line[cur_t] != cur_job+job_idx :
            if cur_job != "N":
                print(f"{cur_job} {job_idx} {start_t} {end_t+1} Complete")
            cur_job, job_idx, start_t, end_t = time_line[cur_t][0], time_line[cur_t][1:], cur_t, cur_t
        else:
            end_t += 1

