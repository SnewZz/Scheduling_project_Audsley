import sys
import task
import scheduler as s

'''
This method allows to read the file which contains the task set and return a list called
tasks_list which is composed of many sublists (the tasks). A sublist represent a task. The first 
element in the sublist is the offset, the second is WCET, the third is the deadline
and the last is the period.  
'''

def fileReader(filename):
	file = open(filename)
	lines = file.readlines()
	tasks = []
	for line in lines:
		tmp = line.split()
		tasks.append(task.Task(tmp[1], tmp[2], tmp[3], tmp[0]))
	return tasks

def main ():
	tasks_list = fileReader(sys.argv[2])
	if sys.argv[1] == "scheduler":
		scheduler = s.Scheduler(tasks_list)
	elif sys.argv[1] == "audsley":
		pass
		
#     soft_task = []
#     deadlines_miss = []
#     reply1 = input("* If you want to work with soft real-time task(s) press Y otherwise press N : ")
#     while reply1 != "Y" and reply1 != "N":
#     	reply1 = input("* If you want to work with soft real-time task(s) press Y otherwise press N : ")
# if reply1 == "Y":
#         reply2 = input("* Please enter the number of a soft task or Stop : ")
#     	while reply2 != "Stop" and len(soft_task) != len(tasks_list):
#             if int(reply2) >= 1 and int(reply2) <= len(tasks_list):
#                 soft_task.append(int(reply2) - 1)
#                 reply2 = input("* Please enter the number of a soft task : ")
#             else:
#                 print("* The task number must be equal or greater than 1 and must be equal or smaller than "+str(len(tasks_list)))
#                 reply2 = input("* Please enter the number of a soft task : ") 
# 	if sys.argv[1] == "audsley":
#          interval_end = getMaxOffset(tasks_list) + (2 * getMaxPeriod(tasks_list))
#         ftp_solution = initialFtpSolution(tasks_list)
# 		audsley(tasks_list)
# 	elif sys.argv[1] == "scheduler":
# 		interval_end = getMaxOffset(tasks_list) + (2 * getMaxPeriod(tasks_list))
# 		ftp_solution = initialFtpSolution(tasks_list)
# 		ftpScheduler(tasks_list)
# 		createGraph(ftp_solution,interval_end,deadlines_miss)

if __name__ == "__main__":
    main()
