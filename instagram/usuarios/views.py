from django.shortcuts import render, redirect
from usuarios.models import *
from publicaciones.models import *
from comentarios.models import *
from seguidores.models import *
from likes.models import *
from django.views.generic import TemplateView
from datetime import datetime, timedelta, time


class login(TemplateView):
	template_name = 'usuarios/login.html'
	def get(self, request, *args, **kwargs):
		if(request.session.get('bienvenido') == 1):
			return redirect('instagram')
		else:
			return render(request, 'usuarios/login.html')
	def post(self, request, *args, **kwargs):
		verificar = usuarios.objects.filter(usuario=request.POST['usuario'], contrasena=request.POST['contrasena']).exists()
		if verificar is True:
			usuario_encontrado = usuarios.objects.get(usuario=request.POST['usuario'], contrasena=request.POST['contrasena'])
			request.session['bienvenido'] = 1
			request.session['usuario_id'] = usuario_encontrado.id
			request.session['usuario'] = request.POST['usuario']
			return redirect('instagram')
		else:
			return render(request, 'usuarios/login.html', {'error' : 'El usuario o la contraseña son incorrectos.'})
class registrarse(TemplateView):
	template_name = 'usuarios/register.html'
	def get(self, request, *args, **kwargs):
		if(request.session.get('bienvenido') == 1):
			return redirect('instagram')
		else:
			return render(request, 'usuarios/register.html')
	def post(self, request, *args, **kwargs):
		if(request.POST['usuario'] == '' or request.POST['correo'] == '' or request.POST['nombre'] == '' or request.POST['contrasena'] == ''):
			return render(request, 'usuarios/register.html', {'error' : 'Rellene todos los datos requeridos.'})
		else:
			verUsuario = usuarios.objects.filter(usuario=request.POST['usuario']).exists()
			if verUsuario is True:
				return render(request, 'usuarios/register.html', {'error' : 'Lo siento, el usuario ya existe.'})
			else:
				verCorreo = usuarios.objects.filter(correo=request.POST['correo']).exists()
				if verCorreo is True:
					return render(request, 'usuarios/register.html', {'error' : 'Lo siento, el correo ya existe.'})
				else:
					usuario = usuarios.objects.create(usuario=request.POST['usuario'], correo=request.POST['correo'], nombre_completo=request.POST['nombre'], contrasena=request.POST['contrasena'])
					request.session['bienvenido'] = 1
					request.session['usuario_id'] = usuario.id
					request.session['usuario'] = request.POST['usuario']
					return redirect('instagram')

class perfil(TemplateView):
	template_name = 'usuarios/perfil.html'
	def get(self, request, *args, **kwargs):
		noticias = publicaciones.objects.filter(usuario=request.session['usuario_id'], tipo=1)
		datos = usuarios.objects.filter(id=request.session['usuario_id'])
		cant_publicaciones = publicaciones.objects.filter(usuario=request.session['usuario_id'], tipo=1).count()
		cant_seguidos = seguidores.objects.filter(usuario=request.session['usuario_id']).count()
		cant_seguidores = seguidores.objects.filter(usuario_seguido=request.session['usuario_id']).count()
		return render(request, 'usuarios/perfil.html', {'noticias':noticias, 'datos':datos, 'publicaciones':cant_publicaciones, 'seguidos':cant_seguidos, 'seguidores':cant_seguidores})
	def post(self, request, *args, **kwargs):
		verUsuario = usuarios.objects.filter(usuario=request.POST['buscar']).exists()
		if verUsuario is True:
			usuario_encontrado = usuarios.objects.get(usuario=request.POST['buscar'])
			noticias = publicaciones.objects.filter(usuario=usuario_encontrado.id, tipo=1)
			datos = usuarios.objects.filter(id=usuario_encontrado.id)
			cant_publicaciones = publicaciones.objects.filter(usuario=usuario_encontrado.id, tipo=1).count()
			cant_seguidos = seguidores.objects.filter(usuario=usuario_encontrado.id).count()
			cant_seguidores = seguidores.objects.filter(usuario_seguido=usuario_encontrado.id).count()
			siguiendo = seguidores.objects.filter(usuario=request.session['usuario_id'], usuario_seguido=usuario_encontrado.id).count()
			return render(request, 'usuarios/perfil.html', {'noticias':noticias, 'datos':datos, 'publicaciones':cant_publicaciones, 'seguidos':cant_seguidos, 'seguidores':cant_seguidores, 'siguiendo':siguiendo})
		else:
			return redirect('publicaciones')
class perfil_subir(TemplateView):
	template_name = 'publicaciones/new.html'
	def post(self, request, *args, **kwargs):
		id = usuarios.objects.get(pk = request.session['usuario_id'])
		publicacion = publicaciones.objects.create(usuario=id, imagen=request.FILES['imagen'], mensaje=request.POST['mensaje'], tipo=request.POST['tipo'])
		return redirect('perfil')
class perfil_editar(TemplateView):
	template_name = 'usuarios/update.html'
	def post(self, request, *args, **kwargs):
		id = usuarios.objects.get(id = request.session['usuario_id'])
		id.nombre_completo = request.POST['nombre_completo']
		id.imagen_perfil = request.FILES['imagen_perfil']
		id.save()
		return redirect('perfil')
class cerrar_sesion(TemplateView):
	template_name = 'usuarios/login.html'
	def get(self, request, *args, **kwargs):
		del request.session['bienvenido']
		del request.session['usuario_id']
		del request.session['usuario']
		return render(request, 'usuarios/login.html')
