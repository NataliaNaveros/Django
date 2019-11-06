from django.shortcuts import render

# Create your views here.

def comentarios(request):
	return render(request, 'index.html')