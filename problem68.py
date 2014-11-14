class Node(object):
	def __init__(self, value = float('inf')):
		self.value = value

	def __add__(self, other):
		return self.value + other

	def __radd__(self, other):
		return self + other

	def is_set(self):
		return self.value != float('inf')

	def reset(self):
		self.value = float('inf')

	def __repr__(self):
		return str(self.value)

class Constraint(object):
	# return true, false or None
	def assert_constraint(self):
		raise Exception("Not implemented.")

class EqualityConstraint(Constraint):
	def __init__(self, nodes, compared_nodes):
		self.nodes = nodes
		self.compared_nodes = compared_nodes
	
	def assert_constraint(self):
		if sum(self.nodes) == float('inf') or sum(self.compared_nodes) == float('inf'):
			return None
		return sum(self.nodes) == sum(self.compared_nodes)

class GreaterThanConstraint(Constraint):
	def __init__(self, node, compared_node):
		self.node = node
		self.compared_node = compared_node

	def assert_constraint(self):
		if self.node.value == float('inf') or self.compared_node.value == float('inf'):
			return None
		return self.node.value > self.compared_node.value

class UniqueConstraint(Constraint):
	def __init__(self, nodes):
		self.nodes = nodes

	def assert_constraint(self):
		L = []
		for node in self.nodes:
			if node.value in L:
				return False
			elif node.value != float('inf'):
				L.append(node.value)
		return True

def check_constraint(constraints):
	for constraint in constraints:
		if constraint.assert_constraint() == False:
			#print constraint.__class__
			#print constraint.nodes
			#print constraint.compared_nodes
			return False
	return True

def validate_constraint(constraints):
	for constraint in constraints:
		if constraint.assert_constraint() != True:
			return False
	return True

def compute(L, nodes, values, constraints, index = 0, max_number = -1):
	#print L
	if index == len(L):
		order = ['a', 'b', 'c', 'd', 'c', 'f', 'e', 'f', 'g', 'h', 'g', 'j', 'i', 'j', 'b']
		S = [str(nodes[ch]) for ch in order]
		S = ''.join(S)
		print S
		if len(S) == 16 and int(S) > max_number:
			print S
			max_number = int(S)
	else:
		for value in values:
			V = values[:]
			V.remove(value)
			L[index].value = value
			if check_constraint(constraints):
				compute(L, nodes, V, constraints, index + 1)
		L[index].reset()

def get_node_list(dic, name_list):
	nodes =[]
	for name in name_list:
		nodes.append(dic[name])
	return nodes

def main():	
	nodes = {}
	L = []
	for node_name in list(map(chr, range(97, 107))): #or list(map(chr, range(ord('a'), ord('z')+1))):
		nodes[node_name] = Node()
		L.append(nodes[node_name])

	abc = get_node_list(nodes, 'abc')
	dcf = get_node_list(nodes, 'dcf')
	efg = get_node_list(nodes, 'efg')
	hgj = get_node_list(nodes, 'hgj')
	ijb = get_node_list(nodes, 'ijb')

	constraints = []
	# constraints.append(UniqueConstraint('abcdefghij'))
	constraints.append(EqualityConstraint(dcf, abc))
	constraints.append(EqualityConstraint(efg, abc))
	constraints.append(EqualityConstraint(hgj, abc))
	constraints.append(EqualityConstraint(ijb, abc))
	constraints.append(GreaterThanConstraint(nodes['d'], nodes['a']))
	constraints.append(GreaterThanConstraint(nodes['e'], nodes['a']))
	constraints.append(GreaterThanConstraint(nodes['h'], nodes['a']))
	constraints.append(GreaterThanConstraint(nodes['i'], nodes['a']))

	compute(L, nodes, range(1, 11), constraints)

main()