from django.shortcuts import render
from usuarios.models import *
from publicaciones.models import *
from comentarios.models import *
from seguidores.models import *
from likes.models import *
from django.views.generic import TemplateView
from datetime import datetime, timedelta, time

class seguir(TemplateView):
	template_name = 'usuarios/perfil.html'
	def post(self, request, *args, **kwargs):
		id = usuarios.objects.get(pk = request.session['usuario_id'])
		id_seguido = usuarios.objects.get(pk = request.POST['id'])
		existe = seguidores.objects.filter(usuario=id, usuario_seguido=id_seguido).count()
		if existe == 0:
			crear = seguidores.objects.create(usuario=id, usuario_seguido=id_seguido)
		else:
			borrar = seguidores.objects.get(usuario=id, usuario_seguido=id_seguido)
			borrar.delete()
		usuario_encontrado = usuarios.objects.get(id=request.POST['id'])
		noticias = publicaciones.objects.filter(usuario=usuario_encontrado.id, tipo=1)
		datos = usuarios.objects.filter(id=usuario_encontrado.id)
		cantidad_publicaciones = publicaciones.objects.filter(usuario=usuario_encontrado.id, tipo=1).count()
		cantidad_seguidos = seguidores.objects.filter(usuario=usuario_encontrado.id).count()
		cantidad_seguidores = seguidores.objects.filter(usuario_seguido=usuario_encontrado.id).count()
		siguiendo = seguidores.objects.filter(usuario=request.session['usuario_id'], usuario_seguido=usuario_encontrado.id).count()
		return render(request, 'usuarios/perfil.html', {'noticias':noticias, 'datos':datos, 'publicaciones':cantidad_publicaciones, 'seguidos':cantidad_seguidos, 'seguidores':cantidad_seguidores, 'siguiendo':siguiendo})
