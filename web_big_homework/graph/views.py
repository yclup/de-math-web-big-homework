import sys

sys.path.append('algorithms')

from django.shortcuts import render, redirect
import graph_APIs
from graph_APIs import DataOfNode
# Create your views here.

def home_page(request):
	cvgraph = graph_APIs.CVGraph('data/graph.gpickle')
	data = cvgraph.return_data_to_draw()
	return render(request, 'home.html', {'data': data})