"""Django"""
from django.http import HttpResponse

def comentario(request):
 	return HttpResponse('Comentarios')

# def likes(request):
	
# 	return HttpResponse('Me gusta')

# def publicaiones(request):
	
# 	return HttpResponse('Publicaciones')

# def seguidores(request):
	
# 	return HttpResponse('Seguidores')

# def usuarios(request):
	
# 	return HttpResponse('Usuarios')