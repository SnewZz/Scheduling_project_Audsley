import job

class Task:

	def __init__(self,offset,wcet,deadline,period,task_number):
		self.offset = int(offset)
		self.wcet = int(wcet)
		self.deadline = int(deadline)
		self.period = int(period)
		self.task_number = int(task_number)
		self.current_job = job.Job(offset,wcet,deadline)
		self.soft = False
		self.jobs_deadlines_misses = [] 
		self.schedule_solution = []

	'''
	Create the following job of the task. 
	'''
	def new_current_job(self):
		new_offset = self.current_job.release + self.period
		new_deadline = new_offset + self.deadline
		new_cmp_req = self.wcet
		self.current_job = job.Job(new_offset,new_cmp_req,new_deadline)

	'''
	It defines this task as a soft task.
	'''
	def setSoftTask(self):
		self.soft = True 

	'''
	It defines this task as a hard task.
	'''
	def setHardTask(self):
		self.soft = False

	'''
	It reinitializes the table which contains the solution of the scheduling for the task.
	'''
	def reinitializeScheduleSolution(self):
		self.schedule_solution = []

	def __str__(self):
		return "task : " + str(self.task_number)