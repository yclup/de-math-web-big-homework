import networkx as nx 
from create_graph import Node, Side
GRAPH_PATH = "../data/graph.gpickle"

class CVGraph:
	def __init__(self, graph_path=GRAPH_PATH):
		self.graph_path = graph_path
		self.graph = self.retrive_and_create_graph(self.graph_path)
		self.create_node_dictionary()

	def create_node_dictionary(self):
		self.node_dictionary = {}
		for node in self.graph.nodes:
			self.node_dictionary[node.name] = node 

	def return_node_object_via_name(self, node_name: str):
		return self.node_dictionary[node_name]


	def return_node_names_as_list(self): 
		return [node.name for node in self.graph.nodes]

	def return_side_num_of_a_node_by_name(self, node: str):
		return len(nx.edges(self.graph, nbunch=self.return_node_object_via_name(node)))

	def test(self):
		print(self.return_side_num_of_a_node_by_name("松冈祯丞"))

	def retrive_and_create_graph(self, graph_path):
		return nx.read_gpickle(graph_path)


def test():
	cv_graph = CVGraph()
	cv_graph.test()

