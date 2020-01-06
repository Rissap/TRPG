import numpy

class GlobalMap():
	def __init__(self):
		self.map = numpy.nan_to_num(numpy.genfromtxt('database/map.txt', delimiter=',')).astype(int)


MAP = GlobalMap()