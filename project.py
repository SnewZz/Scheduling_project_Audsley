import numpy as np
import matplotlib.pyplot as plt
import matplotlib, random, sys

'''
This method allows to read the file which contains the task set and return a list called
tasks_list which is composed of many sublists (the tasks). A sublist represent a task. The first 
element in the sublist is the offset, the second is WCET, the third is the deadline
and the last is the period.  
'''
def fileReader(filename):
	file = open(filename)
	data = file.read().split()
	cnt = 0
	task = []
	tasks_list = []
	for item in data:
		cnt = cnt + 1
		task.append(int(item))
		if cnt == 4:
			cnt = 0
			task.append(1)
			tasks_list.append(task)
			task = []
	return tasks_list

def initialFtpSolution(tasks_list):
	ftp_solution = []
	for i in range(len(tasks_list)):
		ftp_solution.append([])
	return ftp_solution

'''
This method returns the maximum offset.
'''
def getMaxOffset(tasks_list):
	max_value = 0
	for task in tasks_list:
		if task[0] > max_value:
			max_value = task[0]
	return max_value

'''
This method returns the period of the lowest priority task.
'''
def getMaxPeriod(tasks_list):
	return tasks_list[-1][-2]

 
'''
def timeValue(tasks_list):
	for i in range(len(tasks_list)):
		tasks_list[i][2] = tasks_list[i][2] - 1
	return tasks_list'''

'''
This method checks the deadlines. If one is missed, it returns True.
Otherwise it returns False. 
'''
def verifyDeadlines(tasks_list,time):
	task_number = 0
	for task in tasks_list:
		if task[2] <= time and task[1] > 0 :
			if task_number not in soft_task:
				print("The task " + str(task_number + 1) + " misses its deadline")
				return True
			else:
				deadlines_miss.append((task_number,task[2])) 
		task_number = task_number + 1
	return False

'''
This method checks if one of the tasks in the task_list can begin. 
If it is the case, it returns the number of the task. Else, it 
returns -1. 
'''
def canBegin(tasks_list, time):
	task_number = 0
	for task in tasks_list:
		if task[0] <= time and task[1] > 0:
			return task_number
		task_number = task_number + 1
	return -1

def modifyOffset(task):
	task[0] = task[0] + task[3]
	return task

def modifyDeadline(task,task_number):
	task[2] = task[0] + fileReader(file_name)[task_number][2]  
	return task

def modifyWCET(task,task_number):
	task[1] = fileReader(file_name)[task_number][1]
	return task

'''
This method executes the task and so I decrement its WCET 
'''
def executeTask(task,task_number,time):
	task[1] = task[1] - 1
	if task[1] == 0 : #and task[0] <= time 
		#print("==> " + str(task_number) + " deadline : " + str(task[2]) + " time : " + str(time)
		task[4] = task[4] + 1
		modifyOffset(task)
		modifyDeadline(task,task_number) #It is OK because the value (ligne 78) of task[0] has been modified
		modifyWCET(task,task_number)
	elif task[2] <= time and task[1] > 0:
			deadlines_miss.append((task_number,task[2]))


	return task


def testOffset(task,interval_end):
	if task[0] < interval_end:
		return False
	else:
		return True

def ftpScheduler(tasks_list):
	time = 0 
	task_number = 0 # 1 = 2 eme task
	task_duration = 0
	task_start = 0
	while time <= interval_end and not verifyDeadlines(tasks_list,time): 
		answer = canBegin(tasks_list, time)
		if answer != -1:
			if answer != task_number:
				ftp_solution[task_number].append((task_start,task_duration))
				task_duration = 1
				task_start = time
			else:
				task_duration = task_duration + 1
			task_number = answer
			tasks_list[task_number] = executeTask(tasks_list[task_number],task_number,time)
		time = time + 1	
	ftp_solution[task_number].append((task_start,task_duration)) #Quand une deadline a été manqué pour mettre ce qui a été fait et pour le dernier job executer 
		
	

def colorChoice(colors_use):
	colors_list = list(matplotlib.colors.cnames.keys()) #['b','orange','deepskyblue','c','m','y','p']#
	color = random.choice(colors_list)
	while color in colors_use and len(colors_use) < len(colors_list):
		color = random.choice(colors_list)
	colors_use.append(color)
	return color

def generateTaskName(tasks_list):
	tasks_name = []
	names_position = []
	position = 0.5
	for i in range(len(tasks_list)):
		tasks_name.append("Task "+str(i + 1))
		names_position.append(position)
		position = position + 1
	return tasks_name,names_position

def createGraph(solution,interval_end,deadlines_miss):
	fig, ax = plt.subplots()
	ax.grid(True)
	ax.set_xlim(0,interval_end)
	ax.set_ylim(0,len(solution))
	names,positions = generateTaskName(solution)
	ax.set_yticks(positions)
	ax.set_yticklabels(names)
	colors_use = []

	for index in range(len(solution)):
		color = colorChoice(colors_use)
		ax.broken_barh(solution[index], (index, 1), facecolors=color)

	y = 0
	for task in fileReader(file_name):
		print(task)
		offset = task[0]
		print(offset)
		while offset < interval_end:
			 plt.vlines(x = offset, ymin = y, ymax = y + 0.5,colors = 'black',linestyles = 'solid')
			 plt.vlines(x = offset + task[2], ymin = y + 0.5, ymax = y + 1,colors = 'green',label = 'vline_multiple - full height')
			 offset = offset + task[3]
		y = y + 1


	for elem in deadlines_miss:
		plt.vlines(x = elem[1], ymin = elem[0], ymax = elem[0] + 1,colors = 'red',label = 'vline_multiple - full height')

	plt.show()


if __name__ == "__main__":
	file_name = sys.argv[2]
	soft_task = []

	deadlines_miss = []

	tasks_list = fileReader(file_name)
	reply1 = input("* If you want to work with soft real-time task(s) press Y otherwise press N : ")
	while reply1 != "Y" and reply1 != "N":
		reply1 = input("* If you want to work with soft real-time task(s) press Y otherwise press N : ")
	if reply1 == "Y":
		reply2 = input("* Please enter the number of a soft task or Stop : ")
		while reply2 != "Stop" and len(soft_task) != len(tasks_list):
			if int(reply2) >= 1 and int(reply2) <= len(tasks_list):
				soft_task.append(int(reply2) - 1)
				reply2 = input("* Please enter the number of a soft task : ")
			else:
				print("* The task number must be equal or greater than 1 and must be equal or smaller than "+str(len(tasks_list)))
				reply2 = input("* Please enter the number of a soft task : ") 
	if sys.argv[1] == "audsley":
		pass #A faire 
	elif sys.argv[1] == "scheduler":
		interval_end = getMaxOffset(tasks_list) + (2 * getMaxPeriod(tasks_list))
		ftp_solution = initialFtpSolution(tasks_list)
		ftpScheduler(tasks_list)
		createGraph(ftp_solution,interval_end,deadlines_miss)


	
	

