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
            print(self.tasks_list[0])
            self.result_list.insert(0, self.tasks_list[0])
            return s.startScheduler()
        if(not self.findLowestPriorityViable()):
            return False
        else:
            return self.audsley()

	# def findLowestPriorityViable(self):
    #     print("1")
    #     for task in self.result_list:
    #         print(str(task))
    #     print("--------------")
    #     for i, taski in enumerate(self.tasks_list):
    #         print("taski : ", taski)
    #         tmplist = []
    #         for j, taskj in enumerate(self.tasks_list):
    #             print("taskj : ", taskj)
    #             print("bug : ", not i is j)
    #             if not i is j :
    #                 taskj.setSoftTask()
    #                 print("insert soft : ", taskj)
    #                 tmplist.insert(0, taskj)
    #             else : 
    #                 taskj.setHardTask()
    #                 print("hard : ", taskj)
    #         tmplist.append(taski)
    #         s = scheduler.Scheduler(tmplist)
    #         if s.startScheduler():
    #             print("append")
    #             for tmp in tmplist:
    #                 print(tmp)
    #             self.result_list.insert(0, tmplist[-1])
    #             del self.tasks_list[i] #remove the new lowest priority 
    #             return True 
    #     self.result_list = []
    #     return False
    
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

            # for task in s.tasks_list:
            #     print(task)
            # print("###############")

            if s.startScheduler():
                self.result_list.insert(0,  hard_task)
                del self.tasks_list[i] #remove the new lowest priority 
                self.reinitializeTasksList()
                return True 
            self.reinitializeTasksList()
        self.result_list = []
        return False
	
    def reinitializeTasksList(self):
        """
        This method set all the tasks from the tasks_list to hard and reinitialize their current_job to the first one.
        """
        for task in self.tasks_list:
                task.setHardTask()
                task.current_job = task.first_job()