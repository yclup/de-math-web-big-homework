import networkx as nx 
from create_graph import Node, Side
import math 
GRAPH_PATH = "../data/graph.gpickle"

def convert_side_to_info_dic(attr_dic):
	side = attr_dic['edge']
	return {'start_cv': side.start_cv, 
			'end_cv': side.end_cv,
			'start_char': side.start_char,
			'end_char': side.end_char, 
			'anime_name': side.anime_name, 
			'year': side.year,
			'weight': side.weight}

class DataOfNode:
	def __init__(self, name, pos, radius, hue):
		self.name = name 
		self.pos_x = pos[0] 
		self.pos_y = pos[1]
		self.r = radius
		self.hue = hue

class CVGraph:
	def __init__(self, graph_path=GRAPH_PATH):
		self.graph_path = graph_path
		self.graph = self.retrive_and_create_graph(self.graph_path)
		self.create_node_dictionary()

	def return_number_of_nodes(self):
		return len(self.graph.nodes)

	def create_pos_dictionary(self):
		self.pos_dictionary = nx.drawing.layout.spring_layout(self.graph, k=0.3, dim=2, scale=1e3)

	def create_node_dictionary(self):
		self.node_dictionary = {}
		for node in self.graph.nodes:
			self.node_dictionary[node.name] = node 

	def return_node_object_via_name(self, node_name: str):
		return self.node_dictionary[node_name]

	def return_position_of_node_as_tuple(self, node_name: str):
		return tuple(self.pos_dictionary[self.return_node_object_via_name(node_name)] + 1000)

	def return_hue_of_node(self, node_name: str):
		return int((self.return_side_num_of_a_node_by_name(node_name) *360 / 2000) % 360)

	def return_node_names_as_list(self): 
		return [node.name for node in self.graph.nodes]

	def return_radius_of_node(self, node_name: str):
		square = self.return_side_num_of_a_node_by_name(node_name)
		radius = math.log(square)
		return radius

	def return_side_num_of_a_node_by_name(self, node_name: str):
		return len(nx.edges(self.graph, nbunch=self.return_node_object_via_name(node_name)))

	def return_sorted_nodes_as_list(self, reverse=True):
		return sorted(list(self.graph.nodes), 
			key=lambda node: self.return_side_num_of_a_node_by_name(node.name), 
			reverse=reverse)

	def return_data_to_draw(self):
		self.create_pos_dictionary()
		data = []
		for node in self.graph.nodes:
			data.append(DataOfNode(node.name, self.return_position_of_node_as_tuple(node.name), 
				self.return_radius_of_node(node.name), self.return_hue_of_node(node.name)))
		return data	

	def retrive_and_create_graph(self, graph_path):
		return nx.read_gpickle(graph_path)

	def test(self):
		print(len(self.graph.edges))
		print(self.return_line_info_between_two_nodes("中村悠一", "诹访部顺一"))

	def return_line_info_list_of_a_node(self, node_name: str):
		line_info_list = []
		node_object = self.return_node_object_via_name(node_name)
		self_x , self_y = self.return_position_of_node_as_tuple(node_name)
		neighbor_list = nx.neighbors(self.graph, node_object)
		for neighbor in neighbor_list:
			neighbor_x, neighbor_y = self.return_position_of_node_as_tuple(neighbor.name)
			line_info_list.append({'x1': self_x, 'y1': self_y, 'x2': neighbor_x, 'y2': neighbor_y,
										'start': node_name, 'end': neighbor.name})
		return line_info_list

	def return_line_info_between_two_nodes(self, node_name_1, node_name_2):
		if not hasattr(self, "pos_dictionary"):
			self.create_pos_dictionary()
		node_1 = self.return_node_object_via_name(node_name_1)
		node_2 = self.return_node_object_via_name(node_name_2)
		return list(map(lambda attr_dic: convert_side_to_info_dic(attr_dic), 
			self.graph.get_edge_data(node_1, node_2).values()))



class CVSubGraph(CVGraph): #  return "num_of_nodes" nodes with most sides
	def __init__(self, cvgraph, num_of_nodes):
		sorted_nodes = cvgraph.return_sorted_nodes_as_list()
		self.graph = cvgraph.graph.subgraph(sorted_nodes[:num_of_nodes])
		self.create_node_dictionary()
		self.create_pos_dictionary()


def test():
	cv_graph = CVGraph()
	cv_graph.test()
