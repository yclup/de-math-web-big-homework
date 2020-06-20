import sys

sys.path.append('algorithms')

from django.shortcuts import render, redirect
import graph_APIs
# Create your views here.

def home_page(request):
	cvgraph = graph_APIs.CVGraph('data/graph.gpickle')
	node_name = cvgraph.return_node_names_as_list()
	return render(request, 'home.html', {'node_name': node_name})