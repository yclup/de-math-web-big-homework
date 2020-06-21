import sys
sys.path.append('algorithms')

from web_big_homework.settings import BASE_DIR
import os 
from django.shortcuts import render, redirect
from django.http import JsonResponse
import graph_APIs
from graph_APIs import DataOfNode, CVSubGraph
# Create your views here.
CVGRAPH = graph_APIs.CVGraph('data/graph.gpickle')
now_cv_graph = CVGRAPH
main_data = CVGRAPH.return_data_to_draw()

def home_page(request):
	num_of_nodes = CVGRAPH.return_number_of_nodes()
	now_cv_graph = CVGRAPH
	context = {'data': main_data, 'num_of_nodes': num_of_nodes}
	return render(request, 'home.html', context)

def specify_number(request):
	global now_cv_graph
	if request.method == "POST":
		if request.POST['node_num'] != "":
			num_of_nodes = int(request.POST['node_num'])
			now_cv_graph = CVSubGraph(CVGRAPH, num_of_nodes)
			data = now_cv_graph.return_data_to_draw()
			context = {'data': data, 'num_of_nodes': num_of_nodes}
			return render(request, 'home.html', context)
		else:
			return redirect('/')

def line_info_alone(request, node_name: str):
	response = now_cv_graph.return_line_info_list_of_a_node(node_name)
	return JsonResponse(response, safe=False)

def cv_info(request, node_name: str):
	src = "/static/introduction/{}.jpg".format(node_name)
	intro_route = os.path.join(BASE_DIR, "static/introduction/{}.txt".format(node_name))
	with open(intro_route, encoding='utf-8') as f:
		intro = f.readlines()
	response = {'src': src, 'intro': intro}
	return JsonResponse(response, safe=False)

def line_info_double(request, start_node_name: str, end_node_name: str):
	response = now_cv_graph.return_line_info_between_two_nodes(start_node_name, end_node_name)
	return JsonResponse(response, safe=False)