from django.shortcuts import render

# Create your views here.

def likes(request):

	return render(request, 'index.html')