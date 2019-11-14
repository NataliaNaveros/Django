from django.shortcuts import render

# Create your views here.

def like(request):
	return render(request, 'index.html')