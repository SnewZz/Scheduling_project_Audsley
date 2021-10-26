import task, scheduler 

class Audsley:

    def __init__(self, tasks_list):
        self.scheduler = scheduler.Scheduler(tasks_list)
        self.tasks_list = tasks_list
        self.result_list = []

    def findFeasibleFTPAssignment(self):
        output_file = open("audsley.txt", "w")
        if(self.audsley()):
            for task in self.result_list:
                print(task)
                output_file.write(str(task))
            output_file.close()
        else:
            print("no Feasible FTP Assignment")
            output_file.write("no Feasible FTP Assignment")
            output_file.close()
    def audsley(self):    
        if(len(self.tasks_list)==1):
            print("base : ", self.tasks_list[0])
            self.result_list.append(self.tasks_list[0])
            return True
        if(not self.findLowestPriorityViable()):
            return False
        else:
            return self.audsley()

    def findLowestPriorityViable(self):
        print("1")
        for task in self.result_list:
            print(str(task))
        print("--------------")
        for i, taski in enumerate(self.tasks_list):
            print("taski : ", taski)
            tmplist = []
            for j, taskj in enumerate(self.tasks_list):
                print("taskj : ", taskj)
                if not i is j :
                    taskj.setSoftTask()
                    tmplist.insert(0, taskj)
                else : 
                    taskj.setHardTask()
            tmplist.append(taski)
            s = scheduler.Scheduler(tmplist)
            if s.startScheduler():
                print("append")
                for tmp in tmplist:
                    print(tmp," soft:", tmp.soft)
                self.result_list.append(tmplist[-1])
                del self.tasks_list[i] #remove the new lowest priority 
                return True 
        self.result_list = []
        return False