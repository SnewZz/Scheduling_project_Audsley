import scheduler, task, sys, vizualizeScheduling


def fileReader(filename):
	"""
	It reads the file which contains the tasks and creates objects "Task" and add them in a list. At the end of the execution, it returns the list.
	"""
	file = open(filename)
	data = file.readlines()
	task_list = []
	cnt = 1
	for line in data:
		tmp = line.split()
		task_list.append(task.Task(tmp[0],tmp[1],tmp[2],tmp[3],cnt))
		cnt += 1
	return task_list

if __name__ == "__main__":
	try:
		file_name = sys.argv[2]
		task_list = fileReader(file_name)

		if sys.argv[1] == "scheduler":
			s = scheduler.Scheduler(task_list)
			if not s.startScheduler():
				print("The input task set is not schedulable")
			v = vizualizeScheduling.VizualizeScheduling(s)
			v.draw()
		elif sys.argv[1] == "audsley":
			pass
	except AttributeError:
		print("The program must have two arguments : audsley|scheduler task_file")
	except FileNotFoundError:
		print("This file does not exist !")



	

