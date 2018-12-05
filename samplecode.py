import harkpython.harkbasenode as harkbasenode

class HarkNode(harkbasenode.HarkBaseNode):
	def __init__(self):
		# define the output names and types of your node as tuples here.
		self.outputNames=("OUTPUT",)  # one output terminal named "output"
		self.outputTypes=("prim_float",)
	def calculate(self):
		# write your code here.
		srcs=self.SOURCES
		self.outputValues["OUTPUT"] = 0
		print(">>",srcs)
