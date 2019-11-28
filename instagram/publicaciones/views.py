from django.shortcuts import render, redirect
from usuarios.models import *
from publicaciones.models import *
from comentarios.models import *
from seguidores.models import *
from likes.models import *
from django.views.generic import TemplateView
from datetime import datetime, timedelta, time


class instagram(TemplateView):
	template_name = 'publicaciones/publicaciones.html'
	def get(self, request, *args, **kwargs):
		if(request.session.get('bienvenido') != 1):
			return redirect('inicio')
		else:
			usuarios = seguidores.objects.filter(usuario=request.session['usuario_id']).count()
			usuario_propio = publicaciones.objects.filter(usuario=request.session['usuario_id']).count()
			publicacion = []
			gusta = []
			comentar = []
			mensaje = []
			hoy = datetime.now().date()
			manana = hoy + timedelta(1)
			hoy_inicio = datetime.combine(hoy, time())
			hoy_final = datetime.combine(manana, time())
			seguir = seguidores.objects.all().filter(usuario=request.session['usuario_id'])
			for seguidor in seguir:
				publicacion.append(seguidor.usuario_seguido.id)
			
			publicacion.append(request.session['usuario_id'])
			noticias = publicaciones.objects.all().filter(usuario__in=publicacion, tipo=1).order_by('-fecha_creacion')
			historias = publicaciones.objects.all().filter(usuario__in=publicacion, tipo=2, fecha_creacion__gte=hoy_inicio, fecha_creacion__lt=hoy_final).order_by('-fecha_creacion')
			for noticia in noticias:
				cantidad_likes = likes.objects.filter(publicacion=noticia.id).count()
				if cantidad_likes != 0:
					mensaje.append([noticia.id, 'Le gusta a:'])
					obtener_nombres = likes.objects.all().filter(publicacion=noticia.id)
					for obtener in obtener_nombres:
						gusta.append([noticia.id, obtener.usuario.nombre_completo+','])

					if len(gusta) != 0:
						gusta[-1][1] = gusta[-1][1][:-1]

				cantidad_comentarios = comentarios.objects.filter(publicacion=noticia.id).count()
				if cantidad_comentarios != 0:
					comentario = comentarios.objects.all().filter(publicacion=noticia.id)
					for cmt in comentario:
						comentar.append([noticia.id, cmt.usuario.nombre_completo, cmt.mensaje, cmt.id])
			return render(request, 'publicaciones/publicaciones.html', {'usuarios':usuarios, 'usuario_propio':usuario_propio, 'noticias':noticias, 'historias':historias, 'mensaje':mensaje, 'arreglo':gusta, 'comentarios':comentar})

class borrar_publicaciones(TemplateView):
	template_name = 'usuarios/perfil.html'
	def post(self, request, *args, **kwargs):
		borrar = publicaciones.objects.filter(id=request.POST['publicacion_id']) 
		borrar.delete()
		return redirect('perfil')