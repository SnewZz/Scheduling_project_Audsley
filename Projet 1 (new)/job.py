import task

class Job:

	def __init__(self,release,comp_req,deadline):
		self.release = int(release)
		self.comp_req = int(comp_req)
		self.deadline = int(deadline)

	def __str__(self):
		return "(" + str(self.release) + " , " + str(self.comp_req) + " , " + str(self.deadline) +")"
