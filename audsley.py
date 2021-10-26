import task, scheduler 

class Audsley:

    def __init__(self, tasks_list):
        self.scheduler = scheduler.Scheduler(tasks_list)
        self.tasks_list = tasks_list
        self.result_list = len(self.tasks_list) * [0]

    def findFeasibleFTPAssignment(self):
        output_file = open("audsley.txt", "w")
        if(self.audsley(len(self.tasks_list) - 1)):
            for task in self.result_list:
                output_file.write(str(task))
            output_file.close()
        else:
            print("no Feasible FTP Assignment")
            output_file.write("no Feasible FTP Assignment")
            output_file.close()
    
    def audsley(self,index):    
        if(len(self.tasks_list) == 1):
            self.result_list.pop(index)
            self.result_list.insert(0,self.tasks_list[0])
            return True
        if(not self.findLowestPriorityViable(index)):
            return False
        else:
            return self.audsley(index - 1)

	# if(not findLowestPriorityViable(tasks_list, result_list)):
	# 	return False
	# else:
	# 	return audsley(tasks_list, result_list)

    def findLowestPriorityViable(self,index):
        for i, taski in enumerate(self.tasks_list):
            tmplist = []
            for j, taskj in enumerate(self.tasks_list):
                if not i is j :
                    taskj.setSoftTask()
                    tmplist.insert(0, taskj)
            tmplist.append(taski)
            #print(tmplist[len(self.tasks_list) - 1])
            #print(tmplist[0],tmplist[1])
            #print(index)
            s = scheduler.Scheduler(tmplist)
            if s.startScheduler():
                print("==>" + str(tmplist[-1]) + " : " + str(index))
                self.result_list.pop(index)
                self.result_list.insert(index,tmplist[-1])
                del self.tasks_list[i] #remove the new lowest priority 
                for task in self.tasks_list:
                    task.setHardTask()
                    task.current_job = task.first_job()
                return True 
            for task in self.tasks_list:
                task.setHardTask()
                task.current_job = task.first_job()
        self.result_list = []
        return False
	