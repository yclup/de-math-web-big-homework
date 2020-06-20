from django.shortcuts import render, redirect
from algorithms import graph_APIs
# Create your views here.
def home_page(request):
	return render(request, 'home.html')