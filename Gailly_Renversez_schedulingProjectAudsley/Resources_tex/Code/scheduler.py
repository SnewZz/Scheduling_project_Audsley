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