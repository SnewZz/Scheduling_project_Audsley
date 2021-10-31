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