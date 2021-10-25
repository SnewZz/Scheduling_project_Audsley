"""
This class represents a job.
"""

class Job:

	def __init__(self,release,comp_req,deadline):
		"""
		realease is the release time of the job.
		comp_req is the computationnal requirement to achieve the execution of the job.
		deadline is the deadline of the job. 
		"""
		self.release = int(release)
		self.comp_req = int(comp_req)
		self.deadline = int(deadline)

	def __str__(self):
		return "(" + str(self.release) + " , " + str(self.comp_req) + " , " + str(self.deadline) +")"
