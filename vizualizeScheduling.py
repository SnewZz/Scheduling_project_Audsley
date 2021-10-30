import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scheduler 

"""
This class represents the graphical tool used to display the result of the scheduling.
"""
class VizualizeScheduling:

	def __init__(self,scheduler):
		"""
		The attribute scheduler is an instance of teh scheduler which has scheduled the tasks.
		The attribute tasks_name is a list of all the name of the tasks.
		The attribute names_positions is a list of all the positions of the tasks in the graphic.
		"""
		self.scheduler = scheduler
		self.tasks_name = []
		self.names_positions = []

	
	def generateTasksName(self):
		'''
		It generates the name of the task, e.g "Task 1". 
		'''
		position = 0.5
		for task in self.scheduler.tasks_list:
			self.tasks_name.append("Task "+str(task.task_number))
			self.names_positions.append(position)
			position += 1
		
 
	def draw(self):
		"""
		This method displays the graphic of the scheduling.
		"""
		self.generateTasksName()
		fig, ax = plt.subplots()
		ax.grid(True)
		interval_end = self.scheduler.computeFeasibilityInterval()
		ax.set_xlim(0,interval_end)
		ax.set_ylim(0,len(self.scheduler.tasks_list))
		ax.set_yticks(self.names_positions)
		ax.set_yticklabels(self.tasks_name)
		plt.xlabel("Time")
		all_colors = ['orange','blue','green','yellow']
		for index in range(len(self.scheduler.tasks_list)):
			color = all_colors[index % 4]
			ax.broken_barh(self.scheduler.tasks_list[index].schedule_solution, (index, 1), facecolors=color)
		y = 0
		for task in self.scheduler.tasks_list:
			offset = task.offset
			while offset < interval_end:
				plt.quiver(offset,y+0.5,0,1,color = 'black',headwidth = 2.5,minshaft = 2.5,pivot = 'tip')
				plt.quiver(offset + task.deadline,y+1,0,-1,color = 'black',headwidth = 2.5,minshaft = 2.5)
				offset = offset + task.period
			y = y + 1
		for task in self.scheduler.tasks_list:
			for miss in task.jobs_deadlines_misses:
				plt.vlines(x = miss[1], ymin = miss[0] - 1, ymax = miss[0],colors = 'red', linestyles ='solid',linewidth = 3)

		plt.show()


		


				