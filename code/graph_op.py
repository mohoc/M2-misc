import tryalgo

def find_eps_id(G):
	nodes, _ = G
	n = len(nodes)
	eps_id = -1
	found_eps = False
	for i in range(n):
		if nodes[i] == "":
			if found_eps:
				raise IndexError
			else:
				eps_id = i
				found_eps = True
	assert found_eps
	return eps_id

def remove_node_id(G, i):
	nodes, edges = G
	new_nodes = [u for u in nodes]
	new_edges = []
	for l in edges:
		new_edges.append([i for i in l])
	n = len(nodes)
	if i != n-1:
		new_nodes[i] = new_nodes[-1]
		new_edges[i] = [j for j in new_edges[-1]]
		for list_id in range(n):
			new_list = []
			for j in new_edges[list_id]:
				if j == n-1:
					new_list.append(i)
				elif j != i:
					new_list.append(j)
			new_edges[list_id] = new_list
	del new_nodes[-1]
	del new_edges[-1]
	#print(i, new_edges)
	return new_nodes, new_edges

def remove_node_id_list(G, l):
	l.sort()
	n = len(l)
	for i in range(n-1, -1, -1):
		G = remove_node_id(G, l[i])
	return G

def remove_node_id_list_2(G, l):
	nodes, _ = G
	n = len(nodes)
	is_a_removed_id = [False for _ in range(n)]
	for i in l:
		is_a_removed_id[i] = True
	return 0 #TODO
	


def find_cycle_aux(edges, i, current_path):
	if current_path[i]:
		#print(i)
		return True
	else:
		new_current_path = [b for b in current_path]
		new_current_path[i] = True
		#print(edges[i])
		for j in edges[i]:
			found_cycle_j = find_cycle_aux(edges, j, new_current_path)
			if found_cycle_j:
				return True
		return False

def find_cycle(G):
	nodes, edges = G
	n = len(nodes)
	for i in range(n):
		#print(i)
		current_path = [False for _ in range(n)]
		found_cycle = find_cycle_aux(edges, i, current_path)
		if found_cycle:
			return True
	return False

def dir_to_undir(G):
	"""makes a directed "adjacency list" graph undirected"""
	nodes, edges = G
	#copy edges
	new_edges = []
	for l in edges:
		new_edges.append([i for i in l])
	#add the symmetric edges if needed
	n = len(nodes)
	for i in range(n):
		for j in edges[i]:
			if not i in edges[j]:
				new_edges[j].append(i)
	return nodes, new_edges

def strongly_connected_components(G):
	return tryalgo.strongly_connected_components.tarjan(G[1])

def is_strongly_connected(G):
	scc = strongly_connected_components(G)
	return len(scc) <= 1

def connected_components(G):
	G_undir = dir_to_undir(G)
	return tryalgo.strongly_connected_components.tarjan(G_undir[1])

def is_connected(G):
	G_undir = dir_to_undir(G)
	return is_strongly_connected(G_undir)

def only_keep_components_with_cycles(G):
	nodes, edges = G
	cc_list = connected_components(G)
	n = len(nodes)
	to_be_removed = [False for _ in range(n)]
	for cc in cc_list:
		edges_tmp = []
		for l in edges:
			edges_tmp.append([i for i in l])
		is_in_cc = [False for _ in range(n)]
		for i in cc:
			is_in_cc[i] = True
		for j in range(n):
			if not is_in_cc[j]:
				edges_tmp[j] = []
		#print(cc)
		#print(edges_tmp)
		#if tryalgo.dfs.find_cycle(edges_tmp) == None:
		if not find_cycle((nodes, edges_tmp)):
			for i in cc:
				to_be_removed[i] = True
	#print(to_be_removed)
	for i in range(n-1, -1, -1):
		if to_be_removed[i]:
			G = remove_node_id(G, i)
	return G

def keep_nodes_of_paths_of_length_at_least_and_from(G, m, start):
	nodes, edges = G
	n = len(nodes)
	current_nodes = set([start])
	step_count = 0
	while step_count < m:
		new_current_nodes = set()
		for node in current_nodes:
			for neighbor in edges[node]:
				new_current_nodes.add(neighbor)
		current_nodes = new_current_nodes
		step_count += 1
	if current_nodes == set():
		return nodes, [[] for _ in range(n)]
	else:
		visited = [False for _ in range(n)]
		for node in current_nodes:
			visited[node] = True
		while current_nodes != set():
			new_current_nodes = set()
			for node in current_nodes:
				for neighbor in edges[node]:
					if not visited[neighbor]:
						new_current_nodes.add(neighbor)
						visited[neighbor] = True
			current_nodes = new_current_nodes
		to_be_removed = []
		for i in range(n):
			if not visited[i]:
				to_be_removed.append(i)
		return remove_node_id_list(G, to_be_removed)

def exists_path_of_length(G, n):
	nodes, edges = G
	for start in nodes:
		step_count = 0
		current_nodes = set([start])
		while step_count < n:
			new_current_nodes = set()
			for node in current_nodes:
				for neighbor in edges[node]:
					new_current_nodes.add(neighbor)
			current_nodes = new_current_nodes
			step_count += 1
		if current_nodes != set():
			return True
	return False

def remove_components_with_no_path_of_length_at_least(G, k):
	_, edges = G
	ccs = connected_components(G)
	nodes_to_remove = []
	for cc in ccs:
		if not exists_path_of_length((cc, edges), k):
			for node in cc:
				nodes_to_remove.append(node)
	G = remove_node_id_list(G, nodes_to_remove)
	return G



"""
#not working code
def find_cycle_aux(edges, i, already_visited, current_path, newly_visited):
	if already_visited[i]:
		return False,  []
	if current_path[i]:
		return True, []
	else:
		current_path[i] = True
		for j in edges[i]:
			found_cycle_j, newly_visited_j = find_cycle_aux(edges, j, already_visited, current_path, newly_visited)
			if found_cycle_j:
				return True, newly_visited_j + [i]
			else:
				newly_visited += newly_visited_j
		newly_visited.append(i)
		return False, newly_visited

def find_cycle(G):
	nodes, edges = G
	n = len(nodes)
	already_visited = [False for _ in range(n)]
	for i in range(n):
		current_path = [False for _ in range(n)]
		found_cycle, newly_visited = find_cycle_aux(edges, i, already_visited, current_path, [])
		if found_cycle:
			print("youpi", newly_visited)
			return True
		else:
			for u in newly_visited:
				already_visited[u] = True
	return False
"""