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