import task, scheduler 

"""
This class represents an implementation of the Audsley's algorithm
"""

class Audsley:

    def __init__(self, tasks_list):
        """
        The attribute scheduler is the scheduler used for the audsley's algorithm
        The attribute tasks_list is the set of all the tasks to schedule.
        The attribute result_list is the list where the solution of the audsley's algorithm will be store
        """
        self.scheduler = scheduler.Scheduler(tasks_list)
        self.tasks_list = tasks_list
        self.result_list = []

    def findFeasibleFTPAssignment(self):
        """
        This method call the audsley method and write the priority assignment in a file audsley.txt. If the audsley method did not find a 
        solution "No Feasible FTP Assignment" is write in the console.
        """
        print("#################################################")
        if(self.audsley()):
            output_file = open("audsley.txt", "w")
            cnt = 1
            print("###### You can ignore the message(s) above ######")
            print(" ==> A feasible FTP assignement has been found !")
            for task in self.result_list:
                print(" Task "+str(task.task_number) + " becomes Task " + str(cnt))
                output_file.write(str(task))
                cnt += 1
            output_file.close()
        else:
            print("###### You can ignore the message(s) above ######")
            print(" ==> No Feasible FTP Assignment !")
    
    def audsley(self):
        """
        This method is an implementation of the audsley's algorithm. 
        This method will recursively look for a lowest priority-viable until the list's length is equals to 1. 
        If it does not find an LPV the method returns False and this means that the task set is not schedulable. 
        If the size of tasks_list is 1, there will only be a check on the last task to verify that it is schedulable
        """    
        if(len(self.tasks_list) == 1):
            s = scheduler.Scheduler(self.tasks_list)
            self.result_list.insert(0, self.tasks_list[0])
            return s.startScheduler()
        if(not self.findLowestPriorityViable()):
            return False
        else:
            return self.audsley()
    
    def findLowestPriorityViable(self):
        """
        This method try to find the lowest priority-viable in the tasks_list. If it finds one, it removes this task from 
        the tasks_list and adds it to the beginning of the result_list.
        """
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