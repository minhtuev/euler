from graph_utils import Node

def get_or_create_node(list_nodes, dic_nodes, value):
	if value in dic_nodes:
		return dic_nodes[value]
	else:
		dic_nodes[value] = Node(value)
		list_nodes.append(dic_nodes[value])
		return dic_nodes[value]

def dfs(node, checked, dfs_list):
	print node.value
	for neighbor in node.neighbors:
		if not(neighbor in checked):
			checked[neighbor] = True
			dfs(neighbor, checked, dfs_list)
			dfs_list.append(neighbor)


def main():
	f =  open('p079_keylog.txt', 'r')
	lines = f.readlines()
	lines = [line.strip() for line in lines]
	f.close()

	list_nodes = []
	dic_nodes = {}

	for line in lines:
		node1 = get_or_create_node(list_nodes, dic_nodes, int(line[0]))
		node2 = get_or_create_node(list_nodes, dic_nodes, int(line[1]))
		node3 = get_or_create_node(list_nodes, dic_nodes, int(line[2]))
		node1.add_neighbor(node2)
		node2.add_neighbor(node3)

	checked = {}
	number = []
	for node in list_nodes:
		if not(node in checked):
			checked[node] = True
			dfs_list = []
			dfs(node, checked, dfs_list)
			dfs_list.append(node)
			dfs_list = [node.value for node in dfs_list][::-1]
			number = dfs_list + number

	print number

main()