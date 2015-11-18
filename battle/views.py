from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {'pagetitle': 'Battle For Midgard'}
	return render(request, 'index.html', context)