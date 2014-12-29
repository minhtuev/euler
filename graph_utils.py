class Node(object):
	def __init__(self, value):
		self.value = value
		self.neighbors = []

	def add_neighbor(self, node):
		if not(node in self.neighbors):
			self.neighbors.append(node)