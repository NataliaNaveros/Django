from django.shortcuts import render

# Create your views here.

def comentario(request):
	return render(request, 'index.html')