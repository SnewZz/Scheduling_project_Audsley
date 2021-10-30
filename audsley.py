import task, scheduler 

class Audsley:

    def __init__(self, tasks_list):
        self.scheduler = scheduler.Scheduler(tasks_list)
        self.tasks_list = tasks_list
        self.result_list = []

    def findFeasibleFTPAssignment(self):
        output_file = open("audsley.txt", "w")
        if(self.audsley()):
            cnt = 1
            print (self.result_list)
            for task in self.result_list:
                print(" Task "+str(task.task_number) + " becomes Task " + str(cnt)) #A voir si on laisse 
                output_file.write(str(task))
                cnt += 1
            output_file.close()
        else:
            print("No Feasible FTP Assignment")
            output_file.write("No Feasible FTP Assignment")
            output_file.close()
    
    def audsley(self):    
        if(len(self.tasks_list) == 1):
            s = scheduler.Scheduler(self.tasks_list)
            self.result_list.insert(0, self.tasks_list[0])
            return s.startScheduler()
        if(not self.findLowestPriorityViable()):
            return False
        else:
            return self.audsley()
    
    def findLowestPriorityViable(self):
        for i, hard_task in enumerate(self.tasks_list): #loop to try to find the LPV which is an hard task
            tmplist = []
            for j, soft_task in enumerate(self.tasks_list):
                if not i is j :
                    soft_task.setSoftTask()
                    tmplist.insert(0, soft_task)
                else : 
                    hard_task.setHardTask()
            tmplist.append(hard_task)
            s = scheduler.Scheduler(tmplist)

            if s.startScheduler():
                self.result_list.insert(0,  hard_task)
                del self.tasks_list[i] #remove the new lowest priority 
                self.__reinitializeTasksList()
                return True 
            self.__reinitializeTasksList()
        self.result_list = []
        return False
	
    def __reinitializeTasksList(self):
        """
        This method set all the tasks from the tasks_list to hard and reinitialize their current_job to the first one.
        """
        for task in self.tasks_list:
                task.setHardTask()
                task.current_job = task.first_job()