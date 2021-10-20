import numpy as np
import matplotlib.pyplot as plt
import scheduler 

class VizualizeScheduling:

	def __init__(self,scheduler):
		self.scheduler = scheduler
		self.tasks_name = []
		self.names_positions = []

	'''
	It generates the name of the task, e.g "Task 1". 
	'''
	def generateTasksName(self):
		position = 0.5
		for index in range(len(self.scheduler.tasks_list)):
			self.tasks_name.append("Task "+str(index + 1))
			self.names_positions.append(position)
			position += 1

	
	def makeArrow(self,x,y_min,y_max,orientation):
		delta = self.scheduler.computeFeasibilityInterval() // self.scheduler.hyperPeriod()
		if orientation == "up":
			x1, y1 = [x,x+delta*2.5] , [y_max,y_max-0.15]
			x2, y2 = [x-delta*2.5,x] , [y_max-0.15,y_max]
			plt.vlines(x = x, ymin = y_min, ymax = y_max,colors = 'black',linestyles = 'solid')
			plt.plot(x1,y1,x2,y2,color='black')
		elif orientation == "down":
			x1, y1 = [x,x+delta*2.5] , [y_min,y_min + 0.15]
			x2, y2 = [x-delta*2.5,x] , [y_min + 0.15,y_min]
			plt.vlines(x = x, ymin = y_min, ymax = y_max,colors = 'black',linestyles = 'solid')
			plt.plot(x1,y1,x2,y2,color='black')
		




	#Mettre les deadlines manquées et les arrivé et deadline 
	def draw(self):
		self.generateTasksName()
		fig, ax = plt.subplots()
		ax.grid(True)
		ax.set_xlim(0,self.scheduler.computeFeasibilityInterval())
		ax.set_ylim(0,len(self.scheduler.tasks_list))
		ax.set_yticks(self.names_positions)
		ax.set_yticklabels(self.tasks_name)

		all_colors = ['red','blue','green','yellow']

		for index in range(len(self.scheduler.tasks_list)):
			color = all_colors[index % 4]
			ax.broken_barh(self.scheduler.tasks_list[index].schedule_solution, (index, 1), facecolors=color)

		self.makeArrow(370,1,1.5,"down")

		plt.show()

		'''for task in self.scheduler:
			plt.vlines(x = elem[1], ymin = elem[0], ymax = elem[0] + 1,colors = 'red',label = 'vline_multiple - full height')'''


				