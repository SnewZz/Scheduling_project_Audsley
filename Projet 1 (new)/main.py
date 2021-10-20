import scheduler, task, sys


def fileReader(filename):
	file = open(filename)
	data = file.readlines()
	task_list = []
	cnt = 1
	for line in data:
		tmp = line.split()
		task_list.append(task.Task(tmp[0],tmp[1],tmp[2],tmp[3],cnt))
		cnt ++
	return task_list

if __name__ == "__main__":
	file_name = sys.argv[1]
	task_list = fileReader(file_name)
	s = scheduler.Scheduler(task_list)
	s.createJobsSet()
	print(s.canBegin(0))
	

