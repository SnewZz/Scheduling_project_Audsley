import job

"""
This class represents a task. 
"""
class Task:

	def __init__(self,offset,wcet,deadline,period,task_number):
		"""
		The offset is the offset of the task.
		The wcet is the worst case execution time of the task.
		The deadline is the deadline of the task.
		The period is the period of the task.
		The task_number is the number of the task.
		The current_job is the job which is executed at the current time.
		The attribute soft allows to indicate if the task is soft or not.
		The attribute jobs_deadlines_misses allows to keep a track of all the deadline misses of the jobs. 
		The attribute schedule_solution is the solution of the scheduling for this task.  
		"""
		self.offset = int(offset)
		self.wcet = int(wcet)
		self.deadline = int(deadline)
		self.period = int(period)
		self.task_number = int(task_number)
		self.current_job = job.Job(offset,wcet,deadline)
		self.soft = False
		self.jobs_deadlines_misses = [] 
		self.schedule_solution = []


	def new_current_job(self):
		'''
		Create the following job of the task (because the previous job of the task has ended).
		'''
		new_offset = self.current_job.release + self.period
		new_deadline = new_offset + self.deadline
		new_cmp_req = self.wcet
		self.current_job = job.Job(new_offset,new_cmp_req,new_deadline)


	def setSoftTask(self):
		'''
		It defines this task as a soft task.
		'''
		self.soft = True 


	def setHardTask(self):
		'''
		It defines this task as a hard task.
		'''
		self.soft = False


	def reinitializeScheduleSolution(self):
		'''
		It reinitializes the table which contains the solution of the scheduling for the task.
		'''
		self.schedule_solution = []