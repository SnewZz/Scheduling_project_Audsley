import task, scheduler 

class Audsley:

    def __init__(self, tasks_list):
        self.scheduler = scheduler.Scheduler(tasks_list)
        self.tasks_list = tasks_list
        self.result_list = []

    def findFeasibleFTPAssignment(self):
        output_file = open("audsley.txt", "w")
        if(self.audsley()):
            print(self.result_list)
            for task in self.result_list:
                print(task)
                output_file.write(task)
            output_file.close()
        else:
            print("no Feasible FTP Assignment")
            output_file.write("no Feasible FTP Assignment")
            output_file.close()
    def audsley(self):    
        if(len(self.tasks_list)==1):
            return True
        if(not self.findLowestPriorityViable()):
            return False
        else:
            return self.audsley()

	# if(not findLowestPriorityViable(tasks_list, result_list)):
	# 	return False
	# else:
	# 	return audsley(tasks_list, result_list)

    def findLowestPriorityViable(self):
        for i, taski in enumerate(self.tasks_list):
            tmplist = []
            for j, taskj in enumerate(self.tasks_list):
                if not i is j :
                    taskj.setSoftTask()
                    tmplist.insert(0, taskj)
            tmplist.append(taski)
            s = scheduler.Scheduler(tmplist)
            if s.startScheduler():
                self.result_list.insert(0,tmplist[-1])
                del self.tasks_list[i] #remove the new lowest priority 
                return True 
        self.result_list = []
        return False
	# for task in tasks_list:
	# 	if(True):
	# 		result_list.append(task)
	# 		tasks_list.remove(task)
	# 		return True
	# return False