import networkx as nx
import matplotlib.pyplot as plt

#nx graphs have their lists of nodes and edges as attributes.

def listlist_to_nx(G):
	nodes, edges = G
	G_nx = nx.DiGraph()
	n = len(nodes)
	for i in range(n):
		for j in edges[i]:
			G_nx.add_edge(nodes[i], nodes[j])
	return G_nx


def draw_nx(G_nx):
	nx.draw_networkx(G_nx, node_size = 50, node_color = 'w', edge_color = 'r')
	#labels = nx.draw_networkx_labels(G_nx,pos=nx.spring_layout(G_nx))
	plt.show()

def draw_and_save_nx(G_nx, path):
	nx.draw(G_nx)
	plt.savefig("{}.png".format(path))
	plt.show()