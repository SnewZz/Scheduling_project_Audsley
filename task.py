import job

class Task:

    def __init__(self, wcet, deadline, period, offset = 0):
        self.offset = offset
        self.wcet = wcet
        self.deadline = deadline
        self.period = period
        #self.jobs = list<job>()