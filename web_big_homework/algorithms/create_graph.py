#利用数据生成以networkx.MultiGraph形式存储的图，节点是Node类的对象，边的edge属性是一个side类的对象
import networkx as nx 
import json 
import os
EDGE_SOURCE = "../data/edge_info.txt"
GRAPH_PATH = "../data/graph.gpickle"

class Side:
	def __init__(self, edge):
		self.start_cv = edge['start_cv']
		self.start_char = edge['start_char']
		self.end_cv = edge['end_cv']
		self.end_char = edge['end_char']
		self.year = edge['year']
		self.anime_name = edge['anime_name']
		self.weight = edge['weight']

class Node:
	def __init__(self, name):
		self.name = name

	def save_position(self, pos_list):
		self.x = pos_list[0]
		self.y = pos_list[1]

def create_edge_list(source):
	with open(source, encoding='utf-8') as f:
		database = json.load(f)
		edge_list = [Side(edge) for edge in database]
		return edge_list

def create_node_dictionary(edge_list):
	node_dictionary = {}
	for edge in edge_list:
		if edge.start_cv not in node_dictionary:
			node_dictionary[edge.start_cv] = Node(edge.start_cv)
		if edge.end_cv not in node_dictionary:
			node_dictionary[edge.end_cv] = Node(edge.end_cv)
	return node_dictionary

def create_graph(node_dictionary, edge_list):
	g = nx.MultiGraph()
	g.add_nodes_from(node_dictionary.values())
	for edge in edge_list:
		g.add_edge(
			node_dictionary[edge.start_cv], node_dictionary[edge.end_cv],
			edge=edge)
	pos_dic = nx.drawing.layout.spring_layout(g, dim=2, scale=1e3, k=0.3)
	for item in pos_dic:
		item.save_position(pos_dic[item])

	return g 

def save_graph(g):
	if not os.path.exists(GRAPH_PATH):
		nx.write_gpickle(g, GRAPH_PATH)
	else:
		print(GRAPH_PATH, "has already exists")
		still_save = input("still save? y/n")
		if still_save == 'y':
			nx.write_gpickle(g, GRAPH_PATH)
			print("rewrite success")
		else:
			return


def main():
	edge_list = create_edge_list(EDGE_SOURCE)
	node_dictionary = create_node_dictionary(edge_list)
	g = create_graph(node_dictionary, edge_list)
	save_graph(g)
	#print(len(g.edges))
	#print(len(edge_list), len(node_dictionary))