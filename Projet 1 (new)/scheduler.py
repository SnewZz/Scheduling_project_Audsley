import job, task
from math import gcd


class Scheduler:

	def __init__(self,task_list):
		self.task_list = task_list


	'''
	This method checks if one of the jobs in the job list can begin. 
	It starts with the job of the highest priority and ends with the job 
	of the lowest priority. If a job can begin, it returns the task number
	of the corresponding job. If no one can begin, it returns -1.
	'''
	def canBegin(self,time):
		for task in self.task_list:
			if task.current_job.release <= time and task.current_job.comp_req > 0:
				return task.task_number
		return -1

	'''
	At the time t, the method checks if a job misses its deadline. 
	If the job misses its deadline, the method checks if the task corresponding
	to the missed job is soft. If the task is not soft, it returns False. 
	Otherwise, it checks the deadlines of the other jobs and returns True if all the jobs 
	respect their deadlines.     
	'''
	##### Essayer try and catch 
	def verifyDeadlines(self,time):
		for task in self.task_list:
			if task.current_job.deadline <= time and task.current_job.comp_req > 0:
				if not task.soft:
					print("The job of the task " + str(task.task_number) + " misses its deadline")
					return False 
				else:
					task.jobs_deadlines_misses.append((task.task_number,task.current_job.deadline))
		return True 

	'''
	It simulates the executions of a job at a time t. The computationnal requirement 
	of the job is decrease by one. After that, if its computationnal requirement is equal 
	to 0. It means that the job ended and so, the next job of the task to be executed has been modified.
	'''
	def executeTask(self,task_number):
		task = self.task_list[task_number - 1]
		task.current_job.comp_req --
		if task.current_job.comp_req == 0:
			task.new_current_job()

	'''
	It computes the hyperperiod of all the tasks.
	'''
	def hyperPeriod(self):
		hyper_period = self.task_list[0].period
		for index in range(1,len(self.task_list)):
			hyper_period = hyper_period * self.task_list[index].period // math.gcd(hyper_period, self.task_list[index].period)
		return hyper_period

	'''
	It computes the max offset. 
	'''
	def getMaxOffset(self):
		max_offset = self.task_list[0].offset
		for index in range(1,len(self.task_list)):
			if (self.task_list[index].offset > max_offset):
				max_offset = self.task_list[index].offset
		return max_offset

	'''
	It computes the upper bound of the feasibility interval.
	'''		
	def computeFeasibilityInterval(self):
		return getMaxOffset() + 2 * hyperPeriod()


	'''
	It starts the scheduler. 
	'''
	def startScheduler(self):
		time = 0
		job_duration = 0
		job_start = 0 
		task_number = 1
		feas_int = computeFeasibilityInterval()
		while time <= feas_int and verifyDeadlines(time):
			task_to_execute = canBegin(time)
			if task_to_execute != -1:
				if task_to_execute != task_number:
					self.task_list[task_number].schedule_solution.append((job_start,job_duration))
					job_duration = 1
					job_start = time
				else:
					job_duration ++
				task_number = task_to_execute
				executeTask(task_number)
			time ++
		self.task_list[task_number].schedule_solution.append((job_start,job_duration))
		return not time < feas_int










	#Penser quand on a fini de scheduler à vider la liste soft_task et job_set

