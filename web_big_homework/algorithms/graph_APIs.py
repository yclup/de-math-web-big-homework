import networkx as nx 
from create_graph import GRAPH_PATH

class CVGraph:
	def __init__(self):
		self.graph = self.retrive_and_create_graph(GRAPH_PATH)

	def test(self):
		print(len(self.graph.nodes))

	def retrive_and_create_graph(self, graph_path):
		return nx.read_gpickle(graph_path)


def test():
	cv_graph = CVGraph()
	cv_graph.test()

