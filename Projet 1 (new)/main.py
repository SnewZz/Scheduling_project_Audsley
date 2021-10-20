import scheduler, task, sys, vizualizeScheduling


def fileReader(filename):
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
			s.startScheduler()
			v = vizualizeScheduling.VizualizeScheduling(s)
			v.draw()
		elif sys.argv[1] == "audsley":
			pass
	except:
		print("The program must have two arguments : audsley|scheduler task_file")



	

