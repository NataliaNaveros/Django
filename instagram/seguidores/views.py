from django.shortcuts import render

# Create your views here.

def seguidor(request):
	return render(request, 'index.html')