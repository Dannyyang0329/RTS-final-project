import os
import json
from functions import *

MAX_TIME = 100

class Scheduler:
    def __init__(self, input_file):
        # load the json file
        self.schedules = json.load(open(input_file))
        self.output_list = []

    def schedule(self):
        # print number of schedules
        print(len(self.schedules))
        self.output_list.append(str(len(self.schedules))+ "\n")

        for idx, schedule in enumerate(self.schedules):
            print(idx)  # print schedule number
            self.output_list.append(str(idx)+ "\n")
            periodic_jobs = get_job_info(schedule["Periodic"], "Periodic")
            aperiodic_jobs = get_job_info(schedule["Aperiodic"], "Aperiodic")
            sporadic_jobs = get_job_info(schedule["Sporadic"], "Sporadic")

            sorted_periodic = sorted(periodic_jobs, key=lambda job: int(job[1]))
            sorted_sporadic = sorted(sporadic_jobs, key=lambda job: int(job[1]))
            sorted_aperiodic = sorted(aperiodic_jobs, key=lambda job: int(job[0]))

            # init time line
            empty_time_line = ["None"] * MAX_TIME
            time_line = ["None"] * MAX_TIME

            # optimal off-line scheduling in 100 time units
            reject_list = []
            while True:
                is_finish = True
                for p_job in sorted_periodic:
                    res, new_time_line = fillin_schedule(p_job, time_line)
                    if res == True:
                        time_line = new_time_line
                    else:
                        reject_list.append(str(f"{p_job[3][0]} {p_job[3][1:]} -1 -1 Reject"))
                        time_line = empty_time_line.copy()
                        sorted_periodic = remove_reject_task(p_job[3], sorted_periodic)
                        is_finish = False
                        break
                if is_finish == True:
                    break

            for s_job in sorted_sporadic:
                res, new_time_line = fillin_schedule(s_job, time_line)
                if res == True:
                    time_line = new_time_line
                else:
                    reject_list.append(str(f"{s_job[3][0]} {s_job[3][1:]} -1 -1 Reject"))

            for a_job in sorted_aperiodic:
                res, new_time_line = fillin_schedule(a_job, time_line)
                if res == True:
                    time_line = new_time_line
                else:
                    reject_list.append(str(f"{a_job[3][0]} {a_job[3][1:]} -1 -1 Reject"))

            for reject_job in reject_list:
                print(reject_job)
                self.output_list.append(reject_job + "\n")

            tmp = show_schedule(time_line)
            self.output_list += tmp

            # show statistics of "Periodic", "Aperiodic", "Sporadic"
            reject_num = [0, 0, 0]
            for reject_job in reject_list:
                if reject_job[0] == "P":
                    reject_num[0] += 1
                elif reject_job[0] == "A":
                    reject_num[1] += 1
                elif reject_job[0] == "S":
                    reject_num[2] += 1
            periodic_rate = reject_num[0] / len(schedule["Periodic"]) if len(schedule["Periodic"]) != 0 else 0
            aperiodic_rate = reject_num[1] / len(aperiodic_jobs) if len(aperiodic_jobs) != 0 else 0
            sporadic_rate = reject_num[2] / len(sporadic_jobs) if len(sporadic_jobs) != 0 else 0
            rates = str(f"{periodic_rate} {aperiodic_rate} {sporadic_rate}")
            print(rates)
            self.output_list.append(rates + "\n")

            if len(self.schedules)-1 != idx:
                print("FINISH")
                self.output_list.append("FINISH")

        # end of output
        print("-1")
        self.output_list.append("-1\n")

if __name__ == "__main__":
    input_file = input("Enter the json filename to schedule: ")
    if os.path.exists(input_file) == False:
        print("File does not exist")
        exit(1)

    scheduler = Scheduler(input_file)
    scheduler.schedule()
