import job, task
from math import gcd

"""
This class represents a scheduler.
"""
class Scheduler:

	def __init__(self,tasks_list):
		"""
		The attribute tasks_list is the set of all the tasks to schedule.
		"""
		self.tasks_list = tasks_list


	def canBegin(self,time):
		"""
		This method checks if one of the tasks can execute a job. 
		It starts with the task of the highest priority and ends with the task 
		of the lowest priority. If a task can begin a job, it returns the task number
		of the corresponding job. If no one can begin, it returns -1.
		"""
		for task in self.tasks_list:
			if task.current_job.release <= time and task.current_job.comp_req > 0:
				return task.task_number
		return -1

	def getTaskIndex(self,task_number):
		index = 0
		for task in self.tasks_list:
			if task.task_number == task_number:
				return index
			index += 1
		return index

	
	def verifyDeadlines(self,time):
		"""
		At the time t, the method checks if a job misses its deadline. 
		If the job misses its deadline, the method checks if the task corresponding
		to the missed job is soft. If the task is not soft, it returns False. 
		Otherwise, it checks the deadlines of the other jobs and returns True if all the jobs 
		respect their deadlines.     
		"""
		for task in self.tasks_list:
			if task.current_job.deadline <= time and task.current_job.comp_req > 0:
				task.jobs_deadlines_misses.append((task.task_number,task.current_job.deadline))
				if not task.soft:
					print("The job of the task " + str(task.task_number) + " misses its deadline")
					return False 
		return True 

	
	def executeTask(self,task_number):
		"""
		It simulates the executions of a job at a time t. The computationnal requirement 
		of the job is decrease by one. After that, if its computationnal requirement is equal 
		to 0. It means that the job ended and so, the next job of the task to be executed has been modified.
		"""
		task = self.tasks_list[self.getTaskIndex(task_number)]
		task.current_job.comp_req -= 1
		if task.current_job.comp_req == 0:
			task.new_current_job()

	
	def hyperPeriod(self):
		"""
		It returns the hyperperiod of all the tasks.
		"""
		hyper_period = self.tasks_list[0].period
		for index in range(1,len(self.tasks_list)):
			hyper_period = hyper_period * self.tasks_list[index].period // gcd(hyper_period, self.tasks_list[index].period)
		return hyper_period

	
	def getMaxOffset(self):
		"""
		It returns the max offset. 
		"""
		max_offset = self.tasks_list[0].offset
		for index in range(1,len(self.tasks_list)):
			if (self.tasks_list[index].offset > max_offset):
				max_offset = self.tasks_list[index].offset
		return max_offset

			
	def computeFeasibilityInterval(self):
		"""
		It returns the upper bound of the feasibility interval.
		"""
		return self.getMaxOffset() + 2 * self.hyperPeriod()


	def startScheduler(self):
		"""
		It starts the scheduler. It returns true if the task set is schedulable and false otherwise. 
		For more informations about this algorithm, see section 4 in the report.
		"""
		time = 0
		job_duration = 0
		job_start = 0 
		task_number = self.tasks_list[0].task_number
		feas_int = self.computeFeasibilityInterval()
		while time <= feas_int and self.verifyDeadlines(time):
			task_to_execute = self.canBegin(time)
			if task_to_execute != -1:
				if task_to_execute != task_number:
					if task_number != -1:
						self.tasks_list[self.getTaskIndex(task_number)].schedule_solution.append((job_start,job_duration))
						job_duration = 1
						job_start = time
					else:
						job_start = time
						job_duration = 1
				elif task_number == task_to_execute:
					job_duration += 1
				self.executeTask(task_to_execute)
			elif task_number == -1 and task_to_execute == -1:
				pass
			else:
				self.tasks_list[self.getTaskIndex(task_number)].schedule_solution.append((job_start,job_duration))
				job_duration = 0
				job_start = 0 
			task_number = task_to_execute
			time += 1
		if task_number != -1 and time < feas_int:
			self.tasks_list[self.getTaskIndex(task_number)].schedule_solution.append((job_start,job_duration))
		return not time < feas_int




