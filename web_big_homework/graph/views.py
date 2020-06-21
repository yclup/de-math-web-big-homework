import sys

sys.path.append('algorithms')

from django.shortcuts import render, redirect
from django.http import JsonResponse
import graph_APIs
from graph_APIs import DataOfNode, CVSubGraph
# Create your views here.
cvgraph = graph_APIs.CVGraph('data/graph.gpickle')
sub_cv_graph = None 
main_data = cvgraph.return_data_to_draw()

def home_page(request):
	num_of_nodes = cvgraph.return_number_of_nodes()
	context = {'data': main_data, 'num_of_nodes': num_of_nodes}
	return render(request, 'home.html', context)

def specify_number(request):
	global sub_cv_graph
	if request.method == "POST":
		if request.POST['node_num'] != "":
			num_of_nodes = int(request.POST['node_num'])
			sub_cv_graph = CVSubGraph(cvgraph, num_of_nodes)
			data = sub_cv_graph.return_data_to_draw()
			context = {'data': data, 'num_of_nodes': num_of_nodes}
			return render(request, 'home.html', context)
		else:
			return redirect('/')

def line_info(request, node_name: str):
	response = sub_cv_graph.return_line_info_list_of_a_node(node_name)
	return JsonResponse(response, safe=False)
