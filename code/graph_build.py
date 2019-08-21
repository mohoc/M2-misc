import graph_op, list_op
import ahocorasick_op as ac_op
import itertools

#Graphs are defined as a tuple (nodes, edges) with "nodes" a list of labels and "edges" a list of lists of the neighbors' identifier.

"""
def all_words_aux(A, n, tmp):
	if n == 0:
		return tmp
	else:
		new_tmp = []
		for a in A:
			for u in tmp:
				new_tmp.append(a+u)
		return all_words_aux(A, n-1, new_tmp)

def all_words(A, n):
	return all_words_aux(A, n, [""])
"""

def deBruijn(A, F):
	AC_F = ac_op.build_auto(F)
	m = list_op.max_length(F)
	#find all allowed motifs of length m(F) and give them IDs
	motifs = []
	motifs_id = {}
	current_id = 0
	letters = "".join(A)
	for li in itertools.product(letters, repeat=m):
		u = "".join(li)
		if not ac_op.is_substring(AC_F, u):
			motifs.append(u)
			motifs_id[u] = current_id
			current_id += 1
	#compute the adjacency list of every allowed word
	edges = []
	for u in motifs:
		neighbors = []
		for a in A:
			v = u[1:] + a
			if not ac_op.is_substring(AC_F, v):
				neighbors.append(motifs_id[v])
		edges.append(neighbors)
	return motifs, edges

def deBruijn_n(A, F, n):
	G = deBruijn(A, F)
	m = list_op.max_length(F)
	return graph_op.remove_components_with_no_path_of_length_at_least(G, n - m)

def deBruijn_inf(A, F):
	G = deBruijn(A, F)
	#print(G)
	G = graph_op.only_keep_components_with_cycles(G)
	#print(G)
	return G

def hammmingGraph(A, F, n):
	AC_F = ac_op.build_auto(F)
	#find all allowed motifs of length n and give them IDs
	words = []
	words_id = {}
	current_id = 0
	letters = "".join(A)
	for li in itertools.product(letters, repeat=n):
		u = "".join(li)
		if not ac_op.is_substring(AC_F, u):
			words.append(u)
			words_id[u] = current_id
			current_id += 1
	#compute the adjacency list of every allowed word
	edges = []
	for u in words:
		neighbors = []
		for j in range(n):
			for a in A:
				if a != u[j]:
					v = u[:j] + a + u[j+1:]
					if not ac_op.is_substring(AC_F, v):
						neighbors.append(words_id[v])
		edges.append(neighbors + [words_id[u]])
	return words, edges

def acGraph(A, F):
	AC_F = ac_op.build_auto(F)
	auto_nodes, auto_edges, auto_f_links = AC_F.dump()
	#print(auto_nodes)
	#print(auto_edges)
	#print(auto_f_links)
	nodes = []
	nodes_index = {}
	count = 0
	for (node_id, is_end_motif) in auto_nodes:
		if is_end_motif != 1:
			nodes.append(node_id)
			nodes_index[node_id] = count
			count += 1
	"""
	print("")
	print(nodes)
	print(nodes_index)
	"""
	edges = [[] for _ in range(count)]
	f_links = [-1 for _ in range(count)]
	inner_labels = ["" for _ in range(count)]
	is_eps = [True for _ in range(count)]
	for (node_id, label_char, child_node_id) in auto_edges:
		#print(nodes_index[node_id])
		edge_letter = str(label_char)[2]
		try:
			edges[nodes_index[node_id]].append(nodes_index[child_node_id])
			inner_labels[nodes_index[child_node_id]] = edge_letter
			is_eps[nodes_index[child_node_id]] = False
		except KeyError:
			pass
	for (node_id, fail_node_id) in auto_f_links:
		try:
			f_links[nodes_index[node_id]] = nodes_index[fail_node_id]
			#edges[nodes_index[node_id]].append(nodes_index[fail_node_id])
			#print(nodes_index[node_id], nodes_index[fail_node_id])
		except KeyError:
			pass
	eps = -1
	found_eps = False
	for i in range(count):
		if is_eps[i]:
			if found_eps:
				raise IndexError
			else:
				eps = i
				found_eps = True
	assert found_eps
	#print(eps)
	labels = ["" for _ in range(count)]
	found_labels = [False for _ in range(count)]
	found_labels[eps] = True
	nodes_to_consider = [eps]
	while nodes_to_consider != []:
		new_nodes_to_consider = []
		for node_index in nodes_to_consider:
			for child_node_index in edges[node_index]:
				if not found_labels[child_node_index]:
					labels[child_node_index] = labels[node_index] + inner_labels[child_node_index]
					found_labels[child_node_index] = True
					new_nodes_to_consider.append(child_node_index)
		nodes_to_consider = new_nodes_to_consider
	for i in range(count):
		for a in A:
			if not ac_op.is_substring(AC_F, labels[i] + a):
				current_node_index = i
				found_corresponding_child = False
				while not found_corresponding_child:
					for neighbor in edges[current_node_index]:
						if inner_labels[neighbor] == a:
							edges[i].append(neighbor)
							found_corresponding_child = True
							break
					if current_node_index == eps and (not found_corresponding_child):
						edges[i].append(eps)
						found_corresponding_child = True
					else:
						current_node_index = f_links[current_node_index]
	for i in range(count):
		edges[i] = list_op.remove_duplicates(edges[i])
	#print(labels)
	#print(edges)		
	return labels, edges

def acGraph_prime(A, F):
	G_AC_F = acGraph(A, F)
	m = list_op.max_length(F)
	return graph_op.keep_nodes_of_paths_of_length_at_least_and_from(G_AC_F, m, graph_op.find_eps_id(G_AC_F))

def acGraph_n(A, F, n):
	G = acGraph(A, F)
	return graph_op.keep_nodes_of_paths_of_length_at_least_and_from(G, n, graph_op.find_eps_id(G))

def acGraph_prime_n(A, F, n):
	G = acGraph_prime(A, F)
	m = list_op.max_length(F)
	return graph_op.remove_components_with_no_path_of_length_at_least(G, n - m)

def acGraph_prime_inf(A, F):
	return graph_op.only_keep_components_with_cycles(acGraph_prime(A, F))


"""
#old code
def acGraph(F):
	AC_F = ac_op.build_auto(F)
	nodes, edges, f_links = AC_F.dump()
	print(nodes)
	print(edges)
	print(f_links)
	new_nodes = []
	nodes_index = {}
	count = 0
	for (node_id, is_end_motif) in nodes:
		if is_end_motif != 1:
			new_nodes.append(node_id)
			nodes_index[node_id] = count
			count += 1
	print("")
	print(new_nodes)
	print(nodes_index)
	new_edges = [[] for _ in range(count)]
	for (node_id, _, child_node_id) in edges:
		#print(nodes_index[node_id])
		try:
			new_edges[nodes_index[node_id]].append(nodes_index[child_node_id])
		except KeyError:
			pass
	for (node_id, fail_node_id) in f_links:
		try:
			new_edges[nodes_index[node_id]].append(nodes_index[fail_node_id])
		except KeyError:
			pass
	return new_nodes, new_edges
"""









